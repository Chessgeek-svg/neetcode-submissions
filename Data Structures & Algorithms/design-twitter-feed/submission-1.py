class Twitter:

    def __init__(self):
        self.followingDict = {} # int : set()
        self.tweetList = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followingDict:
            self.followingDict[userId] = set()
        self.followingDict[userId].add(userId)
        self.tweetList.append([userId, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        tweetCount = 0
        i = len(self.tweetList) - 1
        newsFeed = []
        while i >= 0 and tweetCount < 10:
            if self.tweetList[i][0] in self.followingDict[userId]:
                newsFeed.append(self.tweetList[i][1])
                tweetCount += 1
            i -= 1
        return newsFeed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followingDict:
            self.followingDict[followerId] = set([followerId])
        self.followingDict[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followingDict and followeeId in self.followingDict[followerId] and followerId != followeeId:
            self.followingDict[followerId].remove(followeeId)
        
