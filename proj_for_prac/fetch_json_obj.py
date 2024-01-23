from flask import Flask,request, jsonify # which conver dict to json obj
app = Flask(__name__)


books_db = [
    {
        'name': 'Physic',          
        'price': 250
    },
    {
         'name': 'Maths',    
        'price': 250
    }    
]


#reterive all the books
@app.route('/books')      # http://127.0.0.1:5000/books
def get_all_books():
    return jsonify({'books':books_db})



#retrieve one books 
@app.route('/book/<string:name>')     #http://127.0.0.1:5000/book/Physic
def get_one_book(name):
    for book in books_db:
        if book['name'] ==  name:
            return jsonify(book)
            
     
    return jsonify({'message':'Book not found'}) 



#create a book
@app.route('/book', methods = ['POST'])    #http://127.0.0.1:5000/book   #POST API
def create_book():
    req_data = request.get_json()      
    if req_data:
        books_db.append(req_data)
        return jsonify({'message': 'Data has been created'})
    else:
        return jsonify({'message': 'Invalid or empty body'}), 400   #400 Bad request





# app.run(port = 5000)
if __name__ == '__main__':
    app.run(debug=True)


