from sql_tink import db
db.create_all()


from sql_tink import User
s = int(input('Enter no of users you are adding:'))

for i in range(s):
    user_name = input('Enter username:')
    mail = input('Enter email address:')
    user = User(username = user_name, email = mail)
    print('%s and %s has been added' %(user_name,mail))
    db.session.add(user)
    db.session.commit()

User.query.all()




