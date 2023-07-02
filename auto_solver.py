import random

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

import time

from solver import WordleSolver


class AutoSolver:
    FIRST_GUESS_WORD_LIST = ["TORES", "TARES", "SLATE"]
    TRY = 0

    def __init__(self):
        self.browser = None
        chrome_options = self.setup_chrome_settings()
        self.open_browser(chrome_options)
        self.start_game()
        with open("words_list.txt", 'r') as w:
            self.possible_words = [x.lower()[:-1] for x in w.readlines()]
        self.cleanup_dataset()


    def solve_interface(self):
        inputs = self.get_input_boxes()

        random.shuffle(self.FIRST_GUESS_WORD_LIST)
        first_word = self.FIRST_GUESS_WORD_LIST[0]
        result = self.solve(first_word, inputs)

        while len(self.possible_words) != 1:
            inputs = self.get_input_boxes()
            print(self.possible_words[:5])
            solutions = WordleSolver().solve(self.possible_words, result)
            if solutions:
                self.possible_words = solutions
            print(self.possible_words[:5])
            current_word = self.possible_words[0]
            result = self.solve(current_word, inputs)
            if result == {}:
                for input_box in inputs:
                    ActionChains(self.browser).move_to_element(input_box).send_keys(keys.Keys.BACKSPACE).perform()
                self.possible_words.remove(current_word)
                self.TRY -= 1

    def solve(self, word, inputs) -> dict:
        word_char_list = list(word)
        for i in range(0, 5):
            """
            0, 0+5
            5, 5+5
            10, 10+5
            15, 15+5
            20, 20+5
            25, 25+5
            """
            ActionChains(self.browser).move_to_element(inputs[i]).send_keys(word_char_list[i % 5]).perform()

        ActionChains(self.browser).move_to_element(inputs[i]).send_keys(keys.Keys.RETURN).perform()
        self.TRY += 1
        time.sleep(5)
        return self.get_results(inputs)

    def open_browser(self, chrome_options):
        self.browser = webdriver.Chrome(options=chrome_options)
        self.browser.maximize_window()
        self.browser.get('https://www.nytimes.com/games/wordle/index.html')
        time.sleep(1)

    def setup_chrome_settings(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--ignore-certificate-errors')
        return chrome_options

    def start_game(self):
        button = self.browser.find_element(by=By.XPATH, value="/html/body/div/div/div/div/div[3]/button[2]")
        button.click()

        time.sleep(1)

        button = self.browser.find_element(by=By.XPATH, value="/html/body/div/div/dialog/div/button")
        button.click()

        time.sleep(1)

    def get_input_boxes(self):
        inputs = []

        for i in range(1, 6):
            print("/html/body/div/div/div[2]/div/div[1]/div/div["
                  +str(self.TRY)
                  +"]/div["
                  + str(i)
                  + "]/div")
            input_box = self.browser.find_element(by=By.XPATH,
                                                  value="/html/body/div/div/div[2]/div/div[1]/div/div["
                                                        + str(self.TRY+1)
                                                        + "]/div["
                                                        + str(i)
                                                        + "]/div")
            inputs.append(input_box)
        self.browser.implicitly_wait(10)
        return inputs

    def get_results(self, inputs: list) -> dict:
        result_dict = {}
        for input_box in inputs:
            color = input_box.get_attribute("aria-label")
            print()
            print(color)
            print()
            if len(color)>1:
                letter, color = color.split()
                if color == "absent":
                    result_dict[letter] = ["b", 0]
                elif color == "correct":
                    result_dict[letter] = ["g", inputs.index(input_box)]
                elif color == "present":
                    result_dict[letter] = ["y", inputs.index(input_box)]
        return result_dict

    def cleanup_dataset(self):
        temp_words = self.possible_words
        for word in self.possible_words:
            for ascii_value in range(33, 65):
                if chr(ascii_value) in word:
                    if word in temp_words:
                        temp_words.remove(word)
        self.possible_words = temp_words


if __name__ == "__main__":
    wordle_solver = AutoSolver()
    wordle_solver.solve_interface()