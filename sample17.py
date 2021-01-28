#example program for get() in Dictionary
d={110:"abc", 111:"def", 112:"xyz"}
print(d)
print(d.get(110))
print(d.get(125))
print(d.get(125,"NA"))
'''if 125 in d:
print(d[125])
else:
   print("NA")'''