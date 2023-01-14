import speech_recognition as sr
import time
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


GPIO.setup(7,GPIO.OUT)
servo=GPIO.PWM(7,50)
servo.start(0)

# create a Recognizer instance
r = sr.Recognizer()

# set the language to use for speech recognition
# this should be a language code from the list at:
# https://cloud.google.com/speech-to-text/docs/languages
LANGUAGE = 'it-IT'  # Italian

# create a microphone instance
mic , speech = sr.Microphone() , []

while True:
    #time.sleep(0.1)
    # listen for speech from the microphone and recognize it
    with mic as source:
        audio = r.listen(source)

    # try to recognize the speech
    try:
        text = r.recognize_google(audio, language=LANGUAGE, show_all=True)
        print(f"You said: {text}")
       
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("Error while making request:", e)

    #print('\n\ntext :',text['alternative'][0]['transcript'])
    if "Apri" in text['alternative'][0]['transcript']:
        print("Apri")
        servo.ChangeDutyCycle(7)
        time.sleep(0.2)
        servo.ChangeDutyCycle(4)

    elif "Chiudi" in text['alternative'][0]['transcript']:
        print("Chiudi")
        servo.ChangeDutyCycle(7)
        time.sleep(0.2)
        servo.ChangeDutyCycle(9)


