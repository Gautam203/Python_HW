def find_string_indices(input_list):
    indices = [str(i) for i, item in enumerate(input_list) if isinstance(item, str)]
    return ''.join(indices)

input_list = ['Sahil', 48, 'Rahul', 'Rohan', 'Karan', 88, 40, "Tarun"]
output = find_string_indices(input_list)
print(output)
