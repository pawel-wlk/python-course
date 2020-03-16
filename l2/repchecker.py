import sys
import hashlib
import os


class FileInfo:
    def __init__(self, filename):
        self.filename = filename
        self.size = os.path.getsize(filename)
        with open(filename, 'rb') as f:
            self.hash = hashlib.md5(f.read()).hexdigest()

    def __eq__(self, other):
        return isinstance(other, FileInfo) and self.hash == other.hash and self.size == other.size


def get_file_infos(dirname):
    for directory in os.walk(dirname):
        dirname, _, files = directory
        for filename in files:
            yield FileInfo(dirname + '/' + filename)


def repcheck(dirname):
    files = list(get_file_infos(dirname))
    print('---')
    for i, file in enumerate(files):
        repetitions = [f for f in files[i:] if file == f]
        if len(repetitions) > 1:
            for repetition in repetitions:
                files.remove(repetition)
                print(repetition.filename)
            print('---')


if __name__ == "__main__":
    repcheck(sys.argv[1])
