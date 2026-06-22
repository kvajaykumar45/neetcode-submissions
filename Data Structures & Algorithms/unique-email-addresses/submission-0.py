class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        count = 0
        ans = set()
        for each in emails:
            local, domain = each.split('@')
            flocal = ""
            for ch in local:
                if ch == ".":
                    continue
                elif ch == '+':
                    break
                else:
                    flocal += ch
            ans.add(flocal+"@"+domain)
        return len(ans)