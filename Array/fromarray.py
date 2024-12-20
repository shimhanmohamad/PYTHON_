from array import *

a = array('i',[1,2,3,4,5,6,7,8,9,0])
#method1 for print without type code...This method is first convert the element in to string and acctre the print the 
print(''.join(map(str,a)))
#method2 for print wwithout type code
print(*a,sep='  ')#when I increase the sep='' space then output also increase the space


b = array('i',[1,2,3,4,5])
c = array('i',[6,7,8,9,0])
x = b + c
print(x)
print(*x,sep=' ')