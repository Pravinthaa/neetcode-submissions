class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=[]
        stack=[]
        c=0
        cars=list(zip(position,speed))
        cars.sort(reverse=True)
        for pos,speed in cars:
            ti=(target-pos)/speed
            time.append(ti)
        for i in range(len(time)):
            if not stack or time[i]>stack[-1]:
                c+=1
                stack.append(time[i])
        return c
        
        