class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for strin in strs:
            strInfo = f"{len(strin)}#{strin}"
            res = res + strInfo

        return res

    def decode(self, s: str) -> List[str]:

        res = []
        word = 0

        while word < len(s):
            char = word

            while s[char] != "#":
                char += 1
            length = int(s[word:char])
            res.append(s[char + 1 : char + length + 1])
            word = char + length + 1
        return res