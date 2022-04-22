"""
контекстный менеджер для работы с файлами
"""


class FileSession:
    """
    Class creates session for work with the wile
    """

    def __init__(self, file_name, mode='r', encoding='utf-8'):
        self.file_name = file_name
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, mode=self.mode,
                         encoding=self.encoding)
        return self

    def read_symbol(self):
        """
        Reads one symbol
        :return: str
        """
        return self.file.read(1)

    def read_line(self):
        """
        Reads one line
        :return: str
        """
        return self.file.readline()

    def read_buffer(self, num):
        """
        Reads few lines
        :return: [str]
        """
        if num > 0:
            buf = []
            for _ in range(num):
                buf.append(self.file.readline())
            return buf
        return None

    def write_symbol(self, symbol):
        """
        Writes one symbol to the file
        :param symbol: str
        """
        if len(symbol) > 1:
            self.file.write(symbol[0])
        else:
            self.file.write(symbol)

    def write_line(self, line):
        """
        Writes one line to the file
        :param line: str
        """
        self.file.write(line)
        self.file.write('\n')

    def write_buffer(self, buf):
        """
        Writes few lines to the file
        :param buf: [str]
        """
        for line in buf:
            self.file.write(line)
            self.file.write('\n')

    def __exit__(self, exception_type, exception_value, traceback):
        self.file.close()


if __name__ == '__main__':
    with FileSession('new.txt', 'w') as file:
        file.write_symbol('H')
        file.write_symbol('Haha')
        file.write_line('Hello, word')
        file.write_buffer(['Hello, word', 'dddsdasd'])

    with FileSession('new.txt', 'r') as file:
        print(file.read_symbol())
        print(file.read_line())
        print(file.read_buffer(5))

    with FileSession('new.txt', 'sdr') as file:
        print(file.read_symbol())
