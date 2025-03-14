from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()  # Use a queue to store timestamps

    def ping(self, t: int) -> int:
        self.queue.append(t)  # Add new request
        while self.queue[0] < t - 3000:  # Remove outdated requests
            self.queue.popleft()
        return len(self.queue)  # Remaining requests in the last 3000 ms
