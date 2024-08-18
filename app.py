from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import nltk
import spacy
import re
from flask_cors import CORS
from c2 import *

# Download necessary NLP models
nltk.download('punkt')
spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # This will enable CORS for all origins
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    response = process_message(msg)
    if not response:
        response = "I'm sorry, I didn't understand that. Can you please specify what kind of HTML/CSS components you need help with?"
    emit('response', response)
    print(response)


def process_message(message):
    info = extract_info(message)
    html, css, js = generate_code(info)
    if css == """<style>
    </style>
    """:
        css = ""

    if not html and not css and not js:
        return None  # Return None to trigger the default response

    response = ""
    if html:
        response += "HTML:\n" + html
    if css:
        response += "CSS:\n" + css
    if js:
        response += "JavaScript:\n" + js

    return response.strip()

def extract_info(message):
    message = message.lower()

    input_types = [
        "button", "checkbox", "color", "date", "datetime-local", "email", "file",
        "hidden", "image", "month", "number", "password", "radio", "range", "reset",
        "search", "submit", "tel", "text", "time", "url", "week"
    ]
    form_elements = re.findall(r'(\d+)\s*({})\s*inputs?'.format('|'.join(input_types)), message)
    other_elements = re.findall(r'(\d+)\s*(labels?|selects?|textareas?|buttons?)', message)
    color_match = re.search(r'background\s*color\s*(\w+)', message)
    nav_match = re.search(r'navbar', message)
    login_form_match = re.search(r'login\s*form', message)
    form_match = re.search(r'form', message)
    card_match=re.search(r'card',message)
    hero_match=re.search(r'hero',message)
    table_match=re.search(r'table',message)
    alert_match=re.search(r'alert',message)
    footer_match=re.search(r'footer',message)

    info = {
        'inputs': [],
        'labels': 0,
        'selects': 0,
        'textareas': 0,
        'buttons': 0,
        'background_color': color_match.group(1) if color_match else None,
        'navbar': bool(nav_match),
        'form': bool(form_match),
        'login_form': bool(login_form_match),
        'card':bool(card_match),
        'table':bool(table_match),
        'hero':bool(hero_match),
        'alert':bool(alert_match),
        'footer':bool(footer_match)
    }

    for count, input_type in form_elements:
        count = int(count)
        info['inputs'].append((count, input_type))

    for count, element in other_elements:
        count = int(count)
        if 'label' in element:
            info['labels'] += count
        elif 'select' in element:
            info['selects'] += count
        elif 'textarea' in element:
            info['textareas'] += count
        

    if login_form_match:
        form_elements = re.findall(r'(\d+)\s*(emails?|select?|username?|password?|button?)', message)
        for count, element in form_elements:
            count = int(count)
            if 'email' in element:
                info['inputs'].append((count, 'email'))
            elif 'select' in element:
                info['selects'] += count
            elif 'username' in element:
                info['inputs'].append((count, 'text'))
            elif 'password' in element:
                info['inputs'].append((count, 'password'))
            elif 'button' in element:
                info['buttons'] += count
    elif form_match:
        # Extracting elements for a general form
        form_elements = re.findall(r'(\d+)\s*(input?|textarea?|label?|select?|button?)', message)
        for count, input_type in form_elements:
            count = int(count)
            if 'input' in input_type:
                info['inputs'].append((count, 'text'))  # Assuming default input type is text
            elif 'textarea' in input_type:
                info['textareas'] += count
            elif 'label' in input_type:
                info['labels'] += count
            elif 'select' in input_type:
                info['selects'] += count
            elif 'button' in input_type:
                info['buttons'] += count    

    return info

def generate_code(info):
    html = ""
    css = "<style>"
    js = ""

    if info['navbar']:
        html += generate_navbar()
        css +=cssNav()
       
    if info['card']:
        html +=generate_cards()
        css += cssCards()

    if info['table']:
        html +=generate_table()
        css += cssTable()

    if info['hero']:
        html += generate_hero_section()
        css+= cssHero()

    if info['alert']:
        html+= generate_alerts()
        css += cssAlerts()

    if info['footer']:
        html += generate_footer()
        css += cssFooter()

    if info['login_form']:
        if not info['inputs']:
            html += generate_login_form()
            css += cssLogin()
        else:
            html += "<form>\n"
            for count, input_type in info['inputs']:
                for i in range(count):
                    html += f"  <input type='{input_type}' placeholder='Input {i + 1} ({input_type})'>\n"
            for i in range(info['selects']):
                html += "  <select>\n    <option>Option 1</option>\n    <option>Option 2</option>\n  </select>\n"
            for i in range(info['buttons']):
                html += "  <button type='submit'>Submit</button>\n"
            html += "</form>\n"

    if info['form']:
        html += "<form>\n"
        for count, input_type in info['inputs']:
            for i in range(count):
                html += f"  <input type='{input_type}' placeholder='Input {i + 1} ({input_type})'>\n"
        for i in range(info['labels']):
            html += f"  <label>Label {i + 1}</label>\n"
        for i in range(info['selects']):
            html += "  <select>\n    <option>Option 1</option>\n    <option>Option 2</option>\n  </select>\n"
        for i in range(info['textareas']):
            html += f"  <textarea placeholder='Textarea {i + 1}'></textarea>\n"
        for i in range(info['buttons']):
            html += f"  <button type='submit'>Button {i + 1}</button>\n"
        html += "</form>\n"

    if info['background_color']:
        css += f"""
        component {{
        background-color: {info['background_color']};
        }}"""

    # code for only html
    if info.get('html', True) and info.get('css', True):
        return html, css + """
    </style>
    """, js
    elif info.get('html', True):
        return html, "", ""
    elif info.get('css', True):
        return "", css + """
    </style>""", ""
    else:
        return html, css + """
</style>
    """, js

if __name__ == '__main__':
    socketio.run(app, debug=True)
