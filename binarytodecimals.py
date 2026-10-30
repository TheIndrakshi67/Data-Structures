def binary_to_decimal(binary_str):
    decimal_value = 0
    # Reverse the string to process from right to left (least significant to most significant bit)
    reversed_binary = binary_str[::-1]
    
    for index in range(len(reversed_binary)):
        if reversed_binary[index] == '1':
            decimal_value += 2 ** index
            
    return decimal_value

# Example Usage:
binary_input = input("Enter your Binary: ")
print(f"Decimal : {binary_to_decimal(binary_input)}")
