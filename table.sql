CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    customer_id VARCHAR(10),
    name VARCHAR(100),
    address TEXT,
    email VARCHAR(100),
    telephone VARCHAR(20),
    contact_preference VARCHAR(10),
    transaction_activity INTEGER,
    customer_preference VARCHAR(10),
    communication_method VARCHAR(10)
);
