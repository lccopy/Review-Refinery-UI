from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search', methods=['POST'])
def search():
    keywords = request.form.get('keywords')
    print(keywords)
    if keywords == '' or None:
        print('no keyword --> get back to home')
        return render_template('home.html')
    # Create a dictionary of query parameters
    params = {'query': keywords}

    # Make a GET request to the API with the parameters
    api_url = 'https://systematicreview-m5r6r5yvzq-ew.a.run.app/topic_search'
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return render_template('results.html', recommended_topics=data['recommended_topics'])
    else:
        return "Failed to retrieve data from the API"



@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.template_filter('format_topic')
def format_topic_name(topic_name):
    words = topic_name.split('_')[1:]  # Exclure le premier élément (ID)
    formatted_words = [word.capitalize() for word in words]
    return ' '.join(formatted_words)

if __name__ == '__main__':
    app.run(debug=False)
