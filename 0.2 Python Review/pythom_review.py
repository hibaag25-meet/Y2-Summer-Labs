import random

temperature = []
GoodDaysCounter = 0

for _ in range(7):
    RandomTemp = random.randint(26,40)
    temperature.append(RandomTemp)

DaysOfTheWeek = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

DaysWithEvenTemperature = []

for i in range(7):
    if temperature[i] % 2 == 0:
        DaysWithEvenTemperature.append(DaysOfTheWeek[i])

HighestTemp = max(temperature)
HighestTempIndex = temperature.index(HighestTemp)

LowestTemp = min(temperature)
LowestTempIndex = temperature.index(LowestTemp)

AverageTemp = sum(temperature)/7

AboveAvg = [temp for temp in temperature if temp > AverageTemp]

print("The weather report")
for i in range(7):
    print(DaysOfTheWeek[i] + ":" + str(temperature[i]))

print(f"Shelly has {GoodDaysCounter} good days")
print(f"The hottest temperature is: {HighestTemp} on {DaysOfTheWeek[HighestTempIndex]}")
print(f"The lowest temperature is {LowestTemp} on {DaysOfTheWeek[LowestTempIndex]}")
print(f"The average temperature was: {AverageTemp}")
print(f"Days above average: {AboveAvg}")

temperature.sort()
print(temperature)