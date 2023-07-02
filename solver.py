import typing


class WordleSolver:

    def solve(self,
              words_list: typing.Optional[typing.List[str]],
              letters_dictionary: typing.Optional[typing.Dict]
              ) -> typing.Optional[typing.List[str]]:
        updated_words_list = []
        if not words_list:
            raise ValueError
        words_list_for_loop = words_list.copy()
        for word in words_list_for_loop:
            for letter, value in letters_dictionary.items():
                color, pos = value[0], value[1]
                # Black
                if color == 'b':
                    if letter not in word:
                        if word not in updated_words_list:
                            updated_words_list.append(word)
                    words_list = updated_words_list

                #Green
                elif color == 'g':
                    if word[pos] == letter:
                        if word not in updated_words_list:
                            updated_words_list.append(word)
                    words_list = updated_words_list

                # Yellow
                elif color == 'y':
                    if letter in word:
                        if word[pos] != letter:
                            if word not in updated_words_list:
                                updated_words_list.append(word)

        return updated_words_list
