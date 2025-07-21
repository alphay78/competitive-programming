class Solution:
    def accountsMerge(self, accounts):
        parent = {}  # Union-Find parent map
        email_to_name = {}  # Map each email to its owner's name

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # Step 1: Initialize parent and email_to_name
        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                # Set the parent of email to itself if not seen before
                if email not in parent:
                    parent[email] = email
                # Map email to name
                email_to_name[email] = name
                # Union the first email with current one in the account
                union(first_email, email)

        # Step 2: Group emails by their root parent
        merged = defaultdict(list)
        for email in parent:
            root = find(email)
            merged[root].append(email)

        # Step 3: Build the result with name and sorted emails
        result = []
        for root_email, email_list in merged.items():
            name = email_to_name[root_email]
            result.append([name] + sorted(email_list))

        return result
