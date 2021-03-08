#---- Given a list, write a Python program to swap first and last element of the list.----
#
# Examples:
#
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]
#
# Input : [1, 2, 3]
# Output : [3, 2, 1]

# num = [1,2,3]
#
# num[0], num[-1] = num[-1], num[0]
#
# print(num)




# ---Given a list in Python and provided the positions of the elements,
# write a program to swap the two elements in the list.---


# lst = [23, 65, 19, 90]
#
# def swap(ls, pos1, pos2):
#     ls[pos1-1], ls[pos2-1] = ls[pos2-1], ls[pos1-1]
#     return ls
#
# print(swap(lst, 1, 2))


# ---Swap elements in String list---

# test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
# print(' '.join(test_list))
# res = [sub.replace("G", '-').replace('e', 'G').replace('-', 'e') for sub in test_list]
# print(res)


# ---Ways to find length of list---
# test_list = [ 'is', 'best', 'for', 'Geeks']
# count=0
# for i in test_list:
#     count +=1
#
# print(count)


#--- Given two numbers, write a Python code to find the Maximum of these two---

# a = 22
# b = 4
#
# print(a if a>b else b)
# # if a > b:
# #     print(a)
# # else:
# #     print(b)


# ---Check if element exists in list in Python---

# test_list = [ 1, 6, 3, 5, 3, 4 ]
#
# # print(4 in test_list)
#
# for i in test_list:
#     if i ==4:
#         print("4 exist")


# ---Different ways to clear a list in Python---
# GEEK = [6, 0, 4, 1]
# print("Before clear:" + str(GEEK))
# GEEK.clear()
# print("after clear:" + str(GEEK))


# ---Reversing a List in Python---

# list = [64, 34, 25, 12, 22, 11, 90]
#
# print(list[::-1])
# new=[]
# for i in list[-1::-1]:
#    new.append(i)
# print(new)


# ---Python | Cloning or Copying a list---

# lst = [64, 34, 25, 12, 22, 11, 90]
# new = list(lst)
# print(id(new))
# print(id(list))



# ---Count occurrences of an element in a list---

# lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
#
# count = 0
# for i in lst:
#     if i == 10:
#         count+=1
# print("10 appear "+ str(count)+" times")


# ---Find sum and average of List in Python---

# lst = [4, 5, 1, 2, 9, 7, 10, 8]
#
# sum=0
# n = len(lst)
# for i in lst:
#     sum += i
# average = sum/n
# print(f'The sum is {sum}')
# print(f'The average is {average}')


# ---Python program to find smallest number in a list---

# list1 = [4, 2, 10]
# small = list1[0]
# for i in list1:
#     if i < small:
#         small = i
# print(f'smalles number is {small}')


# ---Python program to find second largest number in a list---

# lst = [111, 112, 13, 4]
# big = lst[0]
# small = lst[1]
#
# for i in lst:
#     if i > big:
#         small = big
#         big = i
#     elif i > small and i != big:
#         small = i
# print(small)


# ---Python program to print even numbers in a list---

# list1 = [2, 7, 5, 64, 14]
# even = [i for i in list1 if i%2==0]
# print(even)


# ---Python program to print all even numbers in a range---

# start = 4
# end = 15
# for i in range(start, end):
#     if i%2 == 0:
#         print(i)


# Remove multiple elements from a list in Python

# Input: [12, 15, 3, 10]
# Output: Remove = [12, 3], New_List = [15, 10]

Input1= [12, 15, 3, 10]
Remove = [12, 3]

for i in Input1:
    if i in Remove:
        Input1.remove(i)

print(Input1)

