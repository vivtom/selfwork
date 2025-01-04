s = "hello"
s_list = list(s)  # Convert to list
s_list[0], s_list[-1] = s_list[-1], s_list[0]  # Swap first and last characters
s = ''.join(s_list)  # Convert back to string
print(s)  # Output: oellh
