import random
import telebot
from config import token
import requests
import os
print(os.listdir('img'))
    
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot('7657061527:AAHU97O-Cr8kZEVNatwkNMwr_CeoFN0SQoU')
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    with open('img/mem_1.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']

@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['mems'])
def send_mems(message):
    img_name = random.choice(os.listdir('img'))
    with open(f'img/{img_name}', 'rb') as f:  
            bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['animals'])
def send_animals_mems(message):
     img_animals = random.choice(os.listdir('img_animals'))
     with open(f'img_animals/{img_animals}', 'rb') as f:  
            bot.send_photo(message.chat.id, f)  

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    


bot.polling()