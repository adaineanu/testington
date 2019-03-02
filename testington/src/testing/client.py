import requests

if __name__ == '__main__':
    req = requests.post('http://localhost:8080/api/test', json={'email': 'test@test.com', 'message': 'example message'})
    print(req.content)
