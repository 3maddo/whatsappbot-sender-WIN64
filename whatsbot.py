import pyautogui
import time
import csv
import webbrowser
import pyperclip
import requests

# الانتظار قليلاً حتى تتمكن من فتح واتساب لسطح المكتب
print("انتظر قليلاً، ثم ركز على نافذة واتساب...")
time.sleep(5)

# الرسالة التي تريد إرسالها
message = """
هلا، معاكم صوفيا من متجر 612! ✨

حابين نقدم لكم زيت بذور الصبّار الأصلي – سرّ الجمال الطبيعي!

💥 عرض لفترة محدودة: 3 زجاجات (10 مل) بس 30 دينار كويتي!

متجرنا مو بس زيت، عندنا مكملات غذائية وأيضا استشارات طبية مجانية!
الكمية محدودة والتوصيل سريع 🚚
للحجز والاستفسارات، تقدرون تروحون على 
https://www.herbalistclinic.com
"""

# مسار ملف CSV الذي يحتوي على الأرقام
csv_file_path = "C:\\Users\\emada\\OneDrive\\Desktop\\whatsappbot\\numbers.csv"

# مسار الصورة التي تريد إرسالها
image_path = "C:\\Users\\emada\\OneDrive\\Desktop\\whatsappbot\\image.jpg"

# دالة لفتح جهة الاتصال بناءً على الرقم
def open_contact_by_number(number):
    url = f'https://wa.me/{number}'
    webbrowser.open(url)
    time.sleep(12)  # الانتظار قليلاً حتى يتم تحميل الصفحة بشكل جيد
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"الرقم {number} ليس لديه حساب واتساب.")
            return False
    except requests.exceptions.RequestException as e:
        print(f"خطأ في الوصول إلى الرقم {number}: {e}")
        return False

    return True

# قراءة الأرقام من ملف CSV
def read_numbers_from_csv(file_path):
    numbers = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            numbers.append(row[0])  # إضافة الرقم إلى القائمة
    return numbers

# قراءة الأرقام المرسلة سابقًا من ملف CSV
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

# حفظ الأرقام التي تم إرسال الرسائل إليها في ملف جديد
def save_sent_numbers(sent_numbers):
    with open("C:\\Users\\emada\\OneDrive\\Desktop\\whatsappbot\\sent_numbers.csv", mode='w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Number"])
        for number in sent_numbers:
            csv_writer.writerow([number])

# قراءة الأرقام من ملف CSV
numbers = read_numbers_from_csv(csv_file_path)

# قراءة الأرقام المرسلة سابقًا
sent_numbers = read_sent_numbers("C:\\Users\\emada\\OneDrive\\Desktop\\whatsappbot\\sent_numbers.csv")

# قائمة لحفظ الأرقام التي تم إرسال الرسائل إليها في هذه الجلسة
new_sent_numbers = []

# إرسال صورة ثم رسالة لكل رقم
for i, number in enumerate(numbers):
    if i >= 80:  # إرسال الرسائل إلى 40 رقم فقط
        break
    
    if number in sent_numbers:
        print(f"الرقم {number} تم إرسال رسالة له بالفعل.")
        continue  # الانتقال إلى الرقم التالي
    
    if not open_contact_by_number(number):  # إذا لم يكن الرقم على واتساب
        continue  # تخطي الرقم
    
    print(f"إرسال صورة ثم رسالة إلى: {number}")
    time.sleep(5)  # الانتظار قليلاً حتى يفتح الرابط بشكل صحيح

    pyautogui.click(100, 100)  # النقر في مكان عشوائي في نافذة المتصفح للتأكد من أن الفوكس على النافذة
    
    # إرسال الصورة أولاً
    pyautogui.hotkey('ctrl', 'shift', 'a')
    time.sleep(25)  # الانتظار قليلاً حتى يتم فتح نافذة تحميل الصورة
    pyautogui.write(image_path)
    pyautogui.press('enter')
    time.sleep(5)  # الانتظار قليلاً بعد إرسال الصورة

    # نسخ الرسالة إلى الحافظة باستخدام pyperclip
    pyperclip.copy(message)

    # لصق الرسالة من الحافظة
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.keyDown('enter')
    time.sleep(3)  # فترة انتظار قصيرة لمحاكاة الضغط
    pyautogui.keyUp('enter')
    time.sleep(3)
    # إضافة الرقم إلى قائمة الأرقام المرسلة في هذه الجلسة
    new_sent_numbers.append(number)
    print(f"تم إرسال الصورة والرسالة إلى {number}")

# دمج الأرقام المرسلة في هذه الجلسة مع الأرقام المرسلة مسبقًا
sent_numbers.update(new_sent_numbers)

# حفظ الأرقام التي تم إرسال الرسائل إليها
save_sent_numbers(sent_numbers)

print("تم إرسال الصور والرسائل لجميع الأرقام (حتى 40).")
