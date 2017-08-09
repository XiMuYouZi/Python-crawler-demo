from wxpy import *

bot = Bot()
my_friend = bot.friends().search('海欣')[0]
my_friend.send('海欣，你好，我是机器人小冰')


