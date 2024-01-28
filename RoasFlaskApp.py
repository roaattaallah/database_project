from flask import Flask, jsonify, request
from pymongo import MongoClient
import os 


app = Flask(__name__)

# MongoDB connection
 
client = MongoClient("mongodb://roa-attaallah-pro:9DdNdYQgCEsrNFTfOlRcCGLOH8vANAfeJpAaiJeWBeKXnTh7LBygJAAnyk5O0QuzENidvhAThhdQACDbeVmLpQ==@roa-attaallah-pro.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@roa-attaallah-pro@")
mongodb_uri = os.environ.get('MONGODB_URI', 'default-mongodb-uri') 

# Use the "BOOKSTORE" database
db = client["BOOKSTORE"]

@app.route('/')
def hello_world():
    return 'Hello, you accessed the link! my name is ROA K. A. ATTAALLAH'

# Create operation
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.json
    db.CL1.insert_one(new_book)  
    return jsonify({"message": "Book created successfully!"})

# Read operation (get all books)
@app.route('/books', methods=['GET'])
def get_books():
    books = list(db.CL1.find({}, {"_id": 0}))  
    return jsonify({"books": books})

# Read operation 
@app.route('/books/<isbn>', methods=['GET'])
def get_book(isbn):
    book = db.CL1.find_one({"isbn": isbn}, {"_id": 0})  
    if book:
        return jsonify({"book": book})
    else:
        return jsonify({"message": "Book not found"}), 404

# Update operation
@app.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    updated_book_data = request.json
    result = db.CL1.update_one({"isbn": isbn}, {"$set": updated_book_data})  
    if result.modified_count > 0:
        return jsonify({"message": "Book updated successfully!"})
    else:
        return jsonify({"message": "Book not found"}), 404

# Delete operation
@app.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    result = db.CL1.delete_one({"isbn": isbn})  
    if result.deleted_count > 0:
        return jsonify({"message": "Book deleted successfully!"})
    else:
        return jsonify({"message": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5007)
