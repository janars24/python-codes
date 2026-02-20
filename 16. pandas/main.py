#CSV - comma separated values
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data.temp.mean())
max_temp = data.temp.max()
print(max_temp)
data_dict = data.to_dict()
print(data_dict)

print(data[data.temp == data.temp.max()])
print(data[data.temp == 22])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)



