
str = 'X-DSPAM-Confidence:0.8475'
col_pos = str.find(':')
piece = str[col_pos + 1:]
value = float(piece)
count = 0
sum_value = 0

while True:
    str = input('Enter properly formatted string or type "quit": ')
    if 'Confidence' in str:
        col_pos = str.find(':')
        piece = str[col_pos + 1:]
        value = float(piece)
        sum_value += value
        count += 1
    else:
        if str == 'quit' or str == 'QUIT':
            if count != 0:
                print('Average: ', sum_value/count)
                exit()
            else:
                if count == 0:
                    exit()
                print('String not the right format')
                continue
