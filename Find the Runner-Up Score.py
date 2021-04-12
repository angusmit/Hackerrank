#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up.
Input Format
The first line contains n. The second line contains an array A[] of n integers each separated by a space.
Output Format
Print the runner-up score.
Sample Input:
5
2 3 6 6 5
Sample Output:
5
"""
# first solution
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(reversed(sorted(list(set(arr)))))
    print(arr[1])


# In[ ]:


#2nd solution from internet source as learning material
import heapq
if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    a = heapq.nlargest(2, arr)
    print(a[1])