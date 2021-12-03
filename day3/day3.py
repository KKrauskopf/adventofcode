lines = []
with open('/Users/krauskopf/projects/adventofcode/day3/input.txt') as f:
    for line in f.readlines():
        lines.append(line.strip())

# task 1
def func1():
    gamma = build_gamma_list(lines)

    gamma_sequence = build_gamma_sequence(gamma)

    gamma_chars = list(gamma_sequence)
    epsilon_sequence = build_epsilon_sequence(gamma_chars)

    return int(gamma_sequence,2) * int(epsilon_sequence,2)

def build_gamma_sequence(gamma):
    gamma_result = ""
    for row in gamma:
        gamma_result += most_common(row)
    return gamma_result

def build_epsilon_sequence(gamma):
    epsilon_result = ""
    for row in gamma:
        epsilon_result += least_common(row)
    return epsilon_result

def build_gamma_list(lines):
    gamma = []
    for i in range(0, len(lines[0])):
        row = []
        for line in lines:
            row.append(list(line)[i])
        gamma.append(row)
    return gamma

def most_common(list):
    if(list.count("1") >= list.count("0")):
        return "1"
    else:
        return "0"

def least_common(list):
    if(list.count("0") <= list.count("1")):
        return "0"
    else:
        return "1"

def most_common_xd(lst):
    return max(set(lst), key=lst.count)

# task 2
def func2() :
    gamma = build_gamma_list(lines)
    gamma_sequence = build_gamma_sequence(gamma)
    epsilon_sequence = build_epsilon_sequence(gamma)
    remaining_binaries = lines

    for i in range(len(gamma_sequence)):
        remaining_gamma = build_gamma_list(remaining_binaries)
        gamma_sequence = build_gamma_sequence(remaining_gamma)
        remaining_binaries = filter_values(remaining_binaries, i, gamma_sequence[i])
        if(len(remaining_binaries) <= 1):
            break

    ox_value = remaining_binaries[0]

    remaining_binaries = lines
    for i in range(len(epsilon_sequence)):
        remaining_gamma = build_gamma_list(remaining_binaries)
        epsilon_sequence = build_epsilon_sequence(remaining_gamma)
        remaining_binaries = filter_values(remaining_binaries, i, epsilon_sequence[i])
        if(len(remaining_binaries) <= 1):
            break

    co2_value = remaining_binaries[0]
    return int(ox_value,2) * int(co2_value,2)


def filter_values(remaining_binaries, index, gamma_value):
    result = []
    for binary in remaining_binaries:
        if(list(binary)[index] == gamma_value):
            result.append(binary)
    return result


print(func2())