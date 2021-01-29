import random
import sys

teamCount = int(input("Enter number of teams participating : "))
roles = ["ADC","SP","MID","JG","TOP"]
teams = [[["0" for a in range (2)] for b in range (5)] for c in range (teamCount)]

#print("Enter list (Press Ctrl+Z after you press Return/Enter) : ")
#ignInput = sys.stdin.read()
ignInput = """a2z (P4)
Helios (G1)
YanSolo (Unranked, S2-G4 potential)
Kaspian (G4)
DejaVuu (G4)
ThE HuLkK (S4)
AceAlpha7 (B2)
SirMuaj (G3)
Kanababa107 (G3)
EteRnaLouGe (S4)
shababkobir (S4)
kid_McTavish (G4)
iamafukingameboy (S4)
DarkDevilAmio (B2)
Arminius (S2)
MoonBIade (Unranked)
teemo was here (G4)
ItsAdreedFFS (S4)
0mega Sreash (P4)
etos (S2)
Phatman (S1)
CAP.PIKHANA (D4)
GracesSecret (P4)
Eagle Eyee 10 (S3)
Mahathir (G3)
KennyBennyOwO (S4)
Moin Pagla (S3)
Ironclad (S3)
0mega Wolfpack (G1)
Dianamyte (P4)"""
ign = ignInput.splitlines()
#print(ign)

"""Setting roles"""
for d in range (len(teams)):
    for e in range (len(teams[d])):
        teams[d][e][1] = e
            
"""Randomizing names"""
for d in range (len(teams)):
    for e in range (len(teams[d])):
        for f in range (len(teams[d][e])):
            match = False
            while teams[d][e][0]=="0":
                randomnum = random.randint(0,len(ign)-1)
                for g in range(len(teams)):
                    for h in range(len(teams[g])):
                        if randomnum == teams[g][h][0]:
                            match=True
                            break
                        else:
                            match=False
                    if match:
                        break
                if match:
                    continue
                teams[d][e][0] = randomnum

"""Printing"""

for a in range (len(teams)):
    for b in range (len(teams[a])):
        printer = roles[teams[a][b][1]] + " - " + ign[teams[a][b][0]]
        print(printer)
    print()

"""TEST FOR 0 REDUNDANCY"""
"""
for a in range(30):
    for d in range (6):
        for e in range (5):
            b = False
            if teams[d][e][0] == a:
                print(a)
                b = True
                break
        if b :
            break
"""


"""
a2z (P4)
Helios (G1)
YanSolo (Unranked, S2-G4 potential)
Kaspian (G4)
DejaVuu (G4)
ThE HuLkK (S4)
AceAlpha7 (B2)
SirMuaj (G3)
Kanababa107 (G3)
EteRnaLouGe (S4)
shababkobir (S4)
kid_McTavish (G4)
iamafukingameboy (S4)
DarkDevilAmio (B2)
Arminius (S2)
MoonBIade (Unranked)
teemo was here (G4)
ItsAdreedFFS (S4)
0mega Sreash (P4)
etos (S2)
Phatman (S1)
CAP.PIKHANA (D4)
GracesSecret (P4)
Eagle Eyee 10 (S3)
Mahathir (G3)
KennyBennyOwO (S4)
Moin Pagla (S3)
Ironclad (S3)
0mega Wolfpack (G1)
Dianamyte (P4)
"""
