# Generate HTML/CSS code for a navbar
def generate_navbar():
    return """
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
    <style>
        nav{
            width:100%;
            height:200px;
        }
        nav ul {
            list-style-type: none;
            padding: 0;
        }
        nav ul li {
            display: inline;
            margin-right: 10px;
        }
        nav ul li a {
            color: white;
            text-decoration: none;
        }
    </style>
    """


# Generate HTML/CSS code for a form
def generate_form_code(num_inputs):
    form_html = '<form>\n'
    for i in range(num_inputs):
        form_html += f'    <label for="input{i + 1}">Input {i + 1}:</label><br>\n'
        form_html += f'    <input type="text" id="input{i + 1}" name="input{i + 1}"><br><br>\n'
        form_html += '    <input type="submit" value="Submit">\n'
        form_html += '</form>\n'
    return form_html


def generate_login_form():
    return """
    <form action="/submit-form" method="post">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name"><br><br>
        
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email"><br><br>
        
        <label for="age">Age:</label><br>
        <input type="number" id="age" name="age"><br><br>
        
        <label for="gender">Gender:</label><br>
        <select id="gender" name="gender">
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
        </select><br><br>
        
        <label for="bio">Biography:</label><br>
        <textarea id="bio" name="bio" rows="4" cols="50"></textarea><br><br>
        
        <input type="submit" value="Submit">
    </form>
    """
def cssLogin():
    return """
    /* Styles for the form container */
form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    background-color: #f9f9f9;
}

/* Styles for form labels */
label {
    display: block;
    margin-bottom: 8px;
    font-weight: bold;
}

/* Styles for form inputs */
input[type="text"],
input[type="email"],
input[type="number"],
select,
textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box;
}

/* Styles for the submit button */
input[type="submit"] {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
}

/* Hover effect for the submit button */
input[type="submit"]:hover {
    background-color: #45a049;
}

    """


def cssform():
    return """
        form {
            max-width: 300px;
            margin: 0 auto;
        }
        label, input {
            display: block;
            margin-bottom: 10px;
        }
    """
# Generate HTML/CSS code for cards
def generate_cards(num_cards):
    card_html = ''
    for i in range(num_cards):
        card_html += f"""
        <div class="card">
            <img src="" alt="">
            <h2>Card {i + 1} Title</h2>
            <p>Some example text. Some example text.</p>
        </div>\n"""
    return card_html
def cssCards():
    return """
    .card {
        padding: 20px;
        margin: 20px;
        border: 1px solid #ccc;
        box-shadow: 2px 2px 12px #aaa;
    }
    """

# Generate HTML/CSS code for a component with a gradient background
def cssBackgroundColor(color):
    return f"""
    {color[0]} {{ 
    background: {color[1]} ;
    }} """


# Generate HTML/CSS code for a big button
def generate_big_button():
    return """
    <button class="big-button">Big Button</button>
    <style>
        .big-button {
            font-size: 20px;
            padding: 10px 20px;
        }
    </style>
    """


# Generate HTML/CSS code for a component centered on the page
def generate_centered_component():
    return """
    <div class="centered-component">
    </div>
    <style>
        .centered-component {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
    </style>
    """
def csscenter(component):
    return """
    {component} {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
    }
    """

# Generate HTML/CSS code for a button that links to another page
def click_Button():
    return """
    <a href="another_page.html" class="link-button">Go to Another Page</a>
    <style>
        .link-button {
            display: inline-block;
            padding: 10px 20px;
            color: white;
            background-color: blue;
            text-decoration: none;
            border-radius: 5px;
        }
    </style>
    """

def generate_table():
    return """
<table>
    <thead>
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
            <th>Header 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Row 1, Cell 1</td>
            <td>Row 1, Cell 2</td>
            <td>Row 1, Cell 3</td>
        </tr>
        <tr>
            <td>Row 2, Cell 1</td>
            <td>Row 2, Cell 2</td>
            <td>Row 2, Cell 3</td>
        </tr>
        <tr>
            <td>Row 3, Cell 1</td>
            <td>Row 3, Cell 2</td>
            <td>Row 3, Cell 3</td>
        </tr>
    </tbody>
</table>
    """
def cssTable():
    return
"""
    table {
            width: 50%;
            border-collapse: collapse;
        }
    th, td {
        border: 1px solid black;
        padding: 8px;
        text-align: left;
    }
    th {
        background-color: #f2f2f2;
    }
"""
#herSection
def generate_hero_section(arr):
    return f"""
    <section class="hero">
        <div class="hero-background" style="background-image: url(background_image);"></div>
        <h1>{arr[0]}</h1>
        <p>{arr[1]}</p>
    </section>
    """
def cssHero():
    return """
        .hero {{
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
        }}
        .hero-background {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-size: cover;
            background-position: center;
        }}
    """

def generate_footer(copyright_text, social_media_links):
    return f"""
    <footer>
        <p>{copyright_text}</p>
        <ul class="social-media">
            {social_media_links}
        </ul>
    </footer>"""
def cssFooter():
    return """
        footer {{
            background-color: #333;
            color: white;
            padding: 20px;
            text-align: center;
        }}
        .social-media {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}
        .social-media li {{
            display: inline-block;
            margin-right: 10px;
        }}
        .social-media li a {{
            color: white;
            text-decoration: none;
        }}
    </style>
    """

def generate_alerts(alert_type, alert_text):
    return f"""
    <div class="alert {alert_type}">
        {alert_text}
    </div>"""
def cssAlerts():
    return """
    <style>
        .alert {
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .alert.success {
            background-color: #dff0d8;
            color: #3c763d;
        }
        .alert.error {
            background-color: #f2dede;
            color: #a94442;
        }
        .alert.warning {
            background-color: #fcf8e3;
            color: #8a6d3b;
        }
    </style>
    """

