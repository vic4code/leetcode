class Trie:

    def __init__(self):
        self.trie = []

    def insert(self, word: str) -> None:
        self.trie.append(word)

    def search(self, word: str) -> bool:
        if word in self.trie:
            return True
        
        return False
        
    def startsWith(self, prefix: str) -> bool:
        
        for i in self.trie:
            if i.startswith(prefix):
                return True
        
        return False


# Implement by dictionary
class Trie_Dict:
    
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#'

    def search(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            return True
        return False

    def startsWith(self, prefix):
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True
        
if __name__ == '__main__':
    
    word = 'apple'
    prefix = 'app'
    
    obj = Trie()
    obj.insert(word)
    param_2 = obj.search(word)
    param_3 = obj.startsWith(prefix)