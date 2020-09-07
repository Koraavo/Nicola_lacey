"""

 122
 Create the following menu:
 1 Add to file
 2 view all records
 3 delete record
 4 quit program

If the user selects 1, allow them to add to a file called Salaries.csv
which will store their name and salary.
If they select 2 it should display all records in the Salaries.csv file.
If they select 3 it should delete a record.
if they select 4 the program should stop
If they select an incorrect option they should see an error message.
They should keep returning to the menu until they select option 3.

"""
import csv
import os

def add_name(names):
    file = 'C:\\Users\\VoraKinj\\PycharmProjects\\Python_files\\Nichola_lacey\\Salaries.csv'
    names1 = input("\nEnter the name you wish to add: ")
    salary = int(input("Enter the salary: "))
    names.append({
        'Names': names1,
        'Salary': salary
    })

    with open('Salaries.csv', 'a', newline='') as sal:
        writer = csv.DictWriter(sal, fieldnames=names[0].keys())
        writer.writerow({
            'Names': names1,
            'Salary': salary
            })


def delete_record():
    file = open('Salaries.csv', 'r')
    x = 0
    tmp = []
    for row in file:
        tmp.append(row)
    file.close()
    for row in tmp:
        print(x, row)
        x += 1
    del_rec = int(input("Enter the row number you wish to delete?: "))
    del tmp[del_rec]

    file = open('Salaries.csv', 'w')
    for row in tmp:
        file.write(row)
    file.close()


def view_names():
    with open('Salaries.csv', 'r') as sal:
        for row in sal:
            print(row.strip('\n'))


def main():
    names = []
    again = 'y'
    while again == 'y':
        print("What do you wish to do?")
        print("\t1. Add name?\n\t2. View records?\n\t3. Delete a record\n\t4. Quit")
        user_input = input("Please select: ")
        if user_input == '1':
            add_name(names)
            # print(names)
        elif user_input == '2':
            view_names()
            # print(names)
        elif user_input == '3':
            delete_record()
        elif user_input == '4':
            again = 'n'
        else:
            print('wrong input')


if __name__ == '__main__':
    main()
