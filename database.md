# Create a database

1. Use the new database
use animal_shelter

## General syntax for inserting into a collection

db.animals.insert({
    'name': 'Fluffy',
    'age': 3,
    'breed': 'Golden Retriever',
    'type': 'Dog'
})

- to check if its inserted

db.animals.find()

## Insert many

db.animals.insertMany([
    {
        'name': 'Dazzy',
        'age': 5,
        'breed': 'Greyhound',
        'type': 'Dog'
    },
    {
        'name': 'Timmy',
        'age': 1,
        'breed': 'Maltese',
        'type': 'Dog'
    }
])

## To Update using existing key
- Need to include exisitng field if not the rest will not get updated
- To include the 

db.animals.update({
    "_id" : ObjectId("5f33aac44dda0c4a2248165c")
},{
    "name" : "Timmy",
    "age" : 1,
    "breed" : "Terrier",
    "type" : "Dog"
})

## To update by specifying new values for specific fields:

db.animals.update({
    "_id" : ObjectId("5f33aac44dda0c4a2248165c")
},{
    '$set':{
       "name" : "Thunder", 
    }
})

## To delete

db.animals.remove({
    "_id" : ObjectId("5f33aac44dda0c4a2248165b")
})

## Managing Collections

- Each dog has a checkuo

db.animals.insert({
    'name':'Cookie',
    'age': 3,
    'breed':'Shitzu',
    'type':'Dog',
    'checkups':[]
})

db.animals.insert({
    'name':'Frenzy',
    'age': 1,
    'breed':'Lion',
    'type':'cat',
    'checkups':[
        {
        'id':ObjectId(),
        'name': 'Dr Chua',
        'dianogsis':'Heartworms',
        'treatment':'Steroids'
    }
    ]
})

### Add a new sub-document to array

- Suppose Cookie visited a vet for the first time and we store the checkup information.

- (Adding a new element to an array)

db.animals.update({
    '_id':ObjectId("5f33acfbbf91d0dd5c1440df"),
}, {
    '$push': {
        'checkups': {
            '_id':ObjectId(),
            'name':'Dr Tan',
            'diagnosis':'Diabetes',
            'treatment':'Medication'
        }
    }
})

## Remove a sub-document from an array

Pull a checkup element by its id

db.animals.update({
    '_id':ObjectId("5f33acfbbf91d0dd5c1440df")
}, {
    '$pull': {
        'checkups': {
              '_id':ObjectId("5f33addebf91d0dd5c1440e2")
        }
    }
})

## Update an existing element in an array of a document

- We use $elemMatch in the critera to find the exact element in the array. And be sure to use $ to refer to the matched element later when we do the change.

db.animals.update({
    'checkups': {
        '$elemMatch': {
            '_id': ObjectId("5f33b0e3bf91d0dd5c1440e4")
        }
    }
}, {
    '$set': {
        'checkups.$.name':'Dr Su'
    }
})

db.animals.update({
    'checkups._id': ObjectId("5f33b0e3bf91d0dd5c1440e4")
}, {
    '$set': {
        'checkups.$.name':'Dr Zhao',
        'checkups.$.date': ISODate()
    }
})

## Unset a field

db.animals.update({
    '_id':ObjectId("5f33acfbbf91d0dd5c1440df")
}, {
    '$unset': {
        'date':""
    }
})
