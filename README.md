<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>API and SQL Database Optimization for Application Integration</h1>

<p>This project focuses on optimizing SQL databases and developing a RESTful API for seamless integration of multiple applications. The goal is to enhance data flow, reduce system downtime, and improve the overall user experience.</p>

<h2>Project Overview</h2>
<p>The project involves:</p>
<ul>
    <li>Designing an efficient database schema</li>
    <li>Optimizing SQL queries to improve performance</li>
    <li>Developing a RESTful API using Flask</li>
    <li>Implementing caching and pagination in API endpoints</li>
</ul>

<h2>Features</h2>
<ul>
    <li>Efficient database design with indexed tables</li>
    <li>Optimized SQL queries for faster data retrieval</li>
    <li>RESTful API with CRUD operations</li>
    <li>Caching and pagination for optimized API performance</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li>Python</li>
    <li>Flask</li>
    <li>MySQL</li>
    <li>SQL</li>
    <li>Postman (for API testing)</li>
</ul>

<h2>Setup Instructions</h2>
<ol>
    <li>Clone the repository to your local machine.</li>
    <li>Set up the MySQL database using the provided SQL scripts:</li>
    <ul>
        <li><code>schema_creation.sql</code>: Creates the database schema</li>
        <li><code>data_insertion.sql</code>: Inserts sample data</li>
        <li><code>optimization.sql</code>: Adds indexes and optimizes queries</li>
    </ul>
    <li>Install the required Python packages:</li>
    <pre><code>pip install flask flask-caching mysql-connector-python</code></pre>
    <li>Configure the database connection in the <code>api_script.py</code> file.</li>
    <li>Run the API:</li>
    <pre><code>python api_script.py</code></pre>
    <li>Test the API endpoints using Postman or a similar tool.</li>
</ol>

<h2>API Endpoints</h2>
<ul>
    <li><strong>GET /users</strong>: Retrieve all users (with caching)</li>
    <li><strong>GET /users/&lt;user_id&gt;</strong>: Retrieve a specific user by ID</li>
    <li><strong>POST /users</strong>: Create a new user</li>
    <li><strong>GET /users/&lt;user_id&gt;/transactions</strong>: Retrieve transactions for a user (with pagination)</li>
</ul>

<h2>Performance Improvements</h2>
<p>After optimizing the SQL queries and implementing caching in the API, the system experienced a significant reduction in query execution time and system downtime, leading to a better overall user experience.</p>

<h2>Contributing</h2>
<p>If you'd like to contribute to this project, feel free to submit a pull request. Please ensure that your contributions are well-documented and tested.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more details.</p>

</body>
</html>
