def knapsack_greedy(n, m, profit, weight):
    items = []
    for i in range(n):
        items.append((profit[i], weight[i], profit[i] / weight[i]))
        
    items.sort(key=lambda x: x[2], reverse=True)

    total_profit = 0
    selected_items = []

    for i in range(n):
        if weight[i] <= m:
            m -= items[i][1]
            total_profit += items[i][0]
            selected_items.append((i + 1, items[i][1])) 
        else:
            fraction = m / items[i][1]
            total_profit += items[i][0] * fraction
            selected_items.append((i + 1, m))  
            break

    return total_profit, selected_items

def main():
    n = int(input("Enter the number of items: "))
    m = float(input("Enter the maximum capacity of the knapsack: "))
    
    profit = []
    weight = []

    print("Enter the profits of items:")
    for i in range(n):
        p = float(input(f"Profit of item {i + 1}: "))
        profit.append(p)
    
    print("Enter the weights of items:")
    for i in range(n):
        w = float(input(f"Weight of item {i + 1}: "))
        weight.append(w)
        
    total_profit, selected_items = knapsack_greedy(n, m, profit, weight)

    print(f"\nTotal profit: {total_profit}")
    print("Selected items (item index, weight selected):")
    for item in selected_items:
        print(f"Item {item[0]}: {item[1]} weight")

if __name__ == "__main__":
    main()
