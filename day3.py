from fluentpy import _, each, lib

def most_frequent_bit(bits, on_tie_prefer='1'):
    counter = lib.collections.Counter(bits)._
    if counter['1'] == counter['0']:
        return counter[on_tie_prefer]
    return counter.most_common(1)[0][0]

@lib.functools.lru_cache._
def parse_input(input):
    return input.splitlines().star_call(zip).call(list)

int_from_binary_string = _(int).curry(_, 2)._

@lib.functools.lru_cache._
def gamma_rate(input):
    return (
        parse_input(input)
        .map(most_frequent_bit)
        .join()
        .to(int_from_binary_string)
    )

def epsilon_rate(input):
    gamma = gamma_rate(input)
    number_of_bits = gamma.bit_length()
    return gamma ^ (2 ** number_of_bits - 1)

def part1(input):
    return gamma_rate(input) * epsilon_rate(input)

def oxigen_generator_rating(input):
    # here part1 and part2 diverge, because I need to get rid of the input numbers I don't like and then dynamically generate the list of the n-th bit of them for most_frequent_bits
    def nth_bits(numbers, index):
        return numbers.map(each[index]._)
    numbers = input.splitlines()
    for index in range(numbers[0].len()._):
        indicator = most_frequent_bit(
            nth_bits(numbers, index),
            on_tie_prefer='1',
        )
        numbers = _(numbers).filter(
            each[index] == indicator
        ).call(list)
        if numbers.len()._ == 1:
            breakpoint()
            return numbers[0].to(int_from_binary_string)
    assert False, 'should always find a number'

def co2_scrubber_rating(input):
    return 10

def part2(input):
    return oxigen_generator_rating(input) * co2_scrubber_rating(input)

if __name__ == '__main__':
    lib.sys.exit(lib.pytest.main([__file__])._)

    print(part1(_(open('day3.txt').read())))

sample = _("""\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""")

def test_part1():
    assert part1(sample) == 198
    
def test_part2():
    assert oxigen_generator_rating(sample) == 23
    assert co2_scrubber_rating(sample) == 10
    assert part2(sample) == 230