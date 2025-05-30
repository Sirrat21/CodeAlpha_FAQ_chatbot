#C:\miniconda\Conda_install\AI\FAQ_Chatbot\faqschatbot
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from fuzzywuzzy import process
import string
import nltk
from nltk.stem import WordNetLemmatizer


nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()


def preprocess(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(text)
    lemmatized = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(lemmatized)


def load_faqs():
    df = pd.read_csv("faqs.csv")
    faq_dict = {}
    for _, row in df.iterrows():
        question = preprocess(row['question'])
        faq_dict[question] = row['answer']
    return faq_dict


def fuzzy_match(query, faq_dict):
    questions = list(faq_dict.keys())
    match, score = process.extractOne(query, questions)
    if score > 80:
        return faq_dict[match], match
    return None, None

faq_data = load_faqs()


def get_answer():
    user_q = entry.get()
    cleaned_q = preprocess(user_q)

    if cleaned_q in faq_data:
        response = faq_data[cleaned_q]
        result_label.config(text="🤖 " + response)
    else:
        fuzzy_resp, matched_q = fuzzy_match(cleaned_q, faq_data)
        if fuzzy_resp:
            result_label.config(text=f"🤖 {fuzzy_resp}\n\n(Matched with: \"{matched_q}\")")
        else:
            result_label.config(text="🤖 Sorry, I couldn't find an answer. Try rephrasing your question.")


def give_feedback():
    messagebox.showinfo("Feedback", "Thank you for your feedback!\n(Feature coming soon)")


root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("600x450")
root.configure(bg="#f0f4f8")

tk.Label(root, text=" FAQ Chatbot", font=("Helvetica", 20, "bold"), bg="#f0f4f8").pack(pady=10)
tk.Label(root, text="Ask me something about our services:", font=("Helvetica", 12), bg="#f0f4f8").pack()

entry = tk.Entry(root, font=("Helvetica", 14), width=50)
entry.pack(pady=5)

button_frame = tk.Frame(root, bg="#f0f4f8")
button_frame.pack(pady=5)

submit_btn = tk.Button(button_frame, text="Send", command=get_answer, font=("Helvetica", 12), bg="#4CAF50", fg="white")
submit_btn.pack(side="left", padx=10)

feedback_btn = tk.Button(button_frame, text="Feedback", command=give_feedback, font=("Helvetica", 12), bg="#4CAF50", fg="white")
feedback_btn.pack(side="left", padx=10)

result_label = tk.Label(root, text="", wraplength=500, font=("Helvetica", 12), bg="#f0f4f8", justify="left")
result_label.pack(pady=3)

root.mainloop()

