class ATM:

    def __init__(self):
        self.nominals = [20, 50, 100, 200, 500]
        self.remains = dict()
        for nominal in self.nominals:
            self.remains[nominal] = 0

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.remains[self.nominals[i]] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        answer = [0] * 5
        for i in range(len(self.nominals) - 1, -1, -1):
            max_take_out = min(amount // self.nominals[i], self.remains[self.nominals[i]])
            amount -= self.nominals[i] * max_take_out
            answer[i] = max_take_out
        if amount > 0:
            return [-1]
        for i in range(len(answer)):
            self.remains[self.nominals[i]] -= answer[i]
        return answer


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)