'''
There are n cars going to the same destination along a one-lane road. The destination is target miles away.
You are given two integer array position and speed, both of length n, 
where position[i] is the position of the ith car and speed[i] 
is the speed of the ith car (in miles per hour).
A car can never pass another car ahead of it, but it can catch up to it and 
drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. 
The distance between these two cars is ignored (i.e., they are assumed to have the same position).
A car fleet is some non-empty set of cars driving at the same position and same speed. 
Note that a single car is also a car fleet.
If a car catches up to a car fleet right at the destination point, 
it will still be considered as one car fleet.
Return the number of car fleets that will arrive at the destination.

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
'''

'''
The challenging part for this problem is to recognize that
we need to look backward from the last car to the first car
identify the time it takes to reach the target line
if the following car takes less time to reach the target line
then it will be merge into a car fleet thus we pop the time from the stack
since it will be merge into the same velocity of the slow car and we will only be camparing
the slow car with the remaining trailing cars

we need to sort the array based on the position (O(nlogn))

steps:
combine both position and speed (makes it easier when we sort based on the position)
sort the list based on position.

iterate the list backwards and calculate the time it takes to reach the target line
append the time into the carfleet stack
if the stack has at least 2 cars, pop the car that will merge into one carfleet
since the slower car will be representing 

In sum, think of it in terms of time. How much time does it need to get to the target destination.
iterate in reverse (start from the final car and traverse all the way to the first car). If the time
is less than the previous car in the stack, it means that cars will collide. if the time is much greater
than the previous car in the stack, it means that it might form a new car fleet.
'''

class Solution:
    def carFleet(self, target: int, position, speed):

        # Time complexity would be O(NlogN) due to sorting
        # Space complexity would be O(N)

        pair = []
        for i in range(len(position)):
            pair.append([position[i], speed[i]])
        pair.sort()
        stack = []

        for pos, speed in reversed(pair):
            dis = target - pos
            time = dis / speed
            if not stack:
                stack.append(time)
                continue
            if stack and stack[-1] < time:
                stack.append(time)
                
        return len(stack)