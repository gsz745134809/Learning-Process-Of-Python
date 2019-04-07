# 字典树


class TrieNode:
    # Trie node class
    def __init__(self):
        self.children = [Node] * ALPHABET_SIZE

        # isEndOfWord is Trie if node represent
        # the end of the word
        self.isEndOfWord = False
