import random
lettere=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','i','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
lunghezza=input('quanto dev, essere lunga la password?')
lunghezza=int(lunghezza)
a=0
passwort=''
while a<lunghezza:
  passwort=passwort+(lettere[random.randint(0,len(lettere)-1)])
  a=a+1
print(passwort)
  