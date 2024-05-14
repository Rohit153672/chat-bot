import nltk
import numpy as np
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# nltk.download('punkt')  # Uncomment this line if you haven't downloaded nltk punkt tokenizer

# Sample conversation starters for the chatbot
GREETING_INPUTS = ("hello", "hi", "greetings", "hey", "what's up")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello"]

# Sample FAQs and their corresponding answers
FAQS = {
    "What courses are available?": "We offer courses in mathematics, science, literature, and more.",
    "How do I enroll in a course?": "You can enroll in a course by visiting our website and following the enrollment process.",
    "Who are the instructors?": "Our instructors are highly qualified professionals with years of experience in their respective fields.",
    "How can I contact support?": "You can contact our support team via email at support@example.com or by phone at 123-456-7890."
}

# Preprocessing function to tokenize and remove punctuation from text
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = ''.join([char for char in text if char not in string.punctuation])  # Remove punctuation
    return nltk.word_tokenize(text)

# Function to generate response to user input
def generate_response(user_input):
    response = ""
    FAQS[user_input] if user_input in FAQS else None
    if user_input in FAQS:
        response = FAQS[user_input]
    else:
        responses.append(user_input)
        TfidfVec = TfidfVectorizer(tokenizer=preprocess_text, stop_words='english')
        tfidf = TfidfVec.fit_transform(responses)
        vals = cosine_similarity(tfidf[-1], tfidf)
        idx = vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        if (req_tfidf == 0):
            response = "I'm sorry, I don't understand."
        else:
            response = responses[idx]
    return response

# Main function to handle conversation
def chat():
    print("Student Support Bot: I'm here to help you with your questions!")
    while True:
        user_input = input("You: ")
        user_input = user_input.lower()
        if user_input in GREETING_INPUTS:
            print("Student Support Bot: " + np.random.choice(GREETING_RESPONSES))
        elif user_input == "bye":
            print("Student Support Bot: Bye! Have a great day.")
            break
        else:
            print("Student Support Bot: " + generate_response(user_input))

# Initializing conversation history with greeting responses
responses = list(GREETING_RESPONSES)

# Start the chat
chat()
