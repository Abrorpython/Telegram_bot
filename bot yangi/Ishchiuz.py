from telegram import *
from telegram.ext import *
from evosbaza import *
baza=ish()
menu_til=[
    [KeyboardButton("O'zbek tili"),KeyboardButton("Русский язик")]
]
menu_manzil = [
            [
                KeyboardButton("Andijon viloyati"),
                KeyboardButton("Buxoro viloyati")
            ],
            [
                KeyboardButton("Farg'ona viloyati"),
                KeyboardButton("Jizzax viloyati")
            ],
            [
                KeyboardButton("Xorazm viloyti"),
                KeyboardButton("Namangan viloyati")
            ],
            [
                KeyboardButton("Navoiy viloyati"),
                KeyboardButton("Qashqadaryo viloyati")
            ],
            [
                KeyboardButton("Qoraqalpog'iston Respublikasi"),
                KeyboardButton("Samarqand viloyati")
            ],
            [
                KeyboardButton("Sirdaryo viloyati"),
                KeyboardButton("Surxondaryo viloyati")
            ],
            [
                KeyboardButton("Toshkent viloyati"),
                KeyboardButton("Toshkent shahar")
            ],
            [KeyboardButton("⬅️Ortga")]

        ]
button_name=[
    [KeyboardButton("👆Ismingizni yozing👆")],
    [KeyboardButton("⬅️Ortga")]
]
button_familya=[
    [KeyboardButton("👆Familyangizni yozing👆")],
    [KeyboardButton("⬅️Ortga")]
]
button_yosh=[
    [KeyboardButton("👆Yoshingizni kiriting👆")],
    [KeyboardButton("⬅️Ortga")]
]
button_jins=[
    [KeyboardButton("Ayol"),KeyboardButton("Erkak")],
    [KeyboardButton("⬅️Ortga")]
]
button_oila=[
    [KeyboardButton("Turmushga chiqqan"),KeyboardButton("Turmushga chiqmagan")],
    [KeyboardButton("Uylangan"),KeyboardButton("Uylanmagan")],
    [KeyboardButton("⬅️Ortga")]
]

muassasa=[
    [KeyboardButton("👆Qaysi Oliy ta'lim\n Qaysi o'rta ta'limni bitirgansiz yozing👆")],
    [[KeyboardButton("⬅️Ortga")]]
]
mutaxasis=[
    [KeyboardButton("👆Mutaxasislingizni kiriting👆")],
    [KeyboardButton("⬅️Ortga")]
]
hayoq=[
    [KeyboardButton("Ha"),KeyboardButton("Yo'q")],
    [KeyboardButton("⬅️Ortga")]
]
button_telegram=[
    [KeyboardButton("👆Telegram nomingizni kiriting👆")],
    [KeyboardButton("⬅️Ortga")]
]
button_malumot=[
    [KeyboardButton("Magistr"),KeyboardButton("Oliy")],
    [KeyboardButton("Tugallanmagan oliy"),KeyboardButton("O'rta mahsus")],
    [KeyboardButton("⬅️Ortga")]
]
button_malaka=[
        [KeyboardButton("👆Ish malakangizni yozing(raqam)👆")],
        [KeyboardButton("⬅️Ortga")]
]
button_nomer=[
        [KeyboardButton("👆Telefon nomeringizni yozing👆")],
    [KeyboardButton("⬅️Ortga")]
]
butto_info=[
    [KeyboardButton("👆<b>O'zingiz haqingizda qisqagina ma'lumot yozing</b>👆")],
    [KeyboardButton("⬅️Ortga")]
]
def start(update,context):
    update.message.reply_html(f"<b>👇Tilni tanlang👇</b>",reply_markup=ReplyKeyboardMarkup(menu_til,resize_keyboard=True))
    return language
def language(update,context):
    global language2
    language2=update.message.text
    language3=["O'zbek tili","Русский язик"]
    if language2 not in language3:
        update.message.reply_html(f"<b>🆘Xatolik🆘\nBunday til mavjud emas\n👇Tilni tanlang👇</b>")
        return language
    elif language2=="O'zbek tili":
        update.message.reply_html(f"<b>👇Yashash hududingizni tanlang👇</b>",reply_markup=ReplyKeyboardMarkup(menu_manzil,resize_keyboard=True))
        return name
    elif language2=="Русский язик":
        update.message.reply_html(f"<b>👇Где вы живу👇</b>")
        #davomi bor...



def name(update,context):
    global name1
    name1=update.message.text
    list = ["Andijon viloyati", "Buxoro viloyati", "Farg'ona viloyati", "Jizzax viloyati", "Xorazm viloyti",
            "Namangan viloyati", "Navoiy viloyati", "Qashqadaryo viloyati", "Qoraqalpog'iston Respublikasi",
            "Samarqand viloyati", "Sirdaryo viloyati", "Surxondaryo viloyati", "Toshkent viloyati", "Toshkent shahar"]
    if name1 not in list:
        update.message.reply_html(f"<b>Xatolik\nBunday viloyat mavjud emas\n👇Yashash hududingizni tanlang👇</b>")
        return name
    else:
        update.message.reply_html(f"<b>👇Ismingizni kiriting👇</b>",reply_markup=ReplyKeyboardMarkup(button_name,resize_keyboard=True))
        return familya
def familya(update,context):
    global name2
    name2=update.message.text
    if name2=="👆Ismingizni yozing👆":
        update.message.reply_html("<b>🆘Xatolik🆘\n👇Ismingizni kiriting👇</b>")
        return familya
    elif name2=="⬅️Ortga":
        return start(update,context)
    else:
        update.message.reply_html("<b>👇Familyangizni kiriting👇</b>",reply_markup=ReplyKeyboardMarkup(button_familya,resize_keyboard=True))
        return yosh
def yosh(update,context):
    global familya1
    familya1=update.message.text
    if familya1=="👆Familyangizni yozing👆":
        update.message.reply_html("<b>🆘Xatolik🆘\n👇Familyangizni kiriting👇</b>")
        return yosh
    elif familya1=="⬅️Ortga":
        return start(update,context)
    else:
        update.message.reply_html("👇Yoshingizni kiriting👇",reply_markup=ReplyKeyboardMarkup(button_yosh,resize_keyboard=True))
        return jins
def jins(update,context):
    global yosh1
    yosh1=update.message.text
    if yosh1=="👆Yoshingizni kiriting👆":
        update.message.reply_html("<b>🆘Xatolik🆘\n👇Yoshingizni kiriting👇</b>")
        return jins
    elif yosh1=="⬅️Ortga":
        return start(update,context)
    else:
        update.message.reply_html("👇Jinsingizni tanlang👇",reply_markup=ReplyKeyboardMarkup(button_jins,resize_keyboard=True))
        return oila
def oila(update,context):
    list = ["Ayol", "Erkak"]
    global jins1
    jins1=update.message.text
    if jins1 not in list:
        update.message.reply_html("<b>🆘Xatolik🆘\n👇Jinsingizni tanlang👇</b>")
        return oila
    elif jins1=="⬅️Ortga":
        return start(update,context)
    elif jins1=="Erkak":
        update.message.reply_html("👇Oilaviy ahvolingiz👇",reply_markup=ReplyKeyboardMarkup(button_oila,resize_keyboard=True))
        return hudud
    elif jins1=="Ayol":
        update.message.reply_html("👇Oilaviy ahvolingiz👇",reply_markup=ReplyKeyboardMarkup(button_oila,resize_keyboard=True))
        return hudud
def hudud(update,context):
    list = ["Turmushga chiqqan", "Turmushga chiqmagan", "Uylangan", "Uylanmagan"]
    global info
    info=update.message.text
    if info=="⬅️Ortga":
        return start(update,context)
    elif info in list:
        update.message.reply_html("👇Qaysi viloyatda ishlamoqchisiz👇",reply_markup=ReplyKeyboardMarkup(menu_manzil,resize_keyboard=True))
        return work_regions
    else:
        update.message.reply_html("<b>🆘Xatolik🆘\n👇Oilaviy sharoitingizni tanlang👇</b>")
        return hudud
def work_regions(update,context):
    global hudud2
    hudud2=update.message.text
    list = ["Andijon viloyati", "Buxoro viloyati", "Farg'ona viloyati", "Jizzax viloyati", "Xorazm viloyti",
            "Namangan viloyati", "Navoiy viloyati", "Qashqadaryo viloyati", "Qoraqalpog'iston Respublikasi",
            "Samarqand viloyati", "Sirdaryo viloyati", "Surxondaryo viloyati", "Toshkent viloyati", "Toshkent shahar"]
    if hudud2=="⬅️Ortga":
        return start(update,context)
    elif hudud2 not in list:
        update.message.reply_html("<b>🆘Xatolik🆘\n👇Qaysi viloyatda ishlamoqchisiz tanlang👇</b>")
        return work_regions
    else:
        update.message.reply_html("Ma'lumotingiz",reply_markup=ReplyKeyboardMarkup(button_malumot,resize_keyboard=True))
        return malumot
def malumot(update,context):
    global malumot1
    malumot1=update.message.text
    list=["Magistr","Oliy","Tugallanmagan oliy","O'rta mahsus"]
    if malumot1 not in list:
        update.message.reply_html("<b>🆘Xatolik🆘\n👇Ma'lumotingiz haqida quyidagilardan birini tanlang👇</b>")
        return malumot(update,context)
    elif malumot1=="⬅️Ortga":
        return start(update,context)
    else:
        update.message.reply_html("<b>👇Bitirgan muassasangizni kiriting👇</b>",reply_markup=ReplyKeyboardMarkup(muassasa,resize_keyboard=True))
        return talim(update,context)
def talim(update,context):
    global talim2
    talim2=update.message.text
    if talim2=="<b>👇Bitirgan muassasangizni kiriting👇</b>":
        update.message.reply_html("<b>🆘Xatolik🆘\n👇Bitirgan muassasangizni yozing👇</b>")
        return talim(update,context)
    elif talim2=="⬅️Ortga":
        return start(update,context)
    else:
        update.message.reply_html("<b>👇Mutaxasisligingizni kiriting👇</b>",reply_markup=ReplyKeyboardMarkup(mutaxasis,resize_keyboard=True))
        return ayol_nomer
def ayol_nomer(update,context):
    global mutaxsis2
    mutaxsis2=update.message.text
    if mutaxsis2=="<b>👇Mutaxasisligingizni kiriting👇</b>":
        update.message.reply_html("<b>🆘Xatolik🆘\n👇Mutaxasisligingizni yozing👇</b>")
        return ayol_nomer
    elif mutaxsis2=="⬅️Ortga":
        return start(update,context)
    else:
        update.message.reply_html("👇<b>Ish malakangizni yozing(raqam)</b>👇",reply_markup=ReplyKeyboardMarkup(button_malaka,resize_keyboard=True))
        return malaka
def malaka(update,context):
    global malaka1
    malaka1=update.message.text
    if malaka1=="👆Ish malakangizni yozing(raqam)👆":
        update.message.reply_html("<b>🆘Xatolik🆘\n👇Ish malakangizni yozing(raqam bilan)👇</b>")
        return malaka
    elif malaka1=="⬅️Ortga":
        return start(update,context)
    else:
        update.message.reply_html("👇<b>Telegram nomingizni kiriting(username)</b>👇",reply_markup=ReplyKeyboardMarkup(button_telegram, resize_keyboard=True))
        return username
def username(update,context):
    global user,username1
    user = update.message.from_user
    username1=update.message.text

    update.message.reply_html("👇<b>Telefon nomeringizni qo'shasizmi</b>👇",reply_markup=ReplyKeyboardMarkup(hayoq,resize_keyboard=True))
    return nomer
def nomer(update,context):
    list=["Ha","Yo'q"]
    global nomer1
    nomer1=update.message.text
    if nomer1=="⬅️Ortga":
        return start(update,context)
    if nomer1 not in list:
        update.message.reply_html("<b>🆘Xatolik🆘\n👇Telefon raqamingizni qo'shasizmi👇</b>")
        return nomer
    elif nomer1=="Yo'q":
        update.message.reply_html("Rasmingizni yuborasizmi",reply_markup=ReplyKeyboardMarkup(hayoq,resize_keyboard=True))
        return rasm
    elif nomer1=="Ha":
        update.message.reply_html("👇<b>Telefon nomeringizni yozing</b>👇",reply_markup=ReplyKeyboardMarkup(button_nomer,resize_keyboard=True))
        return tel_nomer
def tel_nomer(update,context):
    global tel_raqam
    tel_raqam=update.message.text
    if tel_raqam=="👆Telefon nomeringizni yozing👆":
        update.message.reply_html("<b>🆘Xatolik🆘\n👇Telefon nomeringizni yozing👇</b>")
        return tel_nomer
    else:
        update.message.reply_html("Rasmingizni yuborasizmi",reply_markup=ReplyKeyboardMarkup(hayoq, resize_keyboard=True))
        return rasm
def rasm(update,context):
    list=["Ha","Yo'q"]
    global rasm1
    rasm1=update.message.text
    if rasm1=="⬅️Ortga":
        return start(update,context)
    if rasm1 not in list:
        update.message.reply_html("<b>🆘Xatolik🆘\n👇Ha/Yo'q👇</b>")
        return rasm
    if rasm1=="Ha":
        update.message.reply_html("👇<b>Rasmingizni yuboring</b>👇")
        return rasm2
    elif rasm1=="Yo'q":
        update.message.reply_html("👇✍️<b>O'zingiz haqingizda qisqagina ma'lumot yozing</b>👇",reply_markup=ReplyKeyboardMarkup(butto_info,resize_keyboard=True))
        return summainfo
def summainfo(update,context):
    global info1
    info1=update.message.text
    if info1=="👆<b>O'zingiz haqingizda qisqagina ma'lumot yozing</b>👆":
        update.message.reply_html("<b>🆘Xatolik🆘\n👇✍️O'zingiz haqingizda qisqagina ma'lumot ✍️👇</b>")
        return summainfo
    elif info1=="⬅️Ortga":
        return start(update,context)
    else:
        update.message.reply_html(f"""
        Hodim: {name2},{familya1}
        Yoshi: {yosh1}
        🏘 Yashash manizli: {name1}
        🎓 Ma'lumoti: {malumot1}
        🏛 Tamomlagan: {talim2}
        💻 Mutaxsisligi: {mutaxasis2}
        📰 Ish malakasi: {malaka1}-yil
        ✈️Ishlay oladi: {hudud2}
        📞 Bog'lanish: {tel_raqam}
        ☎ Bog'lanish2: {user.first_name}
        👉 INFO:{info1}
        
        #{hudud} #abror.uz
        #{username1} #ishchi.uz
        
         🛄 Biz sizga yordam beramiz abror.uz
        
        """)
        update.message.reply_html("Ushbu ma'lumotlar admimga yuborildi\nTez orada kanalda e'loningiz ko'rinadi")
        context.bot.send_message(chat_id=1329386793, text=f"""
        Hodim: {name2},{familya1}
        Yoshi: {yosh1}
        🏘 Yashash manizli: {name1}
        🎓 Ma'lumoti: {malumot1}
        🏛 Tamomlagan: {talim2}
        ‍💻 Mutaxsisligi: {mutaxasis2}
        📰 Ish malakasi: {malaka1}-yil
        ✈️Ishlay oladi: {hudud2}
        📞 Bog'lanish: {tel_raqam}
        ☎ Bog'lanish2: {username1}
        👉 INFO:{ayol_info1}
        
        #{hudud} #abror.uz
        #{username1} #ishchi.uz
        
         🛄 Biz sizga yordam beramiz abror.uz
        """)
        return rahmat
def rasm2(update,context):
    user = update.message.from_user
    foto = update.message.photo[-1]
    context.bot.send_photo(user.id, foto, caption=f"""
    Hodim: {name2},{familya1}
        Yoshi: {yosh1}
        🏘 Yashash manizli: {name1}
        🎓 Ma'lumoti: {malumot1}
        🏛 Tamomlagan: {talim2}
        👩‍💻 Mutaxsisligi: {mutaxasis2}
        📰 Ish malakasi: {malaka1}-yil
        ✈️Ishlay oladi: {hudud2}
        📞 Bog'lanish: {tel_raqam}
        ☎ Bog'lanish2: {username1}
        👉 INFO:{info1}
         
        #{hudud} #abror.uz
        #{username1} #ishchi.uz
        
         🛄 Biz sizga yordam beramiz abror.uz
        """)
    update.message.reply_html("Ushbu ma'lumotlar admimga yuborildi\nTez orada kanalda e'loningiz ko'rinadi")
    context.bot.send_photo(chat_id=1329386793, photo=foto, caption=f"""
    Hodim: {name2},{familya1}
        Yoshi: {yosh1}
        🏘 Yashash manizli: {name1}
        🎓 Ma'lumoti: {malumot1}
        🏛 Tamomlagan: {talim2}
        ‍💻 Mutaxsisligi: {mutaxasis2}
        📰 Ish malakasi: {malaka1}-yil
        ✈️Ishlay oladi: {hudud2}
        📞 Bog'lanish: {tel_raqam}
        ☎ Bog'lanish2: {username1}
        👉 INFO:{info1}
         
        #{hudud} #abror.uz
        #{username1} #ishchi.uz
        
         🛄 Biz sizga yordam beramiz abror.uz
        """)
    return rahmat
def rahmat(update,context):
    update.message.reply_html("Biz bilan qoling!!!!")
def main():
    updater=Updater("1659860921:AAHGadCnp3GKGrXZZiqRmANwzsRmnf60zBk",use_context=True)
    dispatcher=updater.dispatcher
    buyruq=ConversationHandler(
        entry_points=[
            CommandHandler("start",start)
        ],
        states={
            language:[MessageHandler(Filters.text,language)],
            name:[MessageHandler(Filters.text,name)],
            familya:[MessageHandler(Filters.text,familya)],
            yosh:[MessageHandler(Filters.text,yosh)],
            jins:[MessageHandler(Filters.text,jins)],
            oila:[MessageHandler(Filters.text,oila)],
            hudud:[MessageHandler(Filters.text,hudud)],
            work_regions:[MessageHandler(Filters.text,work_regions)],
            malumot:[MessageHandler(Filters.text,malumot)],
            talim:[MessageHandler(Filters.text,talim)],
            ayol_nomer:[MessageHandler(Filters.text,ayol_nomer)],
            malaka:[MessageHandler(Filters.text,malaka)],
            username:[MessageHandler(Filters.text,username)],
            nomer:[MessageHandler(Filters.text,nomer)],
            tel_nomer:[MessageHandler(Filters.text,tel_nomer)],
            rasm:[MessageHandler(Filters.text,rasm)],
            summainfo:[MessageHandler(Filters.text,summainfo)],
            rasm2:[MessageHandler(Filters.text,rasm2)],
            rahmat:[Mes  sageHandler(Filters.text,rahmat)]

        },
        fallbacks=[
            CommandHandler("start",start)
        ]
    )
    dispatcher.add_handler(buyruq)
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
# context.bot.send_message(chat_id=123456789, text="""
#
#
#
#             """)