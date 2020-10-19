# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKCYAN = '\033[96m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
OK = '\033[92m'
ERR = '\033[91m'
END = '\033[0m'


def print_ok(message):
    print(f'{message} {OK} OK {END}')


def print_error(message):
    print(f'{message} {ERR} ERROR {END}')


if __name__ == '__main__':
    print_ok('test1')
    print_error('test2')
