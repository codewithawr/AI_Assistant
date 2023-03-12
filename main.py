from audio_handel import audio
from ai_connect import davinci_AI

instraction = audio()
ai_return = davinci_AI()

while True:
    instraction.recode_mic(listen_for=3)
    print(instraction.return_str())
    print(ai_return.Request_davinci(instraction.return_str()))

    if input('x: to stop, c: continue: ').upper() == 'X':
        break


