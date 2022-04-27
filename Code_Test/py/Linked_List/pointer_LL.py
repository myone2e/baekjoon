class Node:
    
    # init 함수가 전달받은 data와 next를 해당 필드에 대입함
    def __init__(self, data = None, next = None): #data: Any & next = Node # next가 뒤쪽 노드를 가르키는 포인터
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.no = 0 # 노드의 개수
        self.head = None # 맨 앞 노드
        self.current = None # 지금 주목하는 노드
    
    # head 는 따로! head.next is None 이걸로 연결 리스트에 노드가 1개인지 확인
    def __len__(self): ## 내장 메서드로 구현됨
        return self.no

    def search(self, data):
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1
    
    def __contains__(self, data):
        return self.search(data) >= 0
    
    # 맨 앞에 노드를 삽임
    def add_first(self, data):
        ptr = self.head
        self.head = self.current = Node(data, ptr)
        self.no += 1
    
    