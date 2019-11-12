class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, L1: ListNode, L2: ListNode) -> ListNode:

        L1Point = L1
        L2Point = L2
        AnswerNode = ListNode(0)
        AnswerPoint = AnswerNode

        while(L1Point != None or L2Point != None):

            tempSum = 0
            if((L1Point == None)&(L2Point!=None)):
                tempSum = L2Point.val + AnswerPoint.val
                L2Point = L2Point.next
            elif((L1Point!=None)&(L2Point == None)):
                tempSum = L1Point.val + AnswerPoint.val
                L1Point = L1Point.next
            elif((L1Point!=None)&(L1Point!=None)):
                tempSum = L1Point.val + L2Point.val + AnswerPoint.val
                L1Point = L1Point.next
                L2Point = L2Point.next

            if(tempSum>=10):
                AnswerPoint.val = (tempSum % 10)
                AnswerPoint.next = ListNode(int(tempSum/10))
            else:
                AnswerPoint.val = tempSum

            if((AnswerPoint.next == None)&(L1Point!=None)or(AnswerPoint.next == None)&(L2Point!=None)):
                AnswerPoint.next = ListNode(0)
                AnswerPoint = AnswerPoint.next
            else:
                AnswerPoint = AnswerPoint.next

        return AnswerNode


L1Node = ListNode(2)
L1Node.next = ListNode(4)
L1Node.next.next = ListNode(3)

L2Node = ListNode(5)
L2Node.next = ListNode(6)
L2Node.next.next = ListNode(4)

tempProblem = Solution()
rst = tempProblem.addTwoNumbers(L1Node,L2Node)
print(rst.val)
print(rst.next.val)
print(rst.next.next.val)