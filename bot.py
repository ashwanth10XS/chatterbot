import nltk
import re
import random
import string

from string import punctuation

# Download stopwords from nltk
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(nltk.corpus.stopwords.words('english'))

def sentence_tokenizer(data):
   # Function for Sentence Tokenization
   return nltk.sent_tokenize(data.lower())

def word_tokenizer(data):
   # Function for Word Tokenization
   return nltk.word_tokenize(data.lower())

def remove_noise(word_tokens):
   # Function to remove stop words and punctuation
   cleaned_tokens = []
   for token in word_tokens:
      if token not in stop_words and token not in punctuation:
         cleaned_tokens.append(token)
   return cleaned_tokens

# Define the Patterns and Responses
patterns = [
   (['hi','hello','hey'], ['Hi there!', 'Hello!', 'Hey!']),
   (['bye','goodbye'], ['Bye', 'Goodbye!']),
   # Modified the regex pattern for general input
   
   (['what is your name','your name'], ["iam a Chatbot." ]),
   (['how old are you'], ["I don't have an age. I'm just a computer program.", "I'm ageless. How can I assist you?"]),
   (['thank you |thanks'], ["You're welcome!", "No problem, happy to help!"]),
   (['sorry|apologize'], ["No need to apologize. How can I assist you?", "It's okay. How can I help?"]),
   (['time|current time'], ["I'm sorry, I can't provide real-time information.", "I don't have access to real-time data."]),
   (['tell me a joke'], ["Why don't scientists trust atoms? Because they make up everything!", "Sure, here's one: Why was the math book sad? Because it had too many problems."]),
   (['what are your hobbies|hobbies'], ["I don't have hobbies. I'm here to answer your questions.", "I'm interested in assisting you. What's on your mind?"]),
   (['not sure|confused'], ["It's okay to be confused. Feel free to ask me anything you'd like to clarify.", "I'm here to help clear up any confusion you may have."]),
   (['(\?)'], ["I’m sorry, but I can’t answer that", "Please ask me another question", "I’m not sure what you mean."]),  # Fixed a syntax issue here
   #e-commerce
   (['what is the popular brand|top brand'],["1 Gucci"]),
   (['best mobile brand'],["apple"]),
   (['best perfume'],["denver"]),
   (['price range of brands'],["between 1-2 lakhs"]),
   (['best e-commerce website'],["amazon"]),
   #healthcare
   (['medicine for fever|fever'],["ASOZEN FORTE - Aceclofenac + paracetamol + Chlorzoxazone."]),
   (['cough'],["Cofsils Naturals Cough Syrup Bottle 100 Ml","dextromethorphan (Robitussin, Delsym)."]),
   (['leg pain'],["acetaminophen or ibuprofen"]),
   (['rashess'],["Benadryl, Zyrtec (cetirizine)", "Claritin (loratadine)"]),
   (['motions'],["meclizine"]),
   (['blood pressure'],["amlodipine", "felodipine and nifedipine"]),
    #customer service & banking
    (['customer care number hdfc'],[" 1800 202 6161 1860 267 6161"]),
    (['customer care number canara'],["1800 1030"]),
    (['customer care number sbi'],["1800 1234"]),
    (['emergency'],["100","112"]),
    (['ambulance'],["108"]),
    
]

def generate_response(user_input):
   # Use regular expressions to match user input to patterns
   for pattern, responses in patterns:
      for p in pattern:
         if re.match(p, user_input):
            # Return a response from the matched pattern
            return random.choice(responses)  # Changed "patterns" to "responses" to return a response from the matched pattern



# Main loop of chatbot
conversation_history = []
while True:
   # User Input
   user_input = input("You: ")
   # End the Loop if the User Says Bye or Goodbye
   if user_input.lower() in ['bye', 'goodbye']:
      print('Chatbot: Goodbye!')
      break
   # Process Query and Generate Response
   chatbot_response = generate_response(user_input)
   # Print Response
   print('Chatbot:', chatbot_response)
