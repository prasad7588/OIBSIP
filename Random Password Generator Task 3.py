import random

while True:
    a=["sfdrst","yegey","gsyug","gedfyweg","gdyeg"]
    b=["!@fgS","()&(*^)",")(*(*))","!@#$%","G&^&^","%$#%"]

    a1=int(input("***enter the type of password *** \n1]low \n2]medium \n3]high \n"  ))
    if a1==1:
        c=random.choice(a)
        print(f'your password is :-{c}')

    if a1==2:
        a+=["DD@#Q#W","F$#^$","^%&^$R","@#$@#","#@#S#$"]
        d=random.choice(a)
        print(f'your password is :-{d}')

    if a1==3:
        b+=["DD@#Q#W","F$#^$","^%&^$R","@#$@#","#@#S#$"]
        e=random.choice(b)
        print(f'your password is :-{e}')

    con=input("you want to continue yes/no :-")   
    if con.lower()!="yes":
        break
    print("****** THANKS ******")