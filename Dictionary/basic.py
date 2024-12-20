my_dic = {'a':'oiu','w':'we','r':'dsa'}
print(my_dic)

print(my_dic.keys())
print(my_dic.values())

for x in my_dic:
    print(x)

for x in my_dic.values():
    print(x)
    
for x,y in my_dic.items():
    print(x,'-',y)


print("**********")
my_dic.pop('a')
print(my_dic)
print("**********")

del my_dic['w']
print(my_dic)