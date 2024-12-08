import string

class WordsFinder:
    def __init__(self, *file_paths):
        self.file_paths = file_paths
        self.all_words = {file_path: self._load_words(file_path) for file_path in self.file_paths}

    def _load_words(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                text = text.translate(str.maketrans('', '', string.punctuation))
                return text.lower().split()
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
            return []

    def get_all_words(self):
        return self.all_words

    def find(self, word):
        word_lower = word.lower()
        results = {}
        for file_path, words in self.all_words.items():
            try:
                results[file_path] = words.index(word_lower) + 1
            except ValueError:
                results[file_path] = -1
        return results

    def count(self, word):
        word_lower = word.lower()
        results = {}
        for file_path, words in self.all_words.items():
            results[file_path] = words.count(word_lower)
        return results


if __name__ == "__main__":
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())
    print(finder2.find('TEXT'))
    print(finder2.count('teXT'))
