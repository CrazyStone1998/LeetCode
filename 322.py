class Solution:
    def coinChange(self, coins, amount: int) -> int:
        # recursion
        if not amount: return 0
        memory = [None for i in range(amount + 1)]
        for i in coins:
            if i <= amount: memory[i] = 1
        MAX_SIZE = 2 ** 3 - 1
        def recursion(coins, amount, memory):
            if amount < 0:
                return MAX_SIZE
            elif memory[amount]:
                return memory[amount]
            else:
                memory[amount] = min([recursion(coins, amount - i, memory) for i in coins]) + 1
            return memory[amount]

        recursion(coins, amount, memory)
        return -1 if memory[-1] >= MAX_SIZE else memory[-1]
