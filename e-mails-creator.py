

student_id= input('Enter student\'s id or type \'exit\' ')
domain= '@example.com'

email=student_id + domain
email_list=[]

if student_id:
    while True:
        student_id= input('Enter student\'s id or type \'exit\' ')
        email = student_id + domain
        email_list.append(email)
        if student_id == 'exit':
            break
else:
    print('enter vaild id')
email_list.pop() #usuwam ostatni e-mail "exit@example.pl'

email_list=set(email_list)  #aby e-emaile się nie powtarzały
for _ in email_list:
    print(_)

email = input('username')

if email:
    print('not value')
else:
    print('not value')