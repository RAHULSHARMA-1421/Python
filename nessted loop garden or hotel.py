def terraced():
    print("terraced garden")
def japanese():
    print("japanese garden")    
def pinjore():
    print("pinjore garden")   
def chandigarh():
    print("chandigarh")
    u1=int(input("press 1 for terraced press 2 for japnese press 3 for pinjore:"))
if u1==1:
    terraced()
elif u1==2:
    japanese()
elif u1==3:
    pinjore()
else:
    print("wrong key entered")



def kanak():
    print("kanakvrindavan garden")
def jawahar():
    print("jawahar circle garden")   
def jai():
    print("jai niwas garden")   
def jaipur():
    print("jaipur")
    u2=int(input("press 1 for kanak press 2 for jawahar press 3 for jai:"))
if u2==1:
    kanak()
elif u2==2:
    jawahar()
elif u2==3:
    jai()
else:
    print("wrong key entered")


def shalimar():
    print("shalimarbaghmughal garden")
def indira():
    print("indiragandhi memorial tulip garden")    
def chashma():
    print("chashmashahi garden")   
def srinagar():
    print("srinagar")
    u3=int(input("press 1 for shalimar press 2 for indira press 3 for chashma:"))
if u3==1:
    shalimar()
elif u3==2:
    indira()
elif u3==3:
    chashma()
else:
    print("wrong key entered")


def hyatt():
    print("hyatt hotel")
def oberoi():
    print("oberoi hotel")
def novotel():
    print("novotel hotel")
def India():
    print("India")
    u4=int(input("press 1 for hyatt press 2 for oberoi press 3 for novotel :"))
    if u4==1:
        hyatt()
    elif u4==2:
        oberoi()
    elif u4==3:
        novotel()
    else:
        print("enter wrong key")


def doubletree():
    print("doubletree")
def hakalodge():
    print("hakalodge")
def rainforest():
    print("rainforest")
def NewZealand():
    print("NewZealand")
    u5=int(input("press 1 for doubletree press 2 for hakalodge press 3 for rainforest :"))
    if u5==1:
        doubletree()
    elif u5==2:
        hakalodge()
    elif u5==3:
        rainforest()
    else:
        print("enter wrong key")

user=int(input("press 1 for chandigarh press 2 for jaipur press 3 for srinagar pess 4 for India press 5 for NewZealand:"))

if user==1:
    chandigarh()
elif user==2:
    jaipur()
elif user==3:
    srinagar()
elif user==4:
    India()
elif user==5:
    NewZealand()
else:
    print("wrong keyword")
