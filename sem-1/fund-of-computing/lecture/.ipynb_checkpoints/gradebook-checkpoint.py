def main():

    student_list = [];
    
    choice = eval(input("\n1. Enter in a new student\n2. Update existing student's grade\n3. Search for student's grade\n4. Exit\n\nPlease enter your choice here: "));
    while(choice>0 and choice<4):
        if(choice==1):
            student_name = input("Student's Last Name: ")
            student_list.append([student_name, 100])
        elif(choice==2):
            for student in student_list:
                student_name = input("Student's Last Name: ")
                if(student[0]==student_name):
                    student[1] = eval(input(f"{student[0]}'s New Grade: "));
        elif(choice==3):
            student_name = input("Student's Last Name: ")
            for student in student_list:
                if(student[0]==student_name):
                    print(student);
        choice = eval(input("\n1. Enter in a new student\n2. Enter in a new student with new grade\n3. Search for student's grade\n4. Exit\n\nPlease enter your choice here: "));


