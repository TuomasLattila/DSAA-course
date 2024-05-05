def sales(cars, customers):
    counter = 0
    for i in range(len(cars)):
        if len(customers) == 0:
            break
        buyer = 0
        found = False
        for j in range(len(customers)):
            if customers[j] >= cars[i]:
                if found == False:
                    buyer = j
                    found = True
                elif customers[j] <= customers[buyer]:
                    buyer = j
        if customers[buyer] >= cars[i]:
            counter += 1
            customers[buyer], customers[len(customers)-1] = customers[len(customers)-1], customers[buyer]
            customers.pop()
    return counter

if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))                        # 3
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))         # 4
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))           # 3
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))   # 5