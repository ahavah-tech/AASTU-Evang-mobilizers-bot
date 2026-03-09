from telebot.types import ReplyKeyboardMarkup

def main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        "I want someone to talk to",
        "Common Muslim questions about Christianity"
    )
    markup.add(
        "Only Jesus materials",
        "I want Bible study plan"
    )
    markup.add("Muslim Evangelism materials",
               "Heart of David"
    )
    markup.add("I pressed it by mistake",
               "")
    return markup

def muslim_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        "አንድ አምላክ እንዴት የአንድ አምላክ ልጅ ይባላል?",
        "አምላክ እንዴት ይወልዳል?"
    )
    markup.add(
        "አምላክ እንዴት ወደ አምላክ ይፀልያል?",
        "ሥላሴ ሚለው ቃል  መፅሐፍ ቅዱስ ላይ አለ ወይ?"
    )
     
    markup.add(
        "እኩል ስልጣን ካላቸው በ ዩሐ5 ለምን አብ ከእኔ ይበልጣል አለ?",
        "ስንት አምላክ ነው ያላቹ?"
    )

    markup.add("⬅ Back to Main Menu")
    return markup

def Only_Jesus_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("አብ፣_ወልድና_መንፈስ_ቅዱስ_የተለያዩ_አካላት_አይደሉምን",
               "የኦንሊ_ጂሰሱ_አብ፣_ወልድና_መንፈስ_ቅዱስ"
               )
    markup.add("ትምህርተ ሥላሴና የአረማውያኑ",
               "የውሃ_ጥምቀት_በኢየሱስ_ክርስቶስ_ስም"
               )
    
    markup.add("⬅ Back to Main Menu")
    return markup


def Islamic_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("ቁርአን pdf",
               "the_quaran_the_bible")
    markup.add("Islamic Evangelism",
               "Islamic material 2")
    markup.add("ግጭት",
               "mehammed in the Bible")
    markup.add("Muslim Apologetics",
               "Muslim Apolemics")
    markup.add("⬅ Back to Main Menu")
    return markup