class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_idx_map = {j:i  for i,j in enumerate(order)}

        for i in range(len(words)-1):
            if self.compare(words[i],words[i+1], order_idx_map):
                return False
        return True
        
    def compare(self,x,y,order_map):
        for i in range(len(x)):
            if i >= len(y):
                return True
            if order_map[x[i]] > order_map[y[i]]:
                return True
            if order_map[x[i]] < order_map[y[i]]:
                return False
        return False