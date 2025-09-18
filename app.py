# Simple Flask App for Beginners
from flask import Flask

# Create Flask app
app = Flask(__name__)

@app.route('/')
def hello():
    """Home page - returns a simple message"""
    return "Hello! This is a simple Flask app with CI/CD pipeline! staging test"

@app.route('/health')
def health():
    """Health check - used to verify the app is running"""
    return "App is healthy and running!"

@app.route('/about')
def about():
    """About page"""
    return "This is a beginner-friendly Flask app for learning CI/CD with GitHub Actions."

# Function to add two numbers (for testing purposes)
def add_numbers(a, b):
    """Simple function to add two numbers"""
    return a + b

# Function to multiply two numbers (for testing purposes)
def multiply_numbers(a, b):
    """Simple function to multiply two numbers"""
    return a * b

if __name__ == '__main__':
    # Run the app
    app.run(debug=True, host='0.0.0.0', port=5000)

