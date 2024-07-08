def checking_of_arithmetic_arranger(problems, problems_splited):
    error1 = False
    error2 = False
    error3 = False
    error4 = False
    # Checking whether the length of problems is greater than 5.
    if len(problems) > 5:
        error1 = True
    index_operator_checking = 1
    index_f_num = 0
    index_s_num = 2
    while index_f_num < len(problems_splited):
        operator_checking = problems_splited[index_operator_checking]
        f_num = problems_splited[index_f_num]
        s_num = problems_splited[index_s_num]
        # Checking whether the operators are addition (+) or subtraction (-).
        if operator_checking != "+" and operator_checking != "-":
            error2 = True
            break
        # Checking whether the first number or second number of the problem is a digit.
        elif not f_num.isdigit() or not s_num.isdigit():
            error3 = True
            break
        # Checking whether the length of the first number or the length of the second number of the problem is greater than 4.
        elif len(f_num) > 4 or len(s_num) > 4:
            error4 = True
            break
        index_operator_checking += 3
        index_f_num += 3
        index_s_num += 3
    # Returning errors
    if error1:
        return 'Error: Too many problems.'
    elif error2:
        return "Error: Operator must be '+' or '-'."
    elif error3:
        return 'Error: Numbers must only contain digits.'
    elif error4:
        return 'Error: Numbers cannot be more than four digits.'
    return None


def print_all_rows_of_arithmetic_arranger(problems_splited, table):
    # Printing all rows of arithmetic arranger.
    def print_first_row_of_arithmetic_arranger(problems_splited, table):
        # Printing the first row of all rows of arithmetic arranger.
        index_first_num_first_row = 0
        index_second_num_first_row = 2
        while index_first_num_first_row < len(problems_splited):
            first_num = problems_splited[index_first_num_first_row]
            second_num = problems_splited[index_second_num_first_row]
            if len(first_num) < len(second_num):
                if index_first_num_first_row == 0:
                    table += f"  {(abs(len(first_num) - (len(second_num)))) * ' '}{first_num}"
                else:
                    table += f"      {(abs(len(first_num) - (len(second_num)))) * ' '}{first_num}"
            if len(first_num) > len(second_num):
                if index_first_num_first_row == 0:
                    table += f"  {first_num}"
                else:
                    table += f"      {first_num}"
            if len(first_num) == len(second_num):
                if index_first_num_first_row == 0:
                    table += f"  {first_num}"
                else:
                    table += f"      {first_num}"
            index_first_num_first_row += 3
            index_second_num_first_row += 3
        return table

    def print_second_row_of_arithmetic_arranger(problems_splited, table):
        # Printing the second row of all rows of arithmetic arranger.
        table += "\n"
        index_first_num_second_row = 0
        index_second_num_second_row = 2
        index_operator = 1
        while index_first_num_second_row < len(problems_splited):
            first_num = problems_splited[index_first_num_second_row]
            second_num = problems_splited[index_second_num_second_row]
            operator = problems_splited[index_operator]
            if len(first_num) < len(second_num):
                if index_first_num_second_row == 0:
                    table += f"{operator} {second_num}"
                else:
                    table += f"    {operator} {second_num}"
            if len(first_num) > len(second_num):
                if index_first_num_second_row == 0:
                    table += f"{operator} {(abs(len(first_num) - (len(second_num)))) * ' '}{second_num}"
                else:
                    table += f"    {operator} {(abs(len(first_num) - (len(second_num)))) * ' '}{second_num}"
            if len(first_num) == len(second_num):
                if index_first_num_second_row == 0:
                    table += f"{operator} {second_num}"
                else:
                    table += f"    {operator} {second_num}"
            index_first_num_second_row += 3
            index_second_num_second_row += 3
            index_operator += 3
        return table

    def print_hyphens_row_of_arithmetic_arranger(problems_splited, table):
        # Printing the third row of all rows of arithmetic arranger.
        table += "\n"
        index_first_num_third_row = 0
        index_second_num_third_row = 2
        while index_first_num_third_row < len(problems_splited):
            first_num = problems_splited[index_first_num_third_row]
            second_num = problems_splited[index_second_num_third_row]
            if len(first_num) < len(second_num):
                if index_first_num_third_row == 0:
                    table += f"--{len(second_num) * '-'}"
                else:
                    table += f"    --{len(second_num) * '-'}"
            if len(first_num) > len(second_num):
                if index_first_num_third_row == 0:
                    table += f"--{len(first_num) * '-'}"
                else:
                    table += f"    --{len(first_num) * '-'}"
            if len(first_num) == len(second_num):
                if index_first_num_third_row == 0:
                    table += f"--{len(second_num) * '-'}"
                else:
                    table += f"    --{len(second_num) * '-'}"
            index_first_num_third_row += 3
            index_second_num_third_row += 3
        return table

    table = print_first_row_of_arithmetic_arranger(problems_splited, table)
    table = print_second_row_of_arithmetic_arranger(problems_splited, table)
    table = print_hyphens_row_of_arithmetic_arranger(problems_splited, table)
    return table


def put_hyphen_in_string(problems_splited, hyphen):
    # Putting a hyphen in the string.
    i_first_num_hyphen = 0
    i_second_num_hyphen = 2
    while i_first_num_hyphen < len(problems_splited):
        first_num = problems_splited[i_first_num_hyphen]
        second_num = problems_splited[i_second_num_hyphen]
        if i_first_num_hyphen == 0:
            if len(first_num) > len(second_num):
                hyphen += f"{2 * '-'}{int(len(first_num)) * '-'}"
            elif len(first_num) == len(second_num):
                hyphen += f"{2 * '-'}{int(len(first_num)) * '-'}"
            elif len(first_num) < len(second_num):
                hyphen += f"{2 * '-'}{int(len(second_num)) * '-'}"
        else:
            if len(first_num) > len(second_num):
                hyphen += f"    {2 * '-'}{int(len(first_num)) * '-'}"
            elif len(first_num) == len(second_num):
                hyphen += f"    {2 * '-'}{int(len(first_num)) * '-'}"
            elif len(first_num) < len(second_num):
                hyphen += f"    {2 * '-'}{int(len(second_num)) * '-'}"
        i_first_num_hyphen += 3
        i_second_num_hyphen += 3
    return hyphen


def print_answers_of_arithmetic_arranger(problems_splited, table, hyphen):
    # Printing answers of arithmetic arranger.
    table += "\n"
    i_first_num_fourth_row = 0
    i_second_num_fourth_row = 2
    i_operator_fourth_row = 1
    i = 0
    splited_hyphen = hyphen.split()
    while i_first_num_fourth_row < len(problems_splited):
        first_num = problems_splited[i_first_num_fourth_row]
        second_num = problems_splited[i_second_num_fourth_row]
        operator = problems_splited[i_operator_fourth_row]
        if operator == '+':
            answer = str(int(first_num) + int(second_num))
        else:
            answer = str(int(first_num) - int(second_num))
        if i_first_num_fourth_row == 0:
            table += f"{int(len(splited_hyphen[i]) - int(len(answer))) * ' '}{answer}"
        else:
            table += f"    {int(len(splited_hyphen[i]) - int(len(answer))) * ' '}{answer}"

        i_first_num_fourth_row += 3
        i_second_num_fourth_row += 3
        i_operator_fourth_row += 3
        i += 1
    return table


def arithmetic_arranger(problems, show_answers=False):
    # Printing result.
    problems_joined = " ".join(problems)
    problems_splited = problems_joined.split()
    # Checking for errors
    error = checking_of_arithmetic_arranger(problems, problems_splited)
    if error:
        return error

    table = ""
    hyphen = ""
    # Printing all rows of arithmetic arranger.
    table = print_all_rows_of_arithmetic_arranger(problems_splited, table)
    if show_answers:
        # Putting hyphen in the string.
        hyphen = put_hyphen_in_string(problems_splited, hyphen)
        # Printing answers of arithmetic arranger.
        table = print_answers_of_arithmetic_arranger(problems_splited, table, hyphen)
    return table


print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "13 + 495", "98 + 40"], True)}')
