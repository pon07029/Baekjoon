import sys
input=sys.stdin.readline
class Node:
    def __init__(self, key, cnt=0):
        self.key = key
        self.child = {}
        self.cnt = cnt

class Trie:

    def __init__(self):
        self.trie = Node(None)
 
    def insert(self, word):
        t = self.trie
        for c in word:
            if c not in t.child:
                t.child[c] = Node(c)
            t = t.child[c]
            t.cnt += 1
        t.child['*'] = True
def count(becnt, cur):
    global cnt
    if cur.cnt !=becnt and cur.key is not None:
        if cur.key.islower():
            cnt+=cur.cnt
        # print(cur.cnt, cur.key, cur.child)
    for w in cur.child:
        if w=='*':
            continue
        count(cur.cnt, cur.child[w])

def f():
    global cnt
    cnt=0
    trie=Trie()
    n=int(input())
    for i in range(n):
        trie.insert(input())
    count(1, trie.trie)
    print("{:,.2f}".format(round((cnt/n),2)))
while True:
    try:
        f()
    except:
        break
