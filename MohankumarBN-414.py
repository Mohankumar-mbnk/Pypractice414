print("----------------------Program-1--------------------------- ")

print("-----------------------A) Palindrome using for loop-------------------")
string = input("Please enter your own Text : ")
str1 = ""

for i in string:
    str1 = i + str1
print("Reverse Order :  ", str1)

if(string == str1):
   print("This is a Palindrome String")
else:
   print("This is Not")

print("----------------------B)Palindrome using Generator Mechanism---------------------")

def check_palindrome(string):
    reversed_string = string[::-1]

def get_sequence_upto(x):
    for i in string:
        str1 = i + str1
    print("Reverse Order :  ", str1)

    if (string == str1):
        print("This is a Palindrome String")
    else:
        print("This is Not")
        yield i
print("----------------Program 2---------------------")

# 2. Sum of 2 digits into output
#-------------------------------------
# n1 = 1234 # int(input("Enter number1 :" ))
# n2 = 9999 # int(input("Enter number2 :" ))
# Output: 9+1 2+9 3+9 4+9
# 10 + 11 + 12 + 13
print("2. Sum of 2 digits into output")
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
num1 = list(str(num1))
num2 = list(str(num2))
def sum_of_two_numbers(n1, n2):
    return int(n1) + int(n2)
x = list(map(sum_of_two_numbers, num1, num2))
print(sum(x))

print("----------------------Program 3--------------------")
# 3. st = "ab@#cd!ef"
# Reverse string considering only alphabets. Symobls should not be reversed
# Output: fe@#dc!ba

string = "ab@cd!ef"
string1 = string[::-1]
string1 = list(string1)
reverse = ''
list = []
for idy, val in enumerate(string1):
    if val.isalpha():
        list.append(val)
    else:
        list.insert(idy, string[idy])
rev_string = reverse.join(list)
print(rev_string)

print("-----------------Program 4-------------------------")
# 4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]'''
#    findout elements duplicate count output in  dict format

from collections import Counter
some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
counts = dict(Counter(some_list))
dup = {key:value for key, value in counts.items() if value > 1}
print(dup)

print("**************Progarm 5*******************")
# 5.  t1 = (1, 2, 3, "a", "c")
#     t2 = ("b", "d", 9, 8, 7)
# Output: (10,10,10,"ab","cd")

print(''*20, "5. ---------------", '' * 20)
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
lis1 = []
lis2 = []
for t in t1:
    if isinstance(t, int):
        for i in t2:
            if i not in lis2 and isinstance(i, int):
                lis2.append(i)
                lis1.append((t + i))
                break
    else:
        for i in t2:
            if i not in lis2 and isinstance(i, str):
                lis2.append(i)
                lis1.append((t + i))
                break
print(lis1)

print("--------------------Program 6-----------------------------------")
# 6. Write a Python program to remove leading zeros from an IP address.
#   input = "216.08.094.196"
#   o/p =  216.8.94.196

inp = "216.08.094.196"
x = inp.replace('0', '')
print(f"IP address after removing zeros is: {x}")
print()

print("-----------------------Program 7---------------------------")

# 7. l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
#    output= [1,2,3,4,5,6,7,8,9,10]

lis = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]


def rec(l):
    li = []
    for i in l:
        if isinstance(i, int):
            li.append(i)
        elif isinstance(i, list):
            x = rec(i)
            li.extend(x)
    return li


print(rec(lis))




