from audio_handel import audio
from ai_connect import GPT_AI

instraction = audio()
ai_return = GPT_AI()

while True:
    instraction.recode_mic()
    print(instraction.return_str())
    print(ai_return.GPT_Request(instraction.return_str()))

    if input('x: to stop, c: continue.: ').upper() == 'X':
        break


