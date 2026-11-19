
class Solution:
    def sortedListToBST(self, head):
        def getLength(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count

        n = getLength(head)

        def build(size):
            nonlocal head

            if size <= 0:
                return None

            left = build(size // 2)

            root = TreeNode(head.val)
            root.left = left

            head = head.next

            root.right = build(size - size // 2 - 1)

            return root

        return build(n)
