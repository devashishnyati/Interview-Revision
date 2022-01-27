import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists):
        head = point = ListNode(0)
        pq = []
        for li in lists:
            if li:
                pq.append(li)
      
        while pq:
            node = heapq.heappop(pq)
            point.next = ListNode(node.val)
            point = point.next
            node = node.next
            if node:
                heapq.heappush(pq, node)

        return head.next

if __name__ == "__main__":
   
    li = []
    cnt = 0
    for i in (1,4,5,7):
        if cnt == 0:
            prev = head = ListNode(i)
        else:
            node = ListNode(i)
            prev.next = node
            prev = prev.next
        cnt += 1
    li.append(head)
    cnt = 0
    for i in (1,3,4):
        if cnt == 0:
            prev = head = ListNode(i)
        else:
            node = ListNode(i)
            prev.next = node
            prev = prev.next
        cnt += 1
    li.append(head)
    cnt = 0
    for i in (2,6):
        if cnt == 0:
            prev = head = ListNode(i)
        else:
            node = ListNode(i)
            prev.next = node
            prev = prev.next
        cnt += 1
    li.append(head)

    # for l in li:
    #     while l:
    #         print(l.val)
    #         l = l.next

    obj = Solution()
    final_list = pt = obj.mergeKLists(li)
    while pt:
        print(pt.val)
        pt = pt.next