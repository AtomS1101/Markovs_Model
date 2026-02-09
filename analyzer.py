import MeCab
import json

class Analyzer:
	def __init__(self):
		self._mecab = MeCab.Tagger("-Owakati")
		self._parts_list = {}
		self._dictionary = {}
		self._parts = ""
		self._word = ""
		self._next_word = ""

	def save(self):
		with open("Dictionary.json", "w", encoding="utf-8") as f, \
			  open("PartsList.json", "w", encoding="utf-8") as g:
			json.dump(self._dictionary, f, ensure_ascii=False)
			json.dump(self._parts_list, g, ensure_ascii=False)

	def addToPartsList(self):
		if self._parts not in self._parts_list:
			self._parts_list[self._parts] = [self._word]
		else:
			if self._word not in self._parts_list[self._parts]:
				self._parts_list[self._parts].append(self._word)

	def addToDictionary(self):
		if self._word not in self._dictionary:
			self._dictionary[self._word] = {self._next_word: 1}
		else:
			if self._next_word not in self._dictionary[self._word]:
				self._dictionary[self._word][self._next_word] = 1
			else:
				self._dictionary[self._word][self._next_word] += 1

	def analyze_text(self, text):
		node = self._mecab.parseToNode(text)
		node = node.next
		while node:
			self._word = node.surface
			self._parts = node.feature.split(",")[0]
			node = node.next
			self._next_word = node.surface
			if self._next_word:
				self.addToPartsList()
				self.addToDictionary()
			else:
				break
