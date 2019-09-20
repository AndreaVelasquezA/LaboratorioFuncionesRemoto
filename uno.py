base=int(input("digite la base del numero: ")) 
expo=int(input("digite el exponente del numero: ")) 

 
def a_power_b(base,expo): 
    num=1

while base!=0:
    base=int(input("digite la base del numero: ")) 
    expo=int(input("digite el exponente del numero: ")) 

        for i in range (1,expo+1): 
            pot=pot*base 


return pot
y=a_power_b(base,expo) 
print(y) 