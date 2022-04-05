
# Here is the scheme of the loop:

# for variable in iterable:
#     statement

oceans = ['Atlantic', 'Pacific', 'Indian', 'Southern', 'Arctic']
for ocean in oceans:
    print(ocean)

for char in 'magic':
    print(char)

# The range() function is used to specify the number of iterations. It returns a sequence of numbers from 0 (by default) and ends at a specified number

for i in range(5):
    print(i)

for i in range(5, 45, 10):
    print(i)

# If you're not going to use the counter variable in your loop, you can show it by replacing its name with the underscore symbol:

for _ in range(100):
    do_smth()


times = int(input('How many times should I say "Hello"?'))
for i in range(times):
    print('Hello!')

# In Python, it is easy to put one loop inside another one – a nested loop.

names = ['Rose', 'Daniel']
surnames = ['Miller']
for name in names:
    for surname in surnames:
         print(name, surname)


string = ""
for i in range(1, 20, 4):
    string += "&" * i

print(string)


digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
variable = input()
for i in variable:
    print(digits[int(i)])


for num in range(1, 101):
    if (num % 5 == 0) and (num % 3 == 0):
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)

