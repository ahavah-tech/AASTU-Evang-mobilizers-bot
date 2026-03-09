import telebot
import os
from .config import BOT_TOKEN
from .database import save_chat
from .keyboards import main_keyboard, muslim_keyboard, Only_Jesus_keyboard, Islamic_keyboard

API_KEY_NEW = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_KEY_NEW)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🙏 Welcome to AASTU Evangelism Bot",
        reply_markup=main_keyboard()
    )
@bot.message_handler(func=lambda m: m.text == "Common Muslim questions about Christianity")
def muslim_menu(message):
    bot.send_message(
        message.chat.id,
        "Here are common Muslim questions:",
        reply_markup=muslim_keyboard()
    )   
#"Son of God" question
@bot.message_handler(func=lambda m: m.text == "አንድ አምላክ እንዴት የአንድ አምላክ ልጅ ይባላል?")
def handle_son_of_god(message):
    file_path =("assets/son_of_god.pdf.Docx","assets/የኢየሱስ መለኮታዊ ልጅነት.pptx")
    if os.path.exists(file_path):
        with open(file_path, "rb") as doc:
            bot.send_document(message.chat.id, doc, caption="Here is the PDF explanation.")
    else:
        bot.send_message(message.chat.id, "File not found. Please contact the admin.")

#"How many Gods" question
@bot.message_handler(func=lambda m: m.text == "ስንት አምላክ ነው ያላቹ?")
def handle_god_count(message):
    file_path = "assets/how many God.Docx"
    if os.path.exists(file_path):
        with open(file_path, "rb") as doc:
            bot.send_document(message.chat.id, doc, caption="Study this guide on the Trinity.")
    else:
        bot.send_message(message.chat.id, "Explanation document is missing.")
@bot.message_handler(func=lambda m: m.text == "አምላክ እንዴት ይወልዳል?")
def handle_begetting(message):
    file_path = "assets/begetting.Docx"
    if os.path.exists(file_path):
        with open(file_path, "rb") as doc:
            bot.send_document(message.chat.id, doc, caption="Study this guide on the Trinity.")
    else:
        bot.send_message(message.chat.id, "Explanation document is missing.")    

@bot.message_handler(func=lambda m: m.text == "አምላክ እንዴት ወደ አምላክ ይፀልያል?")
def handle_pray(message):
    file_path =  "assets/Jesus_pray.Docx"
    if os.path.exists(file_path):
        with open(file_path, "rb") as doc:
            bot.send_document(message.chat.id, doc, caption="Study this guide on the nature of Jesus Christ.")
    else:
        bot.send_message(message.chat.id, "Explanation document is missing.")


@bot.message_handler(func=lambda m: m.text == "ሥላሴ ሚለው ቃል  መፅሐፍ ቅዱስ ላይ አለ ወይ?")
def handle_word_Trinity(message):
    file_path = "assets/ The word Trinity.Docx"
    if os.path.exists(file_path):
        with open(file_path, "rb") as doc:
            bot.send_document(message.chat.id, doc, caption="Study this guide on the Trinity.")
    else:
        bot.send_message(message.chat.id, "Explanation document is missing.")

@bot.message_handler(func=lambda m: m.text == "እኩል ስልጣን ካላቸው በ ዩሐ5 ለምን አብ ከእኔ ይበልጣል አለ?")
def handle_equality_Trinity(message):
    file_path = "assets/Equality with God Father.Docx"
    if os.path.exists(file_path):
        with open(file_path, "rb") as doc:
            bot.send_document(message.chat.id, doc, caption="Study this guide on the Trinity.")
    else:
        bot.send_message(message.chat.id, "Explanation document is missing.")        
@bot.message_handler(func=lambda m: m.text == "⬅ Back to Main Menu")
def back_main(message):
    bot.send_message(
        message.chat.id,
        "Back to main menu:",
        reply_markup=main_keyboard()
    )


@bot.message_handler(func=lambda m: m.text == "Only Jesus materials")
def only_Jesus_menu(message):
    bot.send_message(
        message.chat.id,
        "Here are materials:",
        reply_markup= Only_Jesus_keyboard()
    ) 

@bot.message_handler(func=lambda m: m.text == "አብ፣_ወልድና_መንፈስ_ቅዱስ_የተለያዩ_አካላት_አይደሉምን")
def handle_separate_god(message):
    file_path = "assets/አብ፣_ወልድና_መንፈስ_ቅዱስ_የተለያዩ_አካላት_አይደሉምን.pptx"
    if os.path.exists(file_path):
        with open(file_path, "rb") as doc:
            bot.send_document(message.chat.id, doc, caption="Here is the PPT explanation.")
    else:
        bot.send_message(message.chat.id, "File not found. Please contact the admin.")

@bot.message_handler(func=lambda m: m.text == "የኦንሊ_ጂሰሱ_አብ፣_ወልድና_መንፈስ_ቅዱስ")
def handle_essence_god(message):
    file_path = "assets/የኦንሊ_ጂሰሱ_አብ፣_ወልድና_መንፈስ_ቅዱስ.pptx"
    if os.path.exists(file_path):
        with open(file_path, "rb") as doc:
            bot.send_document(message.chat.id, doc, caption="Here is the PPT explanation.")
    else:
        bot.send_message(message.chat.id, "File not found. Please contact the admin.")

@bot.message_handler(func=lambda m: m.text == "ትምህርተ ሥላሴና የአረማውያኑ")
def handle_Trinity_god(message):
    file_path = "assets/ትምህርተ ሥላሴና የአረማውያኑ.pptx"
    if os.path.exists(file_path):
        with open(file_path, "rb") as doc:
            bot.send_document(message.chat.id, doc, caption="Here is the PPT explanation.")
    else:
        bot.send_message(message.chat.id, "File not found. Please contact the admin.")

@bot.message_handler(func=lambda m: m.text == "የውሃ_ጥምቀት_በኢየሱስ_ክርስቶስ_ስም")
def handle_baptizm(message):
    file_path = "assets/የውሃ_ጥምቀት_በኢየሱስ_ክርስቶስ_ስም.pptx"
    if os.path.exists(file_path):
        with open(file_path, "rb") as doc:
            bot.send_document(message.chat.id, doc, caption="Here is the PPT explanation.")
    else:
        bot.send_message(message.chat.id, "File not found. Please contact the admin.")

@bot.message_handler(func=lambda m: m.text == "⬅ Back to Main Menu")
def back_main(message):
    bot.send_message(
        message.chat.id,
        "Back to main menu:",
        reply_markup=main_keyboard()
    )


@bot.message_handler(func=lambda m: m.text == "Muslim Evangelism materials")
def materials_menu(message):
    bot.send_message(
        message.chat.id,
        "Here are common materials:",
        reply_markup = Islamic_keyboard()
    )


@bot.message_handler(func=lambda m: m.text =="Muslim Apologetics")
def handle_apologetics(message):
    file_path =["assets/Muslim Apologetics - Alemgena Bethel KHC seminar series.pptx",
                "assets/Muslim apologetics - Contradiction the bible - series 3.pptx",
                "assets/Muslim_apologetices_what_the_qur'an_says_abouth_Bible_and_Jesus",
                "assets/Muslim_apologetics_-_Is_Jesus_divine[1]"
                ]
    if os.path.exists(file_path):
        with open(file_path,"rb") as doc:
            bot.send_document(message.chat.id, doc, caption ="Read this carryfully")
    else:
        bot.send_message(message.chat.id,"File not found. please contact the admin.")        


@bot.message_handler(func=lambda m: m.text =="ቁርአን pdf")
def handle_Quran(message):
    file_path =["assets/ቁርአን pdf.pdf", 
                "assets/ግጭት.pdf"
                ]
    if os.path.exists(file_path):
        with open(file_path, "rb") as doc:
            bot.send_message(message.chat.id, doc, caption ="Here is the PPT explanation")
    else:
        bot.send_message(message.chat.id, "File not found. please contact the admin.")


@bot.message_handler(func=lambda m: m.text == "⬅ Back to Main Menu")
def back_main(message):
    bot.send_message(
        message.chat.id,
        "Back to main menu:",
        reply_markup=main_keyboard()
    )
@bot.message_handler(func=lambda m: m.text)
def fallback(message):
    save_chat(message.chat.id, message.from_user.username, message.text)