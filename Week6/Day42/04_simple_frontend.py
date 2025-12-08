"""
Day 42 - Simple Frontend Development
======================================
Learn: Creating simple frontend interfaces for ML applications

Key Concepts:
- Serving static files with FastAPI
- HTML/JavaScript for API interaction
- Template rendering with Jinja2
- Basic styling with CSS
"""

# ========== SETUP ==========
print("=" * 60)
print("SIMPLE FRONTEND DEVELOPMENT")
print("=" * 60)

print("""
A frontend interface allows users to:
- Input data for predictions
- View results visually
- Browse prediction history
- Monitor model performance
""")

# ========== HTML TEMPLATE ==========
print("\n" + "=" * 60)
print("1. BASIC HTML TEMPLATE")
print("=" * 60)

html_template = '''
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ML Prediction Service</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>🤖 ML Prediction Service</h1>
            <p>Enter your features to get predictions</p>
        </header>
        
        <main>
            <!-- Prediction Form -->
            <section class="card">
                <h2>Make Prediction</h2>
                <form id="predictionForm">
                    <div class="form-group">
                        <label for="features">Features (comma-separated):</label>
                        <input 
                            type="text" 
                            id="features" 
                            placeholder="e.g., 5.1, 3.5, 1.4, 0.2"
                            required
                        >
                    </div>
                    <button type="submit" class="btn-primary">
                        🎯 Predict
                    </button>
                </form>
                
                <!-- Result Display -->
                <div id="result" class="result hidden">
                    <h3>Prediction Result</h3>
                    <div id="predictionValue" class="prediction-value"></div>
                    <div id="confidence" class="confidence"></div>
                </div>
            </section>
            
            <!-- Prediction History -->
            <section class="card">
                <h2>Recent Predictions</h2>
                <button onclick="loadHistory()" class="btn-secondary">
                    🔄 Refresh
                </button>
                <div id="history">
                    <table id="historyTable">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Features</th>
                                <th>Prediction</th>
                                <th>Time</th>
                            </tr>
                        </thead>
                        <tbody id="historyBody">
                        </tbody>
                    </table>
                </div>
            </section>
        </main>
        
        <footer>
            <p>ML Prediction Service v1.0.0</p>
        </footer>
    </div>
    
    <script src="/static/app.js"></script>
</body>
</html>
'''
print(html_template)

# ========== CSS STYLES ==========
print("\n" + "=" * 60)
print("2. CSS STYLES")
print("=" * 60)

css_styles = '''
/* static/style.css */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    padding: 20px;
}

.container {
    max-width: 800px;
    margin: 0 auto;
}

header {
    text-align: center;
    color: white;
    margin-bottom: 30px;
}

header h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
}

.card {
    background: white;
    border-radius: 15px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
}

.card h2 {
    color: #333;
    margin-bottom: 20px;
    border-bottom: 2px solid #667eea;
    padding-bottom: 10px;
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 8px;
    font-weight: 600;
    color: #555;
}

.form-group input {
    width: 100%;
    padding: 12px 15px;
    border: 2px solid #ddd;
    border-radius: 8px;
    font-size: 16px;
    transition: border-color 0.3s;
}

.form-group input:focus {
    outline: none;
    border-color: #667eea;
}

.btn-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 12px 30px;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
}

.btn-secondary {
    background: #f0f0f0;
    color: #333;
    border: none;
    padding: 8px 20px;
    border-radius: 6px;
    cursor: pointer;
    margin-bottom: 15px;
}

.btn-secondary:hover {
    background: #e0e0e0;
}

.result {
    margin-top: 25px;
    padding: 20px;
    background: #f8f9fa;
    border-radius: 10px;
    text-align: center;
}

.result.hidden {
    display: none;
}

.prediction-value {
    font-size: 3em;
    font-weight: bold;
    color: #667eea;
    margin: 15px 0;
}

.confidence {
    color: #666;
    font-size: 14px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
}

th, td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #eee;
}

th {
    background: #f8f9fa;
    font-weight: 600;
    color: #555;
}

tr:hover {
    background: #f8f9fa;
}

footer {
    text-align: center;
    color: rgba(255, 255, 255, 0.7);
    margin-top: 30px;
}

/* Loading spinner */
.loading {
    display: inline-block;
    width: 20px;
    height: 20px;
    border: 3px solid #f3f3f3;
    border-top: 3px solid #667eea;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* Responsive */
@media (max-width: 600px) {
    header h1 {
        font-size: 1.8em;
    }
    
    .card {
        padding: 15px;
    }
}
'''
print(css_styles)

# ========== JAVASCRIPT ==========
print("\n" + "=" * 60)
print("3. JAVASCRIPT FOR API INTERACTION")
print("=" * 60)

javascript = '''
// static/app.js

const API_BASE = '';  // Same origin

// Handle prediction form submission
document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const featuresInput = document.getElementById('features').value;
    const features = featuresInput.split(',').map(x => parseFloat(x.trim()));
    
    // Validate input
    if (features.some(isNaN)) {
        alert('Please enter valid numbers separated by commas');
        return;
    }
    
    // Show loading state
    const button = e.target.querySelector('button');
    const originalText = button.innerHTML;
    button.innerHTML = '<span class="loading"></span> Predicting...';
    button.disabled = true;
    
    try {
        const response = await fetch(`${API_BASE}/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ features })
        });
        
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        
        const data = await response.json();
        displayResult(data);
        loadHistory();  // Refresh history
        
    } catch (error) {
        alert(`Prediction failed: ${error.message}`);
    } finally {
        button.innerHTML = originalText;
        button.disabled = false;
    }
});

// Display prediction result
function displayResult(data) {
    const resultDiv = document.getElementById('result');
    const predValue = document.getElementById('predictionValue');
    const confidence = document.getElementById('confidence');
    
    resultDiv.classList.remove('hidden');
    predValue.textContent = data.prediction.toFixed(4);
    
    if (data.confidence) {
        confidence.textContent = `Confidence: ${(data.confidence * 100).toFixed(1)}%`;
    } else {
        confidence.textContent = `Model: ${data.model_version}`;
    }
}

// Load prediction history
async function loadHistory() {
    try {
        const response = await fetch(`${API_BASE}/predictions?per_page=10`);
        const data = await response.json();
        
        const tbody = document.getElementById('historyBody');
        tbody.innerHTML = '';
        
        data.predictions.forEach(pred => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${pred.id}</td>
                <td>${JSON.stringify(pred.input_features)}</td>
                <td>${pred.prediction.toFixed(4)}</td>
                <td>${new Date(pred.created_at).toLocaleString()}</td>
            `;
            tbody.appendChild(row);
        });
        
    } catch (error) {
        console.error('Failed to load history:', error);
    }
}

// Load history on page load
document.addEventListener('DOMContentLoaded', loadHistory);
'''
print(javascript)

# ========== FASTAPI STATIC FILES ==========
print("\n" + "=" * 60)
print("4. FASTAPI SERVING STATIC FILES")
print("=" * 60)

fastapi_static = '''
# main.py - Serving static files and templates

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(title="ML Prediction Service")

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Serve index page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the main HTML page"""
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "ML Prediction Service"}
    )

# Alternative: Serve HTML directly without Jinja2
@app.get("/simple", response_class=HTMLResponse)
async def simple_page():
    """Serve simple HTML without template engine"""
    return """
    <!DOCTYPE html>
    <html>
    <head><title>Simple ML App</title></head>
    <body>
        <h1>ML Prediction</h1>
        <form id="form">
            <input id="features" placeholder="Enter features">
            <button type="submit">Predict</button>
        </form>
        <div id="result"></div>
        <script>
            document.getElementById('form').onsubmit = async (e) => {
                e.preventDefault();
                const features = document.getElementById('features')
                    .value.split(',').map(Number);
                const resp = await fetch('/predict', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({features})
                });
                const data = await resp.json();
                document.getElementById('result').innerText = 
                    'Prediction: ' + data.prediction;
            };
        </script>
    </body>
    </html>
    """
'''
print(fastapi_static)

# ========== JINJA2 TEMPLATES ==========
print("\n" + "=" * 60)
print("5. JINJA2 TEMPLATE FEATURES")
print("=" * 60)

jinja_templates = '''
<!-- templates/base.html - Base template with inheritance -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}ML App{% endblock %}</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <nav>
        <a href="/">Home</a>
        <a href="/history">History</a>
        <a href="/stats">Stats</a>
    </nav>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2024 ML Prediction Service</p>
    </footer>
    
    {% block scripts %}{% endblock %}
</body>
</html>

<!-- templates/index.html - Child template -->
{% extends "base.html" %}

{% block title %}ML Prediction{% endblock %}

{% block content %}
<h1>Make a Prediction</h1>

<form method="post" action="/predict-form">
    <label>Features:</label>
    <input name="features" value="{{ features | default('') }}">
    <button type="submit">Predict</button>
</form>

{% if prediction %}
<div class="result">
    <h2>Result: {{ prediction }}</h2>
    <p>Confidence: {{ confidence | default('N/A') }}</p>
</div>
{% endif %}

<!-- Loop through predictions -->
{% if predictions %}
<h2>Recent Predictions</h2>
<ul>
{% for pred in predictions %}
    <li>
        {{ pred.id }}: {{ pred.prediction }} 
        ({{ pred.created_at | datetimeformat }})
    </li>
{% endfor %}
</ul>
{% endif %}

{% endblock %}

# FastAPI with Jinja2 rendering
from fastapi import Form

@app.post("/predict-form", response_class=HTMLResponse)
async def predict_form(
    request: Request,
    features: str = Form(...),
    db: Session = Depends(get_db)
):
    """Handle form submission and render result"""
    features_list = [float(x.strip()) for x in features.split(',')]
    
    # Make prediction
    prediction = model.predict([features_list])[0]
    
    # Get recent predictions
    recent = crud.get_predictions(db, limit=5)
    
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "features": features,
            "prediction": prediction,
            "predictions": recent
        }
    )
'''
print(jinja_templates)

# ========== COMPLETE FRONTEND EXAMPLE ==========
print("\n" + "=" * 60)
print("6. COMPLETE FRONTEND PROJECT STRUCTURE")
print("=" * 60)

print("""
Project Structure:
==================

ml-app/
├── app/
│   └── main.py           # FastAPI application
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Main page
│   └── history.html      # History page
├── static/
│   ├── css/
│   │   └── style.css     # Styles
│   ├── js/
│   │   └── app.js        # JavaScript
│   └── images/
│       └── logo.png      # Assets
└── requirements.txt

Key Files Content Summary:
==========================

templates/index.html:
- Form for feature input
- Display prediction results
- Show recent predictions

static/css/style.css:
- Modern gradient design
- Responsive layout
- Card-based UI
- Loading animations

static/js/app.js:
- Form submission handler
- API calls with fetch
- Dynamic result display
- History loading

main.py additions:
- StaticFiles mount
- Jinja2Templates setup
- HTML response routes
""")

# ========== ALTERNATIVE FRONTENDS ==========
print("\n" + "=" * 60)
print("7. ALTERNATIVE FRONTEND OPTIONS")
print("=" * 60)

alternatives = '''
# Option 1: Streamlit (Simplest)
# streamlit_app.py

import streamlit as st
import requests

st.title("🤖 ML Prediction Service")

# Input
features = st.text_input("Enter features (comma-separated)")

if st.button("Predict"):
    if features:
        try:
            features_list = [float(x.strip()) for x in features.split(',')]
            response = requests.post(
                "http://localhost:8000/predict",
                json={"features": features_list}
            )
            data = response.json()
            st.success(f"Prediction: {data['prediction']:.4f}")
        except Exception as e:
            st.error(f"Error: {e}")

# Run with: streamlit run streamlit_app.py

# Option 2: Gradio (Quick UI)
# gradio_app.py

import gradio as gr
import requests

def predict(features_str):
    features = [float(x.strip()) for x in features_str.split(',')]
    response = requests.post(
        "http://localhost:8000/predict",
        json={"features": features}
    )
    data = response.json()
    return f"Prediction: {data['prediction']:.4f}"

interface = gr.Interface(
    fn=predict,
    inputs="text",
    outputs="text",
    title="ML Prediction"
)
interface.launch()

# Run with: python gradio_app.py

# Option 3: React/Vue (Production)
# For production apps, use React or Vue.js
# with proper build tooling and state management
'''
print(alternatives)

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
1. HTML Structure
   - Semantic HTML5 elements
   - Forms for user input
   - Sections for organization

2. CSS Styling
   - Modern gradient backgrounds
   - Card-based layouts
   - Responsive design
   - Loading animations

3. JavaScript
   - Fetch API for requests
   - Async/await patterns
   - DOM manipulation
   - Event handling

4. FastAPI Integration
   - StaticFiles for CSS/JS
   - Jinja2Templates for HTML
   - Form handling
   - Multiple response types

5. Best Practices
   - Separate concerns (HTML/CSS/JS)
   - Progressive enhancement
   - Error handling in UI
   - Responsive design
""")

print("\n" + "=" * 60)
print("✅ Simple Frontend Development - Complete!")
print("=" * 60)
