#https://codeforces.com/problemset/problem/71/A

# codeforces
# A WAY TOO LONG WORDS

n = int(input())
for i in range(n):
   word = input()
   print(str(word[0] + str(len(word) - 2) + word[-1]) if len(word) > 10 else word)


