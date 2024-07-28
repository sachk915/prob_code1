
import csv
from faker import Faker

def generate_file(filename, num_rows):
    fake = Faker()
    with open(filename, 'w', encoding='utf-8') as file:
        for _ in range(num_rows):
            first_name = fake.first_name().ljust(10)
            last_name = fake.last_name().ljust(10)
            address = fake.address().replace('\n', ', ').ljust(30)
            date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d').ljust(10)
            
            line = f"{first_name}{last_name}{address}{date_of_birth}\n"
            file.write(line)
    print(f'{filename} generated with {num_rows} rows.')

generate_file('fixed_width_data.txt', num_rows=1000)
