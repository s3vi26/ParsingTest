import configparser
from IPython.display import clear_output
# set up config parser
config = configparser.ConfigParser()
config.sections()
# custom config for boolean values to be properly returned
config.BOOLEAN_STATES = {'on': True, 'off': False, 'yes': True, 'true': True}
# read file with parser
config.read('test.ini')
# set variable for the only section
default_section = config['DEFAULT']
# set list variable for all keys to reference
the_keys_list = list(config['DEFAULT'].keys())

result = 'WRONG'
while result not in the_keys_list:
  result = input("Please provide a Key name you want the Value for: ").lower()
  # if the provided input isnt in the_keys_list then continue to ask for Key name
  if result not in the_keys_list:
    clear_output()
    print(f"Sorry, that isnt a Key I can read. Please select from the list below: \n {the_keys_list}")
    continue
  # check for keys that deliver boolean values
  if result == 'test_mode' or result == 'debug_mode' or result == 'verbose' or result == 'send_notifications':
    print(config['DEFAULT'].getboolean(result))
  # check for keys that deliver int values
  elif result == 'server_id':
    print(int(default_section[result]))
  # check for keys that deliver float values
  elif result == 'server_load_alarm':
    print(float(default_section[result]))
  else:
    print(default_section[result])