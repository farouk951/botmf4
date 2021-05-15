import telebot
from telebot import types
from datetime import datetime
import requests
now = datetime.now()

sudo = 906630665 
sudo1 = 1535915537
token ="1827666209:AAHSEHVIC4r7Bno9c-5Dk7OH9ChYn-po8jc"
bot = telebot.TeleBot("1827666209:AAHSEHVIC4r7Bno9c-5Dk7OH9ChYn-po8jc")
@bot.message_handler(commands = ['start'])
def start(message):
	url = f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@CardinG0Only&user_id={message.chat.id}"
	r = requests.get(url).text
	if ("kicked")in r:
		bot.reply_to(message,text="*Join @CardinG0Only And Press { /start }*",parse_mode="markdown")
	elif ("left")in r:
		bot.reply_to(message,text="*Join @CardinG0Only And Press { /start }*",parse_mode="markdown")
	elif ("kicked")in r:
		bot.reply_to(message,text="*Join @CardinG0Only And Press { /start }*",parse_mode="markdown")
	else :
		if message.chat.id == sudo or sudo1:
		      bot.send_message(sudo or sudo1,text=f"*Hey @{message.from_user.username} \nYou i'll Recieve All messages ✅*",parse_mode="markdown")
		else:
			bot.send_message(message.chat.id,text="""𝐇𝐢 (: 🤍
	
	Send Message :""")
	ti = now.strftime("%D  %H:%M:%S")
@bot.message_handler(commands=["id"])
def id (message):
	bot.send_message(message.chat.id,text=f"* 🆔 : *`{message.chat.id}`",parse_mode="markdown")
@bot.message_handler(commands=["reply"])
def reply(message):
	if message.chat.id == sudo or sudo1:
		try :
			ms = message.text.replace("/reply ","")
			m = ms.split(":")
			bot.send_message(m[0],text=f"*Hey 👋\n\nNew Message  📩 : *`{m[1]}`*\n\nFrom : @{message.from_user.username} ✅*",parse_mode="markdown")
			bot.reply_to(message,text=f"*Done Send ✅\nTo 👤 : {m[0]} *\nMessage 📩 : {m[1]} ",parse_mode="markdown")
		except:
			bot.send_message(message.chat.id,text="*Please Send Valid Form*",parse_mode="markdown")
	else:
		bot.send_message(message.chat.id,text="*⚠️ Command For Only Admins ⚠️*",parse_mode="markdown")
@bot.message_handler(commands=['check'])
def ch(message):
	if message.chat.id == sudo or sudo1:
		if message.text == "":
			bot.reply_to(message,"*Please Send Valid ID*",parse_mode="markdown")
		else:
			b = message.text.replace("/check ","")
			if message.chat.id == sudo:
				bot.reply_to(message,text=f"ID To Check 🆔 {b}\nLink 🔗 : tg://openmessage?user_id={b}")
			else:
				bot.send_message(message.chat.id,text="*⚠️ Command For Only Admins ⚠️*",parse_mode="markdown")
@bot.message_handler(content_types=['text', 'document', 'audio', 'photo'])
def msg(message):
		url = f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@CardinG0Only&user_id={message.chat.id}"
		r = requests.get(url).text
		if ("kicked")in r:
			bot.reply_to(message,text="*Join @CardinG0Only And Press { /start }*",parse_mode="markdown")
			return
		elif ("left")in r:
			bot.reply_to(message,text="*Join @CardinG0Only And Press { /start }*",parse_mode="markdown")
			return
		elif ("kicked")in r:
			bot.reply_to(message,text="*Join @CardinG0Only And Press { /start }*",parse_mode="markdown")
			return
		else :
			if message.chat.id == sudo:
			      bot.send_message(sudo,text=f"*Hey @{message.from_user.username} \n You i'll Recieve All messages ✅*",parse_mode="markdown")
		ti = now.strftime("%D  %H:%M:%S")
		bot.reply_to(message,"𝐃𝐞𝐥𝐢𝐯𝐞𝐫𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 𝐅𝐨𝐫 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞. 💕"+"\nAt : "+ ti)
		bot.send_message(sudo,text=f"*Hey ✅\nNew Message 🌹 :   *`{message.text}`*    \nFrom @{message.from_user.username} 🔃\nAt {ti} ⏳ *\nID Sender 🆔 : `{message.chat.id}` ",parse_mode="markdown")
bot.polling()
