from os import path


PWD = path.dirname(path.abspath(__file__))


def main():
    with open(path.join(PWD, 'in.txt'), 'r') as f:
        f.readline()
        data = f.readlines()

    result = []
    for line in data:
        network_segment = []
        ip, mask = line.split(',')
        for ip_part, mask_part in zip(ip.split('.'), mask.split('.')):
            network_segment.append(str(int(ip_part) & int(mask_part)))

        result.append('.'.join(network_segment))

    with open(path.join(PWD, 'out.txt'), 'w') as f:
        f.write('\n'.join(result))


if __name__ == '__main__':
    main()
