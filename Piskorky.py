#piskorky
#strana a pola
#a=int(input('Zadaj dlzku pola: '))

a=3
posrow=[]
poscol=[]
hodnota=[]
def tabulka():
    print('-'*a*2+('-'))
    for p in range(1,a+1):
        print('| '*a+('|'))
    print('-'*a*2+('-'))

for i in range(1,a*a):
    posrow.append(int(input('Zadaj poziciu riadku: ')))
    poscol.append(int(input('Zadaj poziciu stlpcu: ')))
    hodnota.append(str(input('Zadaj hodnotu: ')))
    tabulka()
