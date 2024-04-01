import random
from faker import Faker
import mysql.connector
from tqdm import tqdm

class DataPipeline:
    def __init__(self, user, password, host, database):
        """
        Initializes DataPipeline object with database credentials.

        Parameters:
            user (str): Username for database authentication.
            password (str): Password for database authentication.
            host (str): Hostname where the database is hosted.
            database (str): Name of the database.
        """
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def create_connection(self):
        """
        Creates a connection to the MySQL database.

        Returns:
            mysql.connector.connection.MySQLConnection: Connection object.
        """
        return mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database
        )

    def ingest_data(self, cursor, records, table_name):
        """
        Ingests data into the specified table.

        Parameters:
            cursor (mysql.connector.cursor.MySQLCursor): Database cursor object.
            records (list): List of tuples containing customer records.
            table_name (str): Name of the table to ingest data into.
        """
        for record in records:
            cursor.execute(f'''
                INSERT INTO {table_name} (customer_id, name, address, email, telephone, contact_preference, transaction_activity, customer_preference, communication_method)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', record)

    def run_pipeline(self, records, table_name):
        """
        Runs the data pipeline to ingest data into the specified table.

        Parameters:
            records (list): List of tuples containing customer records.
            table_name (str): Name of the table to ingest data into.
        """
        conn = self.create_connection()
        cursor = conn.cursor()

        try:
            self.ingest_data(cursor, records, table_name)
            conn.commit()
            print(f"Data ingestion successful for {table_name}.")
        except Exception as e:
            conn.rollback()
            print(f"Error during data ingestion for {table_name}: {str(e)}")
        finally:
            cursor.close()
            conn.close()


def generate_records(table_name):
    """
    Generates fake customer records for a specific table using Faker library.

    Parameters:
        table_name (str): Name of the table.

    Returns:
        list: List of tuples containing customer records.
    """
    fake = Faker('tw_GH')
    records = []
    for _ in range(100000):
        customer_id = f"NWI{fake.random_number(digits=6)}"
        name = fake.name()
        address = fake.address()
        email = fake.email()
        telephone = fake.phone_number()
        contact_preference = random.choice(['SMS', 'Email', 'Call'])
        transaction_activity = fake.random_int(min=0, max=100000)
        customer_preference = random.choice(['App', 'Website'])
        communication_method = random.choice(['SMS', 'Email', 'Call'])

        records.append((customer_id, name, address, email, telephone, contact_preference,
                        transaction_activity, customer_preference, communication_method))

    return records


if __name__ == "__main__":
    # Database credentials for MySQL
    user = "admin"
    password = "password"
    host = "localhost"
    database = "Top 10 Companies"  

    # Table names
    table_names = [
        "Nationwide_Medical_Insurance",
        "Microfin_Rural_Bank",
        "Tropical_Cable_And_Conductor_Ltd",
        "Imperial_Homes_Limited",
        "Zonda_Tec_Ghana_Limited",
        "Wilmar_Africa_Limited",
        "Bayport_Savings_And_Loans_Plc",
        "Ghandour_Cosmetics_Ltd",
        "Star_Assurance_Company_Ltd",
        "DHL_Ghana_Ltd"
    ]

    # Initialize pipeline and run for each table
    pipeline = DataPipeline(user, password, host, database)
    for table_name in table_names:
        records = generate_records(table_name)
        with tqdm(total=len(records), desc=f"Ingesting data into {table_name}", unit=' records') as pbar:
            pipeline.run_pipeline(records, table_name)
            pbar.update(len(records))  # Update progress bar after each table is processed
