def remove_comments(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            # ����Ƿ��������ע��
            if '//' in line:
                line = line[:line.index('//')] + '\n'

            file.write(line)

# ʹ�ú���
remove_comments('old.txt', 'new_no_comments.txt')
