OK = '\033[92m'
ERR = '\033[91m'
END = '\033[0m'


def print_ok(message):
    print(f'{message}\t\t{OK}OK {END}')


def print_error(message):
    print(f'{message}\t\t{ERR}ERROR {END}')


# `**kwargs` zbiera pozostałe argumenty do dict
def test(test_name, solution_function, correct_answer, **kwargs):
    answer = solution_function(**kwargs)  # rozwija kwargs do postaci `key1=val1,key2=val2,...`
    if answer == correct_answer:
        print_ok(test_name)
    else:
        print_error(f'{test_name}, wynik poprawny: {correct_answer}, odpowiedź: {answer}')


# test('test 1', max_element, correct_answer=2, lista=[2, 1], wykladnik=1)
