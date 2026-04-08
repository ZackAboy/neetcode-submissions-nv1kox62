class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []
        self.follows[userId].add(userId)
        for person in self.follows[userId]:
            index = len(self.tweets[person]) - 1
            if index >= 0:
                count, tweet = self.tweets[person][index]
                heap.append((count, tweet, person, index-1))
        
        heapq.heapify(heap)
        while heap and len(res)<10:
            count, tweet, person, index = heapq.heappop(heap)
            res.append(tweet)
            if index>= 0:
                count, tweet = self.tweets[person][index]
                heapq.heappush(heap, (count, tweet, person, index-1))
            
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
