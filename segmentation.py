def split_cpp_programs(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    program_number = 1
    program_lines = []
    for line in lines:
        if line.strip() == '':
            if program_lines:  # 如果程序行非空
                with open(f'{program_number}.cpp', 'w') as file:
                    file.writelines(program_lines)
                program_lines = []
                program_number += 1
        else:
            program_lines.append(line)

    # 保存最后一个程序
    if program_lines:
        with open(f'{program_number}.cpp', 'w') as file:
            file.writelines(program_lines)

    # 打印文件数量
    print(f"Total number of files created: {program_number}")

# 使用函数
split_cpp_programs('new_no_comments.md')
