

# Python Programmieraufgabe 02
# 
# Given an array of integers, return a new array such that each element at index i 
# of the new array is the product of all the numbers in the original array except the one at i.
#       
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division? 
#
#
#    author: python-programmieren.com



# Solution with Division
def productArray_01(input_array):
    N = len(input_array)

    output_array = N*[1]

    prod = 1
    for i in range(N):
        prod *= input_array[i]

    for i in range(N):
        output_array[i] = int(prod/input_array[i])

    return output_array


# Solution without Division
def productArray_02(input_array):
    N = len(input_array)

    output_array = N*[1] 
    left_side = N*[1]
    right_side = N*[1]   
    
    for i in range(1, N):
        left_side[i] = input_array[i-1]*left_side[i-1]

    for i in range(N - 2, -1, -1):
        right_side[i] = input_array[i+1]*right_side[i+1]

    for i in range(N):
        output_array[i] = left_side[i] * right_side[i]

    return output_array



if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]

    print(productArray_01(array))
    print(productArray_02(array))




