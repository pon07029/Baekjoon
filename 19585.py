import sys
input=sys.stdin.readline
# class Trie:
#     def __init__(self):
#         self.trie = {}  # root 
 
#     def insert(self, word):
#         t = self.trie
#         for c in word:
#             if c not in t:
#                 t[c] = {}
#             t = t[c]
#         t['*'] = True # 끝이라는걸 알림
 
#     def search(self, word):
#         t = self.trie
#         for c in word:
#             if c not in t:
#                 return False
#             t = t[c]
#         return '*' in t

# team=Trie()

C,N=map(int, input().split())
col={}
for _ in range(C):
    now = col
    for c in input().rstrip():
        if c not in now:
            now[c] = {}
        now = now[c]
    now[0] = True
name={input().rstrip() for _ in range(N)}

def f(w):
    now = col
    for i in range(len(w)):
        if now.get(0) and w[i:] in name:
            return True
        if w[i] not in now:
            return False
        now = now[w[i]]
for n in range(int(input())):
    print("Yes" if f(input().rstrip()) else "No")