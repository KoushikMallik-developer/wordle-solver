from nltk.corpus import words


class WordCollector:

    IN_FILE_NAME = "words.txt"
    OUT_FILE_NAME = "words_list.txt"

    def get_all_words_from_file(self) -> list:

        try:
            with open(self.IN_FILE_NAME) as word_file:
                valid_words = set(word_file.read().split())
            return valid_words
        except Exception:
            print("Some error occured while getting the words from " + self.IN_FILE_NAME)
            return []

    def get_all_words_from_nltk(self) -> list:
        try:
            all_words_list = words.words()
            return all_words_list
        except Exception:
            print("Some error occured while downloading the words.")
            return []

    def filter_words_by_length(self, words_list: list, length: int) -> list:
        filtered_words_list = [str(y).lower() for y in filter(lambda x: len(x) == length, words_list)]
        return filtered_words_list

    def create_file(self, filename: str):
        try:
            with open(filename, 'w') as f:
                f.write('Hello, world!\n')
            print("File " + filename + " created successfully.")
        except IOError:
            print("Error: could not create file " + filename)

    def write_words_to_file(self, file, words_list: list):
        try:
            with open(file, 'w') as f:
                for word in words_list:
                    f.write(word+"\n")
            print("Word-List is updated to file " + file + " successfully with " + str(len(words_list)) + " words.")
        except IOError:
            print("Error: could not write to file " + file)

    def find_remove_duplicates(self, words_list: list) -> list:
        new_word_list = []
        for word in words_list:
            if word not in new_word_list:
                new_word_list.append(word)
        return new_word_list

if __name__ == "__main__":
    word_collector = WordCollector()

    word_list = word_collector.get_all_words_from_file()
    word_list = word_collector.filter_words_by_length(word_list, 5)
    print(len(word_list))
    word_list = word_collector.find_remove_duplicates(word_list)
    print(len(word_list))
    word_collector.create_file(word_collector.OUT_FILE_NAME)
    word_collector.write_words_to_file(word_collector.OUT_FILE_NAME, word_list)



