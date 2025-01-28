

#condition is like checking in several ocuation 
print("==============Welcome to Exam Score=============")
exam_scrore='1' #input('Write your score(0-100) :')
score=int(exam_scrore)
grade=''
if score<=100 and score>=80:
    grade='A+'
elif score<=79 and score>=60:
    grade='A'
elif score<=59 and score>=50:
    grade='B'
elif score<=49 and score>=40:
    grade='C'
elif score<=39 and score>=33:
    grade='D'
elif score>100:
    grade='Invalid'
else:
    grade='F'

#print('You got grade of :',grade)

age=11
islegal=True if age>=20 else False

print(islegal)


