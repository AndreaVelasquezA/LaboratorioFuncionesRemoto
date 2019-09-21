print("digite el numero: ")
def is_prime(n):
  div=0

for i in range (1,n+1):
    if n%i==0:
         div=div+1
        if n>0:
          if div<=2:
            print("1")
          else:
            print("2")
  else:
    print("sorry")


n=int(input("digite el numero: "))

is_prime(n)