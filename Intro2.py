
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
    say("Hi Dan, How can I help you today?")


if __name__ == '__main__':
    main()
