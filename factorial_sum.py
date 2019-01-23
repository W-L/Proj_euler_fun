def qsum(x):
    nums=str(x)
    qs=0
    for i in nums:
        qs=qs+int(i)
    return qs

import math
print(qsum(math.factorial(100)))

