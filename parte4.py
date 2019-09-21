print("digite el numero: ")
def perfect_number(n):
  s=0
  for i in range (1,n+1):
        if n%i==0:
         s=s+i

  if s=n:
    print("is a perfect number")
  else:
    print("is not a perfect number")

n=int(input("digite el numero: "))
is_prime(n)