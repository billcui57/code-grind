# Design Underground System

## Link

https://leetcode.com/problems/design-underground-system/description/

## Where

Leetcode

## Difficulty

Medium

## Description

An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

Implement the UndergroundSystem class:

void checkIn(int id, string stationName, int t)
A customer with a card ID equal to id, checks in at the station stationName at time t.
A customer can only be checked into one place at a time.
void checkOut(int id, string stationName, int t)
A customer with a card ID equal to id, checks out from the station stationName at time t.
double getAverageTime(string startStation, string endStation)
Returns the average time it takes to travel from startStation to endStation.
The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning a check in at startStation followed by a check out from endStation.
The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.

## Solution Main Idea

Have a dict that uses (startStation,endStation) as key, keep track of cumulative time and n for each.
Have another dict that keeps track of the current station that each id is located at.
Use second dict to store time of getting on


## Code

```python
class UndergroundSystem:

    def __init__(self):
        # {
        #     (startStation, endStation): (cuml_time, n)
        # }
        self.time_tracker = dict()
        # {
        #     id:  (stationName, t)
        # }
        self.cur_stations = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cur_stations[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        cur_station_name, cur_station_t = self.cur_stations[id]
        self.cur_stations.pop(id)
        
        track = (cur_station_name, stationName)
        if track not in self.time_tracker:
            self.time_tracker[track] = (t-cur_station_t, 1)
        else:
            cum_t, cum_n = self.time_tracker[track]
            self.time_tracker[track] = (cum_t + t-cur_station_t, cum_n + 1)

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        cum_t, cum_n= self.time_tracker[(startStation,endStation)]
        return cum_t/cum_n
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
```
