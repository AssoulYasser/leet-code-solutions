class Solution:
    digits_dict = {
        '2' : ['a', 'b', 'c'],
        '3' : ['d', 'e', 'f'],
        '4' : ['g', 'h', 'i'],
        '5' : ['j', 'k', 'l'],
        '6' : ['m', 'n', 'o'],
        '7' : ['p', 'q', 'r', 's'],
        '8' : ['t', 'u', 'v'],
        '9' : ['w', 'x', 'y', 'z']
    }

    letterCombinationsList = []
    repeate_each_letter = 0

    def letterCombinationsLenght(self, digits: str) -> int:
        lenght_list = []
        for index_digit in range(len(digits)):
            try:
                lenght_list.append(len(self.digits_dict[digits[index_digit]]))
            except Exception as e:
                print(e)

        if lenght_list == []:
            return 0
    
        lenght = 1
        for each_len in lenght_list:
            lenght *= each_len
        return lenght

    def initLetterCombinationsList(self, digits: str):
        self.letterCombinationsList = []
        for index in range (self.letterCombinationsLenght(digits)):
            self.letterCombinationsList.append('')

    def changeRepetitionNumber(self, digit: str):
        self.repeate_each_letter = int(self.repeate_each_letter / len(self.digits_dict[digit]))

    def appendNewLettersToList(self, digit: str) -> List[str]:
        letters = self.digits_dict[digit]
        letter_combination_index = 0
        letters_index = 0
        while letter_combination_index < len(self.letterCombinationsList):
            letter_index = int(letters_index/self.repeate_each_letter)
            if letter_index < len(letters):
                self.letterCombinationsList[letter_combination_index] += letters[letter_index]
            else:
                letters_index = 0
                letter_index = int(letters_index/self.repeate_each_letter)
                self.letterCombinationsList[letter_combination_index] += letters[letter_index]
            letters_index += 1
            letter_combination_index += 1


    def letterCombinations(self, digits: str) -> List[str]:
        self.initLetterCombinationsList(digits)
        self.repeate_each_letter = len(self.letterCombinationsList)

        for digit_index in range(len(digits)):
            self.changeRepetitionNumber(digits[digit_index])
            self.appendNewLettersToList(digits[digit_index])
            
        return self.letterCombinationsList









