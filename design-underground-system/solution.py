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