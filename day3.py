from fluentpy import _, each, lib

def extract_bit_by_frequency(bit_string, on_tie_prefer, index):
    counter = lib.collections.Counter(bit_string)._
    if counter['1'] == counter['0']:
        return on_tie_prefer
    return counter.most_common(2)[index][0]

def most_frequent_bit(bits):
    return extract_bit_by_frequency(bits, '1', 0)

def least_frequent_bit(bits):
    return extract_bit_by_frequency(bits, '0', 1)

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

def part2_extraction_rules(input, indicator_extractor):
    def nth_bits(numbers, index):
        return numbers.map(each[index]._)
    
    numbers = input.splitlines()
    for index in numbers[0].len().call(range):
        # needs to be least_frequent_bit
        indicator = indicator_extractor(nth_bits(numbers, index))
        numbers = _(numbers).filter(each[index] == indicator).call(list)
        if numbers.len()._ == 1:
            return numbers[0].to(int_from_binary_string)
    
    assert False, 'should always find a number'

def oxigen_generator_rating(input):
    return part2_extraction_rules(input, indicator_extractor=most_frequent_bit)

def co2_scrubber_rating(input):
    return part2_extraction_rules(input, indicator_extractor=least_frequent_bit)

def part2(input):
    return oxigen_generator_rating(input) * co2_scrubber_rating(input)

if __name__ == '__main__':
    lib.pytest.main([__file__])

    input = _(open('day3.txt')).read()
    print('part1:', part1(input))
    print('part2:', part2(input))

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

def _test_part1():
    assert part1(sample) == 198
    
def test_part2():
    # assert oxigen_generator_rating(sample) == 23
    assert co2_scrubber_rating(sample) == 10
    # assert part2(sample) == 230