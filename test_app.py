# Simple Tests for Beginners
import pytest
from app import app, add_numbers, multiply_numbers

@pytest.fixture
def client():
    """Create a test client for testing our Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_page(client):
    """Test if the home page works"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello! This is a simple Flask app" in response.data

def test_health_page(client):
    """Test if the health page works"""
    response = client.get('/health')
    assert response.status_code == 200
    assert b"App is healthy" in response.data

def test_about_page(client):
    """Test if the about page works"""
    response = client.get('/about')
    assert response.status_code == 200
    assert b"beginner-friendly Flask app" in response.data

def test_add_numbers():
    """Test the add_numbers function"""
    result = add_numbers(2, 3)
    assert result == 5
    
    result = add_numbers(10, 15)
    assert result == 25

def test_multiply_numbers():
    """Test the multiply_numbers function"""
    result = multiply_numbers(3, 4)
    assert result == 12
    
    result = multiply_numbers(5, 6)
    assert result == 30