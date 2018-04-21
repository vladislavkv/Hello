import random

count = int(input('Введите чсило: '))

lastName = []
firstName = []
middleName = []

file = open('fios.csv', 'r', encoding = 'utf-8')

for line in file:
    mas = line.split(',')
    lastName.append(mas[0])
    firstName.append(mas[0])
    middleName.append(mas[0])

for randomCount in  range(count):
    randomLastName = random.randrange(0,100)
    randomFirstName = random.randrange(0,100)
    randomMiddleName = random.randrange(0,100)
    
    print(lastName[randomLastName],
          firstName[randomFirstName],
          middleName[randomMiddleName])

file.close()
