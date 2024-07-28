import csv
import hashlib

def hash_value(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def anonymize_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        header = next(reader)
        writer.writerow(header)
        
        for row in reader:
            row[0] = hash_value(row[0]) 
            row[1] = hash_value(row[1]) 
            row[2] = hash_value(row[2]) 
            
            writer.writerow(row)

input_csv = 'large_sample_data.csv'
output_csv = 'anonymized_large_sample_data.csv'
anonymize_csv(input_csv, output_csv)
print(f'Anonymized CSV file saved to {output_csv}')
