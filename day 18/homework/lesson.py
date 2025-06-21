for i in range (1, 100):
    print (i)


count = 1
while count < 50:
    print(count)
    count = count + 2




password = '0143'
guess = input('please try to guess the password: ')
while guess != password:
    guess = input('Incorrect! Please try again: ')
print('Correct!')