def starzig(seq):
    i=0

    while i<=5:
        #print(space+'*')
        #space=space*i
        #print(i)
        space=' '
        i+=1
        space=space*i
        print(space+seq)

    i=i-1
    #print(i)
    while i>0:
        #print("iterable",i)
        space=' '
        space=space*i
        #print("len=",len(space))
        print(space+seq)
        i=i-1

size=input("enter your required size: ")
size=int(size)
seq=input("Enter what you want to be printed")
user=input("Enter your choice: s for start and t for stop: ")
for i in range(size):
    if user=='s':
        starzig(seq)
        #stop=input()
        #if stop=='t':
        #    break
