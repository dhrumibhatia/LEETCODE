
words = ["abba","baba","bbaa","cd","cd"]
li = []
for i in words:
    li.append(i)
    if len(li)>=2 and sorted(li[-1]) == sorted(li[-2]):
        print(sorted(li[-1]),sorted(li[-2]))
        li.pop() #remove last element
print(li)

#Approach2
class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        i = 1
        while i < len(words):
            # Check if the current word and the previous word are anagrams
            if sorted(words[i]) == sorted(words[i - 1]):
                # If they are anagrams, delete the current word
                del words[i]
            else:
                # If not, move to the next word
                i += 1
        return words

#Approach3
class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        #automatically get first word
        hashMap ={0: words[0]} 
        for i in range(1,len(words)):
            notAnagram = words[i]
            #sort words in alphabetical order
            #if not the same add to hashMap
            if sorted(words[i]) != sorted(words[i-1]):
                hashMap[i] = notAnagram
        return list(hashMap.values())

#Approach4
class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        def is_anagram(s, t):
            if sorted(s) == sorted(t):
                return True
            return False
        ans = [words[0]]
        for i in range(1, len(words)):
            if is_anagram(words[i], words[i-1]) == False:
                ans.append(words[i])
        return ans