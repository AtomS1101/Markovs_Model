import json
import random
from settings import Settings

class Predict:
	def __init__(self):
		self._first_word = ""
		self._sentence = []
		self._word = ""
		self._dictionary = {}
		self._parts = {}

	def loadDictionary(self):
		with open("Dictionary.json", "r", encoding="utf-8") as f:
			self._dictionary = json.load(f)

	def loadParts(self):
		if not self._parts:
			with open("PartsList.json", "r", encoding="utf-8") as f:
				self._parts = json.load(f)

	def selectWord(self):
		total = 0
		for word, possibility in self._dictionary[self._sentence[-1]].items():
			total += possibility
		rand = random.randint(1, total)
		for word, possibility in self._dictionary[self._sentence[-1]].items():
			rand -= possibility
			if rand <= 0:
				self._word = word
				break

	def setFirstWord(self):
		self.loadParts()
		self._first_word = random.choice(self._parts["名詞"])
		self._sentence.append(self._first_word)

	def generate(self, sentence_length):
		for n in range(sentence_length):
			self.setFirstWord()
			flag = True
			while flag:
				self.selectWord()
				self._sentence.append(self._word)
				if self._word[-1] == Settings.sign["comma"]:
					flag = False
		return Settings.sign["space"].join(self._sentence)
