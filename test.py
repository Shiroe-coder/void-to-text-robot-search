from selenium import webdriver
from time import sleep
from tkinter import*
import os
from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(ChromeDriverManager().install())
from googlesearch import search
import requests
import urllib
from bs4 import BeautifulSoup

def google_scrape(url):
    thepage = urllib.request.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text
def seacrh(te):
    i = 1
    query = te
    for url in search(query, stop=1):
        a = google_scrape(url)
        i += 1
    return a
import speech_recognition
import pyttsx3
import wikipedia
wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()

robot_ear = speech_recognition.Recognizer()
#robot_say = pyttsx3.init()
robot = "i'm Listening"
while True:
	me = ''
	with speech_recognition.Microphone() as mic:
		print("robot: " + robot)
		robot_ear.adjust_for_ambient_noise(mic, duration=1)
		try:
			audio = robot_ear.listen(mic, timeout=4)
		except:
			audio = ""
			robot = "i can't hear you, try again"
	print(audio)
	try:
		me = robot_ear.recognize_google(audio ,language="vi")
	except:
		me == ''
	print("you: " + me)
	if me =='':
		robot = "i can't hear you, try again"
	elif "hello" in me:
		robot = 'hello, i am robot, can i help you ?'
	elif "bye" in me:
		robot = 'goodbye'
		print("robot: " + robot)
		#robot_say.say(robot)
		#robot_say.runAndWait()
		break
	else:
		robot = seacrh(me)
	
	print("robot: " + robot)
	#robot_say.say(robot)
	#robot_say.runAndWait()
