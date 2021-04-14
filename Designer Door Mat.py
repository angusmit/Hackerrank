"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat.
Design specifications are as follows:
1. Size of mat must be NXM. (N is an odd natural number and M is 3 times N.)
2. Design should have 'WELCOME' written in the center.
3. Design pattern should only use '|', '.' and '-' characters.
Sample Designs
    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
----------WELCOME----------
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
N,M = map(int,input().split())
for i in range(1, N, 2):
    print(str('.|.'*i ).center(M, '-'))
print(str('WELCOME').center(M, '-'))
for i in range(N-2, -1, -2):
    print(str('.|.'*i ).center(M, '-'))
