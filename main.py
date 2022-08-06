"""
* BAB37ZPR - Základy programování
* HW03 - Caesarova šifra
* Uploaded at 12.11.2021 13:07
* Score: 5/5
* Coding style chaged at 6.8.2022
"""
import sys


abcd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def main():
    code, overhear = get_code_overhear(sys.argv[1])
    if not check_input(code, overhear):
        return False

    with open('output.txt', 'w') as output_fd:
        if not output_fd:
            print("Error: can't open output file!")
            return False

        result = shift_code(code, get_shift_amount(code, overhear))
        output_fd.write(result)

    return True


def get_code_overhear(filename):
    with open(filename, 'r') as fd:
        lines = fd.readlines()
        # get code msg
        code = lines[0]
        code = code[:(len(code)-1)]
        # get overhear msg
        overhear = lines[1]

    return code, overhear


def get_shift_amount(code, overhear):
    match_counter = [[] for _ in range(len(abcd))]

    for i in range(len(abcd)):
        for j in range(len(code)):
            idx = abcd.index(code[j])
            if (abcd[(idx+i) % len(abcd)] == overhear[j]):
                match_counter[i].append(1)

    shift = match_counter.index((max(match_counter)))
    return shift


def shift_code(code, shift_amount):
    result = ''

    for i in range(len(code)):
        idx = abcd.index(code[i])
        result = result + ((abcd[(idx + shift_amount) % len(abcd)]))

    return result


def check_input(code, overhear):
    def check_input_by_abcd():
        for i in range(len(code)):
            try:
                abcd.index(code[i])
            except IndexError:
                pass
            except ValueError:
                return False
        for j in range(len(overhear)):
            try:
                abcd.index(overhear[j])
            except ValueError:
                return False
            except IndexError:
                pass
        return True

    def check_input_length():
        if (len(code) > len(overhear)) or (len(code) < len(overhear)):
            return False
        return True

    if not check_input_by_abcd():
        print('Error: Wrong input!')
        return False
    if not check_input_by_abcd() and not check_input_length():
        print('Error: Wrong input!')
        return False
    if not check_input_length():
        print('Error: Wrong input length!')
        return False

    return True


if __name__ == '__main__':
    main()
