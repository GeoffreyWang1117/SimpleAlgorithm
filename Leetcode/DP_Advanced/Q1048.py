'''
Sort the words by their lengths. This ensures that when we process a word, we have already processed all possible predecessors of that word.
Use a dictionary to store the longest chain length ending at each word.
For each word, try removing each character to form a predecessor and see if it exists in the dictionary. If it does, update the current word's chain length.
Track the maximum chain length found during the process.
'''

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        longest_chain = {}

        max_chain_length =1

        for word in words:
            current_chain_length = 1
            for i in range(len(word)):
                predecessor = word[:i]+word[i+1:]
                if predecessor in longest_chain:
                    current_chain_length = max(current_chain_length,longest_chain[predecessor]+1)
            longest_chain[word]=current_chain_length
            max_chain_length=max(max_chain_length,current_chain_length)

        return max_chain_length
