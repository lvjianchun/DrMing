import os
import sys
import time
from src import textToVoice, voiceToText, loadBinaryTree
from src.wit_query_agent import query_agent, response_parser
import speech_recognition as sr
#from test.decision_tree import knowledge_base


wit = query_agent.QueryAgent()
knowledgebase = loadBinaryTree.load()


def say(text):
	#os.system("say '%s' --voice Samantha" % text)
	textToVoice.TextToSpeech(text)

def get_user_voice_input(default=None):
	print("[DEBUG] try talking now")
	text = voiceToText.GetInputVoiceToText(default)
	print("[DEBUG] User said %s " % text)
	return text

def main():
	while True:
		try:
			say("Hi, I'm Doctor Ming. How are you today?")
			text = get_user_voice_input()
			text = "I am wheezing. What's wrong with me"

			#say("We are pretending you said %s" % text)
			response = wit.send(text)
			parser = response_parser.responseParser(response)
			if parser.has("intent"):
				intent, conf = parser.get("intent")
				if intent == 'descOfSymptom' and conf > 0.75:
					say("Let me see how can I help")
					symptom, conf = parser.get("symptom")
					root = loadBinaryTree.get_by_symptom(symptom)
					process_decision_tree(root)
					say("Hope you have a good day! See ya")
					break
			else:
				say("I cross checked with my good friends, Alexa and Siri, but we all don't understand. Let's try again")
				continue
		except sr.UnknownValueError as unknown_error:
			say("Sorry, I did not hear anything from you.")
			say("Let's start over again")
			continue
		except Exception as e:
			print(e)
			say("Something went wrong. Bye!")
			break


def process_decision_tree(root):
	say("How old are you?")
	age = get_user_voice_input("43")

	mini_wit = query_agent.QueryAgent("R3XLCEB34LG3HE3ISBF46QWBAJFW6E4F")
	while loadBinaryTree.IsLeafNode(root) is False:
		question_to_ask = loadBinaryTree.get_question(root)
		say("%s" % question_to_ask)
		print("[DEBUG] asked (%s)" % question_to_ask)
		is_acceptable_answer = False
		while not is_acceptable_answer:
			try:
				res = get_user_voice_input()
				if res:
					# small hack to narrow error
					response = mini_wit.send(res)
					p = response_parser.responseParser(response)
					res = 'yes' if p.has("positive") else res
					res = 'no' if p.has("negative") else res

					is_acceptable_answer = True if res in ['yes', 'no'] else None
				if not is_acceptable_answer:
					say("Let's try it again")
					say(question_to_ask)

			except sr.UnknownValueError:
				say("Sorry, I did not hear anything from you. Let's try again.")
				continue
			except sr.RequestError:
				say("Sorry, I don't understand you. Let's try again.")
				continue


		root = root.Yes if is_acceptable_answer and 'yes' in res else root.No

	say("Please stick out your tongue.")
	time.sleep(3)
	say("Okay")
	say("Let me check your pulse pattern.")
	time.sleep(2)

	say("Dr. Ming suggested you to %s" % loadBinaryTree.get_question(root))

if __name__ =='__main__' :
	main()
