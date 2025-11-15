import argparse
import sys
from collections import deque
import random


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Lab 10: Обход графа алгоритмом BFS',
        usage='python lab10.py [размер_графа] [стартовая_вершина] [взвешенность] [ориентация] [плотность]'
    )
    
    parser.add_argument('args', nargs='*', help='Аргументы в любом порядке')
    
    return parser.parse_args()

def smart_convert(value):
    """Умное преобразование типов"""
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value

def classify_arguments(args):
    """Классифицирует аргументы по типам"""
    numbers = []
    strings = []
    floats = []
    
    for arg in args:
        converted = smart_convert(arg)
        
        if isinstance(converted, int):
            numbers.append(converted)
        elif isinstance(converted, float):
            floats.append(converted)
        else:
            strings.append(converted)
    
    return numbers, strings, floats

def validate_graph_parameters(params):
    """Проверяет корректность параметров графа"""
    errors = []
    
    # Проверка размера графа
    if params['graph_size'] < 1:
        errors.append("Размер графа должен быть положительным числом")
    
    # Проверка стартовой вершины
    if params['start_vertex'] < 0:
        errors.append("Стартовая вершина не может быть отрицательной")
    if params['start_vertex'] >= params['graph_size']:
        errors.append(f"Стартовая вершина {params['start_vertex']} должна быть в диапазоне [0, {params['graph_size']-1}]")
    
    # Проверка плотности
    if not (0.0 <= params['density'] <= 1.0):
        errors.append("Плотность графа должна быть в диапазоне [0.0, 1.0]")
    
    # Проверка допустимых значений для mode и type
    valid_modes = ['weighted', 'unweighted', 'взвешенный', 'невзвешенный']
    valid_types = ['ori', 'unori', 'directed', 'undirected', 'ориентированный', 'неориентированный']
    
    if params['weighted_mode'].lower() not in [m.lower() for m in valid_modes]:
        errors.append(f"Недопустимый режим взвешенности: {params['weighted_mode']}. Допустимые: {valid_modes}")
    
    if params['graph_type'].lower() not in [t.lower() for t in valid_types]:
        errors.append(f"Недопустимый тип графа: {params['graph_type']}. Допустимые: {valid_types}")
    
    return errors

def process_arguments(args_list, default_values=None):
    """Обрабатывает список аргументов для работы с графами"""
    if default_values is None:
        default_values = {
            'graph_size': 10,
            'start_vertex': 0,
            'weighted_mode': 'unweighted',
            'graph_type': 'unori',
            'density': 0.5
        }
    
    numbers, strings, floats = classify_arguments(args_list)
    
    result = default_values.copy()
    
    # Заполняем числа (размер графа и стартовая вершина)
    if len(numbers) >= 1:
        result['graph_size'] = numbers[0]
    if len(numbers) >= 2:
        result['start_vertex'] = numbers[1]
    
    # Заполняем строки (режим и тип графа)
    if len(strings) >= 1:
        first_str = strings[0].lower()
        if first_str in ['weighted', 'unweighted', 'взвешенный', 'невзвешенный']:
            result['weighted_mode'] = strings[0]
        else:
            result['graph_type'] = strings[0]
    
    if len(strings) >= 2:
        second_str = strings[1].lower()
        if second_str in ['ori', 'unori', 'directed', 'undirected', 'ориентированный', 'неориентированный']:
            result['graph_type'] = strings[1]
        elif 'weighted_mode' not in result or result['weighted_mode'] == default_values['weighted_mode']:
            result['weighted_mode'] = strings[1]
    
    # Заполняем плотность
    if len(floats) >= 1:
        result['density'] = floats[0]
    
    return result

def generate_graph(size, is_weighted, is_directed, density):
    """
    Генерирует матрицу смежности графа
    """
    graph = [[0] * size for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            if i == j:
                continue  # нет петель
                
            if random.random() < density:
                if is_weighted:
                    weight = random.randint(1, 10)  # веса от 1 до 10
                else:
                    weight = 1  # невзвешенный граф
                
                graph[i][j] = weight
                
                # Если неориентированный, добавляем обратное ребро
                if not is_directed and i != j:
                    graph[j][i] = weight
    
    return graph

def bfsd(G, v):
    """
    BFS обход графа с вычислением расстояний
    G - матрица смежности
    v - стартовая вершина
    возвращает массив расстояний от v до всех вершин
    """
    q = deque()
    q.append(v)
    dist = [-1] * len(G)
    dist[v] = 0

    while q:
        v = q.popleft()  # исправлено на popleft для настоящего BFS
        for i in range(len(G)):
            if G[v][i] > 0 and dist[i] == -1:
                q.append(i)
                dist[i] = dist[v] + G[v][i]

    return dist

def print_graph_info(graph, is_directed, is_weighted):
    """Выводит информацию о графе"""
    size = len(graph)
    edges = 0
    total_weight = 0
    
    for i in range(size):
        for j in range(size):
            if graph[i][j] > 0:
                edges += 1
                total_weight += graph[i][j]
    
    # Для неориентированного графа делим на 2
    if not is_directed:
        edges = edges // 2
    
    print(f"  • Ребра: {edges}")
    if is_weighted:
        print(f"  • Общий вес: {total_weight}")
        if edges > 0:
            print(f"  • Средний вес: {total_weight/edges:.2f}")

def print_usage_examples():
    """Показывает примеры использования"""
    print("\n📋 Примеры использования:")
    print("  python lab10.py 10 0 weighted ori 0.6        # все параметры")
    print("  python lab10.py 20 5                         # только размер и стартовая вершина")
    print("  python lab10.py 15 weighted                  # размер и взвешенность")
    print("  python lab10.py 10 0 unweighted              # размер, стартовая и тип взвешенности")
    print("  python lab10.py                              # все параметры по умолчанию")

def print_current_config(params):
    """Выводит текущую конфигурацию графа"""
    is_directed = params['graph_type'] in ['ori', 'directed', 'ориентированный']
    is_weighted = params['weighted_mode'] in ['weighted', 'взвешенный']
    
    print(f"\n🎯 Конфигурация графа:")
    print(f"  • Размер: {params['graph_size']} вершин")
    print(f"  • Стартовая вершина: {params['start_vertex']}")
    print(f"  • Тип: {'ориентированный' if is_directed else 'неориентированный'}")
    print(f"  • Взвешенность: {'взвешенный' if is_weighted else 'невзвешенный'}")
    print(f"  • Плотность: {params['density']:.2f}")