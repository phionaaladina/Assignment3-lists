student_names = ['Sandra', 'Patricia', 'Phiona', 'Anita']

student_marks = [80, 56, 78, 90]


#adding a new item to the list
#students_names.append('Michelle')

print(student_names)

''''
slicing, printing, deleting
1. Print Patricia to Anita
2. Add Masha at the 4th position
3. Update the name Fiona to Fiona Aladina
4. Diplay the length of the students list
5. Print all the student names using a for loop
6. Sum of students marks
'''

#1. Print Patricia to Anita
print(student_names[1:])


#2. Add Masha at the 4th position
student_names.insert(4, 'Masha')
print(student_names)


#3. Update the name Phiona to Phiona Aladina
student_names[2] = 'Phiona Aladina'
print(student_names)


#4. Diplay the length of the students list
print(f'The length of the students list is:', len(student_names))


#5. Print all the student names using a for loop

for name in student_names:
    print (name)


#6. Total marks
total_marks = sum(student_marks)
print(total_marks)