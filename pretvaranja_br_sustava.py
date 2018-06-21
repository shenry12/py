import random
import fje
bodovi=0
t=1

#RANDOM ODABIR DULJINE BROJA
def bin_duljina():
    d=random.randint(2,8)
    return d

#RANDOM ODABIR POJEDINE ZNAMENKE
def bin_znamenka():
    z=random.randint(0,1)
    return z

#FUNKCIJA ZA SLAGANJE BIN BROJA
def bin_broj():
    global broj
    broj=''
    for i in range(0,bin_duljina()):
      broj+=str(bin_znamenka())

    if broj[0]=='0':
        while broj[0]=='0':
            kraj=len(broj)
            broj=broj[1:kraj]

    #if broj[0]=='0':
     #   print("A",broj)
     #   broj=broj[1:kraj]
     #   print("B",broj)

    broj='0b'+broj
   # print("C",broj)

    return broj

#BINARNI U DEKADSKI
def bin_dek():
    binarni=bin_broj()
    kraj=len(binarni)
    print("Pretvori ",binarni[2:kraj],"(2) u dekadski (10)")
    dekadski=int(input())
    dek2bin=str(bin(dekadski))
   #print("binarni=",binarni,"\ndek2bin=",dek2bin)
    if dek2bin==binarni:
        print(dek2bin,"==",binarni)
        global bodovi
        bodovi+=1
        izbornik()
    else:
        print(dek2bin,"!=",binarni)
        izbornik()

def dek_okt3(dekadski):

    d=len(dekadski)
    br=''

    for i in range(0,d):
        #print(dekadski[i])
        #print(bin(int(dekadski[i])))
        br=br+str(bin(int(dekadski[i])))
        br=br.replace("0b","")

    return "0b"+br

#BINARNI U OKTALNI
def bin_okt():
    binarni=bin_broj()
    print("Pretvori ",binarni[2:],"(2) u oktalni (8)")
    dekadski=input()

    dek2okt=dek_okt3(dekadski)

    #print("binarni=",binarni,"\ndek2okt=",dek2okt)
    if dek2okt==binarni:
        print(dek2okt,"==",binarni)
        global bodovi
        bodovi+=1
        izbornik()
    else:
        print(dek2okt,"!=",binarni)
        izbornik()

#DEKADSKI U BINARNI
def dek_bin():
    dekadski=random.randrange(1,1024)
    print("Pretvori ",dekadski,"(10) u binarni (2)")
    binarni=str(input())
    dek2bin=str(bin(dekadski))
    binarni="0b"+binarni
    if dek2bin==binarni:
        print(dek2bin,"==",binarni)
        global bodovi
        bodovi+=1
        izbornik()
    else:
        print(dek2bin,"!=",binarni)
        izbornik()


#DEKADSKI U HEKSADEKADSKI
def dek_hek():
	dekadski=random.randrange(1,1024)
	print("Pretvori ",dekadski,"(10) u heksadekadski (16)")
	heksadekadski=str(input())
	dek2hex=str(hex(dekadski))
	heksadekadski="0x"+heksadekadski
	if dek2hex==heksadekadski:
		print(dek2hex,"==",heksadekadski)
		global bodovi
		bodovi+=1
		izbornik()
	else:
		print(dek2hex,"!=",heksadekadski)
		izbornik()

#DEKADSKI U OKTALNI
def dek_okt():
	dekadski=random.randrange(1,1024)
	print("Pretvori ",dekadski,"(10) u oktalni (8)")
	oktalni=input() #staro oktalni=str(input())
	dek2okt=oct(dekadski) #staro oktalni=str(input())
	oktalni="0o"+oktalni

	if dek2okt==oktalni:
		print(dek2okt,"==",oktalni)
		global bodovi
		bodovi+=1
		izbornik()
	else:
		print(dek2okt,"!=",oktalni)
		izbornik()

def okt_bin():
    oktalni=int(fje.gen_broj(8,t))
    #print(fje.hex_oct2bin(int(oktalni),3))
    print("Pretvoriti",oktalni,"(8) u binarni (2)\nObvezno unijeti vodeće nule")
    binarni=input("Unos: ")
    #print(type(oktalni))
    #print(type(binarni))
    fje.provjera_rjesenja(oktalni,binarni,8,2)

def hex_bin():
    hexadekadski=(fje.gen_broj(16,t))
    print("Pretvoriti",hexadekadski,"(16) u binarni (2)\nObvezno unijeti vodeće nule")
    binarni=input("Unos: ")
    fje.provjera_rjesenja(hexadekadski,binarni,16,2)

#IZBORNIK
def izbornik():
    global t

    print("Trenutni bodovi:",bodovi)
    odabir=input("Odaberi tip zadatka:\n1. Dekadski u binarni\n2. Dekadski u heksadekadski\n3. Dekadski u oktalni\n4. Binarni u dekadski\n5. Binarni u oktalni\n6. Oktalni u binarni\n7. Heksadekadski u binarni\n8. TEST GEN-BIN\n9. TEST GEN-DEK\n0. TEST GEN-HEX\n")

    if odabir=='1':
        dek_bin()
    elif odabir=='2':
        dek_hek()
    elif odabir=='3':
        dek_okt()
    elif odabir=='4':
        bin_dek()
    elif odabir=='5':
        bin_okt()
    elif odabir=="6":
        okt_bin()
    elif odabir=="7":
        hex_bin()           #POPRAVITIhex_oct2bin jer ne radi za dvoznamenkaste hex brojeve
    elif odabir=="8":
        fje.gen_broj(2,t)
    elif odabir=="9":
        fje.gen_broj(10,t)
    elif odabir=="0":
        fje.gen_broj(16,t)
    else:
        print("Nedozvoljen odabir.")
        izbornik()

izbornik()
