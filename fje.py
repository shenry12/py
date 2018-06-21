import random

def hex_oct2bin(x,HO):
    lista=[]
    listaB=[]

    while x>0:
        lista.insert(0,bin(x%10).lstrip("0b"))
    #print("Z:",bin(x%10).lstrip("0b"))
        x//=10

    #print(lista)

    for i in lista:
    #print("i:",i,"tip:",type(i))
        while len(i)<HO:
            i="0"+i
            #print("i:",i)
        listaB.append(i)
    #print(listaB)
    return stringify(listaB)

def gen_broj(baza,tezina):
    #TEŽINA=DULJINA BROJA
    if tezina==1:
        d=random.randint(2,3)
    elif tezina==2:
        d=random.randint(2,4)
    elif tezina==3:
        d=random.randint(3,5)
    elif tezina==4:
        d=random.randint(3,6)
    elif tezina==5:
        d=random.randint(4,7)
    elif tezina==6:
        d=random.randint(5,8)

    #ODABIR ZNAMENKE PREMA BAZI SUSTAVA
    z=random.randint(0,baza-1)
    broj=[]
    #GENERIRANJE BROJA U LISTU
    for i in range(d):
        broj.append(str(random.randint(0,baza-1)))
    #print(broj)

    if baza==16: #zamjena brojeva u slova za hex brojevni sustav
        broj = [w.replace('10', 'A') for w in broj]
        broj = [w.replace('11', 'B') for w in broj]
        broj = [w.replace('12', 'C') for w in broj]
        broj = [w.replace('13', 'D') for w in broj]
        broj = [w.replace('14', 'E') for w in broj]
        broj = [w.replace('15', 'F') for w in broj]
    #print(broj)

    #LISTA U STRING PA RETURN INT
    #str_broj=""
    #for i in broj:
    #    str_broj+=i
    #return str_broj

    return stringify(broj)

def stringify(lista): #pretvaranje liste u string - string jer int gubi vodeće nule za pojedinu znamenku
    str_broj=""
    for i in lista:
        str_broj+=i
    return str_broj

def provjera_rjesenja(x,y,bazaX,bazaY):
    if bazaX==8:
        tempX=hex_oct2bin(x,3)
    elif bazaX==16:
        #print("X:",x)
        x=x.replace("A","10")
        x=x.replace("B","11")
        x=x.replace("C","12")
        x=x.replace("D","13")
        x=x.replace("E","14")
        x=x.replace("F","15")
        #print("X:",x)
        tempX=hex_oct2bin(int(x),4)
    #print("X:",tempX,"Y:",y)
    if tempX==y:
        print(tempX,"==",y)
        print("\nTočno rješenje")
    else:
        print("\nNetočno rješenje\nUnesena vrijednost:",y,"\nTočno rješenje:",tempX,)
