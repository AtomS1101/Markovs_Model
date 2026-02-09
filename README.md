# Markov chain language model
This is a language model using a simple Markov chain.
The `sample.txt` and `Dictionary.json` were trained using parts of "吾輩は猫である".

# How to use?
1. Just run `main.py` to get ten awkward sentences and see the Markov chain in action with the sample `Dictionary.json`.
2. If `Dictionary.json` already exists, you will be asked whether to re-train the model. You can skip this by pressing Enter, or type "y" to start a new training session.

# Required
```
pip install mecab-python3
pip install unidic-lite
```

# Note
> The language settings in `setting.py` do not change the MeCab language configuration. It only replace punctuation and spaces.
