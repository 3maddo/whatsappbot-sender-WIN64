# WhatsApp Bot

This is a Python-based automation bot for sending messages via WhatsApp Web.

## Features
- Sends automated messages to contacts from a CSV file.
- Supports sending images along with messages.
- Uses PyAutoGUI for automation and web scraping.

## Requirements

- Python 3.x
- Google Chrome
- ChromeDriver

### Install Dependencies
```bash
pip install pyautogui pyperclip requests
```

## Project Structure
```
whatsappbot/
│
├── chromedriver.exe
├── e.py
├── image.jpg
├── LICENSE.chromedriver
├── numbers.csv
├── python.py
├── PyWhatKit_DB.txt
├── sent_numbers.csv
├── THIRD_PARTY_NOTICES.chromedriver
└── whatsboth.py
```

## Usage

1. Run the script:
```bash
python whatsboth.py
```

2. WhatsApp Web will open. Scan the QR code if not already logged in.

3. The bot will send the message from `whatsboth.py` to the numbers in `numbers.csv`.

## CSV File Format

Ensure the `numbers.csv` file contains numbers in this format: ( without + )
```
1234567890
0987654321
```

## Notes
- Make sure ChromeDriver is compatible with your Chrome version.
- Allow the bot enough time to interact with WhatsApp Web.

## Disclaimer
This project is for educational purposes only. Use it responsibly and comply with WhatsApp's terms of service.

