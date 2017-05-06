import os
import sys
#from src import textToVoice, voiceToText, wit_query_agent
from src import textToVoice, voiceToText

while True:
	try:
		text = voiceToText.GetInputVoiceToText()
		print(text)
		textToVoice.textToVoice(text)
	except Exception as e:
		print(e)
	
