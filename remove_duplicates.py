# The default list the unsorted items in it
default_list = ['a','a','b','b','f',1,2,4,87,77,88,99,1,1,1,2,3,4,4,5,6,1,2,3,4,7,5,7,8,5,7,8,]

# Create a new empty list to contain the unique items with no duplications
unique_list = []

# Loop through the default list
for eachItem in default_list:
    # If the item of the default list is not inside the unique list, then
    if eachItem not in unique_list:
        # That item will be append into the unique list
        unique_list.append(eachItem)

# Print the unique list without duplication
print(unique_list)