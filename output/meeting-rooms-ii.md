# Meeting Rooms II

## Link

https://leetcode.com/problems/meeting-rooms-ii/description/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

## Solution Main Idea

Sort intervals by starttime. Have a minheap on endtime, where it represents the list of rooms. Top of heap is therefore most likely to be free. Add to heap a new room if no room free


## Code

```python
class Solution:

    def isOverlapping(self,a,b):
        return not ((a[1] < b[0]) or (b[1] < a[0]))
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals = list(sorted(intervals, key = lambda x : x[0]))

        rooms = []

        heapq.heappush(rooms, intervals[0][1])

        for i in range(1,len(intervals)):
            room_end = heapq.heappop(rooms)
            if intervals[i][0] < room_end:
                heapq.heappush(rooms,room_end)
                heapq.heappush(rooms, intervals[i][1])
            else:
                heapq.heappush(rooms, intervals[i][1])
        
        return len(rooms)

        


        
        


```
