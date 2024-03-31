from faker import Faker
import pandas as pd
import random
 
fake = Faker('tw_GH')
 
# Generate 100,000 records
records = []
for _ in range(100000):
    individual = {
        'customer_name': fake.name(),
        'address': fake.address(),
        'email': fake.email(),
        'telephone': fake.phone_number(),
        'country': 'Ghana',
        'contact_preference': random.choice(['SMS', 'Email', 'Call']),

        # Example transaction activity
        'transaction_activity': fake.random_int(min=0, max=100),
        'customer_preference': random.choice(['App', 'Website']),

        # Default communication method
        'communication_method': random.choice(['SMS', 'Email', 'Call'])
    }
 
    records.append(individual)
 
data = pd.DataFrame(records)
print(len(data))
data.head()

# save the data
Bayportgh_fakedata = data.to_csv('Bayportgh_fakedata.csv', index = False)