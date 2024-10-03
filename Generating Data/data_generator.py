import csv
import random
from ecommerce_utils import fake, product_categories, product_names_mapping, countries, websites, payment_type_choices

def generate_valid_record():
    """Generates a valid e-commerce record according to the specified schema."""
    order_id = fake.random_number(digits=6)
    customer_id = fake.random_number(digits=6)
    customer_name = fake.name()
    product_id = fake.random_number(digits=6)
    product_category = random.choice(product_categories)
    product_name = random.choice(product_names_mapping[product_category])
    payment_type = fake.random_element(payment_type_choices)  # Types: Card, Internet Banking, UPI, Wallet
    qty = random.randint(1, 1000)
    price = round(random.uniform(5.0, 1000.0), 2)  # Price range between 5 and 1000
    datetime = fake.date_time_between(start_date='-1y', end_date='now').strftime("%Y-%m-%d %H:%M")
    country = random.choice(list(countries.keys()))
    city = random.choice(countries[country])
    ecommerce_website_name = random.choice(websites)
    payment_txn_id = fake.uuid4().split('-')[0]
    payment_txn_success = random.choice(['Y', 'N'])  # Y=Success, N=Failed
    failure_reason = "" if payment_txn_success == 'Y' else "Invalid CVV."  # Reason for payment failure
    
    return [
        order_id, customer_id, customer_name, product_id, product_name, product_category,
        payment_type, qty, price, datetime, country, city, ecommerce_website_name,
        payment_txn_id, payment_txn_success, failure_reason
    ]

def generate_rogue_record():
    """Generates a rogue e-commerce record with anomalies in 'price' and 'qty', while keeping other columns valid."""
    
    # Rogue values for 'price' and 'qty'
    price = round(random.uniform(10000.0, 50000.0), 2)  # Unreasonably high price
    qty = random.randint(10000, 50000)  # Unreasonably high quantity
    
    # Other fields remain valid
    order_id = fake.random_number(digits=6)
    customer_id = fake.random_number(digits=6)
    customer_name = fake.name()
    product_id = fake.random_number(digits=6)
    product_category = random.choice(product_categories)
    product_name = random.choice(product_names_mapping[product_category])
    payment_type = fake.random_element(payment_type_choices)
    datetime = fake.date_time_between(start_date='-1y', end_date='now').strftime("%Y-%m-%d %H:%M")
    country = random.choice(list(countries.keys()))
    city = random.choice(countries[country])
    ecommerce_website_name = random.choice(websites)
    payment_txn_id = fake.uuid4().split('-')[0]
    payment_txn_success = random.choice(['Y', 'N'])  # Y=Success, N=Failed
    failure_reason = "" if payment_txn_success == 'Y' else "Invalid CVV."
    
    return [
        order_id, customer_id, customer_name, product_id, product_name, product_category,
        payment_type, qty, price, datetime, country, city, ecommerce_website_name,
        payment_txn_id, payment_txn_success, failure_reason
    ]

def write_to_csv(num_records, rogue_percentage, file_name='E-Commerce_data.csv'):
    """Writes valid and rogue records to a CSV file according to the specified schema."""
    num_rogue_records = int(num_records * rogue_percentage)
    
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            'order_id', 'customer_id', 'customer_name', 'product_id', 'product_name', 'product_category', 
            'payment_type', 'qty', 'price', 'datetime', 'country', 'city', 'ecommerce_website_name', 
            'payment_txn_id', 'payment_txn_success', 'failure_reason'
        ])
        
        for _ in range(num_records):
            if random.random() < (num_rogue_records / num_records):
                record = generate_rogue_record()
            else:
                record = generate_valid_record()
            
            writer.writerow(record)


