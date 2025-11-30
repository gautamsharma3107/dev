# Flask Web Framework: Complete Guide

---

## Table of Contents
1. [Introduction to Flask](#introduction-to-flask)
2. [Flask Basics](#flask-basics)
3. [Routing and URL Patterns](#routing-and-url-patterns)
4. [Request and Response](#request-and-response)
5. [Templates with Jinja2](#templates-with-jinja2)
6. [Forms with Flask-WTF](#forms-with-flask-wtf)
7. [Database Integration](#database-integration)
8. [Building APIs](#building-apis)
9. [Authentication](#authentication)
10. [Application Structure](#application-structure)
11. [Popular Extensions](#popular-extensions)
12. [Practical Examples](#practical-examples)
13. [Best Practices](#best-practices)
14. [Practice Exercises](#practice-exercises)

---

## Introduction to Flask

### What is Flask?

Flask is a lightweight, flexible web framework for building web applications and APIs in Python.

### Flask Philosophy

```
Micro-framework:
- Small core
- Minimal dependencies
- Easy to learn
- Highly customizable

Not included:
- ORM (use Flask-SQLAlchemy)
- Form validation (use Flask-WTF)
- Authentication (use Flask-Login)
- Admin panel (use Flask-Admin)

You choose what you need!
```

### Flask vs FastAPI vs Django

```
Flask:
- Lightweight
- Flexible
- Great for learning
- Smaller projects

FastAPI:
- Modern async
- Automatic docs
- Type hints
- APIs focused

Django:
- Full-featured
- Batteries included
- Admin panel
- Large projects
```

---

## Flask Basics

### Installation

```bash
# Create virtual environment
python -m venv venv

# Activate
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install Flask
pip install flask
```

### Creating Your First App

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### Running the App

```bash
# Run with python
python app.py

# Or with flask command
flask run

# With custom host/port
flask run --host=0.0.0.0 --port=8000

# In production (do NOT use flask run)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Application Factory Pattern

```python
from flask import Flask

def create_app(config_name='development'):
    app = Flask(__name__)
    
    # Load configuration
    if config_name == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    
    # Register blueprints
    from routes import main_bp, api_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app

# Usage
if __name__ == '__main__':
    app = create_app('development')
    app.run(debug=True)
```

---

## Routing and URL Patterns

### Basic Routes

```python
from flask import Flask

app = Flask(__name__)

# Simple route
@app.route('/')
def index():
    return 'Home Page'

# Route with method
@app.route('/users', methods=['GET'])
def get_users():
    return 'List of users'

# Multiple methods
@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        return 'Data received'
    return 'Get data'
```

### URL Parameters

```python
# Dynamic routes
@app.route('/users/<int:user_id>')
def get_user(user_id):
    return f'User {user_id}'

@app.route('/posts/<slug>')
def get_post(slug):
    return f'Post: {slug}'

# Multiple parameters
@app.route('/users/<int:user_id>/posts/<int:post_id>')
def get_user_post(user_id, post_id):
    return f'User {user_id}, Post {post_id}'

# Optional parameters (use URL query strings)
@app.route('/search')
def search():
    query = request.args.get('q', 'default')
    return f'Search: {query}'
```

### URL Converters

```python
# Built-in converters
@app.route('/post/<int:post_id>')      # Integer
@app.route('/user/<string:username>')   # String
@app.route('/file/<path:filepath>')     # Path
@app.route('/profile/<uuid:user_id>')   # UUID
@app.route('/date/<any(json, csv):fmt>')  # Any

# Custom converter
from werkzeug.routing import BaseConverter

class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split(',')
    
    def to_url(self, value):
        return ','.join(value)

app.url_map.converters['list'] = ListConverter

@app.route('/tags/<list:tags>')
def get_tags(tags):
    return f'Tags: {tags}'  # ['python', 'flask', 'web']
```

### URL Building

```python
from flask import url_for

@app.route('/')
def index():
    # Generate URLs dynamically
    home_url = url_for('index')
    user_url = url_for('get_user', user_id=1)
    search_url = url_for('search', q='python')
    
    return f'''
    <a href="{home_url}">Home</a>
    <a href="{user_url}">User 1</a>
    <a href="{search_url}">Search</a>
    '''
```

---

## Request and Response

### Request Object

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def handle_form():
    # Method
    method = request.method  # 'GET', 'POST'
    
    # Query parameters
    page = request.args.get('page', 1, type=int)
    all_args = request.args.to_dict()
    
    # Form data
    username = request.form.get('username')
    all_form = request.form.to_dict()
    
    # JSON data
    data = request.get_json()
    json_data = request.json
    
    # Headers
    user_agent = request.headers.get('User-Agent')
    auth_header = request.headers.get('Authorization')
    
    # Cookies
    session_id = request.cookies.get('session_id')
    
    # Files
    file = request.files.get('file')
    
    # Raw data
    raw_data = request.data
    
    # URL and path
    full_url = request.url
    path = request.path
    host = request.host
    
    return 'OK'
```

### Response Object

```python
from flask import Flask, Response, jsonify, make_response

app = Flask(__name__)

# String response (default)
@app.route('/text')
def text_response():
    return 'Hello'

# JSON response
@app.route('/json')
def json_response():
    return jsonify({'name': 'Alice', 'age': 25})

# Status codes
@app.route('/created')
def created_response():
    return jsonify({'id': 1}), 201

# Custom response object
@app.route('/custom')
def custom_response():
    response = make_response('Content')
    response.headers['X-Custom'] = 'value'
    response.set_cookie('my_cookie', 'value')
    return response

# Redirect
from flask import redirect, url_for

@app.route('/old')
def old_route():
    return redirect(url_for('new_route'))

# Large response / streaming
@app.route('/large')
def large_response():
    def generate():
        for i in range(1000):
            yield f'Line {i}\n'
    return Response(generate())
```

### Headers and Cookies

```python
from flask import Flask, Response

@app.route('/headers')
def set_headers():
    response = make_response('OK')
    response.headers['X-API-Version'] = '1.0'
    response.headers['Content-Type'] = 'text/plain'
    return response

@app.route('/cookies')
def set_cookies():
    response = make_response('OK')
    response.set_cookie('user_id', '123', max_age=3600)
    response.set_cookie('session', 'abc', secure=True, httponly=True)
    return response

@app.route('/delete-cookie')
def delete_cookie():
    response = make_response('Deleted')
    response.delete_cookie('user_id')
    return response
```

---

## Templates with Jinja2

### Basic Templates

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My App{% endblock %}</title>
</head>
<body>
    <h1>Welcome {{ name }}!</h1>
</body>
</html>
```

### Python Code

```python
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', name='Alice')
```

### Template Variables

```html
<!-- Display variables -->
<p>{{ username }}</p>
<p>{{ user.email }}</p>
<p>{{ items[0] }}</p>

<!-- Filters -->
<p>{{ name|upper }}</p>           <!-- ALICE -->
<p>{{ name|lower }}</p>           <!-- alice -->
<p>{{ name|title }}</p>           <!-- Alice -->
<p>{{ text|truncate(10) }}</p>    <!-- Truncate text -->
<p>{{ items|length }}</p>         <!-- List length -->
<p>{{ price|round(2) }}</p>       <!-- Round to 2 decimals -->
<p>{{ 'Yes' if active else 'No' }}</p>  <!-- Conditional -->
```

### Control Structures

```html
<!-- If/Else -->
{% if user.is_admin %}
    <p>Admin user</p>
{% elif user.is_moderator %}
    <p>Moderator user</p>
{% else %}
    <p>Regular user</p>
{% endif %}

<!-- For loops -->
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% else %}
    <li>No items</li>
{% endfor %}
</ul>

<!-- Loop variables -->
<ul>
{% for item in items %}
    <li>{{ loop.index }}: {{ item }}</li>
{% endfor %}
</ul>

<!-- loop.index, loop.index0, loop.first, loop.last, loop.length -->
```

### Template Inheritance

```html
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My App{% endblock %}</title>
</head>
<body>
    <header>
        <h1>My App</h1>
        <nav>{% block nav %}{% endblock %}</nav>
    </header>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2025 My App</p>
    </footer>
</body>
</html>
```

```html
<!-- child.html -->
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block nav %}
    <a href="/">Home</a>
    <a href="/about">About</a>
{% endblock %}

{% block content %}
    <h2>Welcome!</h2>
    <p>This is the home page.</p>
{% endblock %}
```

### Macros

```html
<!-- Display macro -->
{% macro render_user(user) %}
    <div class="user">
        <h3>{{ user.name }}</h3>
        <p>{{ user.email }}</p>
    </div>
{% endmacro %}

<!-- Use macro -->
{% for user in users %}
    {{ render_user(user) }}
{% endfor %}

<!-- Import macro -->
{% from 'macros.html' import render_user %}
{{ render_user(user) }}
```

---

## Forms with Flask-WTF

### Installation

```bash
pip install flask-wtf
```

### Creating Forms

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=3, max=20)
    ])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=3, max=20)
    ])
    email = StringField('Email', validators=[
        DataRequired(),
        Email()
    ])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password')
    ])
    submit = SubmitField('Register')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[
        DataRequired(),
        Length(min=5, max=500)
    ])
    submit = SubmitField('Post')
```

### Using Forms in Routes

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        # Form is valid, process data
        username = form.username.data
        password = form.password.data
        
        # Verify credentials...
        return redirect(url_for('dashboard'))
    
    return render_template('login.html', form=form)

# With error handling
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        # Check if user exists
        if User.query.filter_by(username=form.username.data).first():
            flash('Username already taken', 'error')
        else:
            # Create user
            user = User(
                username=form.username.data,
                email=form.email.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html', form=form)
```

### Rendering Forms in Templates

```html
<!-- login.html -->
<form method="POST">
    {{ form.hidden_tag() }}
    
    <fieldset>
        <legend>Login</legend>
        
        {{ form.username.label }}
        {% if form.username.errors %}
            {{ form.username(class="input-error") }}
            <span class="error">
                {% for error in form.username.errors %}
                    {{ error }}
                {% endfor %}
            </span>
        {% else %}
            {{ form.username() }}
        {% endif %}
        
        {{ form.password.label }}
        {{ form.password() }}
        
        {{ form.submit() }}
    </fieldset>
</form>
```

### File Uploads

```python
from flask_wtf.file import FileField, FileAllowed
import os

class UploadForm(FlaskForm):
    file = FileField('Upload File', validators=[
        FileAllowed(['jpg', 'png', 'pdf'], 'Files only!')
    ])
    submit = SubmitField('Upload')

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'jpg', 'png', 'pdf'}

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    
    if form.validate_on_submit():
        file = form.file.data
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            flash('File uploaded!', 'success')
    
    return render_template('upload.html', form=form)
```

---

## Database Integration

### Flask-SQLAlchemy Setup

```bash
pip install flask-sqlalchemy
```

### Models

```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    def set_password(self, password):
        from werkzeug.security import generate_password_hash
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
```

### Application Configuration

```python
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()
```

### Migrations with Flask-Migrate

```bash
pip install flask-migrate
```

```python
from flask_migrate import Migrate

migrate = Migrate(app, db)
```

```bash
# Initialize migrations
flask db init

# Create migration
flask db migrate -m "Add post model"

# Apply migration
flask db upgrade

# Rollback
flask db downgrade
```

### Database Operations

```python
# Create
user = User(username='alice', email='alice@example.com')
user.set_password('password123')
db.session.add(user)
db.session.commit()

# Read
user = User.query.filter_by(username='alice').first()
all_users = User.query.all()
user = User.query.get(1)

# Update
user.email = 'new@example.com'
db.session.commit()

# Delete
db.session.delete(user)
db.session.commit()

# Query
users = User.query.filter(User.created_at > some_date).all()
count = User.query.count()
```

---

## Building APIs

### Flask-RESTful

```bash
pip install flask-restful
```

```python
from flask_restful import Api, Resource, reqparse

api = Api(app)

class UserListAPI(Resource):
    def get(self):
        users = User.query.all()
        return {
            'status': 'success',
            'data': [{'id': u.id, 'username': u.username} for u in users]
        }
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('password', required=True)
        args = parser.parse_args()
        
        user = User(username=args['username'], email=args['email'])
        user.set_password(args['password'])
        db.session.add(user)
        db.session.commit()
        
        return {
            'status': 'created',
            'id': user.id
        }, 201

class UserAPI(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
    
    def put(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('email')
        args = parser.parse_args()
        
        if args['username']:
            user.username = args['username']
        if args['email']:
            user.email = args['email']
        
        db.session.commit()
        return {'status': 'updated'}
    
    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        
        db.session.delete(user)
        db.session.commit()
        return {'status': 'deleted'}

# Register API resources
api.add_resource(UserListAPI, '/api/users')
api.add_resource(UserAPI, '/api/users/<int:user_id>')
```

### Flask-RESTX

```bash
pip install flask-restx
```

```python
from flask_restx import Api, Resource, fields, Namespace

api = Api(app, version='1.0', title='My API')
ns = api.namespace('users', description='User operations')

# Define models
user_model = api.model('User', {
    'id': fields.Integer(required=True),
    'username': fields.String(required=True),
    'email': fields.String(required=True)
})

@ns.route('/')
class UserList(Resource):
    @ns.doc('list_users')
    def get(self):
        '''List all users'''
        return [{'id': 1, 'username': 'alice', 'email': 'alice@example.com'}]
    
    @ns.expect(user_model)
    @ns.response(201, 'User created')
    def post(self):
        '''Create new user'''
        return api.payload, 201

@ns.route('/<int:id>')
class User(Resource):
    @ns.doc('get_user')
    @ns.marshal_with(user_model)
    def get(self, id):
        '''Get user by ID'''
        return {'id': id, 'username': 'alice', 'email': 'alice@example.com'}
```

---

## Authentication

### Flask-Login

```bash
pip install flask-login
```

```python
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect to login

class User(UserMixin, db.Model):
    # ... model fields ...
    pass

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials', 'error')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Protect routes
from flask_login import login_required

@app.route('/dashboard')
@login_required
def dashboard():
    return f'Hello {current_user.username}'

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)
```

---

## Application Structure

### Project Layout

```
myapp/
├── app.py                 # Main application
├── config.py              # Configuration
├── requirements.txt       # Dependencies
├── wsgi.py               # WSGI entry point
├── app/
│   ├── __init__.py        # App factory
│   ├── models.py          # Database models
│   ├── forms.py           # WTForms forms
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py        # Main blueprint
│   │   ├── auth.py        # Auth blueprint
│   │   └── api.py         # API blueprint
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   └── dashboard.html
│   └── static/
│       ├── css/
│       ├── js/
│       └── images/
└── migrations/            # Database migrations
```

### Application Factory

```python
# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_name='development'):
    app = Flask(__name__)
    
    # Load config
    if config_name == 'production':
        from config import ProductionConfig
        app.config.from_object(ProductionConfig)
    else:
        from config import DevelopmentConfig
        app.config.from_object(DevelopmentConfig)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    # Register blueprints
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.api import api_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app
```

### Blueprints

```python
# app/routes/main.py
from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

# app/routes/auth.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app import db
from app.models import User
from app.forms import LoginForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
```

---

## Popular Extensions

### Flask-Mail

```bash
pip install flask-mail
```

```python
from flask_mail import Mail, Message

mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your@email.com'
app.config['MAIL_PASSWORD'] = 'password'

@app.route('/send-email')
def send_email():
    msg = Message('Hello', sender='from@example.com', recipients=['to@example.com'])
    msg.body = 'This is the body'
    msg.html = '<p>This is HTML</p>'
    mail.send(msg)
    return 'Email sent'
```

### Flask-Caching

```bash
pip install flask-caching
```

```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/expensive')
@cache.cached(timeout=300)  # Cache for 5 minutes
def expensive_operation():
    # Do expensive work...
    return 'Result'

# Clear cache
cache.clear()
```

### Flask-CORS

```bash
pip install flask-cors
```

```python
from flask_cors import CORS

CORS(app)

# Or specific routes
@app.route('/api/data')
@cross_origin()
def get_data():
    return {'data': 'value'}
```

---

## Practical Examples

### Complete Blog Application

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.secret_key = 'secret'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255))
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username exists', 'error')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        post = Post(title=title, content=content, author=current_user)
        db.session.add(post)
        db.session.commit()
        
        flash('Post created!', 'success')
        return redirect(url_for('index'))
    
    return render_template('create_post.html')

@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        flash('Post not found', 'error')
        return redirect(url_for('index'))
    return render_template('view_post.html', post=post)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

---

## Best Practices

### Code Organization

```
✓ Use blueprints for modular code
✓ Separate models, forms, routes
✓ Use application factory
✓ Configuration management
✓ Logging and error handling
```

### Security

```
✓ Use HTTPS in production
✓ Set SECRET_KEY securely
✓ Hash passwords
✓ CSRF protection (Flask-WTF)
✓ Validate input
✓ SQL injection prevention (use ORM)
✓ XSS prevention (template escaping)
```

### Performance

```
✓ Use caching
✓ Database query optimization
✓ Use CDN for static files
✓ Minimize templates
✓ Use production WSGI server
```

---

## Practice Exercises

### 1. Basic App
- Create simple Flask app
- Add routes
- Render templates

### 2. Database
- Create models
- Add/query records
- Relationships

### 3. Forms
- Create forms
- Validate input
- Handle file uploads

### 4. Authentication
- User registration
- Login/logout
- Protected routes

### 5. Blog App
- Users, posts, comments
- Full CRUD
- Relationships

### 6. REST API
- Create endpoints
- JSON responses
- Error handling

---

# End of Notes
