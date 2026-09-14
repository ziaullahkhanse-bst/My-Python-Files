def filter_list(lst):
   
    result = []
    for item in lst:
        if type(item) == int:  # Keep only integers
            result.append(item)
    return result

# Test the function
print(filter_list([1, 2, 'a', 'b']))           # [1, 2]
print(filter_list([1, 'a', 'b', 0, 15]))       # [1, 0, 15]
print(filter_list([1, 2, 'aasf', '1', '123', 123]))  # [1, 2, 123]
