class MyHashMap:

    def __init__(self):
        self.map=[[-1]*1000 for _ in range(1001)]

    def put(self, key: int, value: int) -> None:
        row, col = key//1000, key%1000
        self.map[row][col]=value

    def get(self, key: int) -> int:
        row, col = key//1000, key%1000
        return self.map[row][col]

    def remove(self, key: int) -> None:
        row,col = key//1000, key%1000
        self.map[row][col]=-1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)