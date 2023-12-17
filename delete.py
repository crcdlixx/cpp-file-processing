def remove_comments(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            # 检查是否存在行内注释
            if '//' in line:
                line = line[:line.index('//')] + '\n'

            file.write(line)

# 使用函数
remove_comments('old.txt', 'new_no_comments.txt')
