#warship.py
import random
import os
cmove=[]
bh= ["A","B","C","D","E","F","G","H"]
br= ["1","2","3","4","5","6","7","8"]
pb={1:["_","_","_","_","_","_","_","_","\n"],2:["_","_","_","_","_","_","_","_","\n"],3:["_","_","_","_","_","_","_","_","\n"],4:["_","_","_","_","_","_","_","_","\n"],5:["_","_","_","_","_","_","_","_","\n"],6:["_","_","_","_","_","_","_","_","\n"],7:["_","_","_","_","_","_","_","_","\n"],8:["_","_","_","_","_","_","_","_","\n"]}
cb={1:["_","_","_","_","_","_","_","_","\n"],2:["_","_","_","_","_","_","_","_","\n"],3:["_","_","_","_","_","_","_","_","\n"],4:["_","_","_","_","_","_","_","_","\n"],5:["_","_","_","_","_","_","_","_","\n"],6:["_","_","_","_","_","_","_","_","\n"],7:["_","_","_","_","_","_","_","_","\n"],8:["_","_","_","_","_","_","_","_","\n"]}
def board():
    os.system('cls')
    print("Computer's board")
    print("\n","A",*cb[1],"B",*cb[2],"C",*cb[3],"D",*cb[4],"E",*cb[5],"F",*cb[6],"G",*cb[7],"H",*cb[8],"  1 2 3 4 5 6 7 8")
    print("Your board")
    print("\n","A",*pb[1],"B",*pb[2],"C",*pb[3],"D",*pb[4],"E",*pb[5],"F",*pb[6],"G",*pb[7],"H",*pb[8],"  1 2 3 4 5 6 7 8")

def cship():
    x=random.choice('ABCDEFGH')
    y=random.choice('12345678')
    z=str(x)+str(y)
    if z in cmove:
        cship()
    else:
        cmove.append(z)
    board()
    print(cmove)
    
def ship1():
    bat=input("Input blank for battleship: ")
    if bat[0] in bh and bat[1] in br : 
        bat2=input("Input 2 blank for battleship: ")
    if (bh.index(bat2[0])==bh.index(bat[0])-1 or bh.index(bat2[0])==bh.index(bat[0])+1 or (bh.index(bat2[0])==bh.index(bat[0]))) and (br.index(bat2[1])==br.index(bat[1])-1 or br.index(bat2[1])==br.index(bat[1])+1 or br.index(bat2[1])==br.index(bat[1]))  :
        pb[bh.index(bat[0])+1][br.index(bat[1])]= "◼"
        pb[bh.index(bat2[0])+1][br.index(bat2[1])]= "◼"
        board()
    else:
        print("invalid input (Note:remember that the square should be a adjecent square)")
        ship1()    
    board()
ship1()
cship()
compare=input("Input blank for compare: ")
if compare in cmove:
    print("true")
def bombing():
    bomb=input("Input blank for bombing: ")
    if bomb in cmove:
        cb[bh.index(bomb[0])+1][br.index(bomb[1])]= "☠"
        board()
    else:
        cb[bh.index(bomb[0])+1][br.index(bomb[1])]= "●"
        board()
x=1
while x==1:
    bombing() 
    
    