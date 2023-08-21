# Set Union:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2) # Creating a new set with elements from both sets
print("Union operation", union_set)

# Set Intersection:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2) # Creating a new set with common elements from both sets
print("intersection operation", intersection_set)
# Set Difference:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2) # Creating a new set with elements in set1 but not in set2
print("difference operation", difference_set)
# Set Symmetric Difference:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1.symmetric_difference(set2) # Creating a new set with elements that are in either of the sets, but not both
print("Usymmetric_difference operation", symmetric_difference_set)