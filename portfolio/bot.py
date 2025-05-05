# import requests
# from environs import Env

# env = Env()
# env.read_env()  # shu yerda .env fayl avtomatik o'qiladi



# def  send_message(text):
#   BOT_TOKEN = env.str("BOT_TOKEN")
#   CHAT_ID = env.str("CHAT_ID")
#   PHOTO = "https://alvarotrigo.com/blog/assets/imgs/2021-10-16/dvlpr-front-end-portfolio-example.jpeg"
#   TEXT = text
#   url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendphoto?chat_id={CHAT_ID}&photo={PHOTO}&caption={TEXT}"
#   response = requests.get(url)