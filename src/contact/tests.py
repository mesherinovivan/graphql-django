import json
import pytest
from graphene_django.utils.testing import graphql_query


@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)

    return func


@pytest.mark.django_db
def test_contacts_request_query(client_query):
    response = client_query(
        '''
        query {
            contacts{
            id,
            createdAt,
            firstName
          }
        }
        '''
    )
    content = json.loads(response.content)
    assert 'errors' not in content


@pytest.mark.django_db
def test_contact_create_request_query(client_query):
    response = client_query(
        '''
            mutation createMutation($input: ContactModelMutationInput!) {
              createContact(input: $input) {
                id
                firstName
                lastName
                birthDate
                gender
                createdAt
                updatedAt
              }
            }
        ''',
        input_data={"firstName": "Test", "lastName": "LastTest", "birthDate": "2021-12-29", "gender": "MALE"}
    )

    content = json.loads(response.content)
    assert 'errors' not in content
