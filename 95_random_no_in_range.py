#95. Program to generate random numbers within ‘n’ range
import random
a,b=eval(input("Enter the range(from,to):"))
rand_no=random.randint(a,b)
print("Random no between {},{} :{}".format(a,b,rand_no))


#print(random.uniform(12.5,19.7))#to get a random floating point number