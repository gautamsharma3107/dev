"""
MINI PROJECT 2: Sentiment Analysis API
=======================================
A Flask API for text sentiment classification

Features:
1. Simple rule-based sentiment (no ML required)
2. Multiple analysis endpoints
3. Batch processing
4. Detailed sentiment breakdown

This is a simplified version that doesn't require ML models,
demonstrating API structure for NLP tasks.

Run: python 02_sentiment_api.py
Test: curl http://localhost:5001/analyze -X POST \
      -H "Content-Type: application/json" \
      -d '{"text": "I love this product! It is amazing."}'
"""

import re
import time
from datetime import datetime
from collections import Counter

try:
    from flask import Flask, request, jsonify
    FLASK_AVAILABLE = True
except ImportError:
    print("Flask not installed. Run: pip install flask")
    FLASK_AVAILABLE = False

# ========== SENTIMENT LEXICON ==========
# Simple word lists for sentiment analysis
POSITIVE_WORDS = {
    'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic',
    'awesome', 'love', 'like', 'best', 'happy', 'joy', 'beautiful',
    'perfect', 'brilliant', 'outstanding', 'superb', 'nice', 'pleasant',
    'positive', 'recommend', 'enjoy', 'helpful', 'thanks', 'thank',
    'impressive', 'delightful', 'satisfied', 'glad', 'pleased'
}

NEGATIVE_WORDS = {
    'bad', 'terrible', 'awful', 'horrible', 'worst', 'hate', 'dislike',
    'poor', 'disappointing', 'disappointed', 'sad', 'angry', 'upset',
    'frustrating', 'annoying', 'useless', 'waste', 'broken', 'fail',
    'failed', 'problem', 'issue', 'bug', 'error', 'wrong', 'never',
    'boring', 'slow', 'expensive', 'overpriced', 'refund'
}

INTENSIFIERS = {
    'very', 'really', 'extremely', 'absolutely', 'totally', 'completely',
    'incredibly', 'highly', 'so', 'too', 'quite'
}

NEGATIONS = {
    'not', "n't", 'no', 'never', 'none', 'nothing', 'neither', 'nobody',
    'hardly', 'barely', 'scarcely'
}

# ========== SENTIMENT ANALYZER ==========
class SentimentAnalyzer:
    """Simple rule-based sentiment analyzer."""
    
    def __init__(self):
        self.positive_words = POSITIVE_WORDS
        self.negative_words = NEGATIVE_WORDS
        self.intensifiers = INTENSIFIERS
        self.negations = NEGATIONS
    
    def preprocess(self, text):
        """Clean and tokenize text."""
        # Lowercase
        text = text.lower()
        # Remove special characters except apostrophes
        text = re.sub(r"[^a-z0-9'\s]", ' ', text)
        # Tokenize
        tokens = text.split()
        return tokens
    
    def analyze(self, text):
        """Analyze sentiment of text."""
        tokens = self.preprocess(text)
        
        positive_count = 0
        negative_count = 0
        found_positive = []
        found_negative = []
        
        negation_active = False
        intensifier_active = False
        
        for i, token in enumerate(tokens):
            # Check for negation
            if token in self.negations:
                negation_active = True
                continue
            
            # Check for intensifier
            if token in self.intensifiers:
                intensifier_active = True
                continue
            
            # Check sentiment
            multiplier = 1.5 if intensifier_active else 1.0
            
            if token in self.positive_words:
                if negation_active:
                    negative_count += multiplier
                    found_negative.append(token)
                else:
                    positive_count += multiplier
                    found_positive.append(token)
            
            elif token in self.negative_words:
                if negation_active:
                    positive_count += multiplier
                    found_positive.append(token)
                else:
                    negative_count += multiplier
                    found_negative.append(token)
            
            # Reset flags after sentiment word
            if token in self.positive_words or token in self.negative_words:
                negation_active = False
                intensifier_active = False
        
        # Calculate scores
        total = positive_count + negative_count
        
        if total == 0:
            sentiment = "neutral"
            confidence = 0.5
            score = 0.0
        else:
            score = (positive_count - negative_count) / total
            
            if score > 0.2:
                sentiment = "positive"
            elif score < -0.2:
                sentiment = "negative"
            else:
                sentiment = "neutral"
            
            confidence = abs(score) * 0.5 + 0.5  # Scale to 0.5-1.0
        
        return {
            "sentiment": sentiment,
            "score": round(score, 4),
            "confidence": round(confidence, 4),
            "details": {
                "positive_count": positive_count,
                "negative_count": negative_count,
                "positive_words": found_positive,
                "negative_words": found_negative,
                "word_count": len(tokens)
            }
        }

# ========== CREATE FLASK APP ==========
if FLASK_AVAILABLE:
    app = Flask(__name__)
    analyzer = SentimentAnalyzer()
    
    @app.route('/')
    def home():
        """API info."""
        return jsonify({
            "name": "Sentiment Analysis API",
            "version": "1.0.0",
            "description": "Analyze text sentiment",
            "endpoints": {
                "GET /": "API info",
                "GET /health": "Health check",
                "POST /analyze": "Analyze single text",
                "POST /analyze/batch": "Analyze multiple texts",
                "POST /keywords": "Extract sentiment keywords"
            }
        })
    
    @app.route('/health')
    def health():
        """Health check."""
        return jsonify({
            "status": "healthy",
            "timestamp": datetime.now().isoformat()
        })
    
    @app.route('/analyze', methods=['POST'])
    def analyze():
        """Analyze sentiment of text."""
        start_time = time.time()
        
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({
                "success": False,
                "error": "Missing 'text' field"
            }), 400
        
        text = data['text']
        
        if not isinstance(text, str):
            return jsonify({
                "success": False,
                "error": "'text' must be a string"
            }), 400
        
        if len(text) > 10000:
            return jsonify({
                "success": False,
                "error": "Text too long (max 10000 characters)"
            }), 400
        
        result = analyzer.analyze(text)
        
        return jsonify({
            "success": True,
            "result": result,
            "processing_time_ms": round((time.time() - start_time) * 1000, 2)
        })
    
    @app.route('/analyze/batch', methods=['POST'])
    def analyze_batch():
        """Analyze multiple texts."""
        start_time = time.time()
        
        data = request.get_json()
        
        if not data or 'texts' not in data:
            return jsonify({
                "success": False,
                "error": "Missing 'texts' field"
            }), 400
        
        texts = data['texts']
        
        if not isinstance(texts, list):
            return jsonify({
                "success": False,
                "error": "'texts' must be a list"
            }), 400
        
        if len(texts) > 100:
            return jsonify({
                "success": False,
                "error": "Too many texts (max 100)"
            }), 400
        
        results = []
        sentiment_counts = Counter()
        
        for i, text in enumerate(texts):
            if not isinstance(text, str):
                results.append({
                    "index": i,
                    "error": "Not a string"
                })
                continue
            
            result = analyzer.analyze(text)
            result["index"] = i
            results.append(result)
            sentiment_counts[result["sentiment"]] += 1
        
        return jsonify({
            "success": True,
            "results": results,
            "summary": {
                "total": len(texts),
                "positive": sentiment_counts["positive"],
                "negative": sentiment_counts["negative"],
                "neutral": sentiment_counts["neutral"]
            },
            "processing_time_ms": round((time.time() - start_time) * 1000, 2)
        })
    
    @app.route('/keywords', methods=['POST'])
    def keywords():
        """Extract sentiment keywords from text."""
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({
                "success": False,
                "error": "Missing 'text' field"
            }), 400
        
        text = data['text']
        tokens = analyzer.preprocess(text)
        
        positive = [t for t in tokens if t in POSITIVE_WORDS]
        negative = [t for t in tokens if t in NEGATIVE_WORDS]
        
        return jsonify({
            "success": True,
            "keywords": {
                "positive": list(set(positive)),
                "negative": list(set(negative)),
                "positive_count": len(positive),
                "negative_count": len(negative)
            }
        })
    
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({
            "success": False,
            "error": "Endpoint not found"
        }), 404

# ========== MAIN ==========
if __name__ == '__main__':
    print("=" * 50)
    print("SENTIMENT ANALYSIS API")
    print("=" * 50)
    
    if not FLASK_AVAILABLE:
        print("Flask is required. Install with: pip install flask")
        exit(1)
    
    print("\nEndpoints:")
    print("  GET  /              - API info")
    print("  GET  /health        - Health check")
    print("  POST /analyze       - Analyze single text")
    print("  POST /analyze/batch - Analyze multiple texts")
    print("  POST /keywords      - Extract keywords")
    print("\nTest with:")
    print('  curl http://localhost:5001/analyze -X POST \\')
    print('       -H "Content-Type: application/json" \\')
    print('       -d \'{"text": "I love this! It is amazing."}\'')
    print("=" * 50)
    
    app.run(debug=True, port=5001, host='0.0.0.0')
