import pyautogui
import time
import csv
import webbrowser  # فتح الرابط باستخدام المتصفح مباشرة
import pyperclip  # لنسخ النصوص إلى الحافظة

# الانتظار قليلاً حتى تتمكن من فتح واتساب لسطح المكتب
print("انتظر قليلاً، ثم ركز على نافذة واتساب...")
time.sleep(5)

# الرسالة التي تريد إرسالها
message = """مرحباً! هذه رسالة آلية من البوت.

هلا، معاكم صوفيا من متجر 612! ✨

حابين نقدم لكم زيت بذور الصبّار الأصلي – سرّ الجمال الطبيعي!

💥 عرض لفترة محدودة: 3 زجاجات (10 مل) بس 30 دينار كويتي!

متجرنا مو بس زيت، عندنا مكملات غذائية وأيضا استشارات طبية مجانية!
الكمية محدودة والتوصيل سريع 🚚
للحجز والاستفسارات، تقدرون تروحون على https://www.herbalistclinic.com
"""

# مسار ملف CSV الذي يحتوي على الأرقام
csv_file_path = "C:\\Users\\emada\\OneDrive\\Desktop\\whatsappbot\\numbers.csv"

# مسار الصورة التي تريد إرسالها
image_path = "C:\\Users\\emada\\OneDrive\\Desktop\\whatsappbot\\image.jpg"

# دالة لفتح جهة الاتصال بناءً على الرقم
def open_contact_by_number(number):
    # افتح نافذة الدردشة مع الرقم باستخدام الرابط المباشر عبر المتصفح
    url = f'https://wa.me/{number}'
    webbrowser.open(url)  # فتح الرابط باستخدام المتصفح
    time.sleep(5)  # الانتظار قليلاً حتى يتم تحميل المحادثة

# قراءة الأرقام من ملف CSV
def read_numbers_from_csv(file_path):
    numbers = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # تخطي العنوان
        for row in csv_reader:
            numbers.append(row[0])  # إضافة الرقم إلى القائمة
    return numbers

# قراءة الأرقام من ملف CSV
numbers = read_numbers_from_csv(csv_file_path)

# إرسال صورة ثم رسالة لكل رقم
for number in numbers:
    print(f"إرسال صورة ثم رسالة إلى: {number}")
    open_contact_by_number(number)  # فتح الدردشة مع الرقم
    time.sleep(5)  # الانتظار قليلاً حتى يفتح الرابط بشكل صحيح

    # إرسال الصورة أولاً
    pyautogui.hotkey('ctrl', 'shift', 'a')  # فتح نافذة تحميل الملفات (في WhatsApp Web)
    time.sleep(2)  # الانتظار قليلاً حتى يتم فتح نافذة تحميل الصورة
    pyautogui.write(image_path)  # كتابة مسار الصورة
    pyautogui.press('enter')  # إرسال الصورة
    time.sleep(5)  # الانتظار قليلاً بعد إرسال الصورة

    # نسخ الرسالة إلى الحافظة باستخدام pyperclip
    pyperclip.copy(message)

    # لصق الرسالة من الحافظة
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')  # إرسال الرسالة
    time.sleep(2)  # الانتظار بعد إرسال الرسالة

    print(f"تم إرسال الصورة والرسالة إلى {number}")

print("تم إرسال الصور والرسائل لجميع الأرقام.")
