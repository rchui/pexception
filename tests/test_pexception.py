import unittest

import pexception

import fixtures


class PExceptionTest(unittest.TestCase):
    maxDiff = None

    def test_parse(self) -> None:
        """Check that the stack trace is parsed correctly."""

        observed = pexception.pexception._parse(fixtures.STACK)
        expected = fixtures.PARSED
        self.assertEqual(expected, observed)

    def test_format(self) -> None:
        """Check that the stack trace is formmated correctly."""

        observed = pexception.pexception._format(*fixtures.PARSED)
        expected = fixtures.FORMATTED
        self.assertEqual(expected, observed)
