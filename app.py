from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>E-Commerce App</title>
</head>
<body style="font-family: Arial; text-align:center;">
<h1>🛒 My E-Commerce Store</h1>
<p>App is running successfully 🚀</p>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)


# ✅ HEALTH CHECK ENDPOINT
@app.route("/health")
def health():
    return jsonify(
        status="UP",
        message="Application is healthy"
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
