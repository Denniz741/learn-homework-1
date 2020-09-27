"""
            Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.
"""
import logging
import ephem
from telegram.ext import Updater , CommandHandler , MessageHandler ,\
     Filters


import settings
logging.basicConfig(filename = 'bot.log' , level = logging.DEBUG)

PROXY = {'proxy_url' : settings.PROXY_URL , 
    'urllib3_proxy_kwargs' : {'username' : settings.PROXY_USERNAME ,
     'password' : settings.PROXY_PASSWORD}}

planets = {
    'Mars': ephem.Mars('2020/09/22'),
    'Venus': ephem.Venus('2020/09/22'),
    'Mercury': ephem.Mercury('2020/09/22'),
    'Uranus' : ephem.Uranus('2020/09/22'),
    'Jupiter': ephem.Jupiter('2020/09/22'),
    'Neptune': ephem.Neptune("2019/09/22"),
    'Saturn': ephem.Saturn('2020/09/22'),
    'Pluto': ephem.Pluto('2020/09/22')
    
     }

def talk_to_me(update,context):
    pass
    
              
def greet_user(update,context):
    print("Вызван /старт")
    update.message.reply_text('Здравствуй пользователь')

def return_locat(update,context):
    print('вызвана команда /planet')
    user_text = str(update.message.text.split()[1].lower().\
        capitalize())
    print(user_text)
    update.message.reply_text(ephem.constellation(planets.get(user_text)))
    


def main():
    mybot = Updater(settings.API_KEY, 
    use_context=True , request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', return_locat))
    dp.add_handler(MessageHandler(Filters.text , talk_to_me))
    
    logging.info(' Бот стартонул')
    
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
     main()


