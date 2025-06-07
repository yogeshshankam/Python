def merge_ordered_sets(set1: set, set2: set) -> set:
    """Merges two sets.
    Args:
        set1 (set): An ordered set.
        set2 (set): An ordered set.
    
    Returns:
        set: A new set containing the elements from sets 1 and 2.  
    """
    sorted_set = sorted(set(set1) | set(set2))
    return set(sorted_set)

# Use case: two ordered sets
set1 = {1, 2, 3, 4}
set2 = {6, 7, 8, 9}
result = merge_ordered_sets(set1, set2)
print(result)
print(type(result))
