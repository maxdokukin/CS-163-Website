from flask import Flask, render_template
import os

app = Flask(__name__)

def get_slides(section_path):
    slides_dir = os.path.join(app.template_folder, section_path, 'slides')
    if not os.path.isdir(slides_dir):
        return []
    return sorted([
        f'{section_path}/slides/{filename}'
        for filename in os.listdir(slides_dir)
        if filename.endswith('.html')
    ])

@app.route('/')
def index():
    slides = get_slides('homepage')
    return render_template('homepage/base.html', slides=slides)

@app.route('/sections/objective')
def objective():
    slides = get_slides('sections/objective')
    return render_template('sections/objective/base.html', slides=slides)

@app.route('/sections/methods')
def methods():
    slides = get_slides('sections/methods')
    return render_template('sections/methods/base.html', slides=slides)

@app.route('/sections/findings')
def findings():
    slides = get_slides('sections/findings')
    return render_template('sections/findings/base.html', slides=slides)

@app.route('/sections/data')
def data():
    slides = get_slides('sections/data')
    return render_template('sections/data/base.html', slides=slides)

if __name__ == '__main__':
    app.run(debug=True)
