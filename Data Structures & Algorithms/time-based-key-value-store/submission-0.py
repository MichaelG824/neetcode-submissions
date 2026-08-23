class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [(value, timestamp)]
        else:
            self.d[key].append((value, timestamp))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        count = len(self.d[key]) - 1
        arr = self.d[key]
        while count > -1:
            if arr[count][1] <= timestamp:
                return arr[count][0]
            count -= 1
        return ""

