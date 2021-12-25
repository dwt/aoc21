from fluentpy import _, each, lib

parsers = {
    'forward': lambda distance: (0, distance),
    'down': lambda distance: (distance, 0),
    'up': lambda distance: (-distance, 0),
}

def parse(line):
    direction, distance = line.split(' ')
    return parsers[direction](int(distance))

def parsed(input_text):
    return _(input_text).splitlines().imap(parse)

def part1(input_text):
    position = parsed(input_text).istarmap(complex).sum()._
    return int(position.imag * position.real)

def part2(input_text):
    def reducer(state, change):
        depth, distance, aim = state
        aim_change, distance_change = change
        
        aim += aim_change
        distance += distance_change
        depth += aim * distance_change
        return depth, distance, aim

    depth, distance, aim = parsed(input_text).reduce(reducer, (0,0,0))
    return depth * distance

if __name__ == '__main__':
    input_text = lib.pathlib.Path('day2.txt').read_text()._
    print('part1:', part1(input_text))
    print('part2:', part2(input_text))
#    lib.sys.exit()

    lib.sys.exit(lib.pytest.main(['day2.py'])._)

sample = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

def test_part1():
    assert part1(sample) == 150

def test_part2():
    assert part2(sample) == 900