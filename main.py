import random
from faker import Faker
import mysql.connector

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

    def run_pipeline(self, records):
        """
        Runs the data pipeline to ingest data into all tables.

        Parameters:
            records (list): List of tuples containing customer records.
        """
        conn = self.create_connection()
        cursor = conn.cursor()

        try:
            # Iterate over each table and ingest data
            for table_name in table_names:
                self.ingest_data(cursor, records, table_name)

            conn.commit()
            print("Data ingestion successful.")
        except Exception as e:
            conn.rollback()
            print(f"Error during data ingestion: {str(e)}")
        finally:
            cursor.close()
            conn.close()


def generate_records():
    """
    Generates fake customer records using Faker library.

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
    database = "Top_10_Companies"  # database name (note: changed to use underscores instead of spaces)

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

    # Generate records
    records = generate_records()

    # Initialize pipeline and run
    pipeline = DataPipeline(user, password, host, database)
    pipeline.run_pipeline(records)
