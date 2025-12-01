"""
DAY 8 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 8 ASSESSMENT TEST - Web & HTTP Fundamentals")
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
Q1. Which HTTP method is used to retrieve data from a server?
a) POST
b) PUT
c) GET
d) DELETE

Your answer: """)

print("""
Q2. What does the HTTP status code 404 indicate?
a) Server error
b) Resource not found
c) Successful request
d) Unauthorized access

Your answer: """)

print("""
Q3. Which HTTP status code indicates a successful POST request that created a new resource?
a) 200 OK
b) 201 Created
c) 204 No Content
d) 202 Accepted

Your answer: """)

print("""
Q4. In a URL like "https://api.example.com:8080/users?page=1", what is ":8080"?
a) Protocol
b) Path
c) Port number
d) Query parameter

Your answer: """)

print("""
Q5. Which data format is most commonly used in REST APIs?
a) XML
b) CSV
c) JSON
d) YAML

Your answer: """)

print("""
Q6. What's the difference between HTTP 401 and 403?
a) 401 means forbidden, 403 means unauthorized
b) 401 means unauthorized (need login), 403 means forbidden (no permission)
c) They are the same
d) 401 is for GET, 403 is for POST

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Given the following JSON string, write Python code to:
    1. Parse it into a Python dictionary
    2. Print the user's name and their second skill

JSON string:
'{\"name\": \"Alice\", \"age\": 28, \"skills\": [\"Python\", \"JavaScript\", \"SQL\"]}'
""")

# Write your code here:
import json

json_string = '{"name": "Alice", "age": 28, "skills": ["Python", "JavaScript", "SQL"]}'

# Your code to parse and print:




print("""
Q8. (2 points) Write a function that takes an HTTP status code and returns the 
appropriate category as a string:
- 2xx returns "Success"
- 4xx returns "Client Error"  
- 5xx returns "Server Error"
- Other returns "Unknown"

Test with: 200, 404, 500, 301
""")

# Write your function here:
def get_status_category(status_code):
    # Your code here
    pass

# Test your function:
# print(get_status_category(200))  # Should print: Success
# print(get_status_category(404))  # Should print: Client Error
# print(get_status_category(500))  # Should print: Server Error
# print(get_status_category(301))  # Should print: Unknown




print("""
Q9. (2 points) Create a Python dictionary representing a REST API response for a 
user list with the following structure:
- status: "success"
- data: list containing 2 user dictionaries (each with id, name, email)
- count: 2

Then convert it to a pretty-printed JSON string.
""")

# Write your code here:




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between PUT and PATCH HTTP methods.
Give an example scenario where you would use each.

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
When done, check your answers with your professor.
You need at least 10 points to pass!

Remember:
- Review topics you got wrong
- Practice more on weak areas
- Ask questions if confused

Good luck! 🚀
""")

"""
ANSWER KEY (Don't look until you're done!)
============================================

Section A (MCQ):
Q1: c) GET
Q2: b) Resource not found
Q3: b) 201 Created
Q4: c) Port number
Q5: c) JSON
Q6: b) 401 means unauthorized (need login), 403 means forbidden (no permission)

Section B (Coding):

Q7:
import json
json_string = '{"name": "Alice", "age": 28, "skills": ["Python", "JavaScript", "SQL"]}'
data = json.loads(json_string)
print(f"Name: {data['name']}")
print(f"Second skill: {data['skills'][1]}")

Q8:
def get_status_category(status_code):
    if 200 <= status_code < 300:
        return "Success"
    elif 400 <= status_code < 500:
        return "Client Error"
    elif 500 <= status_code < 600:
        return "Server Error"
    else:
        return "Unknown"

# Tests:
print(get_status_category(200))  # Success
print(get_status_category(404))  # Client Error
print(get_status_category(500))  # Server Error
print(get_status_category(301))  # Unknown

Q9:
response = {
    "status": "success",
    "data": [
        {"id": 1, "name": "John", "email": "john@example.com"},
        {"id": 2, "name": "Jane", "email": "jane@example.com"}
    ],
    "count": 2
}
json_response = json.dumps(response, indent=4)
print(json_response)

Section C:
Q10: 
PUT is used to replace an entire resource. If any field is missing in the request,
it will be set to null or removed. Use PUT when you want to completely update a resource.
Example: Updating a user's entire profile.

PATCH is used for partial updates. Only the fields included in the request are updated;
other fields remain unchanged. Use PATCH when you only need to update specific fields.
Example: Updating just a user's email address.

PUT example: PUT /users/123 with {"name": "John", "email": "john@new.com", "phone": "123"}
PATCH example: PATCH /users/123 with {"email": "john@new.com"}
"""
