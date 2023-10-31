class Solution:
    def smallestMissingValueSubtree(self, parents: list[int], nums: list[int]) -> list[int]:
        """
        copy copy
        """
        n = len(parents)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)

        res = [1 for _ in range(n)]
        def dfs(node):
            geneSet = {nums[node]}
            for child in children[node]:
                childGeneSet, y = dfs(child)
                res[node] = max(res[node], y)
                if len(childGeneSet) > len(geneSet):
                    geneSet, childGeneSet = childGeneSet, geneSet
                geneSet.update(childGeneSet)
            while res[node] in geneSet:
                res[node] += 1
            return geneSet, res[node]
        
        dfs(0)
        return res

