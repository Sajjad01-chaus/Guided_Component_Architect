from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def preview():
    html = open("generated_component/component.html").read()
    css = open("generated_component/component.css").read()

    return render_template_string(f"""
    <html>
    <head><style>{css}</style></head>
    <body>{html}</body>
    </html>
    """)

if __name__ == "__main__":
    app.run(port=5000)