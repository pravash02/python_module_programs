import fileinput


def delete_line(file_path, line_number):
    with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
        for line_index, line in enumerate(file, 1):
            if line_index != line_number:
                print(line, end='')


delete_line('del_fil.txt', 4)