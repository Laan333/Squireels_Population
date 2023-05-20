import pandas

# Read File
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
all_colors_squirrel = data["Primary Fur Color"]
# First example
# Find data about colors
data_list = all_colors_squirrel.to_list()
num_of_gray = data_list.count("Gray")
num_of_cinnamon = data_list.count("Cinnamon")
num_of_black = data_list.count("Black")
print(num_of_black)

dict_of_colors = {
    "Color": ["Gray", "Cinnamon", "Black"],
    "Count": [num_of_gray, num_of_cinnamon, num_of_black]
}
# Create new DataFrame
new_dataframe = pandas.DataFrame(dict_of_colors)
new_dataframe.to_csv("numbers_of_squirrels.csv")

# Second Example
# Find data about colors
grey_squireels_count = len(data == "Gray")
red_squirrels_count = len(data == "Cinnamon")
black_squirrels_count = len(data == "Black")

dict_of_colors = {
    "Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squireels_count, red_squirrels_count, black_squirrels_count]
}
# Create new DataFrame
new_dataframe = pandas.DataFrame(dict_of_colors)
new_dataframe.to_csv("squirrels.csv")
