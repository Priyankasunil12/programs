d={110:"abc", 101:"xyz",105:"pqr",106:"bcd"}
d[101]="wxy"
print(len(d))
print(d)#
print(d.pop(105))
print(d)
del d[106]
print(d)
d[108]="cde"
print(d.popitem())