import speech_recognition as sr
from ai_speaker.ai_speech import speak_as_ai
from flags.signal_flags import *
from qa_actions.questions_answer import predict_question_from_model
from ui.ui_tk import *
speak_as_ai()

recognizer = sr.Recognizer()

def listenUserInput():
     global IS_RUNNING
     with sr.Microphone() as source:
          try:
               recognizer.adjust_for_ambient_noise(source, duration=1)
               recognizer.energy_threshold = 5000
               print("Ai is Listening.....")
               audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
               print()
               user_input_text = recognizer.recognize_google(audio)
               print("You said: " + user_input_text)
               print()
               if "exit" in user_input_text or "quit" in user_input_text or "terminate" in user_input_text:
                    print("Exiting...")
                    speak_as_ai("Exit The Porgram, See you again Insha Allah")
                    IS_RUNNING = False
                    return
               predict_question_from_model(user_input_text,ai_speaker=speak_as_ai)

          except sr.UnknownValueError:
               speak_as_ai("I don't get it, Please say it again")
          except sr.WaitTimeoutError:
               speak_as_ai("I can't hear you, Please try again")


while IS_RUNNING:
     listenUserInput()
    

     