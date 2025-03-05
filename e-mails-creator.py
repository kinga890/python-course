#(a student's id is a six-digit number)

DOMAIN= '@example.com'
email_list=[]

while True:
    student_id= input('Enter student\'s id or type \'exit\' ')
    email = student_id + DOMAIN

    if student_id == 'exit':
        break
    if email in email_list:
        print('email already exist')
        continue
    if len(student_id) == 6 and student_id.isnumeric() == True:
        email_list.append(email)
    else:
        print('invalid id number')

email_list.sort()

for email_easy_access in email_list:
    print(email_easy_access)