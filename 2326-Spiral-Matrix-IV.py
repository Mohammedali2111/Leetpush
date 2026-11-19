
class Solution:
    def spiralMatrix(self, m, n, head):
        matrix = [[-1] * n for _ in range(m)]

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        curr = head

        while curr:
            # Left to right
            for col in range(left, right + 1):
                if not curr:
                    break
                matrix[top][col] = curr.val
                curr = curr.next
            top += 1

            # Top to bottom
            for row in range(top, bottom + 1):
                if not curr:
                    break
                matrix[row][right] = curr.val
                curr = curr.next
            right -= 1

            # Right to left
            for col in range(right, left - 1, -1):
                if not curr:
                    break
                matrix[bottom][col] = curr.val
                curr = curr.next
            bottom -= 1

            # Bottom to top
            for row in range(bottom, top - 1, -1):
                if not curr:
                    break
                matrix[row][left] = curr.val
                curr = curr.next
            left += 1

        return matrix
