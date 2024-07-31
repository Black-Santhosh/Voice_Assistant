import pyttsx3
import webbrowser
import random
import speech_recognition as sr
import wikipedia
import wolframalpha
import os
import sys
import pywhatkit


engine = pyttsx3.init() # object creation

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 130)     # setting up new voice rate
client = wolframalpha.Client('XRGT2L-WJ89LX2HHJ')


voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voices', voices[0].id)  #changing index, changes voices. o for male (or) 1 for female
def speak(audio):
    print('J.A.C.K : ' + audio)
    engine.say(audio)
    engine.runAndWait()
    engine.stop()
    
speak('I am your assistant JACK,How may I help you?')

while True:
    def myCommand():
    
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:                                                                       
            print("Listening...")
            r.pause_threshold =  1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            r.pause_threshold =  0.5

        try:
            command = r.recognize_google(audio).lower()
            print('User: ' + command + '\n')
            
        except sr.UnknownValueError:
            speak('Sorry TRY Writing your command Sir')
            command = str(input('Command: '))
        return command
        #youtube
    def run_assistant():
        command = myCommand()

        if 'jack' in command:
                speak('tell me santhosh');        

        elif "play" in command:
            song = command.replace("play ","")
            pywhatkit.playonyt(song)

        elif 'open whatsapp' in command:
                speak('okay')
                webbrowser.open('https://web.whatsapp.com/')  

        elif 'open google' in command:
                speak('okay')
                webbrowser.open('www.google.co.in')  

        elif 'wish to mam' in command:
                speak(' Respected teachers staffs I feel so blessed to have a teachers like you who not only pushes me towards achieving my goal but also supports me in every step. Today I celebrate you for being selfless, devoted, hardworking, and the wisest person in the classroom. I am grateful to be your student. Happy Teachers Day')
        elif 'hai' in command:
                speak('hi sir')
        elif 'how are you' in command:
                speak('i am fine sir . how may i help you sir')   
        elif 'kalam vision' in command:
                speak('To create the inspired student community to exercise their ardent potentials to elevate India to a Super Power, a Leader of the World.  To break the barrier of frog-in-well mind set / attitude in the rural students to draw him to the global platform for achievement')                                 

        elif 'vaigai college of engineering' in command:
                speak('To create the inspired student community to exercise their ardent potentials to elevate India to a Super Power, a Leader of the World.  To break the barrier of frog-in-well mind set / attitude in the rural students to draw him to the global platform for achievement')                                 


        elif 'music' in command:
                song = command.replace("music ",'')
                music_folder = 'E:\\music\\'
                random_music = music_folder+song+'.mp3'
                speak('Okay, here is your music! Enjoy!')
                os.startfile(random_music) 

        elif 'play movie' in command or 'play video' in command:
                music_folder = 'E:\\movie\\'
                music = ['1']
                random_music = music_folder + random.choice(music) +'.mp4'
                speak('Okay, here is your movie! Enjoy!')
                os.system(random_music) 

        elif 'nothing' in command or 'abort' in command or 'stop' in command or 'bye' in command:
                speak('okay')
                speak('Bye santhosh, have a good day.')
                sys.exit() 
                
        else:
                command = command
                speak('Searching...')
                try:
                    try:
                        res = client.command(command)
                        results = next(res.results).text
                        speak('google says - ')
                        speak('Got it.')
                        speak(results)
                        
                    except:
                        results = wikipedia.summary(command, sentences=4)
                        speak('Got it.')
                        speak(results)
                        webbrowser.open('www.google.com')
                except:
                    
            
                    speak('any Command! Sir!')
                      
    run_assistant()