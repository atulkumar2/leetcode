import time
from datetime import timedelta
import random
import kthlargest


def gen_rand_list(k):
    return random.sample(range(-9999, 10000), k)


start_time = time.monotonic()

inputs = [
    (3, [5, -1], [2, 1, -1, 3, 4]),
    (3, [4, 5, 8, 2], [3, 5, 10, 9, 4]),
    (1, [], gen_rand_list(7)),
    (2, [-1], gen_rand_list(5)),
    (3, [5, -1], gen_rand_list(6)),
    (4, [4, 5, 8, 2], gen_rand_list(10)),
    (1, [], gen_rand_list(25)),
    (3, [5, -1], gen_rand_list(250)),
    (2, [-1], gen_rand_list(2500)),
    (10, gen_rand_list(100), gen_rand_list(2500)),
    (100, gen_rand_list(1000), gen_rand_list(2500)),
    (4500, gen_rand_list(5000), gen_rand_list(5000)),
    (1500, gen_rand_list(5000), gen_rand_list(5000)),
    (6500, gen_rand_list(9000), gen_rand_list(7500)),
    (8500, gen_rand_list(8000), gen_rand_list(9999)),
]

for input in inputs:
    k, nums, entries = input
    obj = kthlargest.KthLargest(k, nums)

    output = []
    for n in entries:
        output.append(obj.add(n))

    print("input: %s %s\noutput: %s\n" % (k, nums, output))
    #print("input: %s %s %s\noutput: %s\n" % (k, nums, entries, output))

end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))
