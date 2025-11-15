from func import *


def main():
    try:
        args = parse_arguments()
        
        # Значения по умолчанию
        default_values = {
            'graph_size': 10,
            'start_vertex': 0,
            'weighted_mode': 'unweighted',
            'graph_type': 'unori',
            'density': 0.5
        }
        
        # Обрабатываем аргументы
        parsed = process_arguments(args.args, default_values)
        
        # Проверяем корректность параметров
        validation_errors = validate_graph_parameters(parsed)
        if validation_errors:
            print("❌ Ошибки в параметрах графа:")
            for error in validation_errors:
                print(f"  • {error}")
            print_usage_examples()
            sys.exit(1)
        
        # Выводим конфигурацию
        print_current_config(parsed)
        
        # Определяем флаги для генерации графа
        is_directed = parsed['graph_type'] in ['ori', 'directed', 'ориентированный']
        is_weighted = parsed['weighted_mode'] in ['weighted', 'взвешенный']
        
        # Генерируем граф
        print(f"\n🔧 Генерация графа...")
        graph = generate_graph(
            size=parsed['graph_size'],
            is_weighted=is_weighted,
            is_directed=is_directed,
            density=parsed['density']
        )
        
        # Выводим информацию о графе
        print_graph_info(graph, is_directed, is_weighted)
        
        # Выполняем BFS обход
        print(f"\n🚀 BFS обход из вершины {parsed['start_vertex']}:")
        distances = bfsd(graph, parsed['start_vertex'])
        
        # Выводим результаты обхода
        print(f"\n📊 Расстояния от вершины {parsed['start_vertex']}:")
        reachable = 0
        for i, dist in enumerate(distances):
            status = str(dist) if dist != -1 else "недостижима"
            print(f"  Вершина {i}: {status}")
            if dist != -1:
                reachable += 1
        
        print(f"\n📈 Статистика:")
        print(f"  • Достижимо вершин: {reachable}/{len(graph)}")
        print(f"  • Процент достижимости: {reachable/len(graph)*100:.1f}%")
        
        if reachable > 0:
            max_dist = max(d for d in distances if d != -1)
            print(f"  • Максимальное расстояние: {max_dist}")
        
        # Показываем подсказку если аргументов мало
        if len(args.args) < 3:
            print(f"\n💡 Использовано {len(args.args)} из 5 возможных аргументов")
            print_usage_examples()
        
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        print_usage_examples()
        sys.exit(1)

if __name__ == "__main__":
    main()