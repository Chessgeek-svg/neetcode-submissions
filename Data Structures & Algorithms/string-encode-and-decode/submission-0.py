class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            length = len(string)
            res += str(length) + "#" + string
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = j = 0
        while i < len(s):
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            string = s[i:j]
            res.append(string)
            i = j
        return res