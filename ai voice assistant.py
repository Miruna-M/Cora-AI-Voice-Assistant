# Recognise Speech
import speech-recognition as recognizer 
from gtts import gTTS
import random
import os
import pyttsx3
import bs4 as bs
import urllib.request

# Open Browser
import webbrowser 
import time

# Get Time Details
from time import ctime 

# Screenshot
import pyautogui 

# Play An Audio File
import playsound 
import winshell
import dirCleanUp
from pygame import mixer
import pyjokes

class ai:
    name = ''
    def Name(self, name):
        self.name = name

class user:
    name = ''
    def Name(self, name):
        self.name = name

def chatbot(text):
    text = str(text)
    chat.say(text)
    chat.runAndWait()

def userSpeech(terms):
    for a in terms:
        if a in userVoice:
            return True

# Initialise Recogniser
b = recognizer.Recognizer() 

# Listen For Audio & Convert It To Text
def micRecord(ask=""):

    # Record With Microphone
    with recognizer.Microphone() as record: 
        if ask:
            chatbot(ask)
        b.pause_threshold = 1
        b.adjust_for_ambient_noise(record, duration=1)

        # Listen For Audio Via Record
        userAudio = b.listen(record, 5, 5)  
        print("Done Listening")
        userVoice = ''
        try:

            # Convert Audio To Text
            userVoice = b.recognize_google(userAudio)  
        except recognizer.RequestError:

            # Error: Service Not Available
            chatbot('Sorry, this service is unavailable.') 
        except recognizer.UnknownValueError: 

            # Error: userVoice Unclear
            chatbot('Sorry, can you repeat that?') 
            # Print What User Says      
        print(">>", userVoice.lower()) 
        return userVoice.lower()

# Get String & Make An Audio File
def chatbot(aiVoice):
    aiVoice = str(aiVoice)
    b = random.randint(1,20000000)

    # Text To Speech
    c = gTTS(text=aiVoice, lang='en')     
    recording = 'userAudio' + str(r) + '.mp3'

    # Save As mp3
    c.save(recording) 

    # Play Audio File
    playsound.playsound(recording) 
    print(aiSpeech.name + ":", aiVoice)

    # Remove Audio File
    os.remove(recording) 

    # Name
    if userSpeech(["what is your name","what's your name","tell me your name"]):
        if User.name:

            # Get User's Name
            chatbot(f"My name is {aiSpeech.name}, {User.name}") 
        else:

            # If User's Name Is Not Provided
            chatbot(f"My name is {aiSpeech.name}. What's your name?") 

    if userSpeech(["my name is"]):
        userName = userVoice.split("is")[-1].strip()
        chatbot("Nice to meet you " + userName)

        # Remember userName
        User.Name(userName) 

    # Greeting
    if userSpeech(["how are you","how are you doing"]):
        chatbot("I'm very well, thanks for asking " + User.name)

    # Search Youtube
    if userSpeech(["youtube"]):
        search = userVoice.split("for")[-1]
        search = search.replace("on youtube","").replace("search","")
        url = "https://www.youtube.com/results?search_query=" + search
        webbrowser.get().open(url)
        chatbot("Here is what I found for " + search + "on youtube.")

    # Search Google
    if userSpeech(["search for"]) and 'youtube' not in userVoice:
        search = userVoice.split("for")[-1]
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        chatbot("Here is what I found for" + search + "on google.")

    # Search Weather
    if userSpeech(["weather"]):
        search = userVoice.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        chatbot("Here is what I found for weather on google.")

    # Search Location On Google Maps
    if userSpeech(["where am I", "what is my location"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        chatbot("According to google maps, this is your location.")

    # Search Definition On Wikipedia
    if userSpeech(["definition of"]):
        definition=micRecord("what do you need the definition of")
        url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                chatbot('Im sorry, i could not find that definition, please try a web search')
            elif definitions[1]:
                chatbot('Here is what i found '+definitions[1])
            else:
                chatbot ('Here is what i found '+definitions[2])
        else:
                chatbot("Im sorry i could not find the definition for "+definition + "Please try a web search")

    # Time
    if userSpeech(["what's the time","tell me the time","what time is it","what is the time"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        chatbot(time)

     # Calculator
    if userSpeech(["plus","minus","multiply","divide","power","+","-","*","/"]):
        calculator = userVoice.split()[1]

        if calculator == 'power':
            chatbot(int(userVoice.split()[0]) ** int(userVoice.split()[2]))
        elif calculator == 'multiply' or 'x':
            chatbot(int(userVoice.split()[0]) * int(userVoice.split()[2]))
        elif calculator == 'divide':
            chatbot(int(userVoice.split()[0]) / int(userVoice.split()[2]))
        if calculator == '+':
            chatbot(int(userVoice.split()[0]) + int(userVoice.split()[2]))
        elif calculator == '-':
            chatbot(int(userVoice.split()[0]) - int(userVoice.split()[2]))        
        else:
            chatbot("Sorry, can you repeat that")

    # Screenshot
    if userSpeech(["capture","my screen","screenshot"]):
        screenshot = pyautogui.screenshot()
        screenshot.save('D:/screenshot/screen.png')

    # Play Music From PC
    if userSpeech(["play music", "play song"]):
        chatbot("Now playing...")

        # Access Music Folder
        music = "C:\\Users\\Tiffany\\Downloads\\Music\\music" 
        songs = os.listdir(music)
        print(songs)
        playmusic(music + "\\" + songs[0])

    # Stop Music From PC
    if userSpeech(["stop music"]):
        chatbot("Stopping music.")
        stopmusic()

    # Empty Recycle Bin
    if userSpeech(["empty recycle bin"]):
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        chatbot("Recycle bin emptied")

    # Clean Up Directory
    if userSpeech(["clean up directory"]):
        chatbot("Please provide directory path.")
        directory = input()
        if os.path.exists(directory):
            dirCleanUp.clear_dir(directory)
            chatbot('Directory is organized.')

    # Play Rock Paper Scissors
    if userSpeech(["game"]):
        userVoice = micRecord("Rock Paper or Scissors")
        moves=["rock", "paper", "scissors"]
        userMove=random.choice(moves)
        aiMove=userVoice
        chatbot("The computer chose " + userMove)
        chatbot("You chose " + aiMove)
        if aiMove==userMove:
            chatbot("It's a tie")
        elif aiMove== "rock" and userMove== "scissors":
            chatbot("You win")
        elif aiMove== "paper" and userMove== "rock":
            chatbot("You win")
        elif aiMove== "scissors" and userMove== "paper":
            chatbot("You win")
        elif aiMove== "rock" and userMove== "paper":
            chatbot("I win")
        elif aiMove== "paper" and userMove== "scissors":
            chatbot("I win")
        elif aiMove== "scissors" and userMove== "rock":
            chatbot("I win")

    # Coin Toss
    if userSpeech(["toss","flip","coin"]):
        moves=["head", "tails"]   
        userMove=random.choice(moves)
        chatbot("I chose " + userMove)

    # Tell A Joke
    if userSpeech(["tell me joke", "give me a funny story", "make me laugh"]):
        chatbot(pyjokes.get_joke())

    # Exit Program
    if userSpeech(["exit", "quit", "goodbye"]):
        chatbot("Goodbye. See you next time!")
        exit()

# Play Music    
def playmusic(song):
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()

# Stop Music
def stopmusic():
    mixer.music.stop()

time.sleep(1)

chat = pyttsx3.init()
User = user()
User.name = ""
aiSpeech = ai()
aiSpeech.name = 'Cora'

while(1):
    userVoice = record_audio("Recording") # get the voice input
    print("Done")
    print("You said:", userVoice)








    

    
    

    

    
    
    
     

    
   

    
        
    
    
    
    


    
    
   
      



