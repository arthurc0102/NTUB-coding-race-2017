from os import path


PWD = path.dirname(path.abspath(__file__))


def main():
    with open(path.join(PWD, 'in.txt'), 'r') as f:
        f.readline()
        data = iter(f.readlines())

    result = []
    for user1, user2 in zip(data, data):
        user1 = set(user1.replace('\n', '').split(',')[1:])
        user2 = set(user2.replace('\n', '').split(',')[1:])
        result.append(str(len(user1 & user2)))

    with open(path.join(PWD, 'out.txt'), 'w') as f:
        f.write('\n'.join(result))


if __name__ == '__main__':
    main()
