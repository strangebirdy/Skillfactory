import numpy as np

number = np.random.randint(1, 101)  # Загадали число
print("Загадано число от 1 до 100")


def game_core_v3(number):
    """Сначала создаём список из чисел от 1 до 100,
    а затем последовательно сравниваем наше число number со средним элементом списка,
    сдвигая список влево или вправо, в зависимости от значения числа number"""
    predict_ls = []
    for i in range(1, 101):
        predict_ls.append(i)

    mid_elem = len(predict_ls) // 2  # Определяем средний элемент списка
    left_elem = 0
    right_elem = len(predict_ls) - 1

    count = 1

    while predict_ls[mid_elem] != number and left_elem <= right_elem:
        count += 1
        if number > predict_ls[mid_elem]:
            left_elem = mid_elem + 1
        else:
            right_elem = mid_elem - 1
        mid_elem = (left_elem+right_elem) // 2

    return count  # Выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # Фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


print(score_game(game_core_v3))
