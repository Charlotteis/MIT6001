# Write a while loop that sums the value 1 through end, inclusive.
# End is defined already within the MIT tester
number = 1
result = 0
end = 6
while number <= end:
    result += number
    number += 1

print(result)
