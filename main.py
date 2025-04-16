import requests
import collections

def get_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return ""

def count_word_frequencies(url, words_to_count, case_sensitive=True):
    text = get_text(url)
    if not text:
        return {}
    
    if not case_sensitive:
        text = text.lower()
        words_to_count = [word.lower() for word in words_to_count]

    words = text.split()
    
    counter = collections.Counter(words)
    
    frequencies = {word: counter[word] for word in words_to_count}
    return frequencies

def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    with open(words_file, 'r', encoding='utf-8') as file:
        words_to_count = [line.strip() for line in file if line.strip()]

    frequencies = count_word_frequencies(url, words_to_count, case_sensitive=True)
    
    print(frequencies)

if __name__ == "__main__":
    main()
