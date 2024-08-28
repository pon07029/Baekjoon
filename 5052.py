import sys

input = sys.stdin.readline

class Node(object):
    def __init__(self, has_end=False):
        self.has_end = has_end
        self.children = dict()

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    # 트라이에 전화번호 추가 
    def insert(self, num):
        curr_node = self.head
        
        for d in num:
            # 현재 노드에 해당하는 숫자의 자식이 없으면 생성
            if curr_node.children.get(d) is None:
                curr_node.children[d] = Node()
            # 해당하는 숫자 자식으로 이동
            curr_node = curr_node.children[d]
        curr_node.has_end = True
    
    # 트라이에서 전화번호 조회
    def search(self, num):
        curr_node = self.head
        
        for d in num:
            # 해당하는 숫자의 자식이 없으면 전화 가능하므로 일관성 있음
            if curr_node.children.get(d) is None:
                return True
            curr_node = curr_node.children[d]
            # 현재 위치에서 끝나는 전화번호가 있다면 해당 번호로 전화되므로 일관성 없음
            if curr_node.has_end:
                return False
        return True
        
        
if __name__=="__main__":
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        phone_numbers = [input().rstrip() for _ in range(n)]
        phone_numbers.sort(key=lambda x : len(x))
        data = Trie()
        for number in phone_numbers:
            # 일관성 없으면 즉시 NO 출력후 다음 테스트케이스 탐색
            if data.search(number) == False:
                print("NO")
                break
            # 일관성 있으면 데이터 삽입
            data.insert(number)
        # 모든 전화번호가 일관성 있다면 YES 출력
        else:
            print("YES")