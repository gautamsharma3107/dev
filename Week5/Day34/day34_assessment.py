"""
DAY 34 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 34 ASSESSMENT TEST - Model Deployment Basics")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# 1 point each
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. Which Python module is RECOMMENDED for saving scikit-learn models?
a) pickle
b) json
c) joblib
d) marshal

Your answer: """)

print("""
Q2. What HTTP method should be used for ML prediction endpoints?
a) GET
b) POST
c) PUT
d) DELETE

Your answer: """)

print("""
Q3. What HTTP status code indicates a bad request (invalid input)?
a) 200
b) 400
c) 404
d) 500

Your answer: """)

print("""
Q4. Which Flask function converts a Python dictionary to JSON response?
a) json.dumps()
b) return json
c) jsonify()
d) to_json()

Your answer: """)

print("""
Q5. What status code should be returned when the model is not loaded?
a) 400 Bad Request
b) 404 Not Found
c) 500 Internal Error
d) 503 Service Unavailable

Your answer: """)

print("""
Q6. Which is the correct way to get JSON data from a Flask POST request?
a) request.json()
b) request.get_json()
c) request.data
d) request.body

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write code to save a model with joblib and include 
    compression level 3. Assume the model variable is called 'classifier'.
""")

# Write your code here:




print("""
Q8. (2 points) Write a Flask health check endpoint that returns:
    {"status": "healthy", "model_loaded": true/false}
    Use a global variable 'model' to check if model is loaded.
""")

# Write your code here:




print("""
Q9. (2 points) Write input validation code that:
    - Checks if 'features' key exists in data dict
    - Checks if features is a list
    - Checks if there are exactly 4 features
    - Returns (True, None) if valid, or (False, error_message) if invalid
""")

# Write your code here:
def validate_input(data):
    pass  # Your code here




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain why we should load the model at application 
     startup instead of loading it for each prediction request.
     Give at least two reasons.

Your answer:
""")

# Write your explanation here as comments:
# 




# ============================================================
# TEST COMPLETE
# ============================================================

print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)
print("""
When done, check your answers with the answer key below.
You need at least 10 points to pass!

Remember:
- Review topics you got wrong
- Practice more on weak areas
- Build the mini project to solidify learning

Good luck! 🚀
""")

"""
ANSWER KEY (Don't look until you're done!)
============================================

Section A (MCQ):
Q1: c) joblib - Optimized for large numpy arrays, recommended by scikit-learn
Q2: b) POST - Used for sending data (features) to get predictions
Q3: b) 400 - Bad Request indicates invalid input from client
Q4: c) jsonify() - Flask's function to create JSON responses
Q5: d) 503 - Service Unavailable indicates the service isn't ready
Q6: b) request.get_json() - Parses JSON from request body

Section B (Coding):

Q7:
import joblib
joblib.dump(classifier, "model.joblib", compress=3)

Q8:
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "model_loaded": model is not None
    })

Q9:
def validate_input(data):
    if data is None or 'features' not in data:
        return False, "Missing 'features' field"
    
    features = data['features']
    
    if not isinstance(features, list):
        return False, "'features' must be a list"
    
    if len(features) != 4:
        return False, f"Expected 4 features, got {len(features)}"
    
    return True, None

Section C:
Q10: Reasons to load model at startup:

1. Performance: Loading a model takes time (disk I/O, deserialization).
   Loading per request would add significant latency to every prediction.

2. Memory Efficiency: Loading once means one copy in memory.
   Loading per request could cause memory issues with concurrent requests.

3. Consistency: Single model instance ensures all predictions use the
   same model version during the application lifecycle.

4. Resource Management: Prevents potential resource exhaustion from
   repeatedly opening/closing model files.

5. Startup Validation: Errors in model loading are caught at startup,
   not during user requests, making debugging easier.

Scoring:
- Section A: 6 points (1 each)
- Section B: 6 points (2 each)
- Section C: 2 points

Total: 14 points
Pass: 10+ points (70%)
"""
