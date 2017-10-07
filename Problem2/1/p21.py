from os import path


PWD = path.dirname(path.abspath(__file__))
MAPPING = {
    'A': '10',
    'B': '11',
    'C': '12',
    'D': '13',
    'E': '14',
    'F': '15',
    'G': '16',
    'H': '17',
    'I': '34',
    'J': '18',
    'K': '19',
    'L': '20',
    'M': '21',
    'N': '22',
    'O': '35',
    'P': '23',
    'Q': '24',
    'R': '25',
    'S': '26',
    'T': '27',
    'U': '28',
    'V': '29',
    'W': '32',
    'X': '30',
    'Y': '31',
    'Z': '33',
}
WEIGHTED = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]


def main():
    with open(path.join(PWD, 'in.txt'), 'r') as f:
        f.readline()
        data = f.readlines()

    result = []
    for line in data:
        line = line.replace('\n', '')
        if len(line) != 10 or line[1] not in ['1', '2']:
            result.append('F')
            continue

        no = list(MAPPING[line[0]]) + list(line[1:])
        r = 0
        for i, j in zip(no, WEIGHTED):
            r += (int(i) * j)

        result.append('T' if r % 10 == 0 else 'F')

    with open(path.join(PWD, 'out.txt'), 'w') as f:
        f.write('\n'.join(result))


if __name__ == '__main__':
    main()
