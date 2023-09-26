import random

szam = random.randint(1,3)

szam1=str(input('Válasz kő, papir vagy olló válasz:'))

#kő
if szam1=='kő' and szam==1:
    print(f'Gép válasza:{szam}')
    print('mind a ketten követ választotatok így ez döntetlen')
    
#papir    
if szam1=='papir' and szam==2:
    print(f'Gép válasza:{szam}')
    print('mind a ketten papirt választotatok így ez döntetlen')
    
#olló    
if szam1=='olló' and szam==3:
    print(f'Gép válasza:{szam}')
    print('mind a ketten ollót választotatok így ez döntetlen')
    
    
#olló papir    
if szam1=='olló' and szam==2 or szam1=='papir' and szam==3:
    print(f'Gép válasza:{szam}')
    print('Az olló nyert')
    
if szam1=='kő' and szam==3 or szam1=='olló' and szam==1:
    print(f'Gép válasza:{szam}')
    print("A kő nyert!")
#kő papír
if szam1=='kő' and szam==2 or szam1=='papir' and szam==1:
    print(f'Gép válasza:{szam}')
    print("A papír nyert!")    
    
    
    
    
    
    
    
