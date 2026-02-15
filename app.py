from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>E-Commerce App</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">

<style>
body {
    margin: 0;
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #667eea, #764ba2);
}

header {
    background: #222;
    color: white;
    padding: 15px;
    text-align: center;
    font-size: 24px;
    font-weight: 600;
}

.container {
    padding: 30px;
    max-width: 1200px;
    margin: auto;
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 25px;
}

.card {
    background: white;
    border-radius: 15px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    overflow: hidden;
    transition: transform 0.3s ease;
}

.card:hover {
    transform: translateY(-8px);
}

.card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.card-content {
    padding: 20px;
    text-align: center;
}

.product-title {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 10px;
}

.price {
    color: #764ba2;
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 15px;
}

.btn {
    background: linear-gradient(135deg, #ff7a18, #ffb347);
    border: none;
    padding: 10px 18px;
    border-radius: 25px;
    color: white;
    font-weight: 500;
    cursor: pointer;
}

footer {
    text-align: center;
    padding: 15px;
    color: white;
    margin-top: 30px;
}
</style>
</head>

<body>

<header>🛒 My E-Commerce Store</header>

<div class="container">
    <div class="product-grid">

        <div class="card">
            <img src="https://picsum.photos/300/200?1">
            <div class="card-content">
                <div class="product-title">Wireless Headphones</div>
                <div class="price">₹2,499</div>
                <button class="btn">Add to Cart</button>
            </div>
        </div>

        <div class="card">
            <img src="https://picsum.photos/300/200?2">
            <div class="card-content">
                <div class="product-title">Smart Watch</div>
                <div class="price">₹3,999</div>
                <button class="btn">Add to Cart</button>
            </div>
        </div>

        <div class="card">
            <img src="https://picsum.photos/300/200?3">
            <div class="card-content">
                <div class="product-title">Gaming Mouse</div>
                <div class="price">₹1,299</div>
                <button class="btn">Add to Cart</button>
            </div>
        </div>

        <div class="card">
            <img src="https://picsum.photos/300/200?4">
            <div class="card-content">
                <div class="product-title">Laptop Backpack</div>
                <div class="price">₹1,799</div>
                <button class="btn">Add to Cart</button>
            </div>
        </div>

    </div>
</div>

<footer>© 2026 My E-Commerce App | Flask</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(debug=True)
