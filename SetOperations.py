input_E = input("Enter elements of set E separated by commas: ")
E = set(map(int, input_E.split(",")))

input_N = input("Enter elements of set N separated by commas: ")
N = set(map(int, input_N.split(",")))

union_set = E.union(N)
print("Union of E and N is", union_set)

intersection_set = E.intersection(N)
print("Intersection of E and N is", intersection_set)


difference_set = E.difference(N)
print("Difference of E and N is", difference_set)

symmetric_difference_set = E.symmetric_difference(N)
print("Symmetric difference of E and N is", symmetric_difference_set)
