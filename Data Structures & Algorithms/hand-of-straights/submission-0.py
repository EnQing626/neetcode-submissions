class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        cnts = Counter(hand)
        for start in sorted(cnts.keys()):
            while cnts[start]:
                for end in range(start, start + groupSize):
                    if not cnts[end]:
                        return False
                    cnts[end] -= 1
        return True