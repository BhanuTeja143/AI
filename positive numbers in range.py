def print_positive_numbers(lst):
    positive_numbers = [num for num in lst if num > 0]
    print("Output:", positive_numbers)

input_str = input("Enter a list of numbers separated by commas: ")
input_list = [int(x.strip()) for x in input_str.split(",")]

print("Input:", input_list, end=" ")
print_positive_numbers(input_list)
