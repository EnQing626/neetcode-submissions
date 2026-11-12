class Twitter:

    def __init__(self):
        self.users={}
        self.posts=[]

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId]=set()
        self.posts.append([userId,tweetId])
        
    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        following=self.users[userId]
        temp_users={userId}|following
        n=10
        news_feed=[]
        for post in reversed(self.posts):
            if n==0:
                return news_feed
            if post[0] in temp_users:
                news_feed.append(post[1])
                n-=1
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId==followeeId:
            return
        if followerId not in self.users:
            self.users[followerId]=set()
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].discard(followeeId)
