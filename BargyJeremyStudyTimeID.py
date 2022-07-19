#Study Time Identifier
#Jeremy Bargy
#Feb. 9, 2020

startProgram='Y'
while startProgram == 'Y' or startProgram =='y':



    #Display welcome page and developer name
    print('\n\t\t\t\tHello Students!\n\t\t\t\t---------------')
    print('Thank you for choosing our school to advance your education.')
    print('This program was made by Jeremy Bargy.')

    #Display description of program
    print('\n\t\t\t\tInstructions\n\t\t\t\t------------')
    print('The program being used is designed to help students identify their study needs for this semester.')
    print('A student with this information can build and develop their own study habits to meet their academic goals.\n\n')
    print('Here is a list of how to use this program:\n')
    print('1) The program will ask users if this is data to enter. Data will be entered one user at a time.')               #step 1
    print('\ta: You will enter a "y" or "Y" for Yes and the program will continue to ask for your information.')
    print('\tb: You will enter a "n" or "N" for No and the program will enter the next sequence.\n')
    print('2) The program will ask users for their first name.')                                                            #step 2
    print('\ta: Be sure to enter letters for your name and not leave an empty box.\n')
    print('3) The program will ask users for their last name.')                                                             #step 3
    print('\ta: Be sure to enter letters for your name and not leave an empty box.\n')
    print('4) The program will ask users to enter their credit hours they are enrolled in.')                                #step 4
    print('\ta: Be sure to enter in a positive number.')
    print('\tb: Be sure to enter a number that equals credit hours for one standard class.')
    print('\tc: 1 class is equal to 3 credit hours. 4 classes is equal to 12 credit hours.\n')
    print('5) The program will ask users for the grade they are aiming to achieve.')                                       #step 5
    print('\ta: The program assumes that grade is the same for all the classes a user is enrolled in.')
    print('\tb: Be sure to entered letters for value and not null value')
    print('\tc: Letter grade entered must correspond with standard grading scales.\t i.e. A,B,C,D, or F\n')
    print('6) The program will ask if there is another student to enter their data.')                                       #step 6
    print('\ta: You will enter a "y" or "Y" for Yes and the program will continue to ask for your information.')
    print('\tb: You will enter a "n" or "N" for No and the program will enter the next sequence.\n')

    print('Take a minute to ready through the instructions before you begin.\n\n')

    #Initialize variables
    beginSequence= ''       #str
    contSequence= 'Y'        #str
    firstName=''            #str
    lastName=''             #str
    creditHours=0           #int
    studyHours= 0           #int
    totalNumStudents= 0     #int
    totalCredits=0          #int
    AverageCredits= 0.0     #float
    AverageStudyHours=0.0   #float
    TotalStudyHours= 0      #int
    alltotalStudyHours=0    #int
    numberofClasses= 0      #int
    CLASSPERHOURS= 3        #int constant


    #make sure the user is ready to enter their study data
    print('Have you read the instructions and are ready to begin?')
    print('Enter "Y" for yes. Please use capital letters.')
    print('Or enter "N" for no. Please use capital letters.')
    beginSequence = input('Begin program? ')
    while not(beginSequence == 'Y' or beginSequence == 'y') or beginSequence=='' or beginSequence== ' ':
        print('Error: please read the instructions and enter "Y" for yes to begin: \n')
        beginSequence= input('Begin program? \n')

    # continue processing as long as there are user to enter data
    while contSequence == 'Y' or contSequence =='y':
        # Get student first name data
        firstName= input('\nPlease enter your first name: \n')
        while not(firstName.isalpha()) or firstName==' ' or firstName=='':
            print('Error: incorrect input: \n')
            firstName= input('Please your first name: \n')

        #initialize accumulator for averages and totals
        totalNumStudents +=1

        # Get student last name data
        lastName= input('Please enter your last name: \n')
        while not(lastName.isalpha()) or lastName== ' ' or lastName=='':
            print('Error: incorrect input: \n')
            lastName= input('Please your last name: \n')

        # Get student user to enter credit hours enrolled in
        creditHours = (input('Please enter the credit hours you are currently enrolled in. i.e. 1 class will be entered as 3 credit hours: \n'))
        while not(creditHours.isdigit()) or not(int(creditHours) % 3 ==0 ) or int(creditHours) > 18 or int(creditHours) <3 or int(creditHours) == ' ' or int(creditHours)=='':
            print('Error: incorrect input: \n')
            creditHours = (input('Please enter the credit hours you are currently enrolled in. i.e. Must be between 1 and 6 classes. Or as required, 3 - 18 credit hours. \n'))
        creditHours= int(creditHours)
        
        #initialize accumulator for credit hour averages and totals
        totalCredits += creditHours

        # Get student user to enter grade wanting to earn
        grade= input('Please enter the grade you wish to earn. i.e. A,B,C,D, or F:\n')
        while not(grade.isalpha()) or not(grade=='A' or grade=='a' or grade =='B' or grade== 'b' or grade== 'C' or grade== 'c' or grade== 'D' or grade== 'd' or grade== 'F' or grade== 'f') or grade == '' or grade == ' ':
            print('Error: incorrect input: \n')
            grade= input('Please enter the grade you wish to earn: \n\n\n')
        if grade == 'A' or grade == 'a':
            studyHours = 15
        elif grade == 'B' or grade == 'b':
            studyHours = 12
        elif grade == 'C' or grade == 'c':
            studyHours = 9
        elif grade == 'D' or grade == 'd':
            studyHours = 6
        else:
            studyHours = 0

        #Calculate the number of classes enrolled in
        numberofClasses = creditHours / CLASSPERHOURS

        #Calculate the total study hours for student
        TotalStudyHours = studyHours * numberofClasses

        #initialize accumulator for totalstudy hour averages and totals
        alltotalStudyHours += TotalStudyHours

        #Display Student name, total study hours, credit hours enrolled in, and grade they want to earn
        print('\n\tStudy Time Info for:\n\t--------------------')
        print('Student Name:\t |\t', firstName, lastName)
        print('Credits:\t |\t', creditHours)
        print('Study Hours:\t |\t', TotalStudyHours)
        print('Grade:\t\t |\t', grade.upper(),'\n\n')

        #get the next students study data
        print('Is there another student who has data to enter?')
        print('Enter "Y" for yes. Please use capital letters.')
        print('Or enter "N" for no. Please use capital letters.')
        contSequence = input('Another user? ')
        while not(contSequence == 'Y' or contSequence=='y'  or contSequence == 'N' or contSequence=='n') or contSequence=='' or contSequence== ' ':
            print('Error: incorrect input: \n')
            contSequence= input('Another user? \n')


    #Calculate average credit hours
    AverageCredits = totalCredits / totalNumStudents

    #Calculate average study hours
    AverageStudyHours = alltotalStudyHours /totalNumStudents

    #Display total number of students
    print('\n\n\t\t\tGroup Study Info:\n\t\t\t------------------')
    print('Total Number of Students: \t|\t', totalNumStudents)
    print('Average Credit Hours: \t\t|\t', AverageCredits)
    print('Average Study Hours: \t\t|\t', AverageStudyHours )

    #repeat program if more groups need to enter data.
    print('\n\nWould you like to restart this program?')
    startProgram = input('Please enter "Y" to restart program. \n Or "N" to end the program: ')
    while not(startProgram == 'Y' or startProgram=='y' or startProgram=='N' or startProgram=='n') or startProgram=='' or startProgram== ' ':
        print('\nError: please "Y" for yes to restart: ')
        print('Or enter "N" to end the program: ')
        startProgram= input('Restart program? \n')


    print('\nThank you for using our program.')
    print('Good luck this semester!')
