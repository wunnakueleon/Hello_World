from collections import deque


class BFS():

    def path_finding(self, start, end, valid_positions, obstacles):
        queue = deque([start])
        visited = set([start])
        

        for each_segment_position in obstacles:
            visited.add(each_segment_position)

        node_coordinates = {}

        while queue:
            current = queue.popleft()

            if current == end:
                path = []

                step = end
                
                while step != start:
                    path.append(step)
                    step = node_coordinates[step]

                path.append(start)
                path.reverse()
                return path

            x, y = current
            neighbours = [
                (int(x + 20), int(y)), # East
                (int(x -20), int(y)), # West
                (int(x), int(y + 20)), # North
                (int(x), int(y - 20)) # South
            ]

            for neighbour in neighbours:

                if neighbour in valid_positions and neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    node_coordinates[neighbour] = current

        return None

