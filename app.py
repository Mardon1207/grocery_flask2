from flask import Flask,jsonify,request
from db import GroceryDB


app = Flask(__name__)
db = GroceryDB()


# view all grocery
@app.route('/grocery')
def all_grocery():
    """Get all grocery"""
    grocerys= db.all()
    return jsonify(grocerys)


# view add grocery
@app.route('/grocery/add', methods=["POST"])
def add_grocery():
    """Add a grocery"""

    body =request.get_json()

    db.add(body)

    return jsonify("succes")


# view all grocery by type
@app.route('/grocery/type/<type>')
def all_grocery_by_type(type):
    """Get all grocery by type"""
    print(type)
    data=db.get_by_type(type)
    return jsonify(data)


# view all grocery by name
@app.route('/grocery/name/<name>')
def all_grocery_by_name(name):
    """Get all grocery by name"""
    data=db.get_by_name(name)
    return jsonify(data)


# view all grocery by price
@app.route('/grocery/price/<float:price>')
def all_grocery_by_price(price):
    """Get all grocery by price"""
    data=db.get_by_price(price)
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)