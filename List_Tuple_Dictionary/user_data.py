'''write a program which make a list of cities chosen by adults
and print which person has chosen which city'''

persons = ['thor','hella','oden','loki']
cities = []
for i in range(0,2):
    print()
    print("Name:",persons[i])
    age = persons[i] = int(input("Age: "))
    sex = persons[i] = input("Gender: ")
    location = persons[i] = input("Location: ")
    if age > 18:
        persons = ['thor','hella','oden','loki']
        print("Welcome",persons[i])
        city = input("Choose a city: ")
        cities.append(city)
    print("City selected by",persons[i],"is",city)
print("\nCities selected by adults:", cities)