
from pydataset import data 

#1. Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:
mpg = data('mpg')
mpg.head(10)

##A. On average, which manufacturer has the best miles per gallon?
mpg.groupby('manufacturer').max

#B. How many different manufacturers are there?
count_manufacturers = mpg.groupby('manufacturer').count()
len(count_manufacturers)

#C. How many different models are there?
count_models = mpg.groupby('model').count()
len(count_models)

##D. Do automatic or manual cars have better miles per gallon?


#2. Joining and Merging
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

# Copy the users and roles dataframes from the examples above. 
# What do you think a right join would look like? 
# An outer join? 
# What happens if you drop the foreign keys from the dataframes and try to merge them?