## Setup

Clone the repository:

```bash
https://github.com/djp9327/chatbot.git
```

To start, it is recommend to create a
[virtual environment](https://virtualenv.pypa.io/en/stable/userguide/). If you have not
used `virtualenv` before, install it with: `pip install virtualenv`.

```bash
# Create a virtual environment to manage dependencies
virtualenv venv
source venv/bin/activate (venv\Scripts\active on Windows)
```

Now install the dependencies with pip:

```bash
# Install requirements.txt
pip install -r requirements.txt
```

After the dependencies have installed, we want to prepare the database.

```bash
# Perform data migrations
python manage.py migrate
```

Now we need to create an initial user for logging into the site

```bash
  python manage.py createsuperuser --username admin --email admin@admin.com
  
  # enter the password when prompted. It can be any password that you wish to use. 
  # It is used for login to the admin website.
  ```
Finally, the database is ready to go! We are now ready to run the server:

```bash
python manage.py runserver
```

## Retro

The model definition is made easy by Django through the ORM.  I knew which models I wanted and the relationships between them (Question, QuestionHistory, Response & User).  Django’s built-in authentication system provides User + login logic right out of the box.  Also, the use of [crispy forms](https://github.com/django-crispy-forms/django-crispy-forms) makes rendering form templates and controlling form logic a breeze.

I did run into a bit of a road block in trying to implement the QuestionHistory table.  I knew ultimately that I wanted the history for a question to be represented in an audit table.  Initially, I went with a prebaked solution: [django-simple-history](https://github.com/treyhunner/django-simple-history).  Adding a HistoricalRecords() object to any model will automatically create an audit table to track that model’s changes over time.  This approach worked well until I needed to tie the Response model to the QuestionHistory.  Since django-simple-history is creating a table behind the scenes, it became difficult to link the Response model to the id of the question history.  I opted for a simple approach by dropping django-simple-history (the irony) and creating an audit table manually, with a foreign key back to the Question model.  In this way, I could link a Response to a Question through the QuestionHistory table.

In the future, I would like to improve upon this setup.  For starters, the UI could use a serious facelift.  But more so, I would like to implement the logic around response processing.  A simple rules-based approach might be the best jumping off point and perhaps, with that in place, moving toward a more robust, machine learning implementation.
