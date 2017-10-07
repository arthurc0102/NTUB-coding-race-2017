from os import path


PWD = path.dirname(path.abspath(__file__))


def main():
    with open(path.join(PWD, 'in.txt'), 'r') as f:
        f.readline()
        data = f.readlines()

    result = []
    for line in data:
        number_in_line = [word for word in line if word.isdigit()]
        result.append(''.join(number_in_line) if number_in_line else 'N')

    with open(path.join(PWD, 'out.txt'), 'w') as f:
        f.write('\n'.join(result))


if __name__ == '__main__':
    main()
