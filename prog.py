import foiz

print("Salom")

stringS=int(input("Bankdagi pul qiymatini kiriting:  "))
 
#S=int(stringS)

p=30

while p<0 or p>25:
 p=int(input("Foiz qiymatini kiriting:  "))
 #p=int(a)
foiz.bank_foiz(stringS,p)

S=input("")
