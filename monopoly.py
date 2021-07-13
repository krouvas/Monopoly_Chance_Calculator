##breaking monopoly
#Kyriacos Rouvas
#import modules
from random import randint
import msvcrt as m

##variable dictionary
#10 players
ippiko={"Position":0,"PosLog":[0],"Lefta": 1500,"Property":[],"PrisStat":0}
kanoni={"Position":0,"PosLog":[0],"Lefta": 1500,"Property":[],"PrisStat":0}
autokinito={"Position":0,"PosLog":[0],"Lefta": 1500,"Property":[],"PrisStat":0}
karotsoui={"Position":0,"PosLog":[0],"Lefta": 1500,"Property":[],"PrisStat":0}
arvila={"Position":0,"PosLog":[0],"Lefta": 1500,"Property":[],"PrisStat":0}
daxtilistra={"Position":0,"PosLog":[0],"Lefta": 1500,"Property":[],"PrisStat":0}
siero={"Position":0,"PosLog":[0],"Lefta": 1500,"Property":[],"PrisStat":0}
shillos={"Position":0,"PosLog":[0],"Lefta": 1500,"Property":[],"PrisStat":0}
sombrero={"Position":0,"PosLog":[0],"Lefta": 1500,"Property":[],"PrisStat":0}
varka={"Position":0,"PosLog":[0],"Lefta": 1500,"Property":[],"PrisStat":0}
playerlist=[ippiko,kanoni,autokinito,karotsoui,arvila,daxtilistra,siero,shillos,sombrero,varka]

i=0 #iterator
maxiter=0

#position variables
pos00=0
pos01=0
pos02=0
pos03=0
pos04=0
pos05=0
pos06=0
pos07=0
pos08=0
pos09=0
pos10=0
pos11=0
pos12=0
pos13=0
pos14=0
pos15=0
pos16=0
pos17=0
pos18=0
pos19=0
pos20=0
pos21=0
pos22=0
pos23=0
pos24=0
pos25=0
pos26=0
pos27=0
pos28=0
pos29=0
pos30=0
pos31=0
pos32=0
pos33=0
pos34=0
pos35=0
pos36=0
pos37=0
pos38=0
pos39=0

#prob dictionary & priority # dictionary
probDict={}
prioNumDict={}
prioNumDictDbled={"1":[],"3":[],"6":[],"8":[],"9":[],"11":[],"13":[],"14":[],"16":[],"18":[],"19":[],"21":[],"23":[],"24":[],"26":[],"27":[],"29":[],"31":[],"32":[],"34":[],"37":[],"39":[]}


##function distionary
#two dice function w/ indication for double outcomes
def ddiceRoll():
    dice1=randint(1,6)
    dice2=randint(1,6)
    total=dice1+dice2
    if dice1==dice2:
        dbles=True
    else:
        dbles=False
    
    return total, dbles

# waiting for key press
def PressKey():
    print("Press Any Key to Close Program")
    m.getch()


##probability data gathering loop                               
maxiter=int(input("# of rounds ")) #get iter #

while i<=maxiter:   #rounds
    for player in playerlist:  #turns
        if player["PrisStat"]==0: #check for prison
            move,dbles=ddiceRoll()
            pos=player["Position"]
            pos+=move
            pos=pos%40
            if pos==30:
                player["Position"]=10
                player["PrisStat"]=3
                player["PosLog"].append(player["Position"])
                continue
            else:
                player["Position"]=pos
                player["PosLog"].append(player["Position"])
            
            if dbles==True: #dble 2
                move,dbles=ddiceRoll()
                pos=player["Position"]
                pos+=move
                pos=pos%40
                if pos==30:
                    player["Position"]=10
                    player["PrisStat"]=3
                    player["PosLog"].append(player["Position"])
                    continue
                else:
                    player["Position"]=pos
                    player["PosLog"].append(player["Position"])

                if dbles==True: #dble 3
                    player["Position"]=10
                    player["PrisStat"]=3
                    player["PosLog"].append(player["Position"])
                    continue


        
        elif player["PrisStat"]>0:
            if player["PrisStat"]==3:
                move,dbles=ddiceRoll()
                if dbles==True:
                    player["PrisStat"]=1
                    player["PosLog"].append(player["Position"])
                else:
                    player["PrisStat"]=2
                    player["PosLog"].append(player["Position"])

            elif player["PrisStat"]==2:
                move,dbles=ddiceRoll()
                if dbles==True:
                    player["PrisStat"]=0
                    player["PosLog"].append(player["Position"])
                else:
                    player["PrisStat"]=1
                    player["PosLog"].append(player["Position"])

            else:
                move,dbles=ddiceRoll()
                if dbles==True:
                    player["PrisStat"]=0
                    move,dbles=ddiceRoll()
                    pos=player["Position"]
                    pos+=move
                    pos=pos%40
                    player["Position"]=pos
                    player["PosLog"].append(player["Position"])
                else:
                    player["PrisStat"]=0
                    player["PosLog"].append(player["Position"])

    i+=1

print("end")


#collect position data
for player in playerlist:
    pos00+=player["PosLog"].count(0)
    pos01+=player["PosLog"].count(1)
    pos02+=player["PosLog"].count(2)
    pos03+=player["PosLog"].count(3)
    pos04+=player["PosLog"].count(4)
    pos05+=player["PosLog"].count(5)
    pos06+=player["PosLog"].count(6)
    pos07+=player["PosLog"].count(7)
    pos08+=player["PosLog"].count(8)
    pos09+=player["PosLog"].count(9)
    pos10+=player["PosLog"].count(10)
    pos11+=player["PosLog"].count(11)
    pos12+=player["PosLog"].count(12)
    pos13+=player["PosLog"].count(13)
    pos14+=player["PosLog"].count(14)
    pos15+=player["PosLog"].count(15)
    pos16+=player["PosLog"].count(16)
    pos17+=player["PosLog"].count(17)
    pos18+=player["PosLog"].count(18)
    pos19+=player["PosLog"].count(19)
    pos20+=player["PosLog"].count(20)
    pos21+=player["PosLog"].count(21)
    pos22+=player["PosLog"].count(22)
    pos23+=player["PosLog"].count(23)
    pos24+=player["PosLog"].count(24)
    pos25+=player["PosLog"].count(25)
    pos26+=player["PosLog"].count(26)
    pos27+=player["PosLog"].count(27)
    pos28+=player["PosLog"].count(28)
    pos29+=player["PosLog"].count(29)
    pos30+=player["PosLog"].count(30)
    pos31+=player["PosLog"].count(31)
    pos32+=player["PosLog"].count(32)
    pos33+=player["PosLog"].count(33)
    pos34+=player["PosLog"].count(34)
    pos35+=player["PosLog"].count(35)
    pos36+=player["PosLog"].count(36)
    pos37+=player["PosLog"].count(37)
    pos38+=player["PosLog"].count(38)
    pos39+=player["PosLog"].count(39)



#building probability data
sumed=(pos00+pos01+pos02+pos03+pos04+pos05+pos06+pos07+pos08+pos09+pos10+pos11+pos12+pos13+pos14+pos15+pos16+pos17+pos18+pos19+pos20+pos21+pos22+pos23+pos24+pos25+pos26+pos27+pos28+pos29+pos30+pos31+pos32+pos33+pos34+pos35+pos36+pos37+pos38+pos39)

probs=[pos00/sumed,pos01/sumed,pos02/sumed,pos03/sumed,pos04/sumed,pos05/sumed,pos06/sumed,pos07/sumed,pos08/sumed,pos09/sumed,pos10/sumed,pos11/sumed,pos12/sumed,pos13/sumed,pos14/sumed,pos15/sumed,pos16/sumed,pos17/sumed,pos18/sumed,pos19/sumed,pos20/sumed,pos21/sumed,pos22/sumed,pos23/sumed,pos24/sumed,pos25/sumed,pos26/sumed,pos27/sumed,pos28/sumed,pos29/sumed,pos30/sumed,pos31/sumed,pos32/sumed,pos33/sumed,pos34/sumed,pos35/sumed,pos36/sumed,pos37/sumed,pos38/sumed,pos39/sumed]

##building dictionaries
#probability dictionary
c=0
for k in probs:
    probDict[str(c)]=k
    c+=1



#priority number dictionary
prioNumDict={"1":[60/(probDict["1"]*2),110/(probDict["1"]*10),160/(probDict["1"]*30),210/(probDict["1"]*90),260/(probDict["1"]*160),310/(probDict["1"]*250)],
    "3":[60/(probDict["3"]*4),110/(probDict["3"]*20),160/(probDict["3"]*60),210/(probDict["3"]*180),260/(probDict["3"]*320),310/(probDict["3"]*450)],
    "6":[100/(probDict["6"]*6),150/(probDict["6"]*30),200/(probDict["6"]*90),250/(probDict["6"]*270),300/(probDict["6"]*400),350/(probDict["6"]*550)],
    "8":[100/(probDict["8"]*6),150/(probDict["8"]*30),200/(probDict["8"]*90),250/(probDict["8"]*270),300/(probDict["8"]*400),350/(probDict["8"]*550)],
    "9":[120/(probDict["9"]*8),170/(probDict["9"]*40),220/(probDict["9"]*100),270/(probDict["9"]*300),320/(probDict["9"]*450),370/(probDict["9"]*600)],
    "11":[140/(probDict["11"]*10),240/(probDict["11"]*50),340/(probDict["11"]*150),440/(probDict["11"]*450),540/(probDict["11"]*625),640/(probDict["11"]*750)],
    "13":[140/(probDict["13"]*10),240/(probDict["13"]*50),340/(probDict["13"]*150),440/(probDict["13"]*450),540/(probDict["13"]*625),640/(probDict["13"]*750)],
    "14":[160/(probDict["14"]*12),260/(probDict["14"]*60),360/(probDict["14"]*180),460/(probDict["14"]*500),560/(probDict["11"]*700),660/(probDict["14"]*900)],
    "16":[180/(probDict["16"]*14),280/(probDict["16"]*70),380/(probDict["16"]*200),480/(probDict["16"]*550),580/(probDict["16"]*750),680/(probDict["16"]*950)],
    "18":[180/(probDict["18"]*14),280/(probDict["18"]*70),380/(probDict["18"]*200),480/(probDict["18"]*550),580/(probDict["18"]*750),680/(probDict["18"]*950)],
    "19":[200/(probDict["19"]*16),300/(probDict["19"]*80),400/(probDict["19"]*220),500/(probDict["19"]*600),600/(probDict["19"]*800),700/(probDict["19"]*1000)],
    "21":[220/(probDict["21"]*18),370/(probDict["21"]*90),520/(probDict["21"]*250),670/(probDict["21"]*700),820/(probDict["21"]*875),970/(probDict["21"]*1050)],
    "23":[220/(probDict["23"]*18),370/(probDict["23"]*90),520/(probDict["23"]*250),670/(probDict["23"]*700),820/(probDict["23"]*875),970/(probDict["23"]*1050)],
    "24":[240/(probDict["24"]*20),390/(probDict["24"]*100),540/(probDict["24"]*300),690/(probDict["24"]*750),840/(probDict["24"]*925),990/(probDict["24"]*1100)],
    "26":[260/(probDict["26"]*22),410/(probDict["26"]*110),560/(probDict["26"]*330),710/(probDict["26"]*800),860/(probDict["26"]*975),1010/(probDict["26"]*1150)],
    "27":[260/(probDict["27"]*22),410/(probDict["27"]*110),560/(probDict["27"]*330),710/(probDict["27"]*800),860/(probDict["27"]*975),1010/(probDict["27"]*1150)],
    "29":[280/(probDict["29"]*24),430/(probDict["29"]*120),580/(probDict["29"]*360),730/(probDict["29"]*850),880/(probDict["29"]*1025),1030/(probDict["29"]*1200)],
    "31":[300/(probDict["31"]*26),500/(probDict["31"]*130),700/(probDict["31"]*390),900/(probDict["31"]*900),1100/(probDict["31"]*1100),1300/(probDict["31"]*1275)],
    "32":[300/(probDict["32"]*26),500/(probDict["32"]*130),700/(probDict["32"]*390),900/(probDict["32"]*900),1100/(probDict["32"]*1100),1300/(probDict["32"]*1275)],
    "34":[320/(probDict["34"]*28),520/(probDict["34"]*150),720/(probDict["34"]*450),920/(probDict["34"]*1000),1120/(probDict["34"]*1200),1320/(probDict["34"]*1400)],
    "37":[350/(probDict["37"]*35),550/(probDict["37"]*175),750/(probDict["37"]*500),950/(probDict["37"]*1100),1150/(probDict["37"]*1300),1350/(probDict["37"]*1500)],
    "39":[400/(probDict["39"]*50),600/(probDict["39"]*200),800/(probDict["39"]*600),1000/(probDict["31"]*1400),1200/(probDict["39"]*1700),1400/(probDict["39"]*2000)]}

#priority number dictionary for double values
for k in [1,3,6,8,9,11,13,14,16,18,19,21,23,24,26,27,29,31,32,34,37,39]:
    for j in prioNumDict[str(k)]:
        prioNumDictDbled[str(k)].append(j/2)


#show results
print("pos 00")
print(pos00)
print("pos 01")
print(pos01)
print("pos 02")
print(pos02)
print("pos 03")
print(pos03)
print("pos 04")
print(pos04)
print("pos 05")
print(pos05)
print("pos 06")
print(pos06)
print("pos 07")
print(pos07)
print("pos 08")
print(pos08)
print("pos 09")
print(pos09)
print("pos 10")
print(pos10)
print("pos 11")
print(pos11)
print("pos 12")
print(pos12)
print("pos 13")
print(pos13)
print("pos 14")
print(pos14)
print("pos 15")
print(pos15)
print("pos 16")
print(pos16)
print("pos 17")
print(pos17)
print("pos 18")
print(pos18)
print("pos 19")
print(pos19)
print("pos 20")
print(pos20)
print("pos 21")
print(pos21)
print("pos 22")
print(pos22)
print("pos 23")
print(pos23)
print("pos 24")
print(pos24)
print("pos 25")
print(pos25)
print("pos 26")
print(pos26)
print("pos 27")
print(pos27)
print("pos 28")
print(pos28)
print("pos 29")
print(pos29)
print("pos 30")
print(pos30)
print("pos 31")
print(pos31)
print("pos 32")
print(pos32)
print("pos 33")
print(pos33)
print("pos 34")
print(pos34)
print("pos 35")
print(pos35)
print("pos 36")
print(pos36)
print("pos 37")
print(pos37)
print("pos 38")
print(pos38)
print("pos 39")
print(str(pos39) +"\n")

print("sum\n")
print(str(sumed) +"\n")

print("all probabilities\n")
print(str(probDict) +"\n")
print("priority numbers\n")
print(str(prioNumDict) +"\n")
print("priority numbers with double gains\n")
print(prioNumDictDbled)

PressKey() #gives user a chance to copy data