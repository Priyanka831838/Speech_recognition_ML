import speech_recognition as sr
import webbrowser as web

if __name__ == "__main__":
    path = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"  
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say a URL")
        audio = r.listen(source)
        print("Recognizing Now.....")

        try:
            dest = r.recognize_google(audio)
            print("You have said:", dest)
            web.get(path).open(dest)  
        except Exception as e:
            print("Error:", str(e))