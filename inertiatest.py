import pyttsx3  # module used for speaking
import datetime    # module to display date and time
import speech_recognition as sr # module to recoganize voice
import wikipedia   # module for searching wikipedia
import webbrowser  # module for website opening and searching them
import os       # module to open apps 
import smtplib # module for sending email
import random  # module for random number genrator
import sys  # module for exiting the system
import cv2   # module for opening webcam
from englisttohindi.englisttohindi import EngtoHindi     # module for english to hindi translation
from requests import get   # module for 
import psutil  # module for cpu percentage and battery percentage
import pyautogui # module to take screenshot
import json # module for reading news
from urllib.request import urlopen
import time # module for stop listning
import wolframalpha # calculator and meaning



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


try:
    wolframalpha_app_id = 'GLXG6H-YAKG7Y9EAE'
except Exception:
    print("Some function will not work")
    speak("Some function will not work")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning boss")
        speak("Good Morning boss")

    elif hour >= 12 and hour < 18:
        print("Good Afternoon boss")
        speak("Good Afternoon boss")

    else:
        print("Good evening boss")
        speak("Good evening boss")

    speak("I am Inertia. present at your service")

def takeCommand():
    r=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening........")
            # speak("How can i help you")
            # speak("Listning")
            r.pause_threshold=1
            audio=r.listen(source)

        try:
            print("recognizing....")
            # speak("recognizing your query")
            query=r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Could'nt recoganise your voice, Speak again....")
            speak("Could not recoganise your voice")
            speak("Speak again")
            return "None"
        return query
    except Exception:
        print("Microphone not found")
        speak("Microphone not found")


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.google.com", 507)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at"+usage)
    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def screenshot():
    speak("What name should i give to it")
    name=takeCommand().lower()
    img=pyautogui.screenshot()
    speak("screenshot taken sucessfully")
    name=takeCommand().lower()
    img.save(f"C:\\Users\\shivam\\Pictures\\Screenshots\\{name}.png")

def game(comp, you):
    if comp == you:  # when you and computer choose same choices game returns None i.e DRAW
        return None
    elif comp == 'rock':
        if you == 'scissors':  # you choose secissors computer choosed rock function returns false i.e LOST
            return False
        elif you == 'paper':  # you choose paper computer choosed rock function returns false i.e WIN
            return True
    elif comp == 'paper':
        if you == 'rock':  # you choose secissors computer choosed paper function returns false i.e LOST
            return False
        elif you == 'scissors':  # you choose rock computer choosed paper function returns false i.e WIN
            return True
    elif comp == 'scissors':
        if you == 'paper':  # you choose rock computer choosed secissors function returns false i.e LOST
            return False
        elif you == 'rock':  # you choose paper computer choosed secissors function returns false i.e WIN
            return True



def TaskExecution():
    wishMe()
    
    while True:
        query=takeCommand().lower()

        '''logics for executing tasks based on query'''
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("Acording to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            speak("What should i search on YouTube, Boss")
            find=takeCommand().lower()
            speak("searching Youtube")
            webbrowser.open(f"{find}")

        elif 'open google' in query:
            speak("What should i search on google, Boss")
            find=takeCommand().lower()
            speak("searching Google")
            webbrowser.open(f"{find}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open whatsaap' in query:
            webbrowser.open("whatsaapweb.com")

        elif 'play music' in query:
            music_dir = 'D:\\SONGS'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(F"boss the time is {strTime}")
            print(F"boss the time is {strTime}")

        elif 'date' in query:
            year=datetime.datetime.now().year
            month=datetime.datetime.now().month
            date=datetime.datetime.now().day
            # day=datetime.datetime.now().day
            print(f"The current date is: {date}/{month}/{year}")
            speak("The current date is")
            speak(date)
            speak(month)
            speak(year)
        
        elif 'open vs code' in query:
            codePath="C:\\Users\\shivam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should i say")
                content= takeCommand()
                to = "shivampandey2716593@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!!")
            except Exception as e:
                print(e)
                speak("Sorry unable to send email")



        elif 'open autocad' in query:
            autocadPath="C:\\Program Files\\Autodesk\\AutoCAD 2018\\acad.exe"
            os.startfile(autocadPath)

        elif 'open telegram' in query:
            tgPath="C:\\Users\\shivam\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(tgPath)

        elif 'open opera' in query:
            operaPath="C:\\Users\\shivam\\AppData\\Local\\Programs\\Opera\\launcher.exe"
            os.startfile(operaPath)

        elif 'open filmora' in query:
            filmoraPath="C:\\Program Files (x86)\\Wondershare\\Wondershare Filmora (CPC)\\Wondershare Filmora9.exe"
            os.startfile(filmoraPath)

        elif 'open photoshop' in query:
            photoshopPath="C:\\Program Files (x86)\\Photoshop\\x64\\Photoshop.exe"
            os.startfile(photoshopPath)

        elif 'open chrome' in query:
            chromePath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif 'open pdf reader' in query:
            pdfreaderPath="C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(pdfreaderPath)

        elif 'open microsoft teams' in query:
            Path="C:\\Users\\shivam\\AppData\\Local\\Microsoft\\Teams\\Teams.exe"
            os.startfile(Path)

        elif 'who are you' in query:
            speak("I am an virtual assistant created by my master Saurabh Panday")
            speak("My name is inertia and i am here to help you")

        elif 'what is your name' in query:
            speak("My name is inertia and i am here to help you")

        elif 'how are you' in query:
            speak("I am fine sir tell me how can i help you")       

        elif 'who created you' in query:
            speak("I am created by Saurabh Panday")

        elif 'what is your job' in query:
            speak("I work for you")
            speak("My job is to help you and make your life easier")

        elif 'thankyou' in query:
            speak("It is my pleasure to help you")
            speak("If you want me to do something else let me know")

        elif 'your features' in query:
            speak("I can do anyting for you boss")
            speak("here are some of my features")           
            speak("i can search wikipedia for you")           
            speak("i can open your aaplications for you")
            speak("i can search queries for you")
            speak("If you are boared i can play a game for you")
            speak("I can solve your maths problems for you")
            speak("Tell me boss how can i help you")

        elif 'show me your code' in query:
            speak("I am not authorized to reveal my codes to anyone boss")

        elif 'calculate' in query:
            client=wolframalpha.Client(wolframalpha_app_id)
            index=query.lower().split().index('calculate')
            query=query.split()[index+1:]
            res=client.query(''.join(query))
            answer=next(res.results).text
            print("the answer is"+answer)
            speak("the answer is"+answer)


        elif 'what is' in query or 'who is' in query:
            client=wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)

            except StopIteration:
                print("No Results")



        elif 'make me laugh' in query:
            
            speak("Here is a joke for you")
            randno= random.randint(1,10)
            if randno==1:
                speak("I had a dream where an evil queen forced me to eat a gigantic marshmallow")
                speak("When I woke up, my pillow was gone")

            elif randno==2:
                speak(" What sits up a tree and goes aaaaaahhhh An owl with a speech impediment")

            elif randno==3:
                speak("Doctor: You're obese")
                speak("Patient: For that I definitely want a second opinion.") 
                speak("Doctor: You’re quite ugly, too.")

            elif randno==4:
                speak("Siri, why am I still single?") 
                speak("Siri activates front camera.")
        
            elif randno==5:
                speak("Dentist warns his patient")
                speak("This might be a bit painful.")
                speak("Patient said That is OK, I will handle its")
                speak("The dentist sigh and said For a while now I have been having an affair with your wife.")

            elif randno==6:
                speak("Patient said Oh Doctor, I’m starting to forget things.")
                speak("Doctor said Since when have you had this condition")
                speak("Patient said What condition")

            elif randno==7:
                speak("How can you tell your acne is really starting to get out of hand?")
                speak("The blind start reading your face")

            elif randno==8:
                speak("Where do we get virgin wool from")
                speak("Ugly sheep")

            elif randno==9:
                speak("What is invisible and smells of worms")
                speak("A bird’s fart.")

            elif randno==10:
                speak("It has four legs and it can fly, what is it")
                speak("Two birds.")
        
            
        elif 'exit' in query:
            speak("Exiting the command panel")
            speak("going offline")
            break
            


        elif 'translate' in query:
            speak("What should i translate boss")
            translate=takeCommand().lower()
            # creating a EngtoHindi() object 
            res = EngtoHindi(translate) 

            # displaying the translation 
            speak("Here is the translation of your querry")
            print(res.convert)
            speak(res.convert)

        elif 'write note' in query:
            speak("What should i write,boss?")
            notes = takeCommand()
            file = open('notes.txt','w')
            speak("sir should i include date and time?")
            ans=takeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("Note was taken successfully boss")
            else:
                file.write(notes)
                speak("Note was taken successfully boss")

        elif 'show notes' in query:
            speak("showing notes")
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("speaker asked to locate"+location)
            webbrowser.open_new_tab("https://www.google.com/maps/place/"+location)

        # elif 'open camera' in query:
        #     cam=cv2.VideoCapture(0)
        #     while True:
        #         ret, img=cam.read()
        #         cv2.imshow('webcam',img)
        #         k=cv2.waitKey(50)
        #         if k==27:
        #             break
        #     cam.release()
        #     cv2.destroyAllWindows()

        elif 'ip address' in query:
            ip=get('https://api.ipify.org').text
            print(f"Your IP address is\n{ip}")
            speak(f"Your IP address is{ip}")

        elif 'cpu' in query:
            cpu()
        
        elif 'screenshot' in query:
            screenshot()

        elif 'remember that' in query:
            speak("What should i remeber?")
            memory=takeCommand()
            speak("You asked me to remeber that"+memory)
            remeber=open('memory.txt','w')
            remeber.write(memory)
            remeber.close()

        elif 'do you remember anything' in query:
            remeber = open('memory.txt','r')
            speak("You asked me to remeber that"+remeber.read())

        elif 'thankyou' in query:
            speak("It is my pleasure to help you")

        elif 'news' in query:
            speak("How many headlies you wanna hear")
            n=int(takeCommand().lower())
            try:
                jsonObj=urlopen("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=35f8498746684954afcc7780fd86323c")
                data = json.load(jsonObj)
                i=1
                speak("Here are some top headines from bussiness section")
                print("=================TOP HEADLINES=================\n")
                for item in data['articles']:

                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i+=1
                    if i==n+1:
                        break

            except Exception as e:
                print(str(e))

        elif 'play game' in query:
            print(" \t\t\t\t\t\t**********************************************************\t\t\t")
            print(" \t\t\t\t\t\t\t WELCOME TO 'ROCK, PAPER OR SCISSORS' GAME")
            print(" \t\t\t\t\t\t**********************************************************\t\t\t\n")
            speak("WELCOME TO 'ROCK, PAPER OR SCISSORS' GAME")
            while True:

                # Creating a variable which chooses random number between 1 and 9 using random function
                randno = random.randint(1, 9)

                # If random number is between 1 and 3 computer choice will be 'r' i.e rock
                if randno >= 1 and randno <= 3:
                    comp = 'rock'

                # If random number is between 4 and 6 computer choice will be 'p' i.e paper
                elif randno >= 4 and randno <= 6:
                    comp = 'paper'

                # If random number is between 7 and 9  computer choice will be 's' i.e secisors
                elif randno >= 7 and randno <= 9:
                    comp = 'scissors'

                # Taking input from the user in the form of string
                print("Your Turn: Rock, Paper or Scissors?\n")
                print("Speak 'stop' to exit the game")
                speak("Please pick your choice")
                you = takeCommand().lower()
                print(" \t\t\t\t\t\t****************************************************\t\t\t")

                # Output player enters wrong keyword

                if 'stop' in you:
                    break
                
                elif you != 'rock' and you != 'paper' and you != 'scissors':
                    print(" \t\t\t\t\t\t****************************************************\t\t\t")
                    speak("Invalid choice.........")
                    print("Invalid choice.........")
                    print(" \t\t\t\t\t\t****************************************************\t\t\t\n")

                elif 'rock' or 'paper' or 'scissors' in you:
                    a=game(you,comp)
                    if a == None:
                        print(f"You choosed '{you}' and computer choosed '{comp}'")
                        speak(f"You choosed '{you}'")
                        speak(f" and computer choosed '{comp}'")
                        print(" \t\t\t\t\t\t****************************************************\t\t\t")
                        print("The game is drawn!!!!")
                        print(" \t\t\t\t\t\t****************************************************\t\t\t\n")
                        speak("The game is drawn!!!!")

                    # Output when player looses
                    elif a == False:
                        print(f"You choosed '{you}' and computer choosed '{comp}'")
                        speak(f"You choosed '{you}'")
                        speak(f" and computer choosed '{comp}'")
                        print(" \t\t\t\t\t\t****************************************************\t\t\t")
                        print("You Lost Please try again !!!!")
                        print(" \t\t\t\t\t\t****************************************************\t\t\t\n")
                        speak("You Lost Please try again !!!!")

                    # Output when player wins
                    elif a == True:
                        print(f"You choosed '{you}' and computer choosed '{comp}'")
                        speak(f"You choosed '{you}'")
                        speak(f" and computer choosed '{comp}'")
                        print(" \t\t\t\t\t\t****************************************************\t\t\t")
                        print("Congratulations!!!! You won..........")
                        print(" \t\t\t\t\t\t****************************************************\t\t\t\n")
                        speak("Congratulations!!!! You won..........")
        
        elif 'stop listning' in query:
            speak("For how many seconds you want me to stop listning to your commands?")
            ans = int(takeCommand())
            time.sleep(ans)
            print(ans)

        # elif 'temperature' in query:
        #     res = wolframalpha_app_id.query(query)
        #     speak(next(res.results).text)

        else:
            temp = query.replace(' ','+')
            g_url="https://www.google.com/search?q="
            res_g='Sorry your querry does not match any command in me but i searched your answer on internet here is the result'
            print(res_g)
            speak("Sorry your querry does not match any command in me")
            speak("but i searched your answer on internet")
            speak("here is the result")
            webbrowser.open(g_url+temp)

if __name__ == "__main__":
    print("Please speak your password")
    speak("Please speak your password")
    while True:
        try:
            permission = takeCommand().lower()
            if 'inertia' in permission:
                speak("varifying password")
                speak("password matched")
                print("password matched")
                speak("access granted")
                speak("activating inertia")
                speak("going online")
                TaskExecution()

            elif 'sleep' in permission:
                speak("Thanks for using me, sir have a nice day")
                speak("Activating sleep mode")
                speak("falling asleep")
                sys.exit()

            else:
                speak("incorect password")
                print("incorect password")
                speak("access denied")
                speak("Try again")
                print("Please speak your password")
                speak("Please speak your password")

        except Exception:
            speak("Please try again")
            print("Please try again")
