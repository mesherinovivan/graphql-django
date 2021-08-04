# It`s study project for investigate graphql technology. 

### Run project
```bash
git clone https://github.com/mesherinovivan/graphql-django.git
cd graphql-django
virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
src/./manage.py migrate
src/./manage.py runserver

```
#### Postman collection there is directory src/postman/postman_collection.json

### Exemple queries this project

``` graphql
query {
	contacts{
    id,
    createdAt,
    firstName
  }
  
  _debug {
        sql {
          rawSql,
          isSlow,
          duration
        },
    }
}

query {
	contact(id:22){
    id,
    createdAt,
    firstName
  }
  
  _debug {
        sql {
          rawSql,
          isSlow,
          duration
        },
    }
}


query {
	contactsNode(firstName: "Ivanov"){
    edges{node{id, firstName}}
    
  }
  
  _debug {
        sql {
          rawSql,
          isSlow,
          duration
        },
    }
}
```

### Exemple mutations this project

```graphql
mutation{
  deleteContact(id:1){
    message,
    id
  }
}

mutation createMutation {
  createContact(input: {firstName: "1", lastName: "Example 5", birthDate: "2021-12-29", gender: "MALE"}) {
    id
    firstName
    lastName
    birthDate
    gender
    createdAt
    updatedAt
  }
}

mutation createMutation {
  updateContact(input: {id:1, firstName: "1", lastName: "Example 5", birthDate: "2021-12-29", gender: "MALE"}) {
    id
    firstName
    lastName
    birthDate
    gender
    createdAt
    updatedAt
  }
}
```

