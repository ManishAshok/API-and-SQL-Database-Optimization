
# API and SQL Database Optimization for Application Integration

## Project Overview
This project focuses on optimizing a SQL database and developing a RESTful API for application integration. The goal is to enhance data flow, reduce system downtime, and improve user experience.

## Prerequisites
1. MySQL Server installed on your local machine or accessible server.
2. Python 3.x installed on your machine.
3. Flask and Flask-Caching installed (`pip install flask flask-caching`).
4. MySQL Connector for Python installed (`pip install mysql-connector-python`).

## Step-by-Step Instructions

### 1. Set Up the Database

1. **Create the Database Schema**:
   - Execute the `schema_creation.sql` script to create the necessary tables (`users`, `transactions`, and `logs`).
   - You can run this script using MySQL Workbench or the MySQL command line:
     ```bash
     mysql -u yourusername -p yourdatabase < schema_creation.sql
     ```

2. **Insert Sample Data**:
   - Execute the `data_insertion.sql` script to insert sample data into the tables.
   - Use the same command as above to run the script:
     ```bash
     mysql -u yourusername -p yourdatabase < data_insertion.sql
     ```

3. **Optimize the Database**:
   - Execute the `optimization.sql` script to add an index and optimize a query.
   - Run the script using the same method:
     ```bash
     mysql -u yourusername -p yourdatabase < optimization.sql
     ```

### 2. Set Up and Run the API

1. **Configure the Database Connection**:
   - Open the `api_script.py` file in a text editor.
   - Replace the placeholder database connection details with your actual MySQL credentials:
     ```python
     connection = mysql.connector.connect(
         host='localhost',
         user='yourusername',
         password='yourpassword',
         database='yourdatabase'
     )
     ```

2. **Run the API**:
   - Navigate to the directory where `api_script.py` is located.
   - Run the API using Python:
     ```bash
     python api_script.py
     ```

3. **Test the API Endpoints**:
   - Use a tool like Postman or curl to test the API endpoints.
   - Example endpoints:
     - Get all users: `GET http://127.0.0.1:5000/users`
     - Get a user by ID: `GET http://127.0.0.1:5000/users/1`
     - Create a new user: `POST http://127.0.0.1:5000/users` (with JSON body)
     - Get transactions for a user (with pagination): `GET http://127.0.0.1:5000/users/1/transactions?page=1&per_page=10`

### 3. Review and Customize the Report

1. **Open the Report Template**:
   - The report template `Project_Report_Template.docx` is provided with this project.
   - Open it in Microsoft Word or any compatible editor.

2. **Customize the Content**:
   - Modify the content to match the specific details of your project.
   - Add additional sections or details as necessary.

3. **Finalize the Report**:
   - Save the document as a PDF or in any other desired format for final submission.

## Conclusion
By following these steps, you should be able to set up the database, run the API, and achieve the optimization goals outlined in this project. For any further questions or issues, feel free to reach out for assistance.
