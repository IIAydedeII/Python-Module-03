#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        string = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = string.split(",")

        try:
            x_str, y_str, z_str = parts
        except ValueError:
            print("Invalid syntax")
            continue

        coords = []
        for coord in [x_str, y_str, z_str]:
            try:
                coords.append(float(coord))
            except ValueError as e:
                print(f"Error on parameter '{coord}':", e)
                break
        else:
            return coords[0], coords[1], coords[2]


def calc_distance(
    first: tuple[float, float, float], second: tuple[float, float, float]
) -> float:
    return math.sqrt(
        (second[0] - first[0]) ** 2
        + (second[1] - first[1]) ** 2
        + (second[2] - first[2]) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===")
    print("")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print("Got a first tuple:", pos1)
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    print("Distance to center:", round(calc_distance(pos1, (0, 0, 0)), 4))
    print("")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    print(
        "Distance between the 2 sets of coordinates:",
        round(calc_distance(pos1, pos2), 4),
    )


if __name__ == "__main__":
    main()
