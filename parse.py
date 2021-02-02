import configparser

config = configparser.ConfigParser()
config.sections()

with open('test.ini', 'r') as f:
  config_file = f.read()


config.read('test.ini')
  
print(config.sections())

if 'DEFAULT' in config:
  print(config['DEFAULT'])
  for key in config['DEFAULT']:
    print(key)


while True: 
  result = input("Please provide a key to receive it's value: ")
  for key in config['DEFAULT']:
    if key == result.lower():
      print(key)