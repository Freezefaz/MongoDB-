<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

Welcome Freezefaz,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

For mongoDB
mongo "mongodb+srv://cluster0.uaguy.mongodb.net/" --username root


To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.


# For MongoDB

mongo "mongodb+srv://cluster0.uaguy.mongodb.net/" --username root

docs.mongodb.com/manual

# see alll databases
show databases

# use databases
use sample_airbnb
- To create database just use <create_database>
- So beware of typos can create new database

# show collections in a databases
show collections

# Queries

- db refers to the database being used
- to find stuff -> db.collectionName.find()

- to format code -> db.collectionName.find().pretty()

- add limit to first x of records -> db.listingsAndReviews.find().pretty().limit()

Find by criteria
- Find 2 beds 
- db.listingsAndReviews.find({
    'beds': 2
}).pretty().limit(5)

# Projecting
Similar to how we do select * columns in MySQL

Find all the listings with 2 beds and display name and address

- db.listingsAndReviews.find({
    'beds': 2
}, {
    'name': 1, 'address': 1, 'beds': 1
}).pretty().limit(5)

Find all listings and display name, bads and only the country 
- db.lisitingsAndReviews.find({
    'beds': 2
}, {
    'name': 1,
    'address.country': 1,
    'beds': 1
}).pretty().limit(5)

Find all the listings in Brazil
- db.lisitingsAndReviews.find({
    'address.country': 'Brazil'
}, {
    'name': 1,
    'address.country': 1,
    'address.suburb': 1,
    'address.street': 1
}).pretty().limit(5)

# Find by multiple criteria
Add the new criteria to the firt arguement to the 'find' fucntion.

To find the listings with 2 beds and 2 bedrooms

- db.listingsAndReviews.find({
    'beds':2,
    'bedrooms':2
}, {
    'name':1,
    'beds':1,
    'bedrooms':1
}).pretty().limit(10)

# Find by a range or inequality

We can '$gt' or '$lt' to represent greater or lesser than
Lesser than
- db.listingsAndReviews.find({
    'beds': {
        '$lt':3
    }
}, {
    'name':1,
    'beds':1
}).pretty().limit(10)

'$gte' is 'greater than or equal' and '$lte' is lesser than or equal.

for greater than 4 but less than 6 beds
- db.listingsAndReviews.find({
    'beds':{
        '$gte':4,
        '$lte':6
    },
    'bedrooms':3
}, {
    'beds':1,
    'name':1,
    'bedrooms':1
}).pretty().limit(10)

# Find by elements in an array

Case sensitive and make sure no gaps in the keys
- db.listingsAndReviews.find({
    'amenities':'Washer'
}, {
    'name':1,
    'amenities':1
}).pretty().limit(5)

## Find by specific elements in an array
- db.listingsAndReviews.find({
    'amenities':{
        '$all':['Washer', 'Dryer']
        }
}, {
    'name':1,
    'amenities':1
}).pretty().limit(5)

## Find lsitings that include ONE of the specific elements in an array

As long as one of these things are included they will show
- db.listingsAndReviews.find({
    'amenities':{
        '$in':['TV', 'Cable TV']
        }
}, {
    'name':1,
    'amenities':1
}).pretty().limit(5)

- db.listingsAndReviews.find({
    'amenities':{
        '$in':['Kitchen', 'Microwave']
        }
}, {
    'name':1,
    'amenities':1
}).pretty().limit(5)

## Find all listings tht are either in Canada or Brazil

- db.listingsAndReviews.find({
    'address.country':{
        '$in':['Brazil', 'Canada']
    }
}, {
    'name':1,
    'address.country':1
}).pretty().limit(10)

# Advance
## Selectby its objectId

use sample _mflix;

Its id is a javascript class
- db.movies.find({
    '_id':ObjectId('573a1390f29313caabcd4803')
}).pretty()

## Find all listings by Bart
$elemMatch -> to find element match

- db.listingsAndReviews.find({
    'reviews':{
        '$elemMatch':{
            'reviewer_name':'Bart'
        }
    }
},{
    'name':1,
    'reviews':1
}).pretty().limit(5)

## Match by string
Something like 'select * from customers where customerName like

Search all listings which has 'spacious' in its name, i = case insensitive

Use $regex -> regular expression

- db.listingsAndReviews.find({
    'name':{
        '$regex':'Spacious', '$options':'i'
    }
},{
    'name':1
})

## Count how many lisitings there are in total

- db.lisitngsAndReviews.find().count()

## Show all the listings that has >= 10 amenities

- db.listingsAndReviews.find({
    'amenities':{
        '$size':10
        }
},{
    'name':1, 
    'amenities':1
}).pretty()

amenities.6 -> amenities with index 0 - 6

exists true -> will only display those with 6 or more
- db.listingsAndReviews.find({
    'amenities.6':{
        '$exists':true
        }
},{
    'name':1, 
    'amenities':1
}).pretty()

## Compounds criterias: AND OR NOT

Find alll listings from Brazil or Canada that has more than 5 bedrooms
- db.listingsAndReviews.find({
    '$or':[
        {
            'address.country':'Brazil'
        },
        {
            'address.country':'Canada',
            'bedrooms': {
                '$gte':5
            }
        }
    ]
}, {
    'name':1,
    'bedrooms':1,
    'address.country':1
}).pretty()

## Find all listings NOT in Brazil and Canada

- db.listingsAndReviews.find({
   'address.country': {
       '$not': {
           $in:['Brazil', 'Canada']
       }
   }
}, {
    'name':1,
    'address.country':1
}).pretty()
