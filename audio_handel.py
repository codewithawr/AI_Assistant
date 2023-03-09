import speech_recognition as sr
from datetime import datetime as dt

class audio:

    def __init__(self):
        self.r = sr.Recognizer()

    def recode_mic(self, listen_till = None):
        '''This def Record audio from the microphone until gavin time by "listen_till" '''
        with sr.Microphone() as source:
            print(dt.now())
            print("Say something!")
            self.audio = self.r.listen(source, timeout=listen_till)
            print(dt.now())


    def return_str(self):
        '''This def Recognize recorded speech using Google Speech Recognition'''
        try:
            return self.r.recognize_google(self.audio)
        except sr.UnknownValueError:
            raise Exception("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            raise Exception("Could not request results from Google Speech Recognition service; {0}".format(e))


if __name__ == "__main__":
    x = audio()
    x.recode_mic(3)
    print(x.return_str())