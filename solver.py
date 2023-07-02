import typing


class WordleSolver:

    def solve(self,
              words_list: typing.Optional[typing.List[str]],
              letters_dictionary: typing.Optional[typing.Dict]
              ) -> typing.Optional[typing.List[str]]:
        if not words_list:
            raise ValueError
        words_list_for_loop = words_list.copy()
        for letter, value in letters_dictionary.items():
            color, pos = value[0], value[1]
            for word in words_list_for_loop:
                # Black
                if color == 'b':
                    if letter in word:
                        if word in words_list:
                            words_list.remove(word)

        words_list_for_loop = words_list.copy()
        for letter, value in letters_dictionary.items():
            color, pos = value[0], value[1]
            for word in words_list_for_loop:
                # Green
                if color == 'g':
                    if word[pos] != letter:
                        if word in words_list:
                            words_list.remove(word)

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

        return words_list
