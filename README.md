# LibratyManagementSystem

##Objective

Design and create backend of a small application of school library management system.



##start the application

1.install all dependencies

>pip install requirements.txt

2.instialize virtual environment

>.venv/Scripts/activate

3.run the server

>uvicorn main:app --reload

4.open swagger ui on the browser(go to the link http://localhost:8000/docs)

##table structures

Book

|id |name |

-id(integer) is the primary key and id of the book

-name(String) is the name of the book

User

|id |name |books_in_hand |

-id(integer) is the primary key and id of the user

-name(String) is the name of the user

-books_in_hand(integer) is the no of books a person posses at a point of time

Inventory

|id |count |total_issues |


-id(integer) is the primary key and id of the book(example if id of a book is 1 then the count of copies in inventory is value in count column corresponding to id==1)

-count(integer) is the no of copies of any book

-total_issues(integer) is no of times a book was issues totally.


top_five_books_in_demand

|id |book_id |book_name |total_issues |

-id(integer) is the primary

-book_id(integer) is the id of the book

-book_name(string) is the name of the book

-total_issues(integer) is the total no of times a book was issues 


 ##Folder structure of the project  
 
	-Library
		
		-__pycache__
		-essential(contains .py that defines methods that defines what an api does )
			-__pycache__
			-book.py
			-inventory.py
			-user.py
		-routers(contains .py files which will handle get and post requests for  the APIs )
			-__pycache__
			-book.py
			-inventory.py
			-user.py
		-__init__.py
		-main.py
		-models.py
		-schemas.py
		-database.py
	-README.md
	-requireents.txt
	-.gitignore
    -book.db
