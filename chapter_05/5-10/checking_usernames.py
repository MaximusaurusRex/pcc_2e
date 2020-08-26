current_users = ['Hunter2', 'eDwarD_snowDen',
                 'trump2020', 'BlaZeit420', 'asdfasdf']
new_users = ['oatmealcookie53', 'dundermifflin10',
             'Blazeit420', 'foobar01', 'Edward_Snowden']

for i in range(len(current_users)):
    current_users[i] = current_users[i].lower()

for new_user in new_users:
    if new_user.lower() in current_users:
        print('You will need to enter a new username.')
    else:
        print('The username is available.')
