# zadanie: mając daną listę (np kursów akcji) znaleźć jakwiększy procentowy wzrost dzienny,
# czyli największy stosunek w[t+1]/w[t]
from tester import test


def largest_jump(lista):
    return 1


# test('test 1', max_element, correct_answer=2, lista=[2, 1])
test('test1', largest_jump, correct_answer=2, lista=[1, 2])
test('test2', largest_jump, correct_answer=4, lista=[1, 2, 8])
test('test3', largest_jump, correct_answer=1, lista=[4, 2, 2])
