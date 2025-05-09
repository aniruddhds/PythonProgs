def collatz(num):
    while num!=1:
        if num%2==0:
            print(num//2)
            num=num//2
            #return num//2
        else:
            print((3*num)+1)
            num=(3*num)+1
            #return (3*num)+1


user=int(input("Enter a number: "))
collatz(user)