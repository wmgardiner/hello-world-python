"""Unit tests for helloworld.py."""

import unittest

from helloworld import generate_greetings


class TestHelloWorld(unittest.TestCase):
    def test_default_greetings(self) -> None:
        lines = generate_greetings()
        self.assertEqual(len(lines), 5)
        self.assertEqual(lines[0], "Hello, World! (Loop number 1)")
        self.assertEqual(lines[-1], "Hello, World! (Loop number 5)")

    def test_custom_name_and_count(self) -> None:
        lines = generate_greetings(name="GitHub", count=2)
        self.assertEqual(
            lines,
            [
                "Hello, GitHub! (Loop number 1)",
                "Hello, GitHub! (Loop number 2)",
            ],
        )

    def test_negative_count_raises(self) -> None:
        with self.assertRaises(ValueError):
            generate_greetings(count=-1)


    def test_uppercase_option(self) -> None:
        lines = generate_greetings(name="World", count=1, uppercase=True)
        self.assertEqual(lines, ["HELLO, WORLD! (LOOP NUMBER 1)"])


if __name__ == "__main__":
    unittest.main()
