from tester import test


# zadanie: wyznaczyć maksymalny element listy
def max_element(lista):
    return max(lista)


# zadanie: wyznaczyć maksymalną wartość a[i]**wykladnik dla elementów listy
def max_power(lista, wykladnik):
    return max([i**wykladnik for i in lista])


test('test 1', max_element, correct_answer=2, lista=[2, 1])
test('test 2', max_element, correct_answer=2, lista=[1, 2])
test('test 3', max_element, correct_answer=2, lista=[2])
test('test 4', max_element, correct_answer=-1, lista=[-1, -2, -3])

test('test p1', max_power, correct_answer=4, lista=[2, 1], wykladnik=2)
test('test p2', max_power, correct_answer=8, lista=[-2, 2], wykladnik=3)
test('test p3', max_power, correct_answer=2, lista=[2], wykladnik=1)
test('test p4', max_power, correct_answer=-1, lista=[-1, -2, -3], wykladnik=3)
