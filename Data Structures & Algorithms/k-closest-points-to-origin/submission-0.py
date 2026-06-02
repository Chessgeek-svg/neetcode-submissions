class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceMap = {}

        for i in range(len(points)):

            euclid = self.euclid(points[i])
            while distanceMap.get(euclid):
                euclid += .00001
            distanceMap[euclid] = points[i]
        

        keys = list(distanceMap.keys())
        keys.sort()

        res = []
        for i in range(k):
            res.append(distanceMap[keys[i]])
        
        return res
    
    def euclid(self, xy: List[int]):
        return (math.sqrt(xy[0]**2 + xy[1]**2))