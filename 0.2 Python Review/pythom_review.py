import random

temperatures = []

days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

even_temperature = []
odd_temperature = []

avg_temp = []

for i in range(7):
    temperatures.append(random.randint(26, 41))
print(temperatures)


for temp in temperatures:
    if temp % 2 == 1:
        odd_temperature.append(temp)

    else:
        even_temperature.append(temp)

good_days_count = 0 

for i in range(7):
    if temperatures[i] % 2 == 0: 
        good_days_count = good_days_count +1

print ("the number of good days are: " , good_days_count)
    

highest_temp = temperatures[0]
highest_day = days_of_the_week[0]
for i in range(7):
    if highest_temp < temperatures[i]:
        highest_temp = temperatures[i]
        highest_day = days_of_the_week[i]


print("highest temperature is: ",highest_temp)
print("highest temperuture day is:", highest_day)



lowest_temp = temperatures[0] 
lowest_day = days_of_the_week[0]     
for i in range(7):
    if lowest_temp > temperatures[i]:
        lowest_temp = temperatures[i]
        lowest_day = days_of_the_week[i]

print("lowest temperature is: ", lowest_temp)
print("lowest temperature day is:", lowest_day)

avg_temp = temperatures[0]
for i in range[7]:
    avg_temp=sum(temperatures)/ 7
temperature / 7 = avg_temp

print("The average temperatureis: ",avg_temp)
