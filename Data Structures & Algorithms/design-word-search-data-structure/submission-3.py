class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True
        

    def search(self, word: str) -> bool:
        return self.searchTrie(self.trie, word)

    def searchTrie(self, trie, word):
        for i, c in enumerate(word):
            if c == '.':
                for t in trie.children:
                    if self.searchTrie(trie.children[t], word[i + 1:]):
                        return True
                return False

            if c not in trie.children:
                return False
            trie = trie.children[c]

        return trie.isWord
                
