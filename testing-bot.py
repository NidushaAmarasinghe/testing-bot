"""
MIT License
Copyright (c) 2021 Nidusha Amarasinghe
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from cgitb import text
import telebot, requests, json
from telebot import types
from os import getenv

bot = telebot.TeleBot(getenv("BOT_TOKEN"))


# Markup
mark1 = telebot.types.InlineKeyboardMarkup()
mark1.add(telebot.types.InlineKeyboardButton(text='🔁Updates🔁', url='https://t.me/SlapTap'),
          telebot.types.InlineKeyboardButton(text='🧑‍💻Support🧑‍💻', url='https://t.me/SlapTaps')),
mark1.add(telebot.types.InlineKeyboardButton(text='🛠️Socure🛠️', url='https://github.com/NidushaAmarasinghe')),

mark2 = telebot.types.InlineKeyboardMarkup()
mark2.add(telebot.types.InlineKeyboardButton(text='🛠️Socure🛠️', url='https://github.com/NidushaAmarasinghe'),
          

# Commands
@bot.message_handler(commands=['start'])
def send_start(message):
   bot.send_message(message.chat.id, text="💕Hi There! 😁Welcome To Nidusha Official Bot😘\nJoin @SlapTap",parse_mode='Markdown', reply_markup=mark1)

@bot.message_handler(commands=["bots"])
def send_covid(message):
    bot.send_message(message.chat.id, text="Go To @Nidusha_Bot")

@bot.message_handler(commands=["gcovid"])
def send_gcovid(message):
    bot.send_message(message.chat.id, gcovidinfo)

@bot.message_handler(commands=["help"])
def send_help(message):
    bot.send_message(message.chat.id, text=help, reply_markup=mark2) 

@bot.message_handler(commands=["about"])
def send_about(message):
    bot.send_message(message.chat.id, """
• Bot Deverloper-{@NidushaAmarasinghe}
• This Is Nidusha Official Bot
                                      """, parse_mode='Markdown')

# Callback Data
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id)
    if call.data == '1':
        answer = covidinfo
    bot.send_message(call.message.chat.id, answer)           

# Inline Mode             
@bot.inline_handler(lambda query: query.query == 'bots')
def query_text(inline_query):
        in1 = types.InlineQueryResultArticle('1', "My Bots", types.InputTextMessageContent(Click Here To Get Bot List /bots))
        
        bot.answer_inline_query(inline_query.id, [in1])
    
bot.polling()
