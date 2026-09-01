class Solution:
    def minMoves(self, classroom, energy):

        m = len(classroom)
        n = len(classroom[0])

        start = 0
        litter = {}

        # Find S and L
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = r * n + c

                elif classroom[r][c] == 'L':
                    litter[r * n + c] = len(litter)

        k = len(litter)

        if k == 0:
            return 0

        target = (1 << k) - 1

        # queue: position, mask, remaining energy
        queue = [(start, 0, energy)]
        front = 0

        # Best energy seen for (position, mask)
        best = {}

        best[(start, 0)] = energy

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        moves = 0

        while front < len(queue):

            size = len(queue) - front

            for _ in range(size):

                pos, mask, e = queue[front]
                front += 1

                r = pos // n
                c = pos % n

                if mask == target:
                    return moves

                # If energy is 0, we cannot move
                if e == 0:
                    continue

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    new_pos = nr * n + nc
                    new_energy = e - 1
                    new_mask = mask

                    # Collect litter
                    if new_pos in litter:
                        new_mask |= 1 << litter[new_pos]

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    state = (new_pos, new_mask)

                    # Already reached this state with better energy
                    if state in best and best[state] >= new_energy:
                        continue

                    best[state] = new_energy

                    queue.append(
                        (new_pos, new_mask, new_energy)
                    )

            moves += 1

        return -1