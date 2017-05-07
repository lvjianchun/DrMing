#/usr/bin/python

import os
import sys
from collections import defaultdict

class Node:
	def __init__(self, ID):
		self.ID = ID
		self.Yes = None
		self.No = None

Keywork2Tree = defaultdict()
ID2NodeDict = defaultdict()
ID2Description = defaultdict()

def CreateNodeIfNot(ID):
	if ID not in ID2NodeDict:
		n = Node(ID)
		ID2NodeDict[ID] = n
	return ID2NodeDict[ID]

def loadBinaryTree(decision_file):
	with open(decision_file) as f:
		for line in f:
			sp = line.strip().split('\t')
			if len(sp) != 3:
				continue
			ID = sp[0]
			prediction = sp[1]
			child = sp[2]
			if prediction == "Tree":
				Keywork2Tree[ID] = CreateNodeIfNot(child)
			elif prediction == "Yes":
				CreateNodeIfNot(ID).Yes = CreateNodeIfNot(child)
			elif prediction == "No":
				CreateNodeIfNot(ID).No = CreateNodeIfNot(child)

def GetTreeRoot(keyword):
	if keyword in Keywork2Tree:
		return Keywork2Tree[keyword]
	return None

def FindTreeNode(node, answer):
	if answer == True:
		return node.Yes
	return node.No

def IsLeafNode(node):
	return node.Yes == None and node.No == None

def loadTsvDict(file_name, d):
	with open(file_name) as f:
		for line in f:
			sp = line.strip().split('\t')
			if len(sp) == 2:
				d[sp[0]] = sp[1]
def load():
	loadBinaryTree("src/Decision")
	loadTsvDict("src/ID2Description", ID2Description)

def get_by_symptom(s):
	return GetTreeRoot(s)

def get_question(node):
	return ID2Description[node.ID]

if __name__ == '__main__':
	loadBinaryTree("Decision")
	loadTsvDict("ID2Description", ID2Description)
	print("Please type Symptom:")
	symptom = sys.stdin.readline().strip()
	node = GetTreeRoot(symptom)
	if node is None:
		print("Symptom '" + symptom + "' not found.")
		quit()
	while not IsLeafNode(node):
		print("Please answer the question: " + ID2Description[node.ID])
		ans = sys.stdin.readline().strip()
		if ans.lower() == "yes":
			node = node.Yes
		else:
			node = node.No
	print("Dr. Ming Suggestion: " + ID2Description[node.ID])
