
# ------Python program to check whether the string is Symmetrical or Palindrome------

# str = "amaama"
# a= ''
# n = len(str)
# for i in range(n-1, 0-1, -1):
#     a+= str[i]
# if a == str:
#     print("String in palindrome")
# else:
#     print("String is not palindrome")

# n = len(str)
# mid = n // 2
# start= 0
# flag=0
#
# while(start<mid):
#     if(str[start] == str[n-1]):
#         start +=1
#         n -= 1
#         flag = 0
#     else:
#         flag =1
#         break
# if flag == 1:
#     print("String is not palindrome")
# else:
#     print("String is palindrome")



# ---Reverse words in a given String in Python---

# str = "geeks quiz practice code"
# a= str.split(' ')
# n = len(a)
# lst = []
# for i in range(n-1, 0-1, -1):
#     lst.append(a[i])
# print(lst)

# n = len(str)
# output=''
# for i in range(n-1, 0-1, -1):
#     output += str[i]
#
# print(output)



# ---Ways to remove i’th character from string in Python---

# test_str = "GeeksForGeeks"
# n = len(test_str)
# pos = 3
# output = ''
# for i in range(n):
#     if i != pos-1:
#         output+= test_str[i]
#
# print(output)


# ---Avoid Spaces in string length---

# test_str = 'geeksforgeeks 33 best'
# counter = 0
# for i in test_str:
#     if i != ' ':
#         counter +=1
#
# print(f'Total characters are {counter}')




# ---program to print even length words in a string---

s = "This is a python language"
output = ''

for i in s.split(' '):
    if len(i) %2 == 0:
        output += i+' '
print(output)