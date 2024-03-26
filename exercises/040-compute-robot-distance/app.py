def compute_robot_distance(movements):
    x, y = 0, 0

    for movement in movements:
        direction, steps = movement.split()
        steps = int(steps)

        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps
        else:
            raise ValueError(f"Invalid movement direction: {direction}")

    distance = round((x**2 + y**2)**0.5)

    return distance
