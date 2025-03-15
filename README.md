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
├── whatsboth.py
└── autoHotkey.ahk
```

## Usage

1. Run the script:
```bash
python whatsboth.py
```

2. WhatsApp Web will open. Scan the QR code if not already logged in.

3. The bot will send the message from `whatsboth.py` to the numbers in `numbers.csv`.

## CSV File Format

Ensure the `numbers.csv` file contains numbers in this format: ( whithout + )
```
1234567890
0987654321
```

## Notes
- Make sure ChromeDriver is compatible with your Chrome version.
- Allow the bot enough time to interact with WhatsApp Web.
- An **AutoHotkey script (`autoHotkey.ahk`)** is included to automate the process of attaching images. Once WhatsApp Web is open, this script will handle the file selection and sending process. Run the script by double-clicking it or using the following command:
```bash
AutoHotkey.exe autoHotkey.ahk
```
  Ensure AutoHotkey is installed on your system for this to work.

## Disclaimer
This project is for educational purposes only. Use it responsibly and comply with WhatsApp's terms of service.

