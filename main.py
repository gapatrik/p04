# Írj programot, mely beolvas három egész számot, és kiírja a képernyőre a legkisebbet!
szam = int(input(' adjá számot: '))
szam1 = int(input('még 1-et teso: '))
szam2 = int(input('adj meg egy utso számot:'))

if szam < szam1 < szam:
  print('első legkisebb')

elif szam1 > szam > szam2:
  print('harmadik szam a legkissebb')

else :
  print('második szam a legkissebb')