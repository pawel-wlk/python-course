import sys


def analyze_file(file: str):
    bytes_count = 0
    words_count = 0
    lines_count = 0
    max_line_len = 0

    with open(file, 'r') as f:
        for line in f:
            bytes_count += len(bytes(line, 'utf8'))
            words_count += len(line.split())
            lines_count += 1
            cur_line_len = len(line)
            if cur_line_len > max_line_len:
                max_line_len = cur_line_len

    print('bytes:', bytes_count)
    print('words:', words_count)
    print('lines:', lines_count)
    print('longest line:', max_line_len)


if __name__ == '__main__':
    analyze_file(sys.argv[1])
