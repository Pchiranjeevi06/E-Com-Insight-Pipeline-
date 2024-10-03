# ecommerce_data_generator.py
from data_generator import generate_valid_record, generate_rogue_record, write_to_csv

if __name__ == "__main__":
    # Set the number of records
    num_records = 10000
    rogue_percentage = 0.02  # 2% rogue records
    
    # Call the function to write the data to a CSV file
    write_to_csv(num_records, rogue_percentage, 'E-Commerce_data.csv')
    
    print(f"{num_records} records have been generated with rogue records and saved to 'E-Commerce_data.csv'")
