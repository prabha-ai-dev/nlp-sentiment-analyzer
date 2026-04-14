Sentiment Analysis using NLTK (VADER)

Project Overview

This project is a simple **Sentiment Analysis tool** built using Python and NLTK's VADER.
It analyzes product reviews and classifies them as **Positive, Negative, or Neutral**.

---

Features

* Analyze multiple product reviews
* Uses NLTK's VADER sentiment analyzer
* Simple and beginner-friendly code
* No machine learning training required

---

Technologies Used

* Python 
* NLTK (Natural Language Toolkit)

---

Project Structure

* `nlp11.py` → Main Python file for sentiment analysis
* `README.md` → Project documentation

---

How to Run

1. Install NLTK:

```
pip install nltk
```

2. Download VADER lexicon:

```python
import nltk
nltk.download('vader_lexicon')
```

3. Run the script:

```
python nlp11.py
```

---

Example Output

```
I love this phone → Positive
Worst product ever → Negative
It's okay → Neutral
```

---

Future Improvements

* Add text cleaning (remove emojis, punctuation)
* Analyze real-time tweets
* Build a web app interface

---

Author
prabha-ai-dev

---
