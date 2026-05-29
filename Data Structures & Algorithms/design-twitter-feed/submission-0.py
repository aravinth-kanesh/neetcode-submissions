class Twitter:
    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list) # posts are aggregrated by user
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        self.follow(userId, userId) # user sees their own posts too

        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(heap, (count, tweetId, followeeId, index - 1))

        while heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(heap, (count, tweetId, followeeId, index - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)