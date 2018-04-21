file = open('people.csv', 'r', encoding = 'utf-8')

regionDifference = []
regions = []

regoin = ''
population = 0
women = 0
men = 0
difference = 0

for line in file:
    mas = line.split(',')
    regionPopulation = 0
    for a in range(1, len(mas)):
        regionPopulation += int(mas[a])
        population += int(mas[a])
        if a == 1 or a == 2 or a == 3:
            men += int(mas[a])
        else:
            women += int(mas[a])
    regionDifference.append(regionPopulation)
    regions.append(mas[0])
    
maxIndex = regionDifference.index(max(regionDifference))

print('Мужчин -', men)
print('Женщин -', women)
print('Всего -', population)

if men > women:
    difference = men - women
    print('Мужчин больше чем женщин на', difference, 'человек')
else:
    difference = women - men
    print('Женщин больше чем мужчин на', difference, 'человек')

print('Область, в которой больше всего численнсоть населения -', regions[maxIndex])

file.close()
