"""
This program will determine the amount of grades, the average grade, and the percentage of grades above the average grade on a final exam.

Text file will be read and made into a list of intergers

Number of grades = length of list of intergers

Average grade = sum of grades / # of total grades

Percentage of grades above average = grades > average / # of total grades 

"""
"""
Infile will open "Final.txt" and make list of strings and defined 'grades' as the list

'Grades' line of strings will be made into list of intergers 

Average = sum(grades) / len(grades)

Using loop num = 0
Above average % = above_average > average
num += 1 

print(grades)
print(average)
print(100 * num / len(grades))

"""
infile = open ("Final.txt", 'r')
grades = [line.rstrip () for line in infile]
infile.close()
for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0
for grade in grades:
    if grade > average:
        num += 1
print("Number of grades:", len(grades))
print("Average grade:", average)
print("Percentage of grades above average: {0:.2f}%"
                    . format(100 * num / len(grades)))