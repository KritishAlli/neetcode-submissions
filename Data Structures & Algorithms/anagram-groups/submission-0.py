class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key: word sorted by char
        # val: list of indices it appears
        hmap = {}
        outlist = []
        for i in range (0, len(strs)):
            cur_str = strs[i]
            sorted_word = ''
            sorted_word = sorted_word.join(sorted(cur_str))

            if sorted_word in hmap.keys():
                hmap[sorted_word].append(i)
            else:
                hmap[sorted_word] = [i]
        for key, val in hmap.items():
            cur_list = []
            print (key, val)
            for index in val:
                cur_list.append(strs[index])
            outlist.append(cur_list)

        return outlist