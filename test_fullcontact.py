from http import HTTPStatus
import json

def test_person_request(client):
    data={
        "email":"bart@fullcontact.com",
        "twitter":"@bartlorang",
        "phone":"9096975182",
    }
    url = "/person"
    response = client.post(url,json=data)
    assert response.status_code == HTTPStatus.OK

def test_person_request_fail(client):
    data={
        "email":"bart@fullcontact",
        "twitter":"@bartlorang",
        "phone":"9096975182",
    }
    url = "/person"
    response = client.post(url,json=data)  
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR  
    
def test_company_fail_request(client):
    data={
        "domain":"fullcontact"
    }
    url = "/company"
    response = client.post(url,json=data)
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR   



