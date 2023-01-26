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

        


        
        

