import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260220.csv")
print(data)

gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(gray_squirrel)
print(black_squirrel)
print(red_squirrel)

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrel, black_squirrel, red_squirrel]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
