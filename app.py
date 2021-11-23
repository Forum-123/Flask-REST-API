from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers import books

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to our Flask application"}), 200

@app.route("/books", methods=["GET", "POST"])
def books_handler():
    functions = {
        "GET": books.index,
        "POST": books.create
    }
    resp, code = functions[request.method](request)
    return jsonify(resp), code

@app.route("/books/<int:book_id>", methods=["GET", "PUT", "DELETE"])
def book_handler(book_id):
    functions = {
        "GET": books.show,
        "PUT": books.update,
        "DELETE": books.destroy
    }
    resp, code = functions[request.method](request, book_id)
    return jsonify(resp), code

if __name__ == "__main__":
    app.run(debug=True)
