# Ask user to input intergers into a list separated by a space
student_heights = input("Input a list of student heights ").split()

# Print the current list. 
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# Input: List of intgers that represents heights.
# Output: Integer which represents the avg height of the list.

# Psuedocode 
# 1. Implement a counter to sum up the total height of the list.
# 2. Implement a counter to sum up the total number of heights. 
# 3. To get the avg height, divide total height by the number of heights 

total_height = 0
total_number = 0
for index in range (0, len(student_heights)):
    total_height += student_heights[index]
    total_number += 1

# Calculate avg height.
avg_height = round(total_height/total_number)

# Print avg height.
print(avg_height)

# End
