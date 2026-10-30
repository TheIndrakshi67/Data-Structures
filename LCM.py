import math


num1 = int(input("Enter Largest number : "))
num2 = int(input("Enter Smallest number : "))

gcd_value = math.gcd(num1, num2)

lcm_value = abs(num1 * num2) // gcd_value

print(f"LCM is : {lcm_value}")
