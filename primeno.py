"""
It is a module to check wheter a number is prime or not
And for finding its factors
"""
def primeno(num):
    f=1
    for i in range(2,int(num/2)+1):
        if num%i==0:
            print(num," is Not Prime")
            f=0
            break
    if f!=0:
        print(num ," is Prime")
        
def factors(num):
    fact=[]
    for i in range(2,int(num/2)+1):
        if num%i==0:
            fact.append(i)
    return fact
