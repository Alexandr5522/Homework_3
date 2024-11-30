import string


class WordsFinder:
    # Объект этого класса должен принимать при создании неограниченного количество названий файлов
    # и записывать их в атрибут file_names в виде списка или кортежа

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        # подготовительный метод, который возвращает словарь следующего вида:
        # {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
        # Где:'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
        # ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                line = file.read()
                line = line.lower()
                for punc in string.punctuation:
                    if punc in line:
                        line = line.replace(punc, ' ')
                all_words.update({file_name: line.split()})
        return all_words

    def find(self, word):
        # Метод, где word - искомое слово.
        # Возвращает словарь, где ключ - название файла,
        # значение - позиция первого такого слова в списке слов этого файла.
        word = word.lower()
        found_words = {}
        for file_name, words in self.get_all_words().items():
            found = False
            for i in range(len(words)):
                if words[i] == word:
                    found = True
                    break
            if found:
                found_words[file_name] = i + 1  # позиция начинается с 1
        return found_words

    def count(self, word):

        word = word.lower()
        word_number = {}
        for file_name, words in self.get_all_words().items():
            word_number[file_name] = words.count(word)
        return word_number

finder2 = WordsFinder('test_file.txt', 'Rudyard Kipling - If.txt')

print(finder2.get_all_words())

print(finder2.find('if'))

print(finder2.count('if'))