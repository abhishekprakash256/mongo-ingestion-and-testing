from pgsql_helper_kit import create_db_session, User, Db_Helper

# Create database session
engine, session = create_db_session(
    host_name='localhost',
    db_name='test_db',
    user_name='abhi',
    password='mysecretpassword'
)
db_helper = Db_Helper(session, engine)

# Create a new user
db_helper.create_user(username='abhi', password='Qwerty@1234', userhash='JHlks#5')
db_helper.create_user(username='abhi2', password='Qwerty@1235', userhash='JHlks#6')
db_helper.create_user(username='abhi3', password='Qwerty@1236', userhash='JHlks#7')


# Fetch user details
print(db_helper.get_user_password(username='abhi'))

print(db_helper.get_user_hash(username='abhi'))

print(db_helper.check_user_exists(username='abhi'))

print(db_helper.get_all_users())


