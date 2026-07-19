class Solution:
    def reverseBits(self, n: int) -> int:
        stripped_bin = bin(n)[2:]
        answer = stripped_bin.zfill(32)[::-1]
        return int(answer, 2)