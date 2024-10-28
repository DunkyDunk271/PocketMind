from infi.systray import SysTrayIcon
from openai import OpenAI
import openai
import os

def say_hello(systray):
    print("Hello, World!")
menu_options = (("Say Hello", None, say_hello),)
systray = SysTrayIcon("icon.ico", "Example tray icon", menu_options)
systray.start()

#Promp for API key input if none is found
api_file = "api_key.txt"

if not os.path.exists(api_file):
    api_key = input("Please enter your OpenAI API key: ")
    api_file = open("api_key.txt", "w")
    api_file.write(api_key)
    api_file.close()
else:
    api_file = open("api_key.txt", "r")
    api_key = api_file.read()
    api_file.close()

client = OpenAI(api_key=api_key)


stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
