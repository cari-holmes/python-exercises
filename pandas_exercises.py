
from pydataset import data 

#1. Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:
mpg = data('mpg')
mpg.head(10)

##A. On average, which manufacturer has the best miles per gallon?
best_hwy_average = mpg.groupby('manufacturer').hwy.mean()
best_hwy_average
best_cty_average = mpg.groupby('manufacturer').cty.mean()
best_cty_average
best_average_combined = best_hwy_average + best_cty_average
avg = best_average_combined / 2
avg.idxmax()

# best_mpg = mpg[['hwy', 'cty']].agg(['mean'])
# best_mpg

#B. How many different manufacturers are there?
count_manufacturers = mpg.groupby('manufacturer').count()
count_manufacturers
len(count_manufacturers)

# len(mpg.manufacturer.unique())
    ## nunique()

#C. How many different models are there?
count_models = mpg.groupby('model').nunique()
count_models
len(count_models)

###D. Do automatic or manual cars have better miles per gallon?
mpg['mpg'] = (mpg.cty + mpg.hwy) / 2

.contains['auto']
.contains['manual']

#2. Joining and Merging
# Copy the users and roles dataframes from the examples above. 
import numpy as np

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

# What do you think a right join would look like? 
pd.merge(users, roles, left_on='role_id', right_on='id', how='right')

# An outer join? 
pd.merge(users, roles, left_on='role_id', right_on='id', how='outer')

# What happens if you drop the foreign keys from the dataframes and try to merge them?
pd.merge(users, roles, on='id', how='inner')
# pandas will find the commonality between the two dataframes and guess what to merge on


#3. Getting data from SQL databases
#A. Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url formatted like in the examples in this lesson.
import pandas as pd
from env import host, user, password

def get_db_url(host, user, password, database_name):
    url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
    return url

database_name = "employees"
url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
query = """SELECT * FROM employees"""
df = pd.read_sql(query, url)
print(df)

#B. Use your function to obtain a connection to the employees database.
df

#C. Once you have successfully run a query:
    # Intentionally make a typo in the database url. What kind of error message do you see?
        # Operational Error (pymysql.err.OperationalError)("Access denied")
            # tells background on this error
    # Intentionally make an error in your SQL query. What does the error message look like?
        # Programming Error (pymysql.err.ProgrammingError)("You have an error in your SQl syntax; check the manual that corresponds to your MySQL server version")
            # tells where the syntax error is

#D. Read the employees and titles tables into two separate dataframes

query = """SELECT * FROM titles"""
titles = pd.read_sql(query, url)
titles.head(5)

query = """SELECT * FROM employees"""
employees = pd.read_sql(query, url)
employees.head(5)

##E. Visualize the number of employees with each title.
count and plot 

#F. Join the employees and titles dataframes together.
pd.merge(employees, titles, left_on='emp_no', right_on='emp_no', how='inner' )

##G. Visualize how frequently employees change titles.
count and plot

##H. For each title, find the hire date of the employee that was hired most recently with that title.
# titles - emp_no, title, from_date, to_date(9999-01-01)
# employees - emp_no, hire_date

query = """SELECT t.title AS title, CONCAT(e.first_name, " ", last_name) AS name, t.from_date AS hire_date FROM employees AS e
JOIN titles AS t 
ON t.emp_no=e.emp_no
;"""

employees_hire_date = pd.read_sql(query, url)
print(employees_hire_date)
employees_hire_date.head(10)

###I. Write the code necessary to create a cross tabulation of the number of titles by department. (Hint: this will involve a combination of SQL and python/pandas code)
# departments - dept_no, dept_name
# titles - title, emp_no, 
# dept_emp - emp_no, dept_no
database_name = "employees"
url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'

query = """SELECT t.title AS title, d.dept_name AS dept_name FROM dept_emp as de
JOIN titles as t
ON de.emp_no=t.emp_no
JOIN departments as d
ON de.dept_no=d.dept_no
;"""

num_titles = pd.read_sql(query, url)
print(num_titles)
num_titles.groupby(['dept_name']).count()
num_titles.groupby(['title']).count()

#4. Use your get_db_url function to help you explore the data from the chipotle database. Use the data to answer the following questions:
database_name = "chipotle"
url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
query = """SELECT * FROM orders"""
chipotle = pd.read_sql(query, url)
print(chipotle)
chipotle.head(10)

#A. What is the total price for each order?
chipotle["total_price"] = chipotle.

orders['bill'] = orders.drink.map(prices) + orders.meal.map(prices)

orders.tail(5)
#B. What are the most popular 3 items?


#C. Which item has produced the most revenue?

