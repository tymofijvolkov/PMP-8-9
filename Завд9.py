import string
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import *
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('gutenberg', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

print('Список текстів Project Gutenberg:')
print(gutenberg.fileids())

text = nltk.corpus.gutenberg.words('bryant-stories.txt')

total_words = len(text)
unique_words = len(set(word.lower() for word in text))

print('\n1. Кількість слів')
print('Загальна кількість слів у тексті:', total_words)
print('Кількість унікальних слів у тексті:', unique_words)
print(
    f'Порівняння: загальна кількість слів у {total_words / unique_words:.2f} разів більша за кількість унікальних (або унікальні слова становлять {(unique_words / total_words) * 100:.2f}% від усіх слів).'
)
fdist = FreqDist(text)
top_ten = fdist.most_common(10)

print('\n2. 10 найбільш вживаних слів')
print(top_ten)

words_raw, counts_raw = zip(*top_ten)
plt.figure(figsize=(10, 5))
plt.bar(words_raw, counts_raw, color='skyblue', edgecolor='black')
plt.title("10 найбільш уживаних слів (до очищення, 'bryant-stories.txt')")
plt.xlabel('Слова / символи')
plt.ylabel('Частота')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

stop_words = set(stopwords.words('english'))
without_stop_words = [
    word for word in text if word.lower() not in stop_words
]

print('\n3. Очищення тексту')
print('Текст після видалення стоп-слів (перші 20 елементів):')
print(without_stop_words[:20])

table = str.maketrans('', '', string.punctuation)
stripped = [word.translate(table).lower() for word in without_stop_words]

stripped = [
    word for word in stripped if word.isalpha() and word not in stop_words
]

fdist_clean = FreqDist(stripped)
top_ten_clean = fdist_clean.most_common(10)

print('\n10 найбільш вживаних слів після видалення стоп-слів та пунктуації:')
print(top_ten_clean)

words_clean, counts_clean = zip(*top_ten_clean)
plt.figure(figsize=(10, 5))
plt.bar(words_clean, counts_clean, color='lightgreen', edgecolor='black')
plt.title(
    '10 найбільш уживаних слів (після видалення стоп-слів та пунктуації)'
)
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

print('\n4. Лематизація та Стемінг')

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in stripped]
fdist_lemma = FreqDist(lemmatized_words)
top_ten_lemma = fdist_lemma.most_common(10)

print('10 найбільш вживаних слів після лематизації:')
print(top_ten_lemma)

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in stripped]
fdist_stem = FreqDist(stemmed_words)
top_ten_stem = fdist_stem.most_common(10)

print('\n10 найбільш вживаних слів після стемінгу:')
print(top_ten_stem)
