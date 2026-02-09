from analyzer import Analyzer
from predict import Predict
from settings import Settings
import os

def userConfirm():
	if os.path.isfile("Dictionary.json"):
		user_input = input("It seems that the dictionary already exists. Do you want to continue? (y/n): ")
		return user_input.lower() == "y"
	return True

def getSampletext():
	with open("sample.txt", "r", encoding="utf-8") as f:
		text = f.read().strip()
		text = text.replace("\n", "")
		text = text.split(Settings.sign["comma"])
		return text

def main():
	text = getSampletext()
	text = text[:len(text) - 1]
	if userConfirm():
		analyzer = Analyzer()
		for phrase in text:
			analyzer.analyze_text(phrase + Settings.sign["comma"])
		analyzer.save()
	predict = Predict()
	predict.loadDictionary()
	print(predict.generate(Settings.length))

if __name__ == "__main__":
	main()
