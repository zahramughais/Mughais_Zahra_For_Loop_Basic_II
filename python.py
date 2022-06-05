# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(li):
    for x in range(0,len(li),1):
        if li[x] > 0:
            li[x]='big'
    return li
print(biggie_size([-1, 3, 5, -5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values.
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(li):
    count = 0
    for x in range(0,len(li),1):
        if li[x] > 0:
            count += 1
    li[len(li)-1] = count
    return li
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(li):
    count = 0
    for x in range(0,len(li),1):
        count += li[x]
    return count
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5
def average(li):
    count = 0
    for x in range(0,len(li),1):
        count += li[x]
    return (count/len(li))
print(average([1,2,3,4]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(li):
    li_length = 0
    for x in li:
        li_length += 1
    return li_length
print(length([37,2,1,-9]))
print(length([]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. 
# If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(li):
    min = False
    if len(li) > 0:
        min = li[0]
        for x in range(0, len(li)):
            if li[x] < min:
                min = li[x]
    return min
print(minimum([37,2,1,-9]))
print(minimum([]))

# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, 
# have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(li):
    max = False
    if len(li) > 0:
        max = li[0]
        for x in range(0, len(li)):
            if li[x] > max:
                max = li[x]
    return max
print(maximum([37,2,1,-9]))
print(maximum([]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average,
# minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return 
# {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(li):
    li_analysis = {}
    li_analysis['sumTotal'] = sum_total(li)
    li_analysis['average'] = average(li)
    li_analysis['minimum'] = minimum(li)
    li_analysis['maximum'] = maximum(li)
    li_analysis['length'] = length(li)
    return li_analysis
print(ultimate_analysis([37,2,1,-9]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without
# creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(li):
    temp = 0
    for x in range (0, int(len(li)/2)):
        temp = li[x]
        li[x] = li[len(li)-1-x]
        li[len(li)-1-x] = temp
    return li
print(reverse_list([37,2,1,-9]))