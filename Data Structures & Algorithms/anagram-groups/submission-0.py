class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        status = [True] * len(strs)

        for i in range(len(strs)):
            if not status[i]:
                continue

            temp = [strs[i]]
            status[i] = False
            counter_i = Counter(strs[i])

            for j in range(i + 1, len(strs)):
                if status[j] and Counter(strs[j]) == counter_i:
                    status[j] = False
                    temp.append(strs[j])

            result.append(temp)

        return result