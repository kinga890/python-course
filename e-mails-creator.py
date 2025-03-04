

student_id= input('Enter student\'s id or type \'exit\' ')      # FIXME: this part is redundant
domain= '@example.com'

email=student_id + domain                                       # FIXME: and this
email_list=[]

while True:
    student_id= input('Enter student\'s id or type \'exit\' ')
    email = student_id + domain
    email_list.append(email)                                  
    if student_id == 'exit':                                   # FIXME: this check can be moved so that the pop will not be needed
        break
email_list.pop() #usuwam ostatni e-mail "exit@example.pl'

for _ in email_list:                                           # NEAT: "_" is reserved for variables that are unused, this one is
    print(_)                                                   # so it should be named appropriately (e.g. "email")
