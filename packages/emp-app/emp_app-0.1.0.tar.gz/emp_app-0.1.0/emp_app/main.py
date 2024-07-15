from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def get_emp_data():
    resp = requests.get("https://dummy.restapiexample.com/api/v1/employees")
    print(str(resp.content))
    return [{"name": "emp1"}, {"name": "emp2"}]
