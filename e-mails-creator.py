#(a student's id is a six-digit number)

domain= '@example.com'
email_list=[]

while True:
    student_id= input('Enter student\'s id or type \'exit\' ')
    email = student_id + domain

    if student_id == 'exit':
        break
    if email in email_list:
        print('email already exist')
    if len(student_id) == 6 and student_id.isnumeric() == True:
        email_list.append(email)
    else:
        print('invalid id number')

email_list.sort()
email_list=set(email_list)
for email_easy_access in email_list:
    print(email_easy_access)