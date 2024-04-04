from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Basic Details Website'

@app.route('/details')
def details():
    basic_details = {
        'name': 'John Doe',
        'age': 30,
        'location': 'New York'
    }
    return f"""
    <h1>Basic Details</h1>
    <p>Name: {basic_details['name']}</p>
    <p>Age: {basic_details['age']}</p>
    <p>Location: {basic_details['location']}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)