from collections import deque
#list
ll=[1,2,3,4,5,6,7,8]
ll.append(9)
print(ll)
ll.reverse()
print(ll)
queue = deque(['aa','bb','cc'])
queue.popleft()
print(queue)
queue.append("dd")
queue.popleft()
print(queue)

#tuples
tup=1,2,3,"abc"
tup2=tup,(2,3,4,"bcd")
print(tup2)
