class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_idx = collections.defaultdict(list)
        for i,account in enumerate(accounts):
            for email in account[1:]:
                email_to_idx[email].append(i)
        def dfs(i):
            for email in accounts[i][1:]:
                if email in email_set:
                    continue
                email_set.add(email)
                for j in email_to_idx[email]:
                    if not visited[j]:
                        visited[j]=True
                        dfs(j)
        result=[]
        visited=[False]*len(accounts)
        for i in range(len(accounts)):
            if not visited[i]:
                visited[i]=True
                email_set=set()
                dfs(i)
                result.append([accounts[i][0]]+sorted(email_set))
        return result