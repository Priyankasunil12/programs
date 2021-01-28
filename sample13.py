#An example python program for set insertion
s={10,20}
s.add(30)
print(s)
s.add(30)
print(s)# again 30 will not be added in the set
s.update([40,50])
print(s)
s.update({60,70},[80,90])
print(s)