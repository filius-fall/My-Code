from sql_tink import db
db.create_all()


from sql_tink import User,Guest
d = input('Are you User or Guest:')


if d == 'User' or d == 'Guest':
    s = int(input('Enter no of users you are adding:'))

    for i in range(s):

        if d == 'User' :
            user_name = input('Enter username:')
            mail = input('Enter email address:')
            user = User(username = user_name, email = mail)
            print('%s and %s has been added as user' %(user_name,mail))
            db.session.add(user)
            db.session.commit()
        elif d == 'Guest':
            name = input('Enter your name:')
            guest = Guest(name = name)
            print('%s has been added as guest' %(name))
            db.session.add(guest)
            db.session.commit()
else :
        print("YOU DON'T BELONG HERE")


for c in range(3):
    b = input('Dp you want to Query all data(y/n):')

    if b == 'y':
        a = User.query.all()

        print(a)
    elif b == 'n':
        print('Thank You')
    else:
        print('Invalid Input!! Type either y or n')
        print('you have %s attempts remaining' %(2-c))
