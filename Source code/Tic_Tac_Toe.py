def printBoard(x,o):
    zero='X' if x[0] else('O' if o[0] else 0)
    one='X' if x[1] else('O' if o[1] else 1)
    two='X' if x[2] else('O' if o[2] else 2)
    three='X' if x[3] else('O' if o[3] else 3)
    four='X' if x[4] else('O' if o[4] else 4)
    five='X' if x[5] else('O' if o[5] else 5)
    six='X' if x[6] else('O' if o[6] else 6)
    seven='X' if x[7] else('O' if o[7] else 7)
    eight='X' if x[8] else('O' if o[8] else 8)

    print()
    print(f" {zero} | {one} | {two}")
    print(f"------------")
    print(f" {three} | {four} | {five}")
    print(f"------------")
    print(f" {six} | {seven} | {eight}")
    print()

def sum(l,m,n):
    return l+m+n

def checkWinner(x,o):
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for j in win:
        if sum(x[j[0]],x[j[1]],x[j[2]])==3:
            print("\nX won the match")
            printBoard(x,o)
            return 1
        if sum(o[j[0]],o[j[1]],o[j[2]])==3:
            print("\nO won the match")
            printBoard(x,o)
            return 0
    return -1

if __name__ == "__main__":
    x=[0,0,0,0,0,0,0,0,0]
    o=[0,0,0,0,0,0,0,0,0]
    chance=1 #1 for x & 0 for o
    print("* * * * * W E L C O M E * * * * *")

    while(True):
        printBoard(x,o)
        if(chance==1):
            print("X's chance")
            i=int(input("Enter a value : "))
            x[i]=1
        else:
            print("O's chance")
            i=int(input("Enter a value : "))
            o[i]=1

        #checking winner
        w=checkWinner(x,o)
        if w!=-1:
            print("\nMatch is over")
            break
        chance=1-chance
