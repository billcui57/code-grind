class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        busesForStation = {}
        for i, route in enumerate(routes):
            for station in route:
                if station not in busesForStation:
                    busesForStation[station] = set()
                busesForStation[station].add(i)

        queue = []
        queue.append((source, 0))
        visited = set()
        for node, depth in queue:
            visited.add(node)
            if node == target:
                return depth
            for availableBus in busesForStation[node]:
                for station in routes[availableBus]:
                    if station not in visited:
                        queue.append((station, depth + 1))
                routes[availableBus] = []  # seen route, prune it
        return -1
