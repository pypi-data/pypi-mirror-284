from collections.abc import Generator
from typing import Protocol

from genpnize.iter_recipes import grouper


def chop_text(text: str, n: int) -> Generator[str, None, None]:
    for chunk in grouper(text, n, fillvalue=""):
        yield "".join(chunk)


class Producer(Protocol):
    def write_lines(self, text: str) -> Generator[str, None, None]: ...


class GenP:
    letter_count = 13
    conversion = {"!": "!", "?": "?", "！": "!", "？": "?"}

    def write_lines(self, text: str) -> Generator[str, None, None]:
        iterator = chop_text(text.replace("\n", ""), self.letter_count)
        current_line = next(iterator)
        while next_line := next(iterator, ""):
            if next_line in self.conversion:  # next_line is a last line
                yield current_line + self.conversion[next_line]
                break
            else:
                yield current_line
                current_line = next_line
        if next_line == "":  # returns "" instead of StopIteration
            yield current_line
