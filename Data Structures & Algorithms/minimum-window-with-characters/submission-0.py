class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        excess = defaultdict(int)
        original_keys = set(t)
        res = s + t
        left = 0
        for right in range(len(s)):
            #If needed, subtract 1 from the total of that char needed
            if s[right] in need:
                need[s[right]] -= 1
                if need[s[right]] == 0:
                    del need[s[right]]
            #If not currently needed, but part of OG keys, track the extras that are in the curr string
            elif s[right] in original_keys:
                excess[s[right]] += 1

            while not need:
                #Update res if new answer is shorter
                if right - left + 1 < len(res):
                    res = s[left:right + 1]
                #If left pointer points to an extra character, take from the extras first
                if s[left] in excess:
                    excess[s[left]] -= 1
                    if excess[s[left]] == 0:
                        del excess[s[left]]
                #If no extras, put one back on the need for that char
                elif s[left] in original_keys:
                    need[s[left]] = 1
                left += 1
            
        return res if res != s+t else ""