#poloha je dana z laveho horneho rohu do praveho dolneho rohu
#piskorky
miesto=[]
znak=[]
riadok='|'

pole=int(input('Zadaj velkost pola: '))

for i in range(1, (pole*pole)+1):
 
 pocitadlo=0

 miesto.append(int(input('Zadaj polohu: ')))
 znak.append(str(input('Zadaj znak: ')))
 
 for i in range(1,pole+1):
  #zapise riadok do premennej a kazdy riadok sa vytlaci naraz a nasledne zmaze
  for i in range(1,pole+1):
   pocitadlo=pocitadlo+1
   if pocitadlo in miesto:
    riadok=riadok+znak[miesto.index(pocitadlo)]+('|')
   else:
    riadok=riadok+' |'
  print(riadok)
  riadok='|'
  print('-'*(pole*2+1))