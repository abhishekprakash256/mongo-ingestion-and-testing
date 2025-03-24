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
db_helper.create_user(username='test_user', password='secure_pass', userhash='user_hash')

# Fetch user details
print(db_helper.get_user_password(username='test_user'))
print(db_helper.get_user_hash(username='test_user'))
print(db_helper.check_user_exists(username='test_user'))


print(db_helper.get_all_users())