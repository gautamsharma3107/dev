"""
Day 8 - Mini Project 1: Simple HTTP Client
==========================================
Build a command-line HTTP client that can make requests to APIs

This project applies:
- HTTP methods (GET, POST, PUT, DELETE)
- Status code handling
- JSON parsing
- Error handling
"""

import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

print("=" * 60)
print("Mini Project 1: Simple HTTP Client")
print("=" * 60)

class SimpleHTTPClient:
    """
    A simple command-line HTTP client for testing APIs.
    """
    
    def __init__(self):
        self.history = []
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'SimpleHTTPClient/1.0'
        }
    
    def set_header(self, key, value):
        """Set a custom header"""
        self.headers[key] = value
        print(f"✅ Header set: {key}: {value}")
    
    def remove_header(self, key):
        """Remove a header"""
        if key in self.headers:
            del self.headers[key]
            print(f"✅ Header removed: {key}")
        else:
            print(f"❌ Header not found: {key}")
    
    def show_headers(self):
        """Display current headers"""
        print("\n📋 Current Headers:")
        for key, value in self.headers.items():
            print(f"  {key}: {value}")
    
    def _make_request(self, method, url, data=None):
        """Internal method to make HTTP requests"""
        request_data = json.dumps(data).encode() if data else None
        
        req = Request(url, data=request_data, method=method)
        for key, value in self.headers.items():
            req.add_header(key, value)
        
        result = {
            'method': method,
            'url': url,
            'request_data': data,
            'status': None,
            'response_headers': {},
            'response_body': None,
            'error': None
        }
        
        try:
            with urlopen(req, timeout=30) as response:
                result['status'] = response.status
                result['response_headers'] = dict(response.headers)
                
                body = response.read().decode()
                try:
                    result['response_body'] = json.loads(body)
                except json.JSONDecodeError:
                    result['response_body'] = body
                    
        except HTTPError as e:
            result['status'] = e.code
            result['error'] = e.reason
            try:
                body = e.read().decode()
                result['response_body'] = json.loads(body)
            except:
                result['response_body'] = str(e)
                
        except URLError as e:
            result['error'] = f"Connection Error: {e.reason}"
            
        except Exception as e:
            result['error'] = str(e)
        
        self.history.append(result)
        return result
    
    def get(self, url):
        """Make a GET request"""
        return self._make_request('GET', url)
    
    def post(self, url, data):
        """Make a POST request"""
        return self._make_request('POST', url, data)
    
    def put(self, url, data):
        """Make a PUT request"""
        return self._make_request('PUT', url, data)
    
    def patch(self, url, data):
        """Make a PATCH request"""
        return self._make_request('PATCH', url, data)
    
    def delete(self, url):
        """Make a DELETE request"""
        return self._make_request('DELETE', url)
    
    def format_response(self, result):
        """Format and display the response"""
        print("\n" + "=" * 50)
        print(f"📤 {result['method']} {result['url']}")
        print("=" * 50)
        
        if result['request_data']:
            print("\n📋 Request Body:")
            print(json.dumps(result['request_data'], indent=2))
        
        if result['error'] and result['status'] is None:
            print(f"\n❌ Error: {result['error']}")
            return
        
        # Status
        status = result['status']
        if status:
            if 200 <= status < 300:
                emoji = "✅"
            elif 300 <= status < 400:
                emoji = "↪️"
            elif 400 <= status < 500:
                emoji = "⚠️"
            else:
                emoji = "💥"
            print(f"\n{emoji} Status: {status}")
        
        # Response headers
        if result['response_headers']:
            print("\n📋 Response Headers:")
            for key, value in list(result['response_headers'].items())[:5]:
                print(f"  {key}: {value}")
        
        # Response body
        if result['response_body']:
            print("\n📥 Response Body:")
            if isinstance(result['response_body'], dict):
                print(json.dumps(result['response_body'], indent=2)[:1000])
            else:
                print(str(result['response_body'])[:500])
        
        print("\n" + "=" * 50)
    
    def show_history(self):
        """Show request history"""
        print("\n📜 Request History:")
        for i, req in enumerate(self.history[-10:], 1):
            status = req.get('status', 'Error')
            print(f"  {i}. {req['method']} {req['url']} → {status}")


def demo():
    """Demonstrate the HTTP client"""
    client = SimpleHTTPClient()
    
    print("\n🚀 Testing HTTP Client with httpbin.org\n")
    
    # Test GET
    print("\n1️⃣ Testing GET request...")
    result = client.get("https://httpbin.org/get")
    client.format_response(result)
    
    # Test POST
    print("\n2️⃣ Testing POST request...")
    user_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "age": 30
    }
    result = client.post("https://httpbin.org/post", user_data)
    client.format_response(result)
    
    # Test PUT
    print("\n3️⃣ Testing PUT request...")
    update_data = {
        "name": "John Updated",
        "email": "john.new@example.com"
    }
    result = client.put("https://httpbin.org/put", update_data)
    client.format_response(result)
    
    # Test DELETE
    print("\n4️⃣ Testing DELETE request...")
    result = client.delete("https://httpbin.org/delete")
    client.format_response(result)
    
    # Test error handling
    print("\n5️⃣ Testing error handling (404)...")
    result = client.get("https://httpbin.org/status/404")
    client.format_response(result)
    
    # Show history
    client.show_history()
    
    print("\n✅ HTTP Client Demo Complete!")


def interactive_mode():
    """Run the client in interactive mode"""
    client = SimpleHTTPClient()
    
    print("""
    🌐 Simple HTTP Client - Interactive Mode
    ========================================
    Commands:
      get <url>           - Make GET request
      post <url> <json>   - Make POST request
      put <url> <json>    - Make PUT request
      delete <url>        - Make DELETE request
      header <key> <val>  - Set header
      headers             - Show headers
      history             - Show request history
      help                - Show this help
      quit                - Exit
    """)
    
    while True:
        try:
            cmd = input("\n> ").strip()
            if not cmd:
                continue
            
            parts = cmd.split(maxsplit=2)
            action = parts[0].lower()
            
            if action == 'quit':
                print("Goodbye! 👋")
                break
            
            elif action == 'help':
                print("Available commands: get, post, put, delete, header, headers, history, quit")
            
            elif action == 'get' and len(parts) >= 2:
                result = client.get(parts[1])
                client.format_response(result)
            
            elif action == 'post' and len(parts) >= 3:
                data = json.loads(parts[2])
                result = client.post(parts[1], data)
                client.format_response(result)
            
            elif action == 'put' and len(parts) >= 3:
                data = json.loads(parts[2])
                result = client.put(parts[1], data)
                client.format_response(result)
            
            elif action == 'delete' and len(parts) >= 2:
                result = client.delete(parts[1])
                client.format_response(result)
            
            elif action == 'header' and len(parts) >= 3:
                client.set_header(parts[1], parts[2])
            
            elif action == 'headers':
                client.show_headers()
            
            elif action == 'history':
                client.show_history()
            
            else:
                print("❌ Invalid command. Type 'help' for available commands.")
                
        except json.JSONDecodeError:
            print("❌ Invalid JSON format")
        except KeyboardInterrupt:
            print("\nGoodbye! 👋")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    # Run demo
    demo()
    
    # Uncomment to run interactive mode:
    # interactive_mode()
