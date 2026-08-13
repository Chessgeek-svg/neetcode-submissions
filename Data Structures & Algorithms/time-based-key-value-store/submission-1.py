class TimeMap:

    def __init__(self):
        self.dictionary = defaultdict(list)    

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        return_val = ""
        val_array = self.dictionary[key]

        left, right = 0, len(val_array) - 1
        while left <= right:
            mid = (left + right) // 2
            if val_array[mid][0] <= timestamp:
                return_val = val_array[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return return_val
