def starzig(seq):
    i=0

    while i<=5:
        space=' '
        i+=1
        space=space*i
        print(space+seq)

    i=i-1
    while i>0:
        space=' '
        space=space*i
        print(space+seq)
        i=i-1

size=input("enter your required size: ")
size=int(size)
seq=input("Enter what you want to be printed: ")
user=input("Enter your choice: s for start and t for stop: ")
for i in range(size):
    if user=='s':
        starzig(seq)
