from analyzer import Analyzer
from predict import Predict
from settings import Settings

def getSampletext():
	with open("sample.txt", "r", encoding="utf-8") as f:
		text = f.read().strip()
		text = text.replace("\n", "")
		text = text.split(Settings.sign[Settings.language]["comma"])
		return text

def main():
	text = getSampletext()
	text = text[:len(text) - 1]
	analyzer = Analyzer()
	for phrase in text:
		analyzer.analyze_text(phrase + Settings.sign[Settings.language]["comma"])
	analyzer.save()
	predict = Predict()
	predict.loadDictionary()
	print(predict.generate(Settings.sentence_length))

if __name__ == "__main__":
	main()
