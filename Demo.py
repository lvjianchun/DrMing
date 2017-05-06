import os
import sys
#from src import textToVoice, voiceToText, wit_query_agent
from src import textToVoice, voiceToText
from src.wit_query_agent import wit_query_agent


while True:
	try:
		text = voiceToText.GetInputVoiceToText()
		agent = wit_query_agent()
		agent.send(text)
		#look up
		res = "please drink more water"
		textToVoice.TextToSpeech(res)
	except Exception as e:
		print(e)
	
