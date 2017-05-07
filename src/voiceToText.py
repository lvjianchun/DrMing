def GetInputVoiceToText(default):
    import speech_recognition as sr
    #from .textToVoice import TextToSpeech


    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    BING_KEY = "fbd3d5eb1eaf443485cb3e568a132b86"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
    try:
        text = r.recognize_bing(audio, key=BING_KEY)
        print("Microsoft Bing Voice Recognition thinks you said " + text)
        return text
    except sr.UnknownValueError as e:
        if default:
            return default
        raise e
    except sr.RequestError as e:
        if default:
            return default
        print("[ERROR] Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
        raise e

if __name__ == '__main__':
    s = GetInputVoiceToText()
