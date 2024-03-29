from flask import Response, request
from database.models import Books
from flask_restful import Resource

class BooksAPI(Resource):

    def get(self):
        book = Books.objects().to_json()
        return Response(book, mimetype="applicaiton/json", status=200)
    
    def post(self):
        body = request.get_json()
        book = Books(**body).save()
        id = book.id
        return {'id': str(id)}, 200
    
    
class SingleBookAPI(Resource):
    
    def get(self, id):
        book = Books.objects.get(id=id).to_json()
        return Response(book, mimetype="applicaiton/json", status=200)

    def put(self, id):
        body = request.get_json()
        Books.objects.get(id=id).update(**body)
        return 'book updated', 200
    
    def delete(self, id):
        Books.objects.get(id=id).delete()
        return Response("book Deleted Successfully", mimetype="applicaiton/json", status=200)