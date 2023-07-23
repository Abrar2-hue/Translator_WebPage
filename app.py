from flask import Flask, render_template, request
from deep_translator import MyMemoryTranslator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def translator():
    
    if request.method == 'POST':
        if 'english-input' in request.form:
            english_text = request.form['english-input']
            translation = english_to_french(english_text)
            return render_template('web.html', translation=translation, original=english_text, direction="English to French")
        elif 'french-input' in request.form:
            french_text = request.form['french-input']
            translation = french_to_english(french_text)
            return render_template('web.html', translation=translation, original=french_text, direction="French to English")
    return render_template('web.html')

def english_to_french(text):
    translator = MyMemoryTranslator(source='english', target='french')  # Updated language codes
    translation = translator.translate(text)
    return translation

def french_to_english(text):
    translator = MyMemoryTranslator(source='french', target='english')  # Updated language codes
    translation = translator.translate(text)
    return translation

if __name__ == '__main__':
    app.run(debug=True)