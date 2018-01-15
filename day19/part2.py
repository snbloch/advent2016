from math import log

n = 3012210
p = 3 ** int(log(n - 1, 3))
print n - p + max(n - 2 * p, 0)
