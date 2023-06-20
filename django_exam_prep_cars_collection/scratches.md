[http://localhost:8000/](http://localhost:8000/) - index page <br>
[http://localhost:8000/profile/create](http://localhost:8000/profile/create) - profile create page <br>
[http://localhost:8000/catalogue/](http://localhost:8000/catalogue/) - catalogue page <br>
[http://localhost:8000/car/create/](http://localhost:8000/car/create/) - car create page <br>
[http://localhost:8000/car/1/details/](http://localhost:8000/car/1/details/) - car details page <br>
[http://localhost:8000/car/1/edit/](http://localhost:8000/car/1/edit/) - car edit page <br>
[http://localhost:8000/car/1/delete/ ](http://localhost:8000/car/1/delete/ )- car delete page <br>
[http://localhost:8000/profile/details/](http://localhost:8000/profile/details/) - profile details page <br>
[http://localhost:8000/profile/edit/ ](http://localhost:8000/profile/edit/ )- profile edit page <br>
[http://localhost:8000/profile/delete/](http://localhost:8000/profile/delete/) - profile delete page


You will need 2 models:

•	Car
o	Type

o	Model

o	Year

o	Image Url

o	Price
	Float field, required.
	Price cannot be below 1.	
Note: the validations will be examined only by the user side, not the admin side.
