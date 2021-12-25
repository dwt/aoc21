from functools import lru_cache
from pathlib import Path
from itertools import starmap

@lru_cache()
def read_input():
    return list(map(int, Path("day1.input.txt").read_text().splitlines()))

def windowed(iterable, window_size):
    # REFACT achieve the same effect using itertools.tee()
    iterable = list(iterable)
    def windows():
        yield iterable
        for start_index in range(1, window_size):
            yield iterable[start_index:]
    return zip(*windows())

def is_increase(first, second):
    return first < second

def first_part():
    # number_of_increasing_measurements
    windows = windowed(read_input(), 2)
    increases = starmap(is_increase, windows)
    return sum(increases)

def second_part():
    # number ofincreasing sums in sliding windows of size 3
    windows = windowed(read_input(), 3)
    sums = map(sum, windows)
    windows = windowed(sums, 2)
    increases = starmap(is_increase, windows)
    return sum(increases)    
    
## TESTS

from pyexpect import expect

def test_smoke():
    expect(read_input()).has_length(2000)

def test_first_part():
    expect(first_part()) == 1553

def test_windowed_input():
    windows = windowed(read_input(), 2)
    expect(next(windows)).has_length(2)

def test_second_part():
    expect(second_part()) == 1597

if __name__ == "__main__":
    import sys, pytest
    sys.exit(pytest.main([__file__]))
