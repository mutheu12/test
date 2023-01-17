"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""
import random

class CFGStudent():
    def __init__(self, fname, lname,age, email, student_id):
        self.name = fname
        self.surname = lname
        self.age = age
        self.email = email
        self.student_id = student_id

    @staticmethod
    def generate_id(id):
        id = str(random.randint(1000, 10000))


    def get_id(self):
        self.id = student_id

    def get_fullname(self):
        s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
        print(s.get_fullname())
#returns 'Anna Smith'
        print(s.student_id)
#returns '3868' or some other random number


class NanoStudent(CFGStudent):

    def __init__(self, course, grade):
        CFGStudent.__init__(self)
        self.specialization = course
        self.course_grades = grade

    @staticmethod
    def generate_id():
        'your code goes here'
        'create a random new id, which is a word NANO followed by any number between 1,000 and 10,000'
        'return id as a string'
        "Example 'NANO1234' "

    def add_new_grade(self, 'your code goes here'):
        'your code goes here'
        'update course_grades container'
        "Example: pass in a task name and its grade, so that both are added to course_grades"

    def get_course_grades(self):
        'your code goes here'
        'fetch course grades container and its values'



############################################

# Example run

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}



"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence
and return the sum of all even Fibonacci numbers. See more details in the task description in
your assessment paper.
"""


##### TESTS ####

print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))   # should be 0

def even_fibonacci_sum(limit) :
    if (limit < 2) :
        return 0

    n1 = 0
    n2 = 2
    nth= n1 + n2

     while (n2 <= limit) :
        n3 = n2 + n1 % 2 == 0:

        if (n3 > limit) :
            break


        n1 = n2
        n2 = n3
        sum = nth + n2

    return sum



print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=144))  # should be 188
print(even_fibonacci_sum(limit=1))   # should be 0



# """
# TASK 3
#
Validate subsequence. Use suggested tests below to check
correctness of your solution.
# """
#
#
#
# #### TESTS ####
#
array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,-2]

print(is_valid_subsequence(array, sequence))  # FALSE
#
#
# array2 = [5,1,22,25,6,-1,8,10]
# sequence2 = [1,6,-1, 10]
#
# print(is_valid_subsequence(array2, sequence2))  # TRUE
#
#
# array3 = [5,1,22,25,6,-1,8,10]
# sequence3 = [25]
#
# print(is_valid_subsequence(array3, sequence3))  # TRUE
#
#


def is_valid_subsequence():
    array1, s2 = len(array), len(sequence)
    if a1 >s2:
    i = j = 0
    b, c = a1, s2
    while i < a1 and j < s2:
        while array[i] != sequence[j]:
            j += 1
            c -= 1
            if b > c:
                return False
        i, j, b, c = i+1, j+1, d1-1, d2-1
        if b > c:
            return False
    return True
#
# """
# TASK 4
#
# WRITTEN ASSIGNMENT
#
# Write a review on how 'class Employee' can be improved.
# (See PDF document with the code example)
# """
#
#
#
#
#
#
#
#
