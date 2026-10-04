from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Hello from Python Azure DevOps CI/CD!" in response.data


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_hello():
    client = app.test_client()

    response = client.get("/hello")

    assert response.status_code == 200
    assert response.json["message"] == "Hello Aryan!"
    