import telebot
import requests
r = requests.session()
bot = telebot.TeleBot("7009525779:AAEQV7qCzUgjrVSvtTV21OIYR0JqLeLFdEA")
@bot.message_handler(commands=["get"])
def get(message):
	try:
		info = message.text.replace("/get", "")
		splitting = info.split(":")
		username = splitting[0]
		password = splitting[1]
		if username[0] == " ":
			username = username[1:100]
		print(username+ "\n" + password)
		login_url = "https://www.instagram.com/accounts/login/ajax/"
		login_headers = {
	        "accept": "*/*",
	        "accept-encoding": "gzip, deflate,br",
	        "accept-language": "ar,en-US;q=0.9,en;q=0.8",
	        "content-length": "279",
	        "content-type": "application/x-www-form-urlencoded",
	        "origin": "https://www.instagram.com",
	        "referer": "https://www.instagram.com/",
	        "sec-fetch-dest": "empty",
	        "sec-fetch-site": "same-origin",
	        "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
	        "x-csrftoken": "lih2ypMfhzdqwMbm5jIILqxZDj4zLeCW",
	        "x-ig-app-id": "936619743392459",
	        "x-ig-www-claim": "hmac.AR1_p9SjMFQF73bcZgzygDgxb9yBZUn83e69xoDD2qpSdmtW",
	        "x-instagram-ajax": "901e37113a69",
	        "x-requested-with": "XMLHttpRequest"
	    }
		login_data = {"username": username, "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:" + password, "queryParams": "{}",
	            "optIntoOneTap": "false"}
		log = r.post(login_url, headers=login_headers, data=login_data)
		if ('"authenticated":true') in log.text:
			bot.send_message(message.chat.id, text= log.cookies.get_dict()["sessionid"])
		elif ('"authenticated":false') in log.text:
			print(log.text)
			bot.send_message(message.chat.id, text= "wrong password or username")
		elif ('"message":"checkpoint_required"') in log.text:
			bot.send_message(message.chat.id, text="Secure")
		elif('"error_type":"ip_block"') in log.text:
			bot.send_message(message.chat.id, text= "ip blocked")
		elif ('"message":"Please wait a few minutes before you try again."') in log.text:
			bot.send_message(message.chat.id, text= "You've been blocked wait a few minutes before you tru again")
		else:
			bot.send_message(message.chat.id, text= log.text)
	except:
		pass
bot.polling(True)