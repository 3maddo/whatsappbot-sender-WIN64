import pyautogui
import time
import csv
import webbrowser
import pyperclip
import requests

# Wait a bit to open WhatsApp Desktop
print("Wait a bit, then focus on the WhatsApp window...")
time.sleep(5)

# The message to be sent
message = """
HELLO WORLD
"""

# Path to the CSV file with numbers
csv_file_path = "C:\\Users\\emada\\OneDrive\\Desktop\\whatsappbot\\numbers.csv"

# Path to the image to be sent
image_path = "C:\\Users\\emada\\OneDrive\\Desktop\\whatsappbot\\image.jpg"

# Function to open the contact via number
def open_contact_by_number(number):
    url = f'https://wa.me/{number}'
    webbrowser.open(url)
    time.sleep(12)  # Wait a bit for the page to load

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Number {number} does not have a WhatsApp account.")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error accessing number {number}: {e}")
        return False

    return True

# Read numbers from the CSV file
def read_numbers_from_csv(file_path):
    numbers = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            numbers.append(row[0])  # Add number to the list
    return numbers

# Read previously sent numbers from the CSV file
def read_sent_numbers(file_path):
    sent_numbers = set()
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                sent_numbers.add(row[0])
    except FileNotFoundError:
        pass
    return sent_numbers

# Save numbers that have been sent messages to a new file
def save_sent_numbers(sent_numbers):
    with open("C:\\Users\\emada\\OneDrive\\Desktop\\whatsappbot\\sent_numbers.csv", mode='w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Number"])
        for number in sent_numbers:
            csv_writer.writerow([number])

# Read numbers from the CSV file
numbers = read_numbers_from_csv(csv_file_path)

# Read previously sent numbers
sent_numbers = read_sent_numbers("C:\\Users\\emada\\OneDrive\\Desktop\\whatsappbot\\sent_numbers.csv")

# List to store numbers sent in this session
new_sent_numbers = []

# Send image and message to each number
for i, number in enumerate(numbers):
    if i >= 80:  # Send messages to 40 numbers only
        break

    if number in sent_numbers:
        print(f"Number {number} has already been messaged.")
        continue  # Move to the next number

    if not open_contact_by_number(number):  # If the number is not on WhatsApp
        continue  # Skip the number

    print(f"Sending image and message to: {number}")
    time.sleep(5)  # Wait a bit for the link to open

    pyautogui.click(100, 100)  # Click a random spot in the browser to ensure focus

    # Send the image first
    pyautogui.hotkey('ctrl', 'shift', 'a')
    time.sleep(25)  # Wait a bit for the upload window to open
    pyautogui.write(image_path)
    pyautogui.press('enter')
    time.sleep(5)  # Wait a bit after sending the image

    # Copy the message to the clipboard using pyperclip
    pyperclip.copy(message)

    # Paste the message from the clipboard
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.keyDown('enter')
    time.sleep(3)  # Short wait to simulate the press
    pyautogui.keyUp('enter')
    time.sleep(3)

    # Add the number to the sent list for this session
    new_sent_numbers.append(number)
    print(f"Image and message sent to {number}")

# Merge sent numbers from this session with previously sent numbers
sent_numbers.update(new_sent_numbers)

# Save the numbers that have been messaged
save_sent_numbers(sent_numbers)

print("Images and messages have been sent to all numbers (up to 40).")
