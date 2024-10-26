import pyttsx3 as speaker 

DEFAUL_TEXT ="Hello! I'm an AI assistant for computer-related questions. What would you like to ask?"
def speak_as_ai(text=DEFAUL_TEXT, rate=190,volume =1.0,voice=1):
    print("Ai is Speaking...")
    engine = speaker.init()
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)  
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice].id)     
    engine.say(text)
    engine.runAndWait()
    engine.stop()




