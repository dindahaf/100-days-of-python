# # with open("weather_data.csv") as weather_file:
# #     list_of_weather = weather_file.readlines()
# #     print(list_of_weather)
#
# import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data= pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
#
#
# data_dict = data.to_dict()
# print(data_dict)
#
# tempt_list = data["temp"].to_list()
# print(tempt_list)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)
#
# # Get Data in Row
# monday = data[data.day == "Monday"]
# print(monday.temp)
#
# temp_in_f = monday.temp[0] * 9/5 + 32
# print(temp_in_f)
#
# # print(data[data.temp == data.temp.max()])
#
# # Create a dataframe from scratch
#
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76,56,65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")
#
#

import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
}

print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")




