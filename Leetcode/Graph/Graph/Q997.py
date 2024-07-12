'''
To find the town judge, we can use an algorithm that keeps track of the trust relationships using two arrays: one for the number of people each person trusts, and another for the number of people who trust each person. Here's the detailed plan:

Initialize two arrays:

trusts to count how many people each person trusts.
trusted_by to count how many people trust each person.
Iterate through the trust array:

For each trust relationship [a,b], increment trusts[a] and trusted_by[b].
Identify the judge:

The judge should be the person who trusts nobody (trusts[i] == 0) and is trusted by everyone else (trusted_by[i] == n - 1).
Return the judge's label if found, otherwise return -1.
'''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        trusts=[0]*(n+1)
        trusted_by=[0]*(n+1)

        for a,b in trust:
            trusts[a]+=1
            trusted_by[b]+=1

        for i in range(1,n+1):
            if trusts[i] == 0 and trusted_by[i] == n-1:
                return i

        return -1
