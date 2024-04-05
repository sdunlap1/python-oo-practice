import random   

class WordFinder:
    """Find random words from words.txt"""
    def __init__(self, path):
        """Read words from words.txt"""
        self.words = self.read_words(path)
        print(f"{len(self.words)} words read")

    def read_words(self, path):
        """Read words from words.txt and return a list"""
        with open(path) as file:
            return[line.strip() for line in file if line.strip()]

    def random(self):
        """Return random word"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """
    Sprcial Word Finder: ignores comments and blank lines.
    
    >>> swf = SpecialWordFinder('words_with_comments.txt')
    4 words read

    >>> swf.random() in ['kale', 'parsnips', 'apple', 'mango']
    True

    >>> swf.random() in ['kale', 'parsnips', 'apple', 'mango']
    True

    >>> swf.random() in ['kale', 'parsnips', 'apple', 'mango']
    True

    Note: The actual random output can't be predicted, so the test checks if the output is one of the expected words.

    """

    def read_words(self, path):
        """Read words from words.txt, removing comments and blank lines"""
        with open(path) as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#')]
    
