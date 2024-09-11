def knapsack_01(n, m, profit, weight):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, m + 1):
            if weight[i - 1] <= w:
                dp[i][w] = max(profit[i - 1] + dp[i - 1][w - weight[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    print("\nDynamic Programming Table:")
    for i in range(n + 1):
        for w in range(m + 1):
            print(f"{dp[i][w]:4}", end=" ")
        print()

    total_profit = dp[n][m]
    selected_items = []
    w = m

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w -= weight[i - 1]

    selected_items.reverse()

    return total_profit, selected_items

def main():
    n = int(input("Enter the number of items: "))
    m = int(input("Enter the maximum capacity of the knapsack: "))

    profit = []
    weight = []

    print("Enter the profits of items:")
    for i in range(n):
        p = int(input(f"Profit of item {i + 1}: "))
        profit.append(p)
    
    print("Enter the weights of items:")
    for i in range(n):
        w = int(input(f"Weight of item {i + 1}: "))
        weight.append(w)

    total_profit, selected_items = knapsack_01(n, m, profit, weight)

    print(f"\nTotal profit: {total_profit}")
    print("Selected items (1-based index):", selected_items)

if __name__ == "__main__":
    main()
