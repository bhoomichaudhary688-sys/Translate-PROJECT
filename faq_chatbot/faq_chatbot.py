# STEP 1: FAQs (Question - Answer)
faqs = {
    "What is Python?": "Python is a programming language.",
    "What is a chatbot?": "A chatbot is a program that talks with users.",
    "What is NLP?": "NLP stands for Natural Language Processing.",
    "What is cosine similarity?": "Cosine similarity is used to find similarity between texts."
}

# STEP 2: Import libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# STEP 3: Convert questions to list
questions = list(faqs.keys())

# STEP 4: Text preprocessing (TF-IDF)
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(questions)

# STEP 5: Function to find best answer
def get_answer(user_question):
    user_vector = vectorizer.transform([user_question])
    similarity = cosine_similarity(user_vector, faq_vectors)
    index = similarity.argmax()
    return faqs[questions[index]]

# STEP 6: Chatbot loop
print("FAQ Chatbot (type 'exit' to stop)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Bye!")
        break
    print("Chatbot:", get_answer(user_input))