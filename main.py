def split_line(line='', sep=' '):
    if line == '':
        return ['']

    result = []
    value = ''
    flag_quotation_marks = False

    for char in line:
        if char == '"':
            flag_quotation_marks = not flag_quotation_marks
        if char == sep and not flag_quotation_marks:
            result.append(value.strip('"'))
            value = ''
        else:
            value += char

    result.append(value.strip('"'))

    return result


def read_split_line_tests():
    example_1_line = 'Александр Александрович Александров,,2005,11'
    example_1_sep = ','
    example_1_res = ['Александр Александрович Александров', '', '2005', '11']

    print(split_line(example_1_line, example_1_sep), '\n', example_1_res)

    example_2_line = 'Евгений Сергеевич Дёмин;;'
    example_2_sep = ';'
    example_2_res = ['Евгений Сергеевич Дёмин', '', '']

    print(split_line(example_2_line, example_2_sep), '\n', example_2_res)

    example_3_line = 'Анна Павловна Иванова,"[запись 1, запись 2, запись 3]", ,2'
    example_3_sep = ','
    example_3_res = ['Анна Павловна Иванова', '[запись 1, запись 2, запись 3]', ' ', '2']

    print(split_line(example_3_line, example_3_sep), '\n', example_3_res)

    print('Все тесты прошли успешно!')


read_split_line_tests()
