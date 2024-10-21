import speech_recognition as sr
from ai_speaker.ai_speech import speak_as_ai
from flags.signal_flags import *


recognizer = sr.Recognizer()

def listenUserInput():
     with sr.Microphone() as source:
          try:
               recognizer.adjust_for_ambient_noise(source, duration=1)
               recognizer.energy_threshold = 3000
               print("Speak something...")
               audio = recognizer.listen(source)
               user_input_text = recognizer.recognize_google(audio)
               if "exit" in user_input_text or "quit" in user_input_text or "terminate" in user_input_text:
                    print("Exiting...")
                    speak_as_ai("Exit The Porgram, See you again Insha Allah")
                    IS_RUNNING = False
                    return
               speak_as_ai(user_input_text)

          except:
               speak_as_ai("I don't get it, Please say it again")


while IS_RUNNING:
     listenUserInput()