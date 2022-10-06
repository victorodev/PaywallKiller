import telebot 
import os

api_tel = os.getenv("teleapi")
bot = telebot.TeleBot(api_tel)

@bot.message_handler(commands=["start"])
def iniciar (mensagem):
  bot.reply_to(mensagem, text= "Hello, i can remove any paywall, you just need to use the command /remove with the link i will help you!\n\nExample:\n\n/remove <your link here>")

#def verify(mensagem):
  #return True

#@bot.message_handler(func=verify)
@bot.message_handler(commands=["remove"])
def removepaywall(mensagem):
  msg = mensagem.text
  msg = msg.replace("/remove ", "")
  nopayw = "https://12ft.io/" + msg
  response = f"Here's your link, hope you enjoy it! \n\n{nopayw}"
  bot.reply_to(mensagem, response )

bot.polling()
