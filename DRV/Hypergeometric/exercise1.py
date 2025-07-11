"""A certain type of digital camera comes in a 
3-megapixel version and a 4-megapixel version. 
A camera store receives a shipment of 15 of these 
cameras, of which 6 have a resolution of 3 megapixels.
Suppose 5 of these cameras are randomly selected 
to be kept behind the counter; 
the remaining 10 are placed in storage.
Let X be the number of 3-megapixel cameras 
among the 5 selected to be kept behind the counter."""

import hypergeometric as hpg
import math
# 3 mpx -> E, 4mpx -> F
# N: 15, M: 6, N - M: 9
# n: 5

print(hpg.pmf(2, 5, 6, 15))
print(hpg.mean(5, 6, 15))
print(math.sqrt(hpg.var(5, 6, 15)))
