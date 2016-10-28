# Prime Numbers from 0 to n
#Prime Numbers defined
#Lower and upper numbers can change
lower = 2
upper = 50
print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   if num > 0:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)