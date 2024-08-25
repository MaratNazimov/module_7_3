class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_txt in self.file_names:
            with open(file_txt, 'r', encoding='utf-8') as file:
                all_words[file_txt] = [word.strip(',.=!?;: -').lower() for word in file.read().split()]
        return all_words

    def find(self, word):
        all_words = self.get_all_words
        dict_word = {}
        for file_names, words in all_words().items():
            if word.lower() in words:
                dict_word[file_names] = words.index(word.lower()) + 1
        return dict_word

    def count(self, word):
        all_words = self.get_all_words
        dict_count = {}
        for file_names, words in all_words().items():
            dict_count[file_names] = words.count(word.lower())
        return dict_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
