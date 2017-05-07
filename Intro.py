
from src import textToVoice, voiceToText
import time

def say(text):
    textToVoice.TextToSpeech(text)

def get_user_voice_input(default=None):
    print("[DEBUG] try talking now")
    text = voiceToText.GetInputVoiceToText(default)
    print("[DEBUG] User said %s " % text)
    return text

def main():
    while True:
        try:
            text = get_user_voice_input()
            if 'doctor' in text or 'ming' in text:
                say("Hi Dan")
                time.sleep(0.5)
                say("How can I help you today?")
                break
            else:
                print("[DEBUG] nothing")
                continue
        except Exception:
            continue


if __name__ == '__main__':
    main()