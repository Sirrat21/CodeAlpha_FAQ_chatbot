# CodeAlpha_FAQ_chatbot

# FAQS Chatbot

A simple desktop chatbot app built with Tkinter that answers frequently asked questions using fuzzy string matching and a clean graphical interface. It loads questions and answers from a CSV file and uses intelligent matching to provide relevant answers—even when the user's input isn't exact.

## Features

- Instant responses to common FAQs.
- Intelligent fuzzy matching for non-exact questions.
- Simple and user-friendly Tkinter interface.
- Highlight matched question for clarity.
- Feedback button included (for future expansion).
- Easy to update FAQ data via CSV file.

## Installation

- Clone this repository or download the code.
- Make sure you have Python installed (recommended Python 3.7+).
- Install dependencies using pip:

---

*bash*
           pip install -r requirements.txt

---

*Usage*
Run the chatbot locally with:
           python faqschatbot.py

---

*How to Use*
1. Enter your question in the input box.
2. Click Send to get an answer from the chatbot.
3. If a direct match isn't found, the bot will show the closest matching question and answer.
4. Click Feedback to leave a comment (coming soon).

---

*Dependencies*
pandas
fuzzywuzzy
python-Levenshtein
tkinter (usually included with Python)

---

*License*
        This project is open source 

---

*Contact*
         Created by Sirrat Rashid
