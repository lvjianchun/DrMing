import os
import sys
#from src import textToVoice, voiceToText, wit_query_agent
from src import textToVoice, voiceToText, diagnostic
from src.wit_query_agent import wit_query_agent


while True:
	try:
		text = voiceToText.GetInputVoiceToText()
		agent = wit_query_agent()
		response = agent.send(text)
		#look up
		res= diagnostic.GetDiagnosticResult(response)
		textToVoice.TextToSpeech(res)
	except Exception as e:
		print(e)
