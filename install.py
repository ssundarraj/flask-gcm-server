settings_string = """API_KEY = '{API_KEY}'
DATA_STORE = '{DATA_STORE}'
MYSQL = {MYSQL}
"""
API_KEY = None
DATA_STORE = None
MYSQL = {'user': None,
         'pass': None,
         'host': None,
         'db': None}
attempts = 0
max_attempts = 4
method_prompt = "Enter the method you wish to save the data: " \
                + "\n[1] File on the disk"\
                + "\n[2] sqllite"\
                + "\n[3] mysql\n"

API_KEY = raw_input("Enter API Key: ")
while attempts < max_attempts:
    if attempts:
        method_prompt = "Incorrect option. Select one of the given options: "
    DATA_STORE = raw_input(method_prompt)
    if DATA_STORE is '1':
        DATA_STORE = 'file'
        attempts += max_attempts
        # create File
    elif DATA_STORE is '2':
        DATA_STORE = 'sqlite'
        attempts += max_attempts
        # create db file
    elif DATA_STORE is '3':
        DATA_STORE = 'mysql'
        attempts += max_attempts
        # connect and create db
    else:
        attempts += 1

settings_string = settings_string.format(**locals())

with open('./settings.py', 'w') as settings_file:
    settings_file.write(settings_string)
