# CRM System (Customer Relationship Management)
## ©️This Project belongs to AYOMIDE OLADIPUPO

This is a simple Customer Relationship Management (CRM) system built using **Django** (Python web framework), **HTML**, and **MySQL**. The CRM allows users to store and manage customer records, such as personal information (name, email, phone, address, etc.).
This is project is a capstone Project for my Diploma program at the Baze University, Abuja, Nigeria.


## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
- [Database Schema](#database-schema)
- [SQL Queries](#sql-queries)
- [Future Improvements](#future-improvements)

## Project Overview

The CRM system is a simple web-based application for managing customer data. Users can add, update, and delete records and search through the database of customer details. It was developed using Django to provide a scalable and maintainable backend with MySQL as the database management system.

## Features
- Add new customer records
- Edit existing customer records
- Delete customer records
- View a list of all customers
- Search for a customer using name or email

## Technologies
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: MySQL
- **ORM**: Django ORM for database interactions
- **Hosting/Local Environment**: Windows with Django virtual environment

## Setup Instructions

### Prerequisites:
- Python 3.x
- MySQL Server
- Django (use `pip install django`)
- MySQL Connector (use `pip install mysqlclient`)

### Step-by-Step Guide:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-crm-repo.git
   cd your-crm-repo
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the MySQL database:**

   Create a MySQL database for the project:
   ```sql
   CREATE DATABASE crm;
   ```
   
   Update the `settings.py` file with your MySQL credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'crm',
           'USER': 'root',
           'PASSWORD': '',
           'HOST': 'localhost',
           'PORT': '3307',
       }
   }
   ```

5. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Run the server:**
   ```bash
   python manage.py runserver
   ```
   Open your browser and go to `http://127.0.0.1:8000/` to view the app.

## Database Schema

The MySQL database is used to store customer records. The following table structure was used:

**Table: `website_record`**
- `created_at`: Timestamp of when the record was created.
- `first_name`: Customer's first name.
- `last_name`: Customer's last name.
- `email`: Customer's email address.
- `phone`: Customer's phone number.
- `address`: Customer's address.
- `city`: Customer's city.
- `state`: Customer's state.
- `zipcode`: Customer's postal code.

## SQL Queries

To populate the `website_record` table with sample data, the following SQL query was executed:

```sql
USE crm;

INSERT INTO website_record (created_at, first_name, last_name, email, phone, address, city, state, zipcode) VALUES
('2024-09-25 10:30:43.714587', 'John', 'Doe', 'john.doe1@example.com', '1234567890', '123 Elm St', 'New York', 'NY', '10001'),
('2024-09-25 10:31:12.519183', 'Jane', 'Smith', 'jane.smith1@example.com', '2345678901', '456 Maple Ave', 'Los Angeles', 'CA', '90001'),
-- additional rows...
('2024-09-25 10:50:19.381043', 'Aria', 'Russell', 'aria.russell1@example.com', '0123498765', '4747 Riverview Pl', 'Honolulu', 'HI', '96801');
```

## Future Improvements
- Implement user authentication and access control.
- Add more advanced filtering and sorting features for customer data.
- Include pagination for large data sets.
- Enhance the user interface with a more modern design using CSS frameworks like Bootstrap.

---
# CRM-App
