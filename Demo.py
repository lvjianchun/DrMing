import os
import sys
from src import textToVoice, voiceToText, loadBinaryTree
from src.wit_query_agent import query_agent, response_parser
from test.decision_tree import knowledge_base

wit = query_agent.QueryAgent()
knowledgebase = loadBinaryTree.load()


def say(text):
	#os.system("say '%s' --voice Samantha" % text)
	textToVoice.TextToSpeech(text)

def getUserVoiceInput():
	return voiceToText.GetInputVoiceToText()

def main():
	while True:
		try:
			say("Hello! How are you today?")
			text = getUserVoiceInput()
			if not text:
				say("Let's start over again")
				continue
			#text = "I am wheezing. Help me"
			#say("We are pretending you said %s" % text)
			response = wit.send(text)
			parser = response_parser.responseParser(response)
			if parser.has("intent"):
				intent, conf = parser.get("intent")
				if intent == 'descOfSymptom' and conf > 0.75:
					#root = knowledge_base.get_decision_tree()#(parser.get("symptom"))
					root = loadBinaryTree.get_by_symptom("wheezing")
					process_decision_tree(root)
					say("Hope you have a good day! See ya")
					break
			else:
				say("I cross checked with Alexa and Siri, but we all don't understand. Let's try again")
				continue

			# say(res)
		except Exception as e:
			print(e)
			say("Something went wrong. Bye!")
			break


def process_decision_tree(root):
	mini_wit = query_agent.QueryAgent("R3XLCEB34LG3HE3ISBF46QWBAJFW6E4F")
	#while root.is_terminated is False:
	while loadBinaryTree.IsLeafNode(root) is False:
		#question_to_ask = root.question
		question_to_ask = loadBinaryTree.get_question(root)
		print("[DEBUG] ask (%s)" % question_to_ask)
		say("Please answer after Beeeep... %s" % question_to_ask)
		is_acceptable_answer = False
		while not is_acceptable_answer:
			res = getUserVoiceInput()
			if res:
				# small hack to narrow error
				print("[DEBUG]User said: %s" % res)
				response = mini_wit.send(res)
				p = response_parser.responseParser(response)
				res = 'yes' if p.has("positive") else res
				res = 'no' if p.has("negative") else res

				is_acceptable_answer = True if res in ['yes', 'no'] else None
			if not is_acceptable_answer:
				say("Let's try it again")
				say("Please answer after Beeeep... %s" % question_to_ask)

		root = root.Yes if is_acceptable_answer and 'yes' in res else root.No

	say("Dr. Ming suggested you to %s" % loadBinaryTree.get_question(root))

if __name__ =='__main__' :
	main()
