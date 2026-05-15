import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# 1. THE MULTI-LANGUAGE DATASET
# 1 = Spam (Red Alert), 0 = Ham (Safe Message)
data = {
    'text': [
        # --- ENGLISH SPAM ---
        'Get a free iPhone now!', 'Winner of cash prize', 
        'Urgent: Your account is locked, click here', 'Claim your lottery reward',
        'Congratulations, you won a gift card!', 'Double your money in 24 hours',

        # --- ENGLISH SAFE (HAM) ---
        'Meeting at 5pm today', 'Hello, how are you?', 
        'Can we grab coffee tomorrow?', 'The project deadline is Friday',
        'Please send the notes', 'See you at the university library',

        # --- ROMAN URDU/ENGLISH SPAM ---
        'Mubarak ho! Aapne 50,000 ka inaam jeeta hai',
        'Jeeto Pakistan se cash prize hasil karne k liye call karen',
        'BISP ki taraf se 25,000 milay hain, rabta karen',
        'Aapka account block ho gaya hai, foran verify karen',
        'Free balance hasil karne k liye is link par click karen',
        'Inaam nikal aya hai, foran apna address bhejen',
        '8171 program ki taraf se 12000 mubarak ho',

        # --- ROMAN URDU/ENGLISH SAFE (HAM) ---
        'Bhai kahan ho? Pohanch gaye?',
        'Ammi keh rahi hain dahi le ana raste se',
        'Kya haal hai? Khairiyat se ho?',
        'Kal university ana hai ya nahi?',
        'Project ki file email kar di hai check karlo',
        'Bas 5 minute mein pohanch raha hoon',
        'Aaj ki class cancel ho gayi hai',
        'Ghar kab tak aaoge?'
    ],
    'label': [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
}

# 2. CREATE DATAFRAME
df = pd.DataFrame(data)

# 3. VECTORIZATION (The "Dictionary" builder)
# We use ngram_range=(1,2) so it recognizes "Inaam" and also "Inaam jeeta"
cv = CountVectorizer(ngram_range=(1, 2))
X = cv.fit_transform(df['text'])
y = df['label']

# 4. TRAINING THE AI (Multinomial Naive Bayes)
model = MultinomialNB()
model.fit(X, y)

# 5. SAVING THE BRAIN
joblib.dump(model, 'spam_model.pkl')
joblib.dump(cv, 'vectorizer.pkl')

print("--- TRAINING COMPLETE ---")
print(f"Total phrases learned: {len(data['text'])}")
print("AI now understands English and Roman Urdu patterns!")