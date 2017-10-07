from os import path


PWD = path.dirname(path.abspath(__file__))
MAPPING = {
    '00': 'A',
    '01': 'B',
    '100': '0',
    '101': '1',
    '1100': '2',
    '1101': '3',
    '11100': '4',
    '11101': '5',
    '111100': '6',
    '111101': '7',
    '111110': '8',
    '111111': '9',
}


def main():
    with open(path.join(PWD, 'in.txt'), 'r') as f:
        f.readline()
        data = f.readlines()

    result = []
    for line in data:
        start = 0
        line = line.replace('\n', '')
        r = ''
        for end in range(2, len(line) + 1):
            tmp = MAPPING.get(line[start:end])
            if tmp is None:
                continue
            r += tmp
            start = end
        result.append(r[0:4] + ',' + r[4:])

    with open(path.join(PWD, 'out.txt'), 'w') as f:
        f.write('\n'.join(result))


if __name__ == '__main__':
    main()
