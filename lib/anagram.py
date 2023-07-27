class Anagram:
    def __init__(self,word):
        self.word = word
    def match(self, list_of_words):
        # letter is a variable that iterates in list of words and if the letters in list of words are equal, then return the words that are a match.
        # list of words is the ["listen, silent, hoppopotamus"]
        return_words = [letters for letters in list_of_words if sorted(letters) == sorted(self.word)]
        return return_words