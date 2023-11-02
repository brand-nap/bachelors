
def main():
    students = []; #initialize empty list for variable to point at
    
    options = [
               ['1. Add New Student',                    createStudent],
               ['2. Edit Student\'s Existing Grades',       editGrades],
               ['3. Add New Grade(s)',                    assignGrades],
               ['4. View Current Students',              printStudents],
               ['5. Import Filler Students',                      fill],
               ['6. Close Program',                                 '']];
    
    # each option corresponds to a function
    # - every function takes the same parameters: (students)
    

    # menuSelect is recursive. it repeats until a user decides to escape the program entirely
    menuSelect(students, options, 'Welcome to the Student Portal! To escape, simply press Enter');

# this code slaps ngl  -  scroll down for more



























# FUNCTIONS-FUNCTIONS-FUNCTIONS-FUNCTIONS-FUNCTIONS-FUNCTIONS-FUNCTIONS-FUNCTIONS-FUNCTIONS-FUNCTIONS-FUNCTIONS-FUNCTIONS

#      menuSelect    createStudent    selectStudent    assignGrades    editGrades    printStudents    fill    gpa



# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------- Menu Selection -------------------------------------------------
#                       Prints a menu, allows user to pick which function will run next.
# ------------------------------------------------------------------------------------------------------------------

def menuSelect(students, options, text = ''):

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n');
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n');
    print(f'{text}\n'); # formatting


    # prints out all options
    for option in options:
        print(option[0]);

    
    userSelect = input('\nSelect: ');
    if userSelect != '' and int(userSelect) < len(options): # If user doesn't select a given option, end the loop
        
        text = options[int(userSelect)-1][1](students);     # every function returns an output text and takes students as the sole paramter
        menuSelect(students, options, text);                # options will reload after action is complete  -  recursion for the win!


    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n');
    print(printStudents(students) if len(students) > 0 else 'Have a nice day!\n'); #Just a closing result




# ------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------- Create New Student -----------------------------------------------
#                   Creates a new student pseudo-object complete with name, age, and list of grades
# ------------------------------------------------------------------------------------------------------------------

def createStudent(students, student = None, grades = None):
    
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n');
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n');
    # formatting
    
    if student is None:
        student = []; # create new student list - pseudo object

    student.append(input('Student\'s Full Name: '));

    # check if the student name is redundant
    for kid in students:
        if kid[0] == student[0]:
            return 'This student is already in your class\n';

    # if student isn't redundant, continue with assigning values
    student.append(input('Student Age: '));   # age
    student.append([]);                       # grades
    assignGrades(students, student);          # assign grades accordingly
    gpa(student);                             # gpa
    students.append(student);                 # add student to list students
    return printStudents(students);           # return formatted list of students to be printed above menu
    



# ------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- Select Specific Student --------------------------------------------
#                  Prompts user for a name and selects the corresponding student pseudo-object
# ------------------------------------------------------------------------------------------------------------------

def selectStudent(students, selected = None, text = ''):
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n');
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n');
    #formatting
    
    print(f'{printStudents(students)}\n'); # print out students
    
    if selected is None:
        print(f'\n{text}');
        selected = input('Student Name: ');
    
    for student in students:
        if student[0] == selected:
            return student
        
    selectStudent(students, None, 'Invalid Name');
    # continue prompting to select a valid student




# ------------------------------------------------------------------------------------------------------------------
# -------------------------------------------- Assign Student's Grades ---------------------------------------------
#                           adds new grades to a student's given list of grades
# ------------------------------------------------------------------------------------------------------------------

def assignGrades(students, student = None, grades = None):
    
    if student is None:                           # if a student isn't passed in, prompt for a specific student
        student = selectStudent(students); 

    if grades is None:                            # grades = the selected student's grades
        grades = student[2]

    name = student[0].split(" ");                 # first name for UI purposes
    grade = input(f'{name[0]}\'s grades: ');
    
    while grade != '':
        grades.append(int(grade));                # let user input names until they escape with Enter key
        grade = input(f'{name[0]}\'s grades: ');

    gpa(student);                                 # update gpa accordingly

    return f'{student[0]}\'s Revised Grades: {str(student[2])[1:-1]}';
    # return student's revised grades




# ------------------------------------------------------------------------------------------------------------------
# ----------------------------------------- Edit Student's Existing Grades -----------------------------------------
#                                Revises existing grades until user is satisfied
# ------------------------------------------------------------------------------------------------------------------

def editGrades(students):
    
    student = selectStudent(students);                                    # have user pick specific student
    
    name = student[0].split(" ");                                         # get student's first name for UI purposes
    
    print(f'\n{name[0]}\'s grades: {str(student[2])[1:-1]}')              # show grades
    gradeIndex = input('Grade (By Order Shown) to Revise: ');             # have user pick a grade to revise
    
    while gradeIndex != '':
        student[2][int(gradeIndex)-1] = int(input('Revised Grade: '));    # keep prompting for grades to edit
        gradeIndex = input('Grade (by order) to Revise: ');

    gpa(student); #update gpa now that grades changed
        
    return f'{student[0]}\'s Revised Grades: {str(student[2])[1:-1]}';    # return student's revised grades



        
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------- Print Students -------------------------------------------------
#                                Prints the Students list in an aesthetic, legible format
# ------------------------------------------------------------------------------------------------------------------

def printStudents(students):

    # this is ALL literally formatting. nothing fancy here besides some ternary
    
    result = '';
    result += ('\n\n\n\n\n\n----------------- Class of Students -----------------\n\n');
    for student in students:
        result+=f'{student[0]} - {student[1]} years old\n';
        result+=f'Grades: {str(student[2])[1:-1]}\n';
        result+=f'GPA: {student[3]}  ';
        result+='\n' if student[3] == 'F' else f'-  Special Honors\n' if student[3] > 3.8 else f'-  Honors\n' if student[3] > 3.6 else '\n';
        result+='\n';

    result+='-----------------------------------------------------\n\n';
    return result;

    


# ------------------------------------------------------------------------------------------------------------------
# -------------------------------------------- Adds Filler to Students ---------------------------------------------
#                   Adds a list of my friends and their made up grades as filler for testing purposes
# ------------------------------------------------------------------------------------------------------------------

def fill(students):
    print();

    # filler of my people turned into fake students for testing purposes
    filler = [
        ['Sweta Alla', 19, [99, 100, 96, 83]],
        ['Beckett Hyde', 18, [100, 96, 99]],
        ['Colin Beyers', 22, [76, 82, 102, 89]],
        ['Maya Peace', 23, [42, 81, 0, 38]],
        ['William Hathaway', 18, [91, 97, 100, 100]],
        ['Jessica Alschuler', 18, [95, 84, 90, 88]],
        ['Corrina Quaglietta', 19, [82, 62, 77, 72]]
        ]
    
    # check if filler is redundantly being added and escape if so
    for blank in filler:
        gpa(blank);
        for student in students:
            if student[0] == blank[0]:
                return printStudents(students);
                
    students.extend(filler); 
    return printStudents(students);




# ------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------- Grade Point Average -----------------------------------------------
#                                   Calculates and updates a student's GPA
# ------------------------------------------------------------------------------------------------------------------

def gpa(student): 
    grade = sum(student[2])/len(student[2]);

    # calculates gpa on 4.0 scale
    if grade >= 93:
        grade = 4.0;
    elif grade >= 90:
        grade = 3.7;
    elif grade >= 87:
        grade = 3.3;
    elif grade >= 83:
        grade = 3.0;
    elif grade >= 80:
        grade = 2.7;
    elif grade >= 77:
        grade = 2.3;
    elif grade >= 73:
        grade = 2.0;
    elif grade >= 70:
        grade = 1.7;
    elif grade >= 67:
        grade = 1.3;
    elif grade >= 63:
        grade = 1.0;
    elif grade >= 60:
        grade = 0.7;
    else:
        grade = 'F';

    # appends gpa to student pseudo-object
    if len(student) < 4:
        student.append(grade);
    else:
        student[3] = grade;







    
