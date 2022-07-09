# -*- coding: utf-8 -*-

import numpy as np
import math

a, b, d = [int(v) for v in input().split()]

rad = math.radians(d)

r = [[math.cos(rad), -math.sin(rad)], [math.sin(rad), math.cos(rad)]]
r = np.array(r, dtype=np.float128)

vec = np.array([a, b], dtype=np.float128)

ans = r @ vec
print(ans[0], ans[1])
