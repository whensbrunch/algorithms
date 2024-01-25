class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        start = 0
        most_frequent = 0
        max_len = 0
        for end, i in enumerate(s):
            # add the current character to the substring
            counter[i] = counter.get(i, 0) + 1

            # update the most frequent character in the substring
            most_frequent = max(most_frequent, counter[i])

            # if the length of the current substring requires more
            # substitutions than k:
            if (end - start + 1) - most_frequent > k:
                # move start in by one
                counter[s[start]] -= 1
                start += 1
            
            # update max length
            max_len = max(max_len, end-start+1)

        return max_len