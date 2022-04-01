from statistics import mean as m
import statistics

admins ={'pratik':'Pratik@123'}

studentDict={'Jeff':[78,88,93],
           'Alex':[92,76,88],
           'Sam':[89,92,93]}

# for defining grades
def enterGrades():
    nameToEnter=input('Student Name: ')
    gradeToEnter=input('Grade: ')

    if nameToEnter in studentDict:
        print("Adding Grade...")
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('student does not exits.')
    
    print(studentDict)

# for removing student

def removestudent():
    nameToremove=input('What student to remove:')
    if nameToremove in studentDict:
        print('removing student...')
        del studentDict[nameToremove]
        print(studentDict)

# for StudentAvgs

def studentAvgs():
    for eachstudent in studentDict:
        gradeList=studentDict[eachstudent]
        avgGrade =m(gradeList)

    print(eachstudent,'has an average grade of:',avgGrade)

def main():
    print("""
    Welcome to the Grade Central
    [1]-Enter Grade
    [2]-Remove Student
    [3]-Student Average Grade
    [4]-Exit
    """)

    action= input('what would like to do today? (Enter the number): ')
    if action=='1':
        enterGrades()
    elif action=='2':
        removestudent()
    # elif action=='3':
    #     studentAvgs()
    elif action=='4':
        exit()
    else:
        print('No vaild choose are give,try again')
        
login=input('Username: ')
passw=input('Password: ')

if login in admins:
    if admins[login]==passw:
        print('Welcome,',login)
        while True:
         main()
    else:
        print('Invaild password,will detonate in 5 secends!')
else:
    print('Invaild username,calling the FBI to report this')