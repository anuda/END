# write a python program to add two numbers 
num1 = 1.5
num2 = 6.3
sum = num1 + num2
print(f'Sum: {sum}')

# write a python program to multiply two numbers 
num1 = 4
num2 = 3
prod = num1 * num2
print(f'Product: {prod}')


# write a python function to add two user provided numbers and return the sum
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum


# write a program to find and print the largest among three numbers

num1 = 10
num2 = 12
num3 = 14
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print(f'largest:{largest}')


# write a python program to multiply three numbers 
num1 = 4
num2 = 3
num3 = 8
prod = num1 * num2 * num3
print(f'Product: {prod}')

# write a python program to multiply three numbers 
num1 = 4
num2 = 3
num3 = 8
prod = num1 * num2 * num3
print(f'Product: {prod}')

#write a python function to print a string
def print_string(text):
	print(text)

#write a python program to calculate square root of a number
num = 9
sqrt_num = num ** 0.5
print(f'square root: {sqrt_num}')


#write a python function to add two lists
list_1 = [2,34,5]
list_2 = [54,67,342]

result_list =[]
for i in range(0, len(list_1)):
	result_list.append(list_1[i] + list_2[i])
	


# write a python program to find the factorial of a number provided by the user.

num = 13


factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# write a python program to find the ASCII value of the given character

c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))

# write a python function to return size of a list

def size_of_list(l):
	return(len(l))

# write a python program to append to two lists

list_1 = [4,'dasd',34,65,34,'fsd']
list_2 = [54,'fdssd',3,665,634,'ffsdfsdvsd']

appended_list = list_1 + list_2

# write a python function to remove punctuations

def remove_punctuation(text):
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

	my_str = "Hello!!!, he said ---and went."

	no_punct = ""
	for char in my_str:
		if char not in punctuations:
			no_punct = no_punct + char

			return(no_punct)


# write a python function to tokenize a string

def tokenize(text):
	return(text.split(' '))


# write a python function to get factorial of a number using recursion
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)


# write a python function to sort a list

def sort_list(l):
	l.sort()
	return(l)

#write a python program to print text in lower case

text = 'This SENTENCE had a MIX of lower and CAPS alphabets '
print(text.lower())

# write a function to replace a part of a string with another string

def replace_pattern(text,pattern,replacement):
	result = re.sub(pattern, replacement, text)
	return(result)

# write a python program to extract numbers from a list

l1 = [2,34,564,'asdasd','zebra','tsai',4,45,543,0,-1]
num_list=[]
for i in l1:
	if type(i) == int or type(i) == float:
		num_list.append(i)
print(num_list)

# write a python program to multiply two numbers using lambda

x = lambda a, b : a * b
print(x(5, 6))

# write a python program to handle exception if values do not match

try:
	print(x)
except Exception as e:
	print(e)

# write a python program to print numbers between 2 numbers

x1 = 3
x2 = 12
for i in range(x1,x2):
	print(i)