import random

class Game:

    p1=0
    p2=0

    def roll(die):
        if die==4:
            value=random.randint(1,4)                   #random command followed by random integer(range)
            return value
        if die==6:
            value=random.randint(1,6)
            return value
        if die==8:
            value=random.randint(1,8)
            return value
        if die==10:
            value=random.randint(1,10)
            return value
        if die==12:
            value=random.randint(1,12)
            return value
        if die==20:
            value=random.randint(1,20)
            return value
        if die==100:
            value=random.randint(1,100)
            return value



    def player():
        die=int(input("Select your die!: 4,6 or 8:"))
        print("____________________")
        result=Game.roll(die)
        Game.p1+=result


    def computer():
        diecount=random.randint(1,3)
        if diecount==1:
            die=4
        elif diecount==2:
            die=6
        elif diecount==3:
            die=8
        result=Game.roll(die)
        Game.p2+=result





turn=0
print("The first to 10 or more wins!")

while turn <=2:
    Game.player()
    Game.computer()
    print("your total is:", Game.p1)
    print("comp total is:", Game.p2)
    print("_______________________")
    print("Next round!")
    turn+=1

print("_______________________")
print("Game Over!!!")


if Game.p1 > Game.p2:
    print("You win!")
if Game.p2 > Game.p1:
    print("You loose!")