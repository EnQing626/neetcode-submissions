from typing import List

class Twitter:
    def __init__(self):
        self.users = {}      # userId -> set of followeeIds
        self.posts = []      # list of [userId, tweetId] in chronological order

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.append([userId, tweetId])
        if userId not in self.users:
            self.users[userId] = set()

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        
        following = self.users[userId]
        ids = {userId} | following          # include self + all followees
        
        tmp = []
        count = 10
        for post in reversed(self.posts):   # most recent first
            if count == 0:
                break
            if post[0] in ids:
                tmp.append(post[1])
                count -= 1
                
        return tmp

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:        # self-follow is usually no-op
            return
        if followerId not in self.users:
            self.users[followerId] = set()
        self.users[followerId].add(followeeId)   # set → automatic dedup

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].discard(followeeId)   # safe even if not present