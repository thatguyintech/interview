# You are a thief trying to rob from a neighborhood of houses.
# Houses are represented in arrays like this: [1, 10, 32, 4], where each number
# is the value of robbing that house. Once you rob a house, you cannot
# rob the immediately adjacent houses, else you'd be caught.
# 
# A) What is the maximum value of a night on the town, given a neighborhood of houses?
# B) What are the indices of the houses you would rob in that case?

# Memoize the max value up to the current house index
def max_value_of_robbing(houses):

    # edge case
    if len(houses) < 3:
        return max(houses)

    max_two_houses_ago = houses[0]
    max_last_house = max(houses[0], houses[1])

    # either rob the current house or skip it
    for i in range(2, len(houses)):
        current_max = max(max_last_house, max_two_houses_ago + houses[i])
        max_two_houses_ago = max_last_house
        max_last_house = current_max

    return current_max

# We can use the max value to go backwards and find the indices
def path_to_rob(houses, max_value):
    return

# Tests
houses = [1, 10, 10, 2] # 12
houses1= [10, 20] # 20
houses2= [10, 20, 30, 40, 50, 60, 1, 1, 1, 1, 100] # 221
print(max_value_of_robbing(houses))
print(max_value_of_robbing(houses1))
print(max_value_of_robbing(houses2))
