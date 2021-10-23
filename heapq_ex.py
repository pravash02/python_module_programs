"""
Heaps are binary trees for which every parent node has a
    value less than or equal to any of its children.

In heap whatever the element is pushed or pop,
    heap structure is maintained.
"""

import random
import heapq

print("\n---- original list ----")
heap = [random.randint(1, 10) for _ in range(10)]
print(heap)


print("\n---- heapify list ----")
# It will sort the elements with minimum value always at the root
heapq.heapify(heap)
print(heap)


"""
heappush = it inserts the element into heap with structure being 
           maintained
heappop = it will pop the elements in sorted order with structure being 
          maintained
"""

print("\n---- heappush(3) ----")
# heappush inserts the element into heap
heapq.heappush(heap, 9)
print(heap)

print("\n---- heappop ----")
# heappop will pop the elements in sorted order
print(heapq.heappop(heap))


"""
heappushpop = first inserts the given element and then pop the 
              smallest element
heapreplace = first pop the smallest element and then replaces with 
              the given element
"""

l1 = [1, 7, 9, 4, 3]
l2 = [5, 7, 9, 4, 3]
heapq.heapify(l1)
heapq.heapify(l2)

print("\n---- heappushpop(2) ----")
print(l1)
print(heapq.heappushpop(l1, 2))
print(l1)

print("\n---- heapreplace(2) ----")
print(l2)
print(heapq.heapreplace(l2, 2))
print(l2)


"""
nlargset = return the n largest elements from heap
nsmallest = return the n smallest elements from heap
"""

l3 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
heapq.heapify(l3)

print("\n---- nlargest(3) ----")
print(heapq.nlargest(3, l3))

print("\n---- nsmallest(3) ----")
print(heapq.nsmallest(3, l3))
