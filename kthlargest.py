class KthLargest:
    def __init__(self, k: int, nums):
        self.k = k
        self.nums = nums.copy()
        self.topk = nums.copy()

        self.topk.sort()
        if len(self.topk) > self.k:
            self.topk = self.topk[len(self.topk) - self.k :]

        self.topk.reverse()

    def add(self, val: int) -> int:
        self.nums.append(val)

        if len(self.topk) == 0:
            self.topk.insert(0, val)
            return self.topk[-1]

        if val >= self.topk[0]:
            self.topk.insert(0, val)
            if len(self.topk) == (self.k + 1):
                self.topk.pop(-1)
            return self.topk[-1]

        if len(self.topk) < self.k:
            if val <= self.topk[-1]:
                self.topk.append(val)
                return self.topk[-1]
            for i in range(len(self.topk) - 1):
                if val <= self.topk[i] and val >= self.topk[i + 1]:
                    self.topk.insert(i + 1, val)
                    break
            return self.topk[-1]

        if val < self.topk[0] and val > self.topk[-1]:
            for i in range(len(self.topk) - 1):
                if val <= self.topk[i] and val >= self.topk[i + 1]:
                    self.topk.insert(i + 1, val)
                    break
            if len(self.topk) == (self.k + 1):
                self.topk.pop(-1)

        return self.topk[-1]
