# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)


book_list =[
	{

		"id":0,
		"author":"Chinna Acabe",
		"language": "English",
		"title": "Things Fail Apart",
	},
	{

		"id":1,
		"author":"Chinna Acabe",
		"language": "English",
		"title": "Things Fail Apart",
	},
	{

		"id":2,
		"author":"Chinna Acabe",
		"language": "English",
		"title": "Things Fail Apart",
	},{

		"id":3,
		"author":"Chinna Acabe",
		"language": "English",
		"title": "Things Fail Apart",
	}
]
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = "hello world"
		return jsonify({'data': data})


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):

	return jsonify({'data': num**2})



@app.route("/book", methods=['GET','POST'])
def book():
	if request.method == "GET":
		if len(book_list) > 0:
			return jsonify(book_list)
		else:
			'Nothing found', 404

	if request.method == "POST":
		print("post request has been came ")
		new_author=request.form['author']
		
		print(new_author)
		new_language = request.form['language']
		new_title = request.form['title']
		Id= book_list[-1]['id']+	1
		print(Id)

		new_obj ={
			'id':Id,
			'author':new_author,
			'language':new_language,
			'title':new_title

		}
		book_list.append(new_obj)
		return jsonify(book_list), 201



@app.route('/book/<int:id>', methods=['GET','PUT','DELETE'])
def single_book(id):
	if request.method == 'GET':
		for book in book_list:
			if book['id']== id:
				return jsonify[book]
			pass
	if request.method == 'PUT':
		for book in book_list:
			if book['id'] == id:
				book['author'] = request.form['author']
				book['language']= request.form['language']
				book['title']= request.form['title']
				updated_book={
					'id':id,
					'author':book['author'],
					'language':book['language'],
					'title':book['title']
				}

				return jsonify(updated_book)
			
	if request.method =='DELETE':
		for index,book in enumerate(book_list):
			if book['id'] == id:
				book_list.pop(index)
				return jsonify(book_list)
# driver function
if __name__ == '__main__':

	app.run(debug = True)
