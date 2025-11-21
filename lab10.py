from func import *

def main():
    try:
        args = parse_arguments()
        
        identified_params = classify_and_identify_arguments(args.args)
        final_params = apply_defaults(identified_params)
        
        validation_errors = validate_graph_parameters(final_params)
        if validation_errors:
            print("Ошибки в параметрах графа:")
            for error in validation_errors:
                print(f"  • {error}")
            
            sys.exit(1)
        
        print_current_config(final_params, len(args.args))
        
        is_directed = final_params['graph_type'] == 'ori'
        is_weighted = final_params['weighted_mode'] == 'weighted'
        
        print(f"\n Генерация графа...")
        graph = generate_graph(
            size=final_params['graph_size'],
            is_weighted=is_weighted,
            is_directed=is_directed,
            density=final_params['density']
        )
        
        
        print(f"\nBFS обход из вершины {final_params['start_vertex']}:")
        distances = bfsd(graph, final_params['start_vertex'])
        
        print(f"\n Расстояния от вершины {final_params['start_vertex']}:")
        reachable = 0
        for i, dist in enumerate(distances):
            status = str(dist) if dist != -1 else "недостижима"
            print(f"  Вершина {i}: {status}")
            if dist != -1:
                reachable += 1
        
       
        
        if reachable > 0:
            max_dist = max(d for d in distances if d != -1)
            print(f"  • Максимальное расстояние: {max_dist}")
        
        # if len(args.args) < 3:
        #     print(f"\n Подсказка: можно указать до 5 параметров в любом порядке")
        #     print_usage_examples()
        
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()