books = [
    {"id": 1, "title": "Dune", "authors": ["Frank Herbert"], "year": 1965, "genre": "Sci-fi"},
    {"id": 2, "title": "The Hobbit", "authors": ["J. R. R. Tolkien"], "year": 1937, "genre": "Fantasy"},
    {"id": 3, "title": "Carrie", "authors": ["Stephen King"], "year": 1974, "genre": "Horror"},
    {"id": 4, "title": "To Kill a Mockingbird", "authors": ["Harper Lee"], "year": 1960, "genre": "Southern Gothic"},
    {"id": 5, "title": "Perfume: The Story of a Murderer", "authors": ["Patrick Süskind"], "year": 1985, "genre": "Magical Realism"}
]

def index(req):
    return [b for b in books], 200

def find_by_id(bid):
    try:
        book = [b for b in books if b['id'] == bid]
        if len(book) == 0:
            return f"No book found with id of {bid}"
        return book[0]
    except:
        raise Exception(f"No book found with id of {bid}")

def show(req, bid):
    return find_by_id(bid), 200

def create(req):
    new_book = req.get_json()
    new_book["id"] = sorted([b["id"] for b in books])[-1] + 1
    books.append(new_book)
    return new_book, 201

def update(req, bid):
    book = find_by_id(bid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        book[key] = val
    return book, 200

def destroy(req, bid):
    book = find_by_id(bid)
    books.remove(book)
    return f"Book {bid} has been deleted", 204