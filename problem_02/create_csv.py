import csv
from faker import Faker

def generate_csv(filename, num_rows):
    fake = Faker()
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(['first_name', 'last_name', 'address', 'date_of_birth'])
        for _ in range(num_rows):
            writer.writerow([
                fake.first_name(),
                fake.last_name(),
                fake.address().replace('\n', ', '),  
                fake.date_of_birth(minimum_age=18, maximum_age=80)
            ])
    print(f'{filename} generated with {num_rows} rows.')

generate_csv('/problem_02/large_sample_data.csv', num_rows=1000000)

