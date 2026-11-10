class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for x in asteroids:
            if x>0:
                st.append(x)
                continue
            while st and st[-1]>0:
                top=st[-1]
                if top<=-x:
                    st.pop()
                if top>=-x:
                    break
            else:
                st.append(x)
        return st