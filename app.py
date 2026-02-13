from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

app = Flask(__name__)


def get_db():
    def build_mongo_uri():
        # Prefer a full MONGO_URI if provided
        uri = os.getenv('MONGO_URI')
        if uri:
            return uri
        # Otherwise build from separate vars and encode password
        user = os.getenv('MONGO_USER')
        pwd = os.getenv('MONGO_PASS')
        host = os.getenv('MONGO_HOST', 'cluster0.mongodb.net')
        dbname = os.getenv('MONGO_DB', '')
        if not (user and pwd):
            return None
        pwd_enc = quote_plus(pwd)
        db_path = f"/{dbname}" if dbname else ''
        return f"mongodb+srv://{user}:{pwd_enc}@{host}{db_path}?retryWrites=true&w=majority"

    uri = build_mongo_uri()
    if not uri:
        return None, 'MONGO_URI or MONGO_USER/MONGO_PASS not set in environment'
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        # ensure connection
        client.admin.command('ping')
        db = client.get_default_database()
        if db is None:
            db = client['test']
        return db, None
    except Exception as e:
        return None, str(e)


@app.route('/api')
def api_list():
    db, err = get_db()
    if err:
        return jsonify({'error': err}), 500
    try:
        coll = db['submissions']
        data = list(coll.find({}, {'_id': 0}))
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    doc = {'name': name, 'email': email, 'message': message}

    db, err = get_db()
    if err:
        return render_template('index.html', error=err, form=doc)

    try:
        coll = db['submissions']
        coll.insert_one(doc)
        return redirect(url_for('success'))
    except Exception as e:
        return render_template('index.html', error=str(e), form=doc)


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
