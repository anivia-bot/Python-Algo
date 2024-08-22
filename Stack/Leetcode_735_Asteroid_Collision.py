'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, 
the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.
Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Solution:

Create a stack, iterate over the asteroids and add all positvie asteroids into the stack. If
we encouter a negative asteroid, use a while loop till we either find a bigger positive asteroid 
or negative asteroid or an asteroid with the same size. The point is to use a stack to keep track
of the state of the asteroids.
'''

class Solution:
    def asteroidCollision(self, asteroids):
        
        stack = []

        for a in asteroids:

            # if no asteroid in the stack we add one
            if not stack:
                stack.append(a)
                continue

            if a < 0:
                
                # if the negative asteroid is greater, pop till we hit either a negative or 
                # a postive asteroid that is greater than the current negative asteroid
                while stack and stack[-1] > 0 and stack[-1] < abs(a):
                    stack.pop()
                # If the positive asteroid is greater, we do nothing, stack remain the same
                if stack and stack[-1] > 0 and stack[-1] > abs(a):
                    continue
                # If two positive and negative asteroid have the same weight then we destroy
                # the asteroids
                if stack and stack[-1] > 0 and stack[-1] == abs(a):
                    stack.pop()
                    continue
                # If neither case happened, simply just add the asteroid.
                stack.append(a)
            else:
                stack.append(a)

        return stack