import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
import datetime, random


logging.basicConfig(filename='bot2.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start.')
    update.message.reply_text('Положение какой планеты ты хочешь узнать на данный момент?\
         \n/Mercury \n/Venus \n/Earth \n/Mars \n/Jupiter \n/Saturn \n/Uranus \n/Neptune') 
    update.message.reply_text("Также ты можешь ввести в формате 'planet \"название планеты\"'\n\n"\
         + "Хочешь узнать ближайшее полнолуние? /next_full_moon\n\n" + "Посчитай количество слов в предложении /wordcount\n\n"\
             + "Поиграй в города /cities\n" + "Калькулятор /calc")      

# ----------------ПОИСК ПЛАНЕТЫ ПО НАЗВАНИЮ----------------------------------------------------
#----------------------------------------------------------------------------------------------

def planet_coor(update, context):
     
    if update.message.text == "/Mercury":
        date = datetime.date.today()
        coordinates_planet = ephem.Mars(f'{date}')
        constellation = ephem.constellation(coordinates_planet)
        update.message.reply_text(constellation)
        update.message.reply_text(coordinates_planet)
    elif update.message.text == "/Venus":
        date = datetime.date.today()
        coordinates_planet = ephem.Venus(f'{date}')
        constellation = ephem.constellation(coordinates_planet)
        update.message.reply_text(constellation)
        update.message.reply_text(coordinates_planet)
    elif update.message.text == "/Earth":
        date = datetime.date.today()
        coordinates_planet = ephem.Earth(f'{date}')
        constellation = ephem.constellation(coordinates_planet)
        update.message.reply_text(constellation)
        update.message.reply_text(coordinates_planet)
    elif update.message.text == "/Mars":
        date = datetime.date.today()
        coordinates_planet = ephem.Mars(f'{date}')
        constellation = ephem.constellation(coordinates_planet)
        update.message.reply_text(constellation)
        update.message.reply_text(coordinates_planet)    
    elif update.message.text == "/Jupiter":
        date = datetime.date.today()
        coordinates_planet = ephem.Jupiter(f'{date}')
        constellation = ephem.constellation(coordinates_planet)
        update.message.reply_text(constellation)
        update.message.reply_text(coordinates_planet)
    elif update.message.text == "/Saturn":
        date = datetime.date.today()
        coordinates_planet = ephem.Saturn(f'{date}')
        constellation = ephem.constellation(coordinates_planet)
        update.message.reply_text(constellation)
        update.message.reply_text(coordinates_planet)
    elif update.message.text == "/Uranus":
        date = datetime.date.today()
        coordinates_planet = ephem.Uranus(f'{date}')
        constellation = ephem.constellation(coordinates_planet)
        update.message.reply_text(constellation)
        update.message.reply_text(coordinates_planet)
    elif update.message.text == "/Neptune":
        date = datetime.date.today()
        coordinates_planet = ephem.Neptune(f'{date}')
        constellation = ephem.constellation(coordinates_planet)
        update.message.reply_text(constellation)
        update.message.reply_text(coordinates_planet)
    else:
        update.message.reply_text("Я не знаю такой планеты")

# ---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------




# -----------------------ПОДСЧЕТ СЛОВ----------------------------------------------------------
#----------------------------------------------------------------------------------------------

def word_count_func(update, context):
    word = update.message.text
    # if word.isdigit():
    #     update.message.reply_text("Цифры нельзя!")
    if ',' in word or '.' in word:
        word = word.replace(',', ' ')
        word = word.replace('.', ' ')
    word_list = word.split()
    word_count = len(word_list) - 1
    if word_count == 0:
        update.message.reply_text("Ты ничего не написал(")
    else:
        for i in word_list:
            if i.isdigit():
                word_count -= 1
            else:
                continue
        update.message.reply_text(f"Я насчитал {word_count} слов ")

# ---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

# ----------------ПОЛНОЛУНИЕ-------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

def next_full_moon_func(update, context):
    enter_date = update.message.text
    if len(enter_date) == 15:
        enter_date = datetime.date.today()
        next_full_moon = ephem.next_full_moon(enter_date)
        update.message.reply_text('Ближайшее полнолуние будет: ' + str(next_full_moon))
    else:
        enter_date = enter_date.split()
        enter_date = enter_date[-1]
        if '-' in enter_date or '.' in enter_date or ',' in enter_date or '\\' in enter_date :
            enter_date.replace('-', '/')
            enter_date.replace('.', '/')
            enter_date.replace(',', '/')
            enter_date.replace('\\', '/')
        next_full_moon = ephem.next_full_moon(enter_date)
        update.message.reply_text('Ближайшее полнолуние будет: ' + str(next_full_moon))

# ---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------








calc_onoff = 0
start_game_onoff = 0


# -----------------------------НАПРАВЛЯЮЩАЯ ФУНКЦИЯ----------------------------------------------------
#----------------------------------------------------------------------------------------------


def supervisor(update, context):
    global calc_onoff
    global start_game_onoff


# --------------------------КАЛЬКУЛЯТОР--------------------------------------------------------
#----------------------------------------------------------------------------------------------
    def calc_func(expression_user):
        global calc_onoff
        # expression_user = update.message.text


        if expression_user == '/calc':
            calc_onoff = 1
            update.message.reply_text("Ты включил калькулятор. Теперь можешь писать выражения. \
                Если захочешь выйти, набери 'Выход' или 'Exit'.")

        if (expression_user.lower() == "выход") or (expression_user.lower() == "exit") or (expression_user.lower() == "стоп"):
            update.message.reply_text("Пока")
            calc_onoff = 0
            
        elif expression_user != '/calc':
            expression_user = str(expression_user)
            expression_user = expression_user.replace(' ', '')
            check_symbol = 0
            number_of_symbol = len(expression_user)
            if calc_onoff == 1:
                if expression_user == "":
                    update.message.reply_text("Вы ничего не написали.")
                else:
                    for i in expression_user:
                        if i.isdigit() or (i == '+') or (i == '-') or (i == '/') or (i == '*') or (i == '(') or (i == ')'):
                            check_symbol += 1
                    if check_symbol == number_of_symbol:
                        try:
                            update.message.reply_text(str(eval(expression_user)))
                        except ZeroDivisionError:
                            update.message.reply_text('На ноль делить нельзя!')
                    else:
                        update.message.reply_text("В вводе есть недопустимые символы!")
            else:
                update.message.reply_text("Нажми /calc")
    

# ---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

# ----------------ИГРА В ГОРОДА----------------------------------------------------------------
#---------------------------------------------------------------------------------------------- 

    def game_cities_func(start_game_cities):
        global start_game_onoff
        global calc_onoff

        with open("cities_russia.txt", encoding='UTF-8') as cities_russia:
            global_cities_russia_list = cities_russia.readlines()
            count = 0
            for i in global_cities_russia_list:
                if i == "\n":
                    del global_cities_russia_list[count]
                count += 1

        bot_city_random = random.choice(global_cities_russia_list)

        calc_onoff = 0
        # start_game_cities = update.message.text
        start_game_cities = start_game_cities.lower()
        cities_russia_list = global_cities_russia_list

        if start_game_cities == "/cities":
            start_game_onoff = 1
            update.message.reply_text(f'Хорошо, давай сыграем с тобой в игру.\
    Если тебе надоест, набери "Стоп". Если я не смогу придумать слово, набери "След". \nЯ начинаю: {bot_city_random}')
        
        if start_game_cities.lower() == "стоп":
            update.message.reply_text("Пока")
            start_game_onoff = 0

        else:
            user_city = str(start_game_cities)
            bot_city = str(bot_city_random)
            newer_word_letter_bot = ""
            newer_word_letter_user = ""
            user_city_2_word = user_city.split()
            if user_city.lower() == "след":
                bot_city = random.choice(cities_russia_list) 
                update.message.reply_text(str(bot_city)) 
            if len(user_city_2_word) == 2:
                user_city = user_city_2_word[-1]
            if (user_city[-2] == "ы") or (user_city[-2] == "й") or (user_city[-2] == "ъ") or (user_city[-2] == "ь"):
                newer_word_letter_user = user_city[-3]
            if (bot_city[-2] == "ы") or (bot_city[-2] == "й") or (bot_city[-2] == "ъ") or (bot_city[-2] == "ь"):
                newer_word_letter_bot = bot_city[-3]
            if start_game_onoff == 1:
                if (user_city[0] == bot_city[-2]) or (user_city[0] == newer_word_letter_bot):
                    user_city = user_city.capitalize() + '\n'
                    if user_city in cities_russia_list:
                        for i in cities_russia_list:
                            if (i[0].lower() == user_city[-2]) or (i[0].lower() == newer_word_letter_user):
                                # update.message.reply_text("тест")
                                if (i[-2] == "ы") or (i[-2] == "й") or (i[-2] == "ъ") or (i[-2] == "ь"):
                                    continue
                                bot_city_random = i
                                update.message.reply_text(str(bot_city_random))
                                if user_city in cities_russia_list:
                                    cities_russia_list.remove(user_city)
                                if bot_city in cities_russia_list:
                                    cities_russia_list.remove(bot_city)
                                break
                    else:
                        update.message.reply_text("Не правильно. Попробуй еще раз.")
            else:
                update.message.reply_text("Нажми /cities")

# ---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
# ----------------ПОИСК ПЛАНЕТЫ ЧЕРЕЗ СТРОКУ---------------------------------------------------
#----------------------------------------------------------------------------------------------

    def name_planet(planet):
        #user_text = update.message.text
        # date = datetime.date.today()
        # date = str(date)
        # planet_attr = getattr(ephem, planet)
        # planet_now = planet_attr(date)
        # constel = ephem.constellation(planet_now)
        # update.message.reply_text(constel)


        planet = planet.split()
        if len(planet) < 3:
            planet = planet[-1] 
            # date = datetime.date.today()
            date = datetime.date.today()
            date = str(date)
            planet_attr = getattr(ephem, planet)
            planet_now = planet_attr(date)
            constel = ephem.constellation(planet_now)
            update.message.reply_text(constel)
            # if planet == "Mercury":
            #     date = datetime.date.today()
            #     coordinates_planet = ephem.Mercury(f'{date}')
            #     constellation = ephem.constellation(coordinates_planet)
            #     update.message.reply_text(constellation)
            #     update.message.reply_text(coordinates_planet)
            # elif planet == "Venus":
            #     date = datetime.date.today()
            #     coordinates_planet = ephem.Venus(f'{date}')
            #     constellation = ephem.constellation(coordinates_planet)
            #     update.message.reply_text(constellation)
            #     update.message.reply_text(coordinates_planet)
            # elif planet == "Earth":
            #     date = datetime.date.today()
            #     coordinates_planet = ephem.Earth(f'{date}')
            #     constellation = ephem.constellation(coordinates_planet)
            #     update.message.reply_text(constellation)
            #     update.message.reply_text(coordinates_planet)
            # elif planet == "Mars":
            #     date = datetime.date.today()
            #     coordinates_planet = ephem.Mars(f'{date}')
            #     constellation = ephem.constellation(coordinates_planet)
            #     update.message.reply_text(constellation)
            #     update.message.reply_text(coordinates_planet)    
            # elif planet == "Jupiter":
            #     date = datetime.date.today()
            #     coordinates_planet = ephem.Jupiter(f'{date}')
            #     constellation = ephem.constellation(coordinates_planet)
            #     update.message.reply_text(constellation)
            #     update.message.reply_text(coordinates_planet)
            # elif planet == "Saturn":
            #     date = datetime.date.today()
            #     coordinates_planet = ephem.Saturn(f'{date}')
            #     constellation = ephem.constellation(coordinates_planet)
            #     update.message.reply_text(constellation)
            #     update.message.reply_text(coordinates_planet)
            # elif planet == "Uranus":
            #     date = datetime.date.today()
            #     coordinates_planet = ephem.Uranus(f'{date}')
            #     constellation = ephem.constellation(coordinates_planet)
            #     update.message.reply_text(constellation)
            #     update.message.reply_text(coordinates_planet)
            # elif planet == "Neptune":
            #     date = datetime.date.today()
            #     coordinates_planet = ephem.Neptune(f'{date}')
            #     constellation = ephem.constellation(coordinates_planet)
            #     update.message.reply_text(constellation)
            #     update.message.reply_text(coordinates_planet)
            # else:
            #     update.message.reply_text("Я не знаю такой планеты")
            

        else:
            print("Необходимо ввести в формате 'planet \"название планеты\"'")
            update.message.reply_text("Необходимо ввести в формате 'planet \"название планеты\"'")

# ---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
    user_text = update.message.text
    user_text = str(user_text)
    planet = user_text.split()
    if (user_text == '/calc') or (calc_onoff == 1):
        calc_func(user_text)
    elif (user_text == '/cities') or (start_game_onoff == 1):
        game_cities_func(user_text)
    elif planet[0] == '/planet':
        name_planet(user_text)
    


# ---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", word_count_func))
    dp.add_handler(CommandHandler("Mercury", planet_coor))
    dp.add_handler(CommandHandler("Venus", planet_coor))
    dp.add_handler(CommandHandler("Earth", planet_coor))
    dp.add_handler(CommandHandler("Mars", planet_coor))
    dp.add_handler(CommandHandler("Jupiter", planet_coor))
    dp.add_handler(CommandHandler("Saturn", planet_coor))
    dp.add_handler(CommandHandler("Uranus", planet_coor))
    dp.add_handler(CommandHandler("Neptune", planet_coor))
    dp.add_handler(CommandHandler('planet', supervisor))
    dp.add_handler(CommandHandler('next_full_moon', next_full_moon_func))
    # dp.add_handler(CommandHandler('cities', game_cities_func))
    # dp.add_handler(CommandHandler('calc', calc_func))
    dp.add_handler(CommandHandler('cities', supervisor))
    dp.add_handler(CommandHandler('calc', supervisor))

    dp.add_handler(MessageHandler(Filters.text, supervisor))
    #dp.add_handler(MessageHandler(Filters.text, name_planet))
    

    logging.info("Бот стартовал")
 
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()