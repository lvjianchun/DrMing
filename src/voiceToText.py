import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

BING_KEY = "fbd3d5eb1eaf443485cb3e568a132b86"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    text = r.recognize_bing(audio, key=BING_KEY)
    print("Microsoft Bing Voice Recognition thinks you said " + text)
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
