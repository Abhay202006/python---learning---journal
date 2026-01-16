# basics/operators.py
# Topic: Operators in Python

# Arithmetic Operators
a = 10
b = 3

print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division
print(a % b)   # modulus  - returns the remainder
print(a // b)  # floor - divides two number and rounds down to nearest integer aka divides and removes decimal part 
print (a ** b)  # exponentiation (power) 

# Comparison Operators
print(a > b)
print(a < b)
print(a == b)  # - equal to
print(a != b)  # - not equal to
print(a >= b) 
print(a <= b) 


# Logical Operators  - works with True and False

# AND - Both condition must be true
# OR - At least one condition must be true 
# NOT - revesre the value TRUE becomes FALSE and vice versa

x = True
y = False

print(x and y)
print(x or y)
print(not x)

# Assignment Operators
c = 5
c += 2    # c = c + 2
print(c)
