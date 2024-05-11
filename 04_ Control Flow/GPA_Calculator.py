# program to calculate your Gpa grade C or B or A


grade = float(input('please enter your grades in percentage way : '))
if grade >= 60 and grade <=75 :
    print (f'Fine (-_-)! your grade are weak , your grade {grade} = "C" in GPA  ')
elif grade >= 76 and grade <=89 :
    print (f'well Done (~_~)! your grade are very good  , your grade {grade} = "B" in GPA  ')
elif grade >=0 and grade <=59 :
    print (f'oops (-__-)! your grade are very Bad  , your grade {grade} = "F" in GPA  ')
else:
    if grade > 100 :
        print(f'Grade {grade} out of the range ,try again ')
    elif grade < 0 :
        print(f'Grade {grade} out of the range ,try again ')
    else :    
        print (f'execelnt (^_^)! your grade are wonderful  , your grade {grade} = "A" in GPA  ')