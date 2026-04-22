#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])

    args = sys.argv[1:]
    args_len = len(args)

    if not args_len:
        print("No arguments provided!")
    else:
        print("Arguments received:", args_len)
        argi = 1
        for arg in args:
            print(f"Argument {argi}: {arg}")
            argi += 1

    print("Total arguments:", len(sys.argv))


if __name__ == "__main__":
    main()
