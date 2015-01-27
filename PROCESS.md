25/01/2014
----------
- pip3 install Flask

26/01/2014
----------
- Basic 'Hello World' Flask App
- Install Psycopg2, Flask-SQLAlchemy & Flask-Migrate
- Create a new postgres user and associate it with a new postgres database
- Connect database within app.db using SQLAlchemy
- Create Guestbook 'Post' model
- Initialise, Migrate and Upgrade our Database
- pip3 install requests for use with form.
- Copy templates over from guestbook-2.0 (django app) to flask templates folder
- Add static files (img, css) to flask static folder
- Display the latest ten posts in descending order (according to date) in index
- db.drop_table() will rid table complete. Need to create again with python3 manage.py db migrate + python3 manage.py db upgrade
- Add links to form submission and home page in templates
- Wrote form submission view "add_post"
- Website URL validation with 'request' package
- Flask port complete (refactoring and tests next)
- Add CSRF Token Protection with Flask-SeaSurf
