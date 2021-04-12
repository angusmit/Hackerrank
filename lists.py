#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Lists

# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.

# Input Format
# The first line contains an integer, n, denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.

# Constraints
# The elements added to the list must be integers.

# Output Format
# For each command of type print, print the list on a new line.


# Enter your code here. Read input from STDIN. Print output to STDOUT
list = []
n = int(input())
for i in range(n):
    a = input().split()
    if a[0] == "print":
        print(list)
    elif a[0] == "insert":
        eval("list." + a[0] + "(" + a[1] + "," + a[2] + ")")
    elif a[0] == "remove" or a[0] == "append":
        eval("list." + a[0] + "(" + a[1] + ")")
    else:
        eval("list." + a[0] + "()")