import typing


class WordleSolver:

    def solve(self,
              words_list: typing.Optional[typing.List[str]],
              letters_dictionary: typing.Optional[typing.Dict]
              ) -> typing.Optional[typing.List[str]]:
        if not words_list:
            raise ValueError
        if not letters_dictionary:
            return words_list
        words_list = self.remove_blacks(words_list, letters_dictionary)
        words_list = self.remove_yellows(words_list, letters_dictionary)
        words_list = self.process_greens(words_list, letters_dictionary)
        return words_list

    def remove_blacks(self, words_list, letters_dictionary):
        words_list_for_loop = words_list.copy()
        for letter, value in letters_dictionary.items():
            color, pos = value[0], value[1]
            for word in words_list_for_loop:
                # Black
                if color == 'b':
                    if letter in word:
                        if word in words_list:
                            words_list.remove(word)
        return words_list

    def remove_yellows(self, words_list, letters_dictionary) -> typing.Optional[list]:
        words_list_for_loop = words_list.copy()
        for letter, value in letters_dictionary.items():
            color, pos = value[0], value[1]
            for word in words_list_for_loop:
                # Yellow
                if color == 'y':
                    if letter in word:
                        if word[pos] == letter:
                            if word in words_list:
                                words_list.remove(word)
                    else:
                        if word in words_list:
                            words_list.remove(word)
        return words_list

    def process_greens(self, words_list, letters_dictionary) -> typing.Optional[list]:
        words_list_for_loop = words_list.copy()
        for letter, value in letters_dictionary.items():
            color, pos = value[0], value[1]
            for word in words_list_for_loop:
                # Green
                if color == 'g':
                    if letter in word:
                        if word[pos] != letter:
                            if word in words_list:
                                words_list.remove(word)
                    else:
                        if word in words_list:
                            words_list.remove(word)
        return words_list
