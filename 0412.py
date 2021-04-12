# Nested Lists

# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any
# student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, N, the number of students.
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains
# their grade.

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names
# alphabetically and print each one on a new line.


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    list = []
    for i in range(n):
        name = input()
        score = float(input())
        a = [name,score]
        list.append(a)
    lowest_score = min(list, key =lambda x:x[1])[1]
    list2 = [a for a in list if a[1] != lowest_score]
    for i in range(len(list2)):
        list2.sort()
        if list2[i][1] == min(list2, key =lambda x:x[1])[1]:
            print(list2[i][0])

