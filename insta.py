from instabot import  Bot
bot = Bot()
bot.login(username = 'apne account ka name(kiran)',password = "password do login wala")
bot.follow('cpmaurya')# jisko follow krna h uska username

#  upload photo automatic in your profile
bot.upload_photo("image ka path", caption="I Love python")

# unfollow the person
bot.unfollow("cpmaurya")

# send message multiple person at a time
bot.send_message("hello",['cpmaurya','vimal','anushka'])

# follower list ko dekhna
followers = bot.get_user_followers("kiran")
for follower in followers:
    print(bot.get_user_info(follower))

#following ki list lena
followings = bot.get_user_following("kiran")
for following in followings:
    print(bot.get_user_info(follower))




