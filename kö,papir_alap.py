szam1=str(input('kő, papir vagy olló válasz(1):'))
szam2=str(input('kő, papir vagy olló válasz(2):'))

#kő
if szam1=='kő' and szam2=='kő':
    print('mind a ketten követ választotatok így ez döntetlen')
    
#papir    
if szam1=='papir' and szam2=='papir':
    print('mind a ketten papirt választotatok így ez döntetlen')
    
#olló    
if szam1=='olló' and szam2=='olló':
    print('mind a ketten ollót választotatok így ez döntetlen')
    
    
#olló papir    
if szam1=='olló' and szam2=='papir' or szam1=='papir' and szam2=='olló':
    print('Az olló nyert')


