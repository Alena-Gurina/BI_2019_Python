# 1. Составить список из чисел от 1 до 1000, которые имеют в своём составе 7.
with_7 = [i for i in range(1, 1001) if '7' in str(i)]
# print(with_7)

# 2. Взять предложение
# Would it save you a lot of time if I just gave up and went mad now?
# и сделать его же без гласных. up: можно оставить в виде списка слов и не собирать строку.
sent = "Would it save you a lot of time if I just gave up and went mad now?"
no_v = ''.join([i for i in sent if i not in 'aeiouAIEOU'])
# print(no_v)
# P.S. я не относила y к гласным, но нет никаких проблем в том чтобы его добавить в проверочную строку

# 3. Для предложения
# **The ships hung in the sky in much the same way that bricks don't**
# составить словарь, где слову соответствует его длина.
sent = "The ships hung in the sky in much the same way that bricks don't"
len_dict = {i: len(i) for i in sent.split()}
# print(len_dict)

# 4*. Для чисел от 1 до 1000 наибольшая цифра, на которую они делятся (1-9).
dict_div_numb = {i: j for j in range(1, 10) for i in range(1, 1001) if i % j == 0}
# print(dict_div_numb)

# 5*. Список всех чисел от 1 до 1000, не имеющих делителей среди чисел от 2 до 9.
l_no_div = [i for i in range(1, 1001) if sum(0 if i % j != 0 else 1 for j in range(2, 10)) < 1]
# print(l_no_div)
