import subprocess

try:
    from pyrubi import Client
    from pyrubi.types import Message

except:
    try:
        print("a 'pyrubi' lib not find pls wait for downloading...")
        result = subprocess.run(["pip", "install", "pyrubi"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Successfully installed pyrubi.")
        print("Output:", result.stdout)

    except subprocess.CalledProcessError as e:
        print("Failed to install pyrubi.")
        print("Error:", e.stderr)

    except FileNotFoundError:
        print("Could not enter. Pip is not installed or not found.")

import json
import requests

def file_write():
    with open('data.json','w') as file:
        try:
            json.dump({
                    'blocks': blocks,
                    'keywords' : keywords,
                    'api': API,
                    'api_word': API_WORD
                },
                file, indent=4)
        except:
            json.dump({
                    'blocks': [],
                    'keywords' : [],
                    'api': "https://api.daradege.ir/ai?text=",
                    'api_word': "text"
                },
                file, indent=4)

try:
    with open('data.json','r') as file:
        data = json.load(file)
        keywords = data['keywords']
        blocks = data['blocks']
        API = data['api']
        API_WORD = data['api_word']
except Exception as e:
    print('the before not find a json file')
    print(f"i'm a make json file: {e}")
    file_write()

bot = Client('session')
ADMIN_GUIDs = [bot.get_me()['user']['user_guid']] #inter there:inter your object guid
admin = False

decur_messages= []

print(f"---=== client {bot.get_me()['user']['username']} is ready===---")

def startswith(text: str):

    for i in keywords:
        if text.startswith(i):
            return len(i)

@bot.on_message()
def message_handler(message:Message):
    global API, API_WORD, admin
    try:
        text = message.text
    except:
        return
    st = startswith(text)
    if st and message.author_guid not in blocks:
        try:
            response = requests.get(f'{API}{text[st:]}')
            response = response.json()[API_WORD]
            message.reply(response)
        except:
            message.reply('خطا در دریافت پاسخ لطفا از درستی api متمعن شوید')

    elif st and message.author_guid in blocks:
        message.reply('شما حق استفاده از ربات را ندارید')
    
    if message.text == 'admin':
        if message.author_guid in ADMIN_GUIDs:
            admin = not admin
            message.reply(f'حالت ادمین {admin} فعال شد'.replace('False', 'غیر').replace('True',''))

    if message.author_guid in ADMIN_GUIDs and admin:
        try:
            if text == '/block':
                try:
                    message.reply_info
                    blocks.append(message.reply_info.author_guid)
                    message.reply(f"کاربر {bot.get_chat_info(message.reply_info.author_guid)['user']['first_name']} از استفاده از سلف محروم شد")

                except:
                    message.reply('روی کاربر جهت مصدود کردن پاسخ کنید')

            if text == '/unblock':
                try:
                    message.reply_info
                    blocks.remove(message.reply_info.author_guid)
                    message.reply(f"کاربر {bot.get_chat_info(message.reply_info.author_guid)['user']['first_name']} دیگر از استفاده از سلف محروم نیست")

                except:
                    message.reply('روی کاربر جهت رفع مصدود کردن پاسخ کنید')
            
            elif text.startswith('/chenge_key'):
                keywords.append(text[12:])
                message.reply(f'کیلید واژه {text[12:]} بر فهرست کلید واژگان افزوده شد')
            
            elif text == '/save':
                file_write()
                message.reply('داده ها ذخیره سازی شدند')

            elif text.startswith('/chenge_api_word'):
                API_WORD = text[17:]
                message.reply('کلمه API هم به درستی تنظیم شد')

            elif text.startswith('/chenge_api'):
                API = text[11:]
                message.reply('ای پی ای با درستی تنظیم شد')
            
            elif text == '/get_data':
                message.reply(
"""
لیست کلید واژگان:
{}

لیست کاربران مصدود شده:
{}

آدرس aip:
{}

کلید واژه api:
{}

ادمین ها:
{}

این ها تمام اطلاعات قابل تغییر هستند
""".format(
    '\n'.join(keywords),
    "\n".join([bot.get_chat_info(block)['user']['first_name'] for block in blocks]),
    API,
    API_WORD,
    '\n'.join([bot.get_chat_info(block)['user']['first_name'] for block in ADMIN_GUIDs])
    )
)
            elif text == '/help':
                message.reply(
'''
دستورات و راهنمای سلف هوش مصنوعی:
برای استفاده از هوش مصنوعی فقط کافیست ابتدا کلید واژه تنظیم شده را وارد کنید بعد سوال خود را بپرسید مثلا اکر کلید واژه شما هوش مصنوعی باشد:
هوش مصنوعی ایران کجاس؟

دستورات:
/help
- دستوری برای راهنمایی کاربر

/get_data
- دستوری برای بررسی تنظیمات ربات

/save
- دستوری برای ذخیره اطلاعات

/block {reply}
- دستوری برای مصدود کردن کاربران از استفاده

/unblock {reply}
- دستوری برای آزاد سازی استفاده کاربران

/add_admin {reply}
-برای تنظیم مدیران جدید

/rem_admin {reply}
-برای حذف ادمین های از پیش تایین شده

/chenge_key {کلید واژه}
- دستوری برای تنظیم کلید واژه

/rem_chenge_key {کلید واژه}
-برای حذف کلید واژه ها

/chenge_api {api}
- دستوری برای تنظیم api

/chenge_api_key {api key}

-برای تنظیم کلید واژه اتصال api



'''
                    )
            elif message.text == '/add_admin':
                ADMIN_GUIDs.append(message.reply_info.author_guid)
                message.reply(f'کاربر {bot.get_chat_info(message.reply_info.author_guid)['user']['first_name']} به فهرست ادمین ها پیوست')
            
            elif message.text == '/rem_admin':
                ADMIN_GUIDs.append(message.reply_info.author_guid)
                message.reply(f'کاربر {bot.get_chat_info(message.reply_info.author_guid)['user']['first_name']} دیگر در فهرست ادمین ها نیست')
        except Exception as e:
            message.reply(f'خطای غیر منتظره در ادمین پنل: {e}')

        #print(bot.get_chat_info(message.author_guid)['user']['first_name'])
    #bot.download(object_guid=message.author_guid, message_id=message.message_id, save='voice.audio')

bot.run()