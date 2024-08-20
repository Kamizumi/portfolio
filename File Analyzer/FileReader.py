import re

class FileOpenError(Exception):
    pass

def open_file():
    attempts = 0
    while attempts < 3:
        try:
            file_name = input("Enter the file name: ")
            with open(file_name, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print("File not found. Please re-enter.")
...             attempts += 1
...     raise FileOpenError("Maximum attempts reached. Exiting program.")
... 
... def process_content(lines):
...     total_lines = len(lines)
...     total_words = 0
...     word_frequency = {}
...     word_set = set()
... 
...     for line in lines:
...         words = re.findall(r'\b[a-zA-Z]+\b', line.lower())
...         total_words += len(words)
...         word_set.update(words)
...         for word in words:
...             word_frequency[word] = word_frequency.get(word, 0) + 1
...     
...     return total_lines, total_words, word_frequency, word_set
... 
... def display_word_counts(word_frequency):
...     sorted_word_counts = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
...     for word, count in sorted_word_counts:
...         print(f"('{word}', {count})")
... 
... def main():
...     try:
...         lines = open_file()
...         total_lines, total_words, word_frequency, word_set = process_content(lines)
... 
...         print(f"Total lines in the file: {total_lines}")
...         print(f"Total words in the file: {total_words}")
...         print(f"Set of distinct words: {word_set}")
...         print("Word counts:")
...         display_word_counts(word_frequency)
...     except FileOpenError as e:
...         print(e)
... 
... if __name__ == "__main__":
