#before using, search "python instabot" on google, take line and insert to CMD

from instabot import Bot
bot = Bot
bot.login(usename = "shubug70",password = "2003Explorer")


#Upload a photo to instagram
#bot.upload_photo("",caption="") #insert file path to photo and optional caption

#follow a user

bot.follow("") #insert username of person to follow, no @

#Send a DM

bot.send_message("Hello Friend",['','']) #send messages to users, list creates a group message

#pull a list of someones followers
followers = bot.get_user_followers("") #insert account to ping


