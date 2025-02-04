class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        my_dict = {}
        for i in cpdomains:
            count , domain = i.split(" ")
            count = int(count)
            lis = list(domain.split("."))
            var = lis[-1]
            my_dict[var] = my_dict.get(var, 0) + count

            for i in range(len(lis)-2,-1,-1):
                var = lis[i] + '.' + var
                my_dict[var] = my_dict.get(var, 0) + count

        res = []
        for key, val in my_dict.items():
            res.append(str(val) + " " + key)
            
        return res
                
