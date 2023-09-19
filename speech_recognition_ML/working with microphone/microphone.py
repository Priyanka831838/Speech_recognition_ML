import speech_recognition as sr
import pyttsx3
word = sr.Recognizer()
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
with sr.Microphone() as source2:
    print("Silence please, calibrating background noise")
    word.adjust_for_ambient_noise(source2, duration=2)
    print("Now Speak")
    
    audio2 = word.listen(source2)
    MyText = word.recognize_google(audio2)
    MyText = MyText.lower()
    
    print("Did you say --> "+MyText)
    SpeakText(MyText)