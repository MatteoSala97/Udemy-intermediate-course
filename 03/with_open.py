''' 
Create a “student.txt” file, and add three sample names.

Display the contents of the file to the console

Take user input to get three more names, and add them to the file.

'''

with open(r'C:\Users\matteo.sala\Documents\Udemy intermediate course\03\students.txt', 'w') as f:
    f.write('Red Johnson\n')
    f.write('White Smith\n')
    f.write('Blue Doe\n')

with open(r'C:\Users\matteo.sala\Documents\Udemy intermediate course\03\students.txt', 'r') as f:
    print("Initial contents of the file:")
    print(f.read())

new_names = []
for i in range(3):
    name = input(f"Enter name {i+1}: ")
    new_names.append(name)

with open(r'C:\Users\matteo.sala\Documents\Udemy intermediate course\03\students.txt', 'a') as f:
    for name in new_names:
        f.write(name + "\n")

with open(r'C:\Users\matteo.sala\Documents\Udemy intermediate course\03\students.txt', 'r') as f:
    print("Contents of the file after adding three more names:")
    print(f.read())
