

student_id= input('Enter student\'s id or type \'exit\' ')
domain= '@example.com'

email=student_id + domain
email_list=[]

while True:
    student_id= input('Enter student\'s id or type \'exit\' ')
    email = student_id + domain
    email_list.append(email)
    if student_id == 'exit':
        break
email_list.pop() #usuwam ostatni e-mail "exit@example.pl'

for _ in email_list:
    print(_)