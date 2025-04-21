class Solution:    
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = set()
        
        def clear_email(email: str) -> str:
            amp = email.index('@')
            domain = email[amp + 1:]
            local = []
            for i in range(amp):
                if email[i] == '+':
                    break
                if email[i] == '.':
                    continue
                local.append(email[i])

            return ''.join(local) + '@' + domain
        
        for email in emails:
            uniques.add(clear_email(email))

        print(uniques)
            
        return len(uniques)
        