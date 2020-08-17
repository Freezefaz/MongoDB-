# install these dependencies first
# pip3 install pymongo
# pip3 install dnspython

# Go to Mongo Atlas -> connect button -> connect to application - > driver: Python, Version: 3.11 or later


from flask import Flask, render_template, request, redirect, url_for
import pymongo
import os
from dotenv import load_dotenv
import math

# load the variables in the .env file to the environment
load_dotenv()

app = Flask(__name__)

# Connect to database !! Change password !!
# Constants: Not to be changed while program is running
MONGO_URL = os.environ.get("MONGO_URL")
# Connect to specific database
DB_NAME = "sample_airbnb"

# Create the Mongo DB Client
client = pymongo.MongoClient(MONGO_URL)


@app.route("/")
def show_listings():
    # Use mongo client to access our collections
    #db.listingsAndReviews.find()

    # pass the results back to the template
    all_listings = client[DB_NAME].listingsAndReviews.find()
    return render_template("show_listings.template.html", 
                            listings=all_listings)

@app.route('/search')
def search():
# PDL - Program Design Language for planning
# write comments in laymans then do coding

# Get all the search terms from the form
    # GET must use args NOT FORM
    required_listing_name = request.args.get('listing_name') or ''
    required_country = request.args.get('country') or ''

# Define the criteria and search query base on search terms
    criteria = {}

    if required_listing_name:
        criteria['name'] = {
            '$regex': required_listing_name,
            '$options': 'i'
        }

    if required_country:
        criteria['address.country'] = {
            '$regex': required_country,
            '$options': 'i'
        }

# to read and make it into paging
    number_of_results = client[DB_NAME].listingsAndReviews.find(criteria).count()
    page_size = 10
# Start from 0
    number_of_pages = math.ceil(number_of_results / page_size) - 1

# get the current page number from the args. if doesn't exist set to 0
    page_number = request.args.get('page_number') or '0'
    page_number = int(page_number)

# Calculate how many results to skip depending on page number
    number_to_skip = page_number * page_size

    all_listings = client[DB_NAME].listingsAndReviews.find(
        criteria).skip(number_to_skip).limit(page_size)

# read in the data (original)
    # all_listings = client[DB_NAME].listingsAndReviews.find(criteria)


# Pass the data to the template
    return render_template('search.template.html', listings=all_listings,
                            page_number=page_number,
                            number_of_pages=number_of_pages,
                            required_listing_name=required_listing_name,
                            required_country=required_country)




# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)