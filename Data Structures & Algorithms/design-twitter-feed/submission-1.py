class Twitter:
    def __init__(self):
        self.count = 0 # decrement each time for min heap ordering
        self.tweets = defaultdict(list) # userId -> [(count, tweetId)]
        self.following = defaultdict(set) # userId -> {followeeId, ...}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res, heap = [], []

        # iterate through all followers, including themselves
        for followeeId in self.following[userId] | {userId}:
            # check if those followers have posts
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1 # accesses most recent post
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(heap, (count, tweetId, followeeId, index - 1))

        while heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)

            if index >= 0: # access next most recent post from that followee
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(heap, (count, tweetId, followeeId, index - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
