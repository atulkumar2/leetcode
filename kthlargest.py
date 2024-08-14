class KthLargest:
    def __init__(self, k: int, nums):
        self.k = k
        self.nums = nums

        self.topk = nums.copy()
        self.topk.sort()
        self.topk.reverse()
        if len(self.topk) <= self.k:
            return
        else:
            self.topk = self.topk[0 : self.k]

    def add(self, val: int) -> int:
        self.nums.append(val)

        if len(self.topk) < self.k:
            self.topk.append(val)
        else:
            if val >= self.topk[-1]:
                self.topk.insert(0, val)

        self.topk.sort()
        self.topk.reverse()
        if len(self.topk) == (self.k + 1):
            self.topk.pop(-1)

        return self.topk[-1]


inputs = [(3, [4, 5, 8, 2]), (3, []), (3, [5, -1]), (3, [-1])]

for item in inputs:
    k, nums = item
    print("\ninput:", k, nums)
    obj = KthLargest(k, nums)

    output = []

    for n in [3, 3, 8, 5, 5, 10, 7, -2]:
        output.append(obj.add(n))

    print("output:", output)
