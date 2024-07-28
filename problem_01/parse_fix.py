import csv

def parse_fix(input_file, output_file):
    field_specs = {
        'first_name': (0, 10),
        'last_name': (10, 20),
        'address': (20, 50),
        'date_of_birth': (50, 60)
    }
    
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = infile
        writer = csv.writer(outfile)
        
        writer.writerow(field_specs.keys())
        
        for line in reader:
            first_name = line[field_specs['first_name'][0]:field_specs['first_name'][1]].strip()
            last_name = line[field_specs['last_name'][0]:field_specs['last_name'][1]].strip()
            address = line[field_specs['address'][0]:field_specs['address'][1]].strip()
            date_of_birth = line[field_specs['date_of_birth'][0]:field_specs['date_of_birth'][1]].strip()
            
            writer.writerow([first_name, last_name, address, date_of_birth])

parse_fix('fixed_width_data.txt', 'output_data.csv')
