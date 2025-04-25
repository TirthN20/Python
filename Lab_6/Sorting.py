l=[('Sandwich',150),('Pizza',300),('Burger',200)]

import operator
print(sorted(l,key=operator.itemgetter(1),reverse=True))
