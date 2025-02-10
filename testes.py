import os
import requests
def send_simple_message():
  	return requests.post(
  		"https://api.mailgun.net/v3/sandbox1ce19323d1fa4c62bb4282e44d334269.mailgun.org/messages",
  		auth=("api", "af5d23a3d835ae8f3f60a8157f9c8962-1654a412-56055b24"),
  		data={"from": "Mailgun Sandbox <postmaster@sandbox1ce19323d1fa4c62bb4282e44d334269.mailgun.org>",
			"to": "Vinicius deAndrade Piovezan <vinicius.piovezan07@gmail.com>",
  			"subject": "Hello Vinicius deAndrade Piovezan",
  			"text": "Congratulations Vinicius deAndrade Piovezan, you just sent an email with Mailgun! You are truly awesome!"})
   
x = send_simple_message()

print(x.text)
print(x.status_code)