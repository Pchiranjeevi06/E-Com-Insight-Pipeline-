# ecommerce_utils.py
from faker import Faker

# Create a Faker instance
fake = Faker()

# Product categories and types
product_categories = [
    'Electronics', 'Clothing', 'Home & Kitchen', 'Sports & Outdoors',
    'Books', 'Toys & Games', 'Health & Personal Care', 'Automotive',
    'Beauty & Personal Care', 'Office Products', 'pen', 'pencil'
]

product_names_mapping = {
    'Electronics': ['Mobile', 'Laptop', 'Tablet', 'Camera'],
    'Clothing': ['Shirt', 'Pants', 'Dress', 'T-shirt'],
    'Home & Kitchen': ['Cookware', 'Furniture', 'Decor'],
    'Sports & Outdoors': ['Football', 'Tennis Racket', 'Yoga Mat'],
    'Books': ['Paperback', 'Hardcover', 'E-book'],
    'Toys & Games': ['Action Figure', 'Board Game', 'Puzzle'],
    'Health & Personal Care': ['Vitamins', 'Face Wash', 'Shampoo'],
    'Automotive': ['Car Tire', 'Brake Pads', 'Headlights'],
    'Beauty & Personal Care': ['Lipstick', 'Foundation', 'Hair Dryer'],
    'Office Products': ['Notebook', 'Pen', 'Printer'],
    'pen': ['Gel Pen', 'Ball Pen'],
    'pencil': ['Graphite Pencil', 'Mechanical Pencil']
}

# Countries and cities
countries = {
    'India': ['Mumbai', 'Delhi', 'Bengaluru', 'Chennai', 'Kolkata'],
    'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Boston'],
    'UK': ['London', 'Manchester', 'Birmingham', 'Leeds', 'Oxford'],
    'Germany': ['Berlin', 'Munich', 'Frankfurt', 'Hamburg', 'Stuttgart']
}
#payment_type
payment_type_choices= ['Cards', 'InternetBanking', 'UPI', 'Wallet']


# E-commerce websites
websites = ['www.amazon.com', 'www.flipkart.com', 'www.ebay.in', 'www.tatacliq.com', 'www.snapdeal.com']
