# 제 7 강에서 소개된 추상적 자료구조로 LinkedList 라는 이름의 클래스가 정의되어 있다고 가정하고, 이 리스트를 처음부터 끝까지 순회하는 메서드 traverse() 를 완성하세요.

class Node:
    def __init__(self,item):
        self.data =item
        self.next=None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None
    
    def getAt(self,pos):
        if pos <1 or pos > self.nodeCount:
            return None
        i = 1 
        curr = self.head
        while i <pos:
            curr = curr.next
            i+=1
        return curr

    def traverse(self):
        arr=[]
        curr=self.head
        while curr != None:
            arr.append(curr.data)
            curr=curr.next
        return arr

def solution(x):
    return 0
