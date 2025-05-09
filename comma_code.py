def converter(lis):
    if not lis:
        print("Empty List")
        return ''
    string=''
    for i in lis:
        if i==lis[-1]:
            string=string+'and '+i
        else:
            string=string+i+', '
    return string

mlist=[]
s=input("Enter the size of your list: ")
s=int(s)

for i in range(s):
    elem=input("Enter the element of your list: ")
    mlist.append(elem)

str=converter(mlist)
print(str)