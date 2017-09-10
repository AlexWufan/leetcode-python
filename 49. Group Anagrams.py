class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        lib = {}
        res = []
        i = 0
        for x in strs:
            key = tuple(sorted(x))
            if key not in lib:
                lib[key] = i
                i+=1
                res.append([x])
            else:
                res[lib[key]].append(x)
                
        return res


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        lib = collections.defaultdict(list)
        for x in strs:
            key = tuple(sorted(x))
            lib[key].append(x)
                
        return lib.values()