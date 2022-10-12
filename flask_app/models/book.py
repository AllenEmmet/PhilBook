from flask_app.config.mysqlconnections import connectToMySQL

class Book:
    db = 'newPhil'
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO books (title, author) VALUES (%(title)s, %(author)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL(cls.db).query_db(query)
        books = []
        for row in results:
            book = cls(row)
            books.append(book)
            
        return books

    @classmethod
    def get_one_id(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        if (connectToMySQL(cls.db).query_db(query, data)[0]):
            responses = connectToMySQL(cls.db).query_db(query, data)[0]
        else:
            responses = None
        return cls(responses)
    
    
