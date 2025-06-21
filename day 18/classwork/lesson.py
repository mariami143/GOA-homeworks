Num = int(input('please input a number: '))
sum = 0
for i in range(1,Num):
   sum = sum + i
print(sum)



Num = int(input('please input a number: '))
sum = 0
for i in range(1,Num,2):
   sum = sum + i
print(sum)




password = 'Group60123'
guess = input('please try to guess the password: ')
while guess != password:
    guess = input('Incorrect! Please try again: ')
print('Correct!')


count = 1
while count < 100:
   print (count)
   count = count + 2