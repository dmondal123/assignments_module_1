def groupAnagrams(self, strs):
        anamap = defaultdict(list)
        for word in strs:
            sort = ''.join(sorted(word))
            anamap[sort].append(word)
        return list(anamap.values())
