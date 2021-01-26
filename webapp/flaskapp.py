from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'ID': 'Prediction 1',
        'author': 'air-drone-ABC',
        'location': 'Orakei Basin',
        'content': '95% likelihood of debris',
        'date_captured': '2021-01-18 11:21am',
        'image': 'p1.png'
    },
    {
        'ID': 'Prediction 2',
        'author': 'air-drone-XYZ',
        'location': 'Orakei Marina',
        'content': '31% likelihood of debris',
        'date_captured': '2021-01-17 2:10pm',
        'image': 'p2.png'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

if __name__ == '__main__':
    app.run(debug=True)