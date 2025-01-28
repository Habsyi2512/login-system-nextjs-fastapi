from fastapi.testclient import TestClient
from ..main import app
from ..models.user import User
from ..config.database import engine
from sqlmodel import Session, select
import pytest

client = TestClient(app)

def test_delete_all_users():
  response = client.delete("/delete_all_users")
  assert response.status_code == 200
    

def test_register_success():
  response = client.post("/auth/register", json={
    "email": "test1@example.com",
    "password": "Boci12345!",
    "full_name": "Muhammad Habsyi Mubarak"
  })
  assert response.status_code == 201

def test_register_failure_existing_email():
  response = client.post("/auth/register", json={
    "email": "test1@example.com",
    "password": "Boci12345!",
    "full_name": "Muhammad Habsyi Mubarak"
  })
  assert response.status_code == 400
  assert response.json() == {"detail": "Email already registered"}

def test_register_password_non_number():
  response = client.post("/auth/register", json={
    "email": "test1@example.com",
    "password": "Bociiiiiiiiii!",
    "full_name": "Muhammad Habsyi Mubarak"
  })
  output = response.json()["detail"][0]
  assert output['msg'] == "Value error, Password must containt at least one number."

def test_login():
  response = client.post("/auth/token", data={
    "username": "test1@example.com",
    "password": "Boci12345!"
  })
  assert response.status_code == 200