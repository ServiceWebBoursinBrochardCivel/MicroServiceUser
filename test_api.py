import requests

def test_getUsers():
    r = requests.get('http://127.0.0.1:5000/users')
    resultAtt = '[{"id":1,"mail":"test@test.com","password":"test","pseudo":"test"}]\n'
    assert r.text == resultAtt

def test_Exist():
    r = requests.post("http://127.0.0.1:5000/search", json={"mail": "test@test.com","password": "test"})
    resultAtt = 'Existant'
    assert r.text == resultAtt


def test_NotExist():
    r = requests.post("http://127.0.0.1:5000/search", json={"mail": "INCORECT@FAUX.com","password": "INCORRECT"})
    resultAtt = 'Innexistant'
    assert r.text == resultAtt

def test_getUser():
    r = requests.get('http://127.0.0.1:5000/user/1')
    resultAtt = '[1,"test","test@test.com","test"]\n'
    assert r.text == resultAtt

def test_UserDelete():
    r = requests.delete("http://127.0.0.1:5000/user/1")
    resultAtt = 'User with the id 1 has been deleted'
    assert r.text == resultAtt

def test_InsertUser():
    r = requests.post("http://127.0.0.1:5000/users", json={"pseudo": "deux","mail": "deux@test.com","password": "deux"})
    resultAtt = 'User with the id 2 created successful'
    assert r.text == resultAtt  

def test_getUsersFin():
    r = requests.get('http://127.0.0.1:5000/users')
    resultAtt = '[{"id":2,"mail":"deux@test.com","password":"deux","pseudo":"deux"}]\n'
    assert r.text == resultAtt