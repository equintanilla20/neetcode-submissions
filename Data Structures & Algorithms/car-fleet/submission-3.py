class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], (target - position[i]) / speed[i]])
        
        cars.sort(key=lambda x: x[0], reverse=True)

        fleets = []
        for i in range(len(cars)):
            if not fleets or cars[i][1] > fleets[-1]:
                fleets.append(cars[i][1])
                
        return len(fleets)