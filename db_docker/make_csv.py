with open('./db/potential_users.csv', mode='w', encoding='utf-8') as file:
    for i in range(1, 501):
        line = f'{i},email{i}@gmail.com,name {i},surname {i},' \
               f'second_name {i},city {i}\n'
        file.write(line)
