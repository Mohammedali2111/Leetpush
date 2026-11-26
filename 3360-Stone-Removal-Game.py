class Solution:
    def canAliceWin(self, n: int) -> bool:
        move = 10
        alice = True

        while n >= move:
            n -= move
            move -= 1
            alice = not alice

        return not alice