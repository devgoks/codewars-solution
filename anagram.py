def anagrams(word, words):
    return [i for i in words if ''.join(sorted(word)) == ''.join(sorted(i))]