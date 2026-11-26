"""Simple greeting CLI with configurable name and repeat count."""

import argparse
from typing import List, Optional


def generate_greetings(name: str = "World", count: int = 5, uppercase: bool = False) -> List[str]:
    if count < 0:
        raise ValueError("count must be non-negative")
    lines = [f"Hello, {name}! (Loop number {i + 1})" for i in range(count)]
    return [line.upper() for line in lines] if uppercase else lines


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Print greeting lines.")
    parser.add_argument("--name", default="World", help="Name to greet (default: World).")
    parser.add_argument("--count", type=int, default=5, help="Number of iterations (default: 5).")
    parser.add_argument("--uppercase", action="store_true", help="Output greetings in uppercase.")
    args = parser.parse_args(argv)

    for line in generate_greetings(name=args.name, count=args.count, uppercase=args.uppercase):
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
