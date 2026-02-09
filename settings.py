# This language setting is simplified and is used to replace punctuation and spaces.
# It does not support changing the appropriate language settings for MeCab.
class Settings:
	language = "ja"
	length = 10
	sign = {
		"ja": {
			"comma": "。",
			"space": ""
		},
		"en": {
			"comma": ".",
			"space": " "
		}
	}[language]
