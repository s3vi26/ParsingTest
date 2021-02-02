# ParsingTest
This is a simple parsing tool with a test file: `test.ini`
It uses the stdlib `configparser`

# Usage

Run the `parse.py` by using:
```bash
python parse.py
```

It will prompt you with an `input()` question of 
```bash
Please provide a Key name you want the Value for:
```

If the Key name does not exist it will reask the question and provide the key names available for input
```bash
Sorry, that isnt a Key I can read. Please select from the list below:
 ['host', 'server_id', 'server_load_alarm', 'user', 'verbose', 'test_mode', 'debug_mode', 'log_file_path', 'send_notifications']
Please provide a Key name you want the Value for:
```