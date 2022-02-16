from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        current = head
        odd, even = [], []
        length = 1 if head else 0
        
        while current.next:
            length += 1
            current = current.next
        
        current = head
        i = 0
        
        while current:
            if i % 2 == 0:
                odd.append(current.val)
            
            else:
                even.append(current.val)
            
            current = current.next
            i += 1
            
        order = odd + even
        res_head = ListNode(head.val)
        res = res_head
        
        for i in range(1, len(order)):
            res.next = ListNode(order[i])
            res = res.next
        
        return res_head

if __name__ == '__main__':

    List = [1,2,3,4,5]

    head = ListNode(List[0])
    current = head

    for i in range(1, len(List)):
        current.next = ListNode(List[i])
        current = current.next

    ans = Solution().oddEvenList(head)

    while ans:
        print(ans.val)
        ans = ans.next
