try:
    base=int(input("digite la base del numero: ")) 
except ValueError:
    print("las letras no tienen potencia")
try:           
    expo=int(input("digite el exponente del numero: ")) 
except ValueError:
    print("las letras no tienen potencia")
def a_power_b(base,expo): 
    pot=1

    for i in range (1,expo+1): 

        pot=pot*base 

    return pot 




y=a_power_b(base,expo) 

print(y) 