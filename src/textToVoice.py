import os
import sys

def textToVoice(s):
	os.system("say " + s)

if __name__ == '__main__':
	textToVoice("Hello World")
