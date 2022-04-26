class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        
        for string in strs:
            sortedString = "".join(sorted(string))
            
            if sortedString not in groups:
                groups[sortedString] = [string]
            else:
                groups[sortedString].append(string)
        
        result = []
        
        for sortedString in groups:
            result.append(groups[sortedString])
        
        return result