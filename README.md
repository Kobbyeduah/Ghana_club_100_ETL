# Data Pipeline for Customer Record Ingestion
GENERATING 100K USER DATA EACH  FOR CREATING DATA PIPELINE FOR TEN COMPANIES

## Overview
This project implements an ETL (Extract, Transform, Load) pipeline for ingesting synthetic data into a PostgreSQL database for  fictional 10 companies, based in Ghana. The pipeline generates simulated customer data using the Faker library, creates a relational database schema, and loads the generated data into the database. Additionally, it provides functionality to query the data and save the queries into a file.

## Features

- Generates synthetic customer data including demographics, transaction activity, customer preferences, and communication methods.
- Ingests the generated data into a PostgreSQL database.
- Provides Python scripts to execute various data processing tasks and SQL queries.
- Dockerized for easy deployment and reproducibility.

## Details:
- Data Generation: Fake customer records are generated using the Faker library to simulate realistic data.

- Database Interaction: The pipeline establishes a connection to a PostgreSQL database and creates a table (customers) to store the generated records.

- Data Ingestion: Generated customer records are ingested into the database table.

- Error Handling: The pipeline includes error handling mechanisms to ensure data integrity and reliability during ingestion.

## Prerequisites

- [Python 3.0 and above](https://www.python.org)
- [PostgreSQL](https://www.postgresql.org)
- [psycopg2 library](https://pypi.org/project/psycopg2/)
- [Docker](https://www.docker.com)
- [Faker](https://faker.readthedocs.io/en/master/)