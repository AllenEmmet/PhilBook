from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models import user
class Comment:
    db = 'newPhil'
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.post_id = data['post_id']
        self.user = None

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO comments (content, user_id, post_id) VALUES (%(content)s, %(user_id)s, %(post_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_comments(cls, data):
        query="SELECT * FROM comments JOIN users on users.id = comments.user_id WHERE comments.post_id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        
        comments = []
        if results:
            for row in results:
                user_data = {
                'id': row['users.id'], 
                'first_name': row['first_name'], 
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
                this_user = user.User(user_data)
                comment = cls(row)
                comment.user = this_user
                comments.append(comment)
        return comments

    @classmethod
    def delete_comment(cls, data):
        query = "DELETE FROM comments WHERE comments.id = %(id)s;"
        print('is this running')
        return connectToMySQL(cls.db).query_db(query, data)