def salesman(city_map):
    number_of_cities = len(city_map)
    lower_bound = 1382
    #initialize
    paths = [([0], [0]*number_of_cities, 0)] #(path, visited, sum of weights)
    paths[0][1][0] = 1
    biggest_values = []
    for i in range(number_of_cities):
        list = sorted(city_map[i])
        biggest_values.append(list[number_of_cities-1])

    for i in range(number_of_cities):
        length = len(paths)
        if i == number_of_cities-1: 
            for y in range(length): 
                if paths[y][2] + city_map[paths[y][0][path_length-1]][paths[y][0][0]] >= lower_bound:
                    continue
                path_length = len(paths[y][0])
                new_path = (paths[y][0]+[paths[y][0][0]], paths[y][1][:], paths[y][2]+city_map[paths[y][0][path_length-1]][paths[y][0][0]])
                paths.append(new_path)
            paths = paths[length:]
            continue
        for j in range(length):
            if paths[j][2] >= lower_bound:
                continue
            path_length = len(paths[j][0])

            for k in range(number_of_cities):
                if paths[j][2] + city_map[paths[j][0][path_length-1]][k] >= lower_bound or city_map[paths[j][0][path_length-1]][k] == biggest_values[k]:
                    continue
                if city_map[paths[j][0][path_length-1]][k] == 0 or paths[j][1][k] == 1:
                    continue
                new_path = (paths[j][0]+[k], paths[j][1][:], paths[j][2]+city_map[paths[j][0][path_length-1]][k])
                new_path[1][k] = 1
                paths.append(new_path)
        paths = paths[length:]

    sorted_list = sorted(paths, key=lambda x:x[2])
    if len(sorted_list) == 0:
        return None
    return sorted_list[0][0]

if __name__ == "__main__":
    
    cost = 0

    city_map = [
    #     0   1   2   3   4
        [ 0, 12, 19, 16, 29, 15, 8, 19, 5, 9],   # 0
        [12,  0, 27, 25,  5, 24, 25, 15, 15, 35],   # 1
        [19, 27,  0,  8,  4, 9, 34, 44, 24 ,24],   # 2
        [16, 25,  8,  0, 14, 14, 4, 42, 14, 14],   # 3
        [29,  5,  4, 14,  0, 34, 12, 2, 22, 8],
        [15,  24,  9, 14,  34, 0, 11, 1, 16, 19],    # 4
        [8,  25,  34, 4,  12, 11, 0, 13, 17, 22],
        [19,  15,  44, 42,  2, 1, 13, 0, 14, 54],
        [5,  15,  24, 14,  22, 16, 17, 14, 0, 21],
        [9,  35,  24, 14,  8, 19, 22, 54, 21, 0]
        ]

    path = salesman(city_map)
    for i in range(len(city_map)):
        cost += city_map[path[i]][path[i+1]]
    
    print(path)     # [0, 1, 4, 2, 3, 0]
    print(cost)     # 45