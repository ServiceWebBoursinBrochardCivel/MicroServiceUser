import requests


def test_getUser():
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