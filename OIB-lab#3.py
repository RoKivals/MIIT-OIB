from constants import *

contour1 = get_contour()
contour2 = get_contour()
contour3 = get_contour()
arr_contour = (contour1, contour2, contour3)


def encryption(text: str, sequence: list, period: list) -> str:
    sequence_num = 0  # Индекс текущей очереди
    curr_period = period[sequence_num]  # Текущее значение периода
    curr_alp = 0  # Текущий алфавит
    for i in range(len(text)):
        if curr_period == 0:
            sequence_num = (sequence_num + 1) % len(sequence)
            curr_period = period[sequence_num]
            curr_alp = 0
        curr_contour = sequence[sequence_num]
        curr_alp %= len(arr_contour[curr_contour])
        text = text[0:i] + text[i::].replace(text[i], arr_contour[curr_contour][curr_alp][alphabet.index(text[i])], 1)
        curr_period -= 1
        curr_alp += 1
    return text


def decryption(text: str, sequence: list, period: list) -> str:
    sequence_num = 0
    curr_period = period[sequence_num]
    flag = 0
    for i in range(len(text)):
        if curr_period == 0:
            sequence_num = (sequence_num + 1) % len(sequence)
            curr_period = period[sequence_num]
            flag = 0
        curr_contour = sequence[sequence_num]
        curr_alp = flag % len(arr_contour[curr_contour])
        text = text[0:i] + text[i::].replace(text[i], alphabet[arr_contour[curr_contour][curr_alp].index(text[i])], 1)
        curr_period -= 1
        flag += 1
    return text


def main():
    text = input("Введите сообщение для шифрования: ")
    sequence = [int(i) - 1 for i in input("Введите порядок использования контуров: ").strip().split()]
    period = [int(i) for i in input("Введите период использования каждого контура: ").strip().split()]
    coded_text = encryption(text, sequence, period)
    print(f"Зашифрованное сообщение имеет вид: {coded_text}")
    print(f"Дешифрованное сообщение имеет вид: {decryption(coded_text, sequence, period)}")


if __name__ == "__main__":
    main()
