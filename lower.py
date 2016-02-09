# -*- coding: utf-8 -*-

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
for s in L1:
	if isinstance(s,str):
   		L2.append(s.lower())
print(L2)

#更简洁的代码
# L2=[s.lower() for s in L1 if isinstance(s,str)==1]
# print(L2)