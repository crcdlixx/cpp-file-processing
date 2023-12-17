def split_cpp_programs(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    program_number = 1
    program_lines = []
    for line in lines:
        if line.strip() == '':
            if program_lines:  # ��������зǿ�
                with open(f'{program_number}.cpp', 'w') as file:
                    file.writelines(program_lines)
                program_lines = []
                program_number += 1
        else:
            program_lines.append(line)

    # �������һ������
    if program_lines:
        with open(f'{program_number}.cpp', 'w') as file:
            file.writelines(program_lines)

    # ��ӡ�ļ�����
    print(f"Total number of files created: {program_number}")

# ʹ�ú���
split_cpp_programs('new_no_comments.md')
