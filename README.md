# ParsingTest
This is a simple parsing tool with a test file: `test.ini`
It uses the stdlib `configparser`

# Usage
Step 1:
Run the `parse.py` by using:
```bash
python parse.py
```
Step 2:
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

The application will stop running when receiving a correct Key name by outputting the Value for it. If you want to get another value for a Key name then you simply run the file again in Step 1.