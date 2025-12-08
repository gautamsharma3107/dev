"""
Day 35 - Frontend Template Generator
====================================
Learn: Creating simple HTML/CSS/JS frontend for image classification

Key Concepts:
- HTML form for file upload
- CSS styling for modern UI
- JavaScript for async API calls
- Displaying prediction results
"""

import os

# ========== FRONTEND TEMPLATES ==========
print("=" * 60)
print("FRONTEND TEMPLATE GENERATOR")
print("=" * 60)

# ========== BASIC HTML TEMPLATE ==========
BASIC_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Classifier</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f0f2f5;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
            max-width: 500px;
            width: 100%;
        }
        
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
            font-size: 28px;
        }
        
        .upload-area {
            border: 3px dashed #ddd;
            border-radius: 15px;
            padding: 40px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .upload-area:hover {
            border-color: #4CAF50;
            background: #f8fff8;
        }
        
        .upload-area.dragover {
            border-color: #4CAF50;
            background: #e8f5e9;
        }
        
        .upload-icon {
            font-size: 48px;
            margin-bottom: 15px;
        }
        
        input[type="file"] {
            display: none;
        }
        
        .btn {
            display: inline-block;
            background: #4CAF50;
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 25px;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-top: 15px;
        }
        
        .btn:hover {
            background: #45a049;
            transform: translateY(-2px);
        }
        
        #preview {
            margin: 20px 0;
            text-align: center;
            display: none;
        }
        
        #preview img {
            max-width: 100%;
            max-height: 300px;
            border-radius: 10px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        }
        
        #result {
            margin-top: 20px;
            padding: 20px;
            background: #f5f5f5;
            border-radius: 10px;
            display: none;
        }
        
        .prediction-label {
            font-size: 24px;
            color: #333;
            text-align: center;
            margin-bottom: 15px;
        }
        
        .confidence-bar {
            background: #e0e0e0;
            border-radius: 10px;
            height: 30px;
            margin: 8px 0;
            overflow: hidden;
        }
        
        .confidence-fill {
            height: 100%;
            background: linear-gradient(90deg, #4CAF50, #8BC34A);
            border-radius: 10px;
            display: flex;
            align-items: center;
            padding-left: 10px;
            color: white;
            font-weight: bold;
            transition: width 0.5s ease;
        }
        
        .loading {
            text-align: center;
            padding: 20px;
            display: none;
        }
        
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #4CAF50;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🖼️ Image Classifier</h1>
        
        <div class="upload-area" id="dropArea">
            <div class="upload-icon">📁</div>
            <p>Drag & drop an image here</p>
            <p style="color: #888; margin-top: 10px;">or</p>
            <label for="fileInput" class="btn">Choose File</label>
            <input type="file" id="fileInput" accept="image/*">
        </div>
        
        <div id="preview">
            <img id="previewImg" src="" alt="Preview">
        </div>
        
        <div class="loading" id="loading">
            <div class="spinner"></div>
            <p style="margin-top: 10px;">Analyzing image...</p>
        </div>
        
        <div id="result">
            <div class="prediction-label">
                Prediction: <strong id="predClass"></strong>
            </div>
            <div id="topPredictions"></div>
        </div>
    </div>
    
    <script>
        const dropArea = document.getElementById('dropArea');
        const fileInput = document.getElementById('fileInput');
        const preview = document.getElementById('preview');
        const previewImg = document.getElementById('previewImg');
        const loading = document.getElementById('loading');
        const result = document.getElementById('result');
        
        // API endpoint - change this to your server URL
        const API_URL = '/predict';
        
        // Drag and drop handlers
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(event => {
            dropArea.addEventListener(event, e => {
                e.preventDefault();
                e.stopPropagation();
            });
        });
        
        ['dragenter', 'dragover'].forEach(event => {
            dropArea.addEventListener(event, () => {
                dropArea.classList.add('dragover');
            });
        });
        
        ['dragleave', 'drop'].forEach(event => {
            dropArea.addEventListener(event, () => {
                dropArea.classList.remove('dragover');
            });
        });
        
        dropArea.addEventListener('drop', e => {
            const files = e.dataTransfer.files;
            if (files.length) handleFile(files[0]);
        });
        
        fileInput.addEventListener('change', e => {
            if (e.target.files.length) handleFile(e.target.files[0]);
        });
        
        function handleFile(file) {
            // Preview
            const reader = new FileReader();
            reader.onload = e => {
                previewImg.src = e.target.result;
                preview.style.display = 'block';
            };
            reader.readAsDataURL(file);
            
            // Upload
            uploadFile(file);
        }
        
        async function uploadFile(file) {
            loading.style.display = 'block';
            result.style.display = 'none';
            
            const formData = new FormData();
            formData.append('file', file);
            
            try {
                const response = await fetch(API_URL, {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                
                loading.style.display = 'none';
                
                if (data.success) {
                    displayResult(data);
                } else {
                    alert('Error: ' + data.error);
                }
            } catch (error) {
                loading.style.display = 'none';
                alert('Error: ' + error.message);
            }
        }
        
        function displayResult(data) {
            document.getElementById('predClass').textContent = 
                data.prediction.label;
            
            let html = '';
            const predictions = data.top_3 || data.top_predictions || [];
            predictions.forEach(pred => {
                const percent = (pred.confidence * 100).toFixed(1);
                html += `
                    <div class="confidence-bar">
                        <div class="confidence-fill" style="width: ${percent}%">
                            ${pred.label}: ${percent}%
                        </div>
                    </div>
                `;
            });
            
            document.getElementById('topPredictions').innerHTML = html;
            result.style.display = 'block';
        }
    </script>
</body>
</html>
"""

# ========== ADVANCED TEMPLATE (with animations) ==========
ADVANCED_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Image Classifier</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #6366f1;
            --primary-dark: #4f46e5;
            --secondary: #8b5cf6;
            --success: #10b981;
            --background: #f8fafc;
            --card: #ffffff;
            --text: #1e293b;
            --text-light: #64748b;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, var(--background) 0%, #e2e8f0 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .app {
            max-width: 600px;
            width: 100%;
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .header h1 {
            font-size: 2.5rem;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }
        
        .header p {
            color: var(--text-light);
            font-size: 1.1rem;
        }
        
        .card {
            background: var(--card);
            border-radius: 24px;
            padding: 40px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.1);
        }
        
        .upload-zone {
            border: 2px dashed #cbd5e1;
            border-radius: 16px;
            padding: 50px 30px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .upload-zone::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .upload-zone:hover {
            border-color: var(--primary);
        }
        
        .upload-zone:hover::before {
            opacity: 0.05;
        }
        
        .upload-zone.active {
            border-color: var(--primary);
            border-style: solid;
        }
        
        .upload-zone.active::before {
            opacity: 0.1;
        }
        
        .upload-zone > * {
            position: relative;
            z-index: 1;
        }
        
        .upload-icon {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px;
            font-size: 36px;
        }
        
        .upload-text h3 {
            color: var(--text);
            font-size: 1.25rem;
            margin-bottom: 8px;
        }
        
        .upload-text p {
            color: var(--text-light);
            font-size: 0.9rem;
        }
        
        .file-input {
            display: none;
        }
        
        .btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: white;
            padding: 14px 28px;
            border: none;
            border-radius: 12px;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            margin-top: 20px;
            transition: all 0.3s ease;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px -5px rgba(99, 102, 241, 0.4);
        }
        
        .preview-container {
            margin-top: 30px;
            display: none;
        }
        
        .preview-container.show {
            display: block;
            animation: fadeIn 0.5s ease;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .preview-image {
            width: 100%;
            border-radius: 16px;
            box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.1);
        }
        
        .results {
            margin-top: 30px;
            display: none;
        }
        
        .results.show {
            display: block;
            animation: fadeIn 0.5s ease;
        }
        
        .result-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        
        .main-prediction {
            font-size: 1.5rem;
            font-weight: 600;
            color: var(--text);
        }
        
        .confidence-badge {
            background: linear-gradient(135deg, var(--success), #34d399);
            color: white;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 500;
        }
        
        .predictions-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        
        .prediction-item {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .prediction-label {
            width: 100px;
            font-size: 0.9rem;
            color: var(--text);
            font-weight: 500;
        }
        
        .prediction-bar {
            flex: 1;
            height: 28px;
            background: #f1f5f9;
            border-radius: 14px;
            overflow: hidden;
        }
        
        .prediction-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            padding-right: 10px;
            color: white;
            font-size: 0.8rem;
            font-weight: 500;
            transition: width 0.8s ease;
        }
        
        .loading-overlay {
            position: fixed;
            inset: 0;
            background: rgba(255, 255, 255, 0.9);
            display: none;
            align-items: center;
            justify-content: center;
            z-index: 100;
        }
        
        .loading-overlay.show {
            display: flex;
        }
        
        .loading-content {
            text-align: center;
        }
        
        .loading-spinner {
            width: 60px;
            height: 60px;
            border: 4px solid #e2e8f0;
            border-top-color: var(--primary);
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 20px;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="app">
        <div class="header">
            <h1>🤖 AI Image Classifier</h1>
            <p>Upload an image to classify it instantly</p>
        </div>
        
        <div class="card">
            <div class="upload-zone" id="uploadZone">
                <div class="upload-icon">📸</div>
                <div class="upload-text">
                    <h3>Drop your image here</h3>
                    <p>or click to browse files</p>
                </div>
                <label class="btn" for="fileInput">
                    <span>📁</span> Choose Image
                </label>
                <input type="file" class="file-input" id="fileInput" accept="image/*">
            </div>
            
            <div class="preview-container" id="previewContainer">
                <img class="preview-image" id="previewImage" src="" alt="Preview">
            </div>
            
            <div class="results" id="results">
                <div class="result-header">
                    <span class="main-prediction" id="mainPrediction">Loading...</span>
                    <span class="confidence-badge" id="confidenceBadge">0%</span>
                </div>
                <div class="predictions-list" id="predictionsList"></div>
            </div>
        </div>
    </div>
    
    <div class="loading-overlay" id="loadingOverlay">
        <div class="loading-content">
            <div class="loading-spinner"></div>
            <p>Analyzing your image...</p>
        </div>
    </div>
    
    <script>
        const uploadZone = document.getElementById('uploadZone');
        const fileInput = document.getElementById('fileInput');
        const previewContainer = document.getElementById('previewContainer');
        const previewImage = document.getElementById('previewImage');
        const results = document.getElementById('results');
        const loadingOverlay = document.getElementById('loadingOverlay');
        
        const API_URL = '/predict';
        
        // Drag and drop
        uploadZone.addEventListener('dragover', e => {
            e.preventDefault();
            uploadZone.classList.add('active');
        });
        
        uploadZone.addEventListener('dragleave', () => {
            uploadZone.classList.remove('active');
        });
        
        uploadZone.addEventListener('drop', e => {
            e.preventDefault();
            uploadZone.classList.remove('active');
            const files = e.dataTransfer.files;
            if (files.length) processFile(files[0]);
        });
        
        fileInput.addEventListener('change', e => {
            if (e.target.files.length) processFile(e.target.files[0]);
        });
        
        async function processFile(file) {
            // Show preview
            const reader = new FileReader();
            reader.onload = e => {
                previewImage.src = e.target.result;
                previewContainer.classList.add('show');
            };
            reader.readAsDataURL(file);
            
            // Upload and predict
            loadingOverlay.classList.add('show');
            results.classList.remove('show');
            
            const formData = new FormData();
            formData.append('file', file);
            
            try {
                const response = await fetch(API_URL, {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                loadingOverlay.classList.remove('show');
                
                if (data.success) {
                    displayResults(data);
                } else {
                    alert('Error: ' + data.error);
                }
            } catch (error) {
                loadingOverlay.classList.remove('show');
                alert('Error: ' + error.message);
            }
        }
        
        function displayResults(data) {
            const prediction = data.prediction;
            document.getElementById('mainPrediction').textContent = prediction.label;
            document.getElementById('confidenceBadge').textContent = 
                (prediction.confidence * 100).toFixed(1) + '%';
            
            const predictions = data.top_3 || data.top_predictions || [];
            const listHtml = predictions.map(pred => {
                const percent = (pred.confidence * 100).toFixed(1);
                return `
                    <div class="prediction-item">
                        <span class="prediction-label">${pred.label}</span>
                        <div class="prediction-bar">
                            <div class="prediction-fill" style="width: ${percent}%">
                                ${percent}%
                            </div>
                        </div>
                    </div>
                `;
            }).join('');
            
            document.getElementById('predictionsList').innerHTML = listHtml;
            results.classList.add('show');
        }
    </script>
</body>
</html>
"""

# ========== GENERATE TEMPLATES ==========
def generate_basic_template(output_path='index.html'):
    """Generate basic HTML template"""
    with open(output_path, 'w') as f:
        f.write(BASIC_TEMPLATE.strip())
    print(f"✅ Generated basic template: {output_path}")
    return output_path


def generate_advanced_template(output_path='index_advanced.html'):
    """Generate advanced HTML template"""
    with open(output_path, 'w') as f:
        f.write(ADVANCED_TEMPLATE.strip())
    print(f"✅ Generated advanced template: {output_path}")
    return output_path


def generate_all_templates(output_dir='.'):
    """Generate all frontend templates"""
    os.makedirs(output_dir, exist_ok=True)
    
    basic_path = os.path.join(output_dir, 'index.html')
    advanced_path = os.path.join(output_dir, 'index_advanced.html')
    
    generate_basic_template(basic_path)
    generate_advanced_template(advanced_path)
    
    print(f"\n✅ All templates generated in: {output_dir}")
    return [basic_path, advanced_path]


# ========== MAIN ==========
if __name__ == '__main__':
    print("""
Frontend Template Generator
===========================

This script generates HTML templates for image classification apps.

Templates:
1. Basic - Simple, clean design
2. Advanced - Modern design with animations

Usage:
    python 06_frontend_template.py

The templates include:
- Drag and drop file upload
- Image preview
- API call to /predict endpoint
- Result display with confidence bars
    """)
    
    # Generate templates
    print("\nGenerating templates...")
    generate_all_templates()
    
    print("""
Next Steps:
1. Copy index.html to your Flask/FastAPI static folder
2. Update API_URL in the template if needed
3. Run your API server
4. Open the HTML file in a browser

For Flask:
    app.run(debug=True)
    # Access at http://localhost:5000

For FastAPI:
    uvicorn app:app --reload
    # Access at http://localhost:8000
    """)
    
    print("\n" + "=" * 60)
    print("✅ Frontend Template Generator - Complete!")
    print("=" * 60)
