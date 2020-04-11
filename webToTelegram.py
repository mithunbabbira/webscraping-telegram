import telebot
import time
import requests
import bs4


res = requests.get('https://www.worldometers.info/coronavirus/country/india/')
print(res)
n=[]
soup = bs4.BeautifulSoup(res.text, 'lxml')





for i in soup.select('.maincounter-number'):
	n.append(i.text)
print(n[2])




bot_token ='1228157522:AAECEHSq1ImwdM5-vvW5vyKqwJp3Ax60W4E'

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['creator'])
def send_welcome(message):
	bot.reply_to(message,"MITHUN BABBIRA")

@bot.message_handler(commands=['recovered'])
def send_welcome(message):
	bot.reply_to(message,n[2]+"lucky bastards")


@bot.message_handler(commands=['death'])
def send_welcome(message):
	bot.reply_to(message,"just "+n[1]+"AND lot more to go")


@bot.message_handler(commands=['positive'])
def send_welcome(message):
	bot.reply_to(message,n[0]+"yet to die ")

bot.polling()	