# Create a new list called studentNames
# ask the user to add another name to the list
# Add this name and reprint the list with the last names
# author: Zhang Junhao
# DATE: 25/3/17

studentNames = ["Lisa","Liam","Leo","Larry","Linda"]
for i in studentNames:
    print(f"{i} Evans")
new_name = input("please input a new name into the list:")
studentNames.append(new_name)
for i in studentNames:
    print(f"{i} Evans")
