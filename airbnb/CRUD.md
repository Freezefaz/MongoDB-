# Using Mongo with Python

## The dependencies

```
pip3 install dnspython
pip3 install pymongo
```

## Find the connection string
Click on the `Connect` button of your cluster and select `Connect to an application`.

Select driver to be `Python` and version to be `3.11 or later`

## Define the connection string and database name

```
MONGO_URI = '<connection string>'
DB_NAME = 'sample_airbnb'
```

Rememebr to replace the `<password>` in the connection string with your actual password.

# Use environmental variables to hide the MONGO_URI

1. Install `python-dotenv` dependency

2. Create `.env` file in the same folder as `app.py`

3. Create a `.gitignore` file and its content should be

```
.env
```

# Remove .env from github if accidentically pushed

1. Download BFG repo-cleaner and rename it as `bfg.jar`

2. Upload to gitpod

3. Add it to the .gitignore 

4. Run the command in the terminal:

```
java -jar bfg.jar --delete-files .env .
```

5. Delete the report files when done



# Generic Pesudo-code for CRUD 

## READ

1. Get all the data from the database (regardless whether it's just a JSON file, or SQL, or Mongo)

2. Pass the data into the template
