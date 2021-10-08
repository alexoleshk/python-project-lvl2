import argparse
import json

def gen_str(dict, key, char):
    return '\n  {} {}: {}'.format(char, key, dict[key])

def generate_diff(file_path1, file_path2):
    first_file = json.load(open(file_path1))
    second_file = json.load(open(file_path2))

    result = '{'
    first_set = set(first_file)
    second_set = set(second_file)
    union = list(first_set | second_set)
    union.sort()
    intersection = first_set & second_set

    for key in union:
        if key in first_set - second_set:
            result += gen_str(first_file, key, '-')
        elif key in intersection:
            if first_file[key] == second_file[key]:
                result += gen_str(first_file, key, ' ')
            else:
                result += gen_str(first_file, key, '-')
                result += gen_str(second_file, key, '+')
        else:
            result += gen_str(second_file, key, '+')

    result += '\n}'
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))