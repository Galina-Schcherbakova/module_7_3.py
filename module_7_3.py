class WordsFinder:
    def __init__(self, file_path):
        self.file_path = file_path
        self.words = self._load_words()

    def _load_words(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            return text.lower().split()

    def get_all_words(self):
        return self.words

    def find(self, word):
        word_lower = word.lower()
        try:
            return self.words.index(word_lower) + 1
        except ValueError:
            return -1

    def count(self, word):
        word_lower = word.lower()
        return self.words.count(word_lower)


if __name__ == "__main__":
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())
    print(finder2.find('TEXT'))
    print(finder2.count('teXT'))
