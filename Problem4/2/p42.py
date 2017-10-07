from os import path


PWD = path.dirname(path.abspath(__file__))
MAPPING = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
}


def main():
    with open(path.join(PWD, 'in.txt'), 'r') as f:
        f.readline()
        data = f.readlines()

    result = []
    for line in data:
        result.append(''.join(
            [MAPPING.get(word) for word in line.replace('\n', '').split(',')]
        ))

    with open(path.join(PWD, 'out.txt'), 'w') as f:
        f.write('\n'.join(result))


if __name__ == '__main__':
    main()
