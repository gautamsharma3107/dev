"""
Day 8 - Mini Project 2: API Data Fetcher
========================================
Fetch and display data from public APIs

This project applies:
- Making HTTP requests
- Parsing JSON responses
- Handling API pagination
- Displaying data in formatted output
"""

import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

print("=" * 60)
print("Mini Project 2: API Data Fetcher")
print("=" * 60)

class APIDataFetcher:
    """
    Fetch and display data from public APIs.
    """
    
    def __init__(self):
        self.base_headers = {
            'Accept': 'application/json',
            'User-Agent': 'APIDataFetcher/1.0'
        }
    
    def _fetch(self, url):
        """Fetch data from URL"""
        req = Request(url)
        for key, value in self.base_headers.items():
            req.add_header(key, value)
        
        try:
            with urlopen(req, timeout=10) as response:
                return {
                    'success': True,
                    'status': response.status,
                    'data': json.loads(response.read().decode())
                }
        except HTTPError as e:
            return {'success': False, 'error': f"HTTP {e.code}: {e.reason}"}
        except URLError as e:
            return {'success': False, 'error': f"Connection error: {e.reason}"}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def fetch_json_placeholder_users(self):
        """Fetch users from JSONPlaceholder API"""
        print("\n📥 Fetching users from JSONPlaceholder...")
        result = self._fetch("https://jsonplaceholder.typicode.com/users")
        
        if result['success']:
            users = result['data']
            print(f"\n✅ Found {len(users)} users:\n")
            print("-" * 60)
            for user in users:
                print(f"👤 {user['name']}")
                print(f"   Email: {user['email']}")
                print(f"   City: {user['address']['city']}")
                print(f"   Company: {user['company']['name']}")
                print()
        else:
            print(f"❌ Error: {result['error']}")
        
        return result
    
    def fetch_user_posts(self, user_id):
        """Fetch posts by a specific user"""
        print(f"\n📥 Fetching posts for user {user_id}...")
        result = self._fetch(f"https://jsonplaceholder.typicode.com/users/{user_id}/posts")
        
        if result['success']:
            posts = result['data']
            print(f"\n✅ Found {len(posts)} posts:\n")
            print("-" * 60)
            for i, post in enumerate(posts[:5], 1):  # Show first 5
                print(f"📝 Post {i}: {post['title'][:50]}...")
                print(f"   {post['body'][:100]}...")
                print()
            if len(posts) > 5:
                print(f"   ... and {len(posts) - 5} more posts")
        else:
            print(f"❌ Error: {result['error']}")
        
        return result
    
    def fetch_todos(self, user_id=None):
        """Fetch todos, optionally filtered by user"""
        url = "https://jsonplaceholder.typicode.com/todos"
        if user_id:
            url += f"?userId={user_id}"
        
        print(f"\n📥 Fetching todos...")
        result = self._fetch(url)
        
        if result['success']:
            todos = result['data']
            completed = [t for t in todos if t['completed']]
            pending = [t for t in todos if not t['completed']]
            
            print(f"\n✅ Found {len(todos)} todos:")
            print(f"   ✓ Completed: {len(completed)}")
            print(f"   ○ Pending: {len(pending)}")
            print("\n📋 First 5 todos:")
            print("-" * 60)
            for todo in todos[:5]:
                status = "✓" if todo['completed'] else "○"
                print(f"   {status} {todo['title'][:50]}")
        else:
            print(f"❌ Error: {result['error']}")
        
        return result
    
    def fetch_github_repos(self, username):
        """Fetch public repos for a GitHub user"""
        print(f"\n📥 Fetching GitHub repos for {username}...")
        result = self._fetch(f"https://api.github.com/users/{username}/repos?sort=updated&per_page=10")
        
        if result['success']:
            repos = result['data']
            print(f"\n✅ Found {len(repos)} repositories:\n")
            print("-" * 60)
            for repo in repos:
                stars = repo['stargazers_count']
                forks = repo['forks_count']
                lang = repo.get('language', 'Unknown')
                print(f"📦 {repo['name']}")
                print(f"   ⭐ {stars} | 🍴 {forks} | 💻 {lang}")
                if repo['description']:
                    print(f"   📝 {repo['description'][:60]}...")
                print()
        else:
            print(f"❌ Error: {result['error']}")
        
        return result
    
    def fetch_random_users(self, count=5):
        """Fetch random users from RandomUser API"""
        print(f"\n📥 Fetching {count} random users...")
        result = self._fetch(f"https://randomuser.me/api/?results={count}")
        
        if result['success']:
            users = result['data']['results']
            print(f"\n✅ Generated {len(users)} random users:\n")
            print("-" * 60)
            for user in users:
                name = f"{user['name']['first']} {user['name']['last']}"
                print(f"👤 {name}")
                print(f"   📧 {user['email']}")
                print(f"   📍 {user['location']['city']}, {user['location']['country']}")
                print(f"   🎂 Age: {user['dob']['age']}")
                print()
        else:
            print(f"❌ Error: {result['error']}")
        
        return result
    
    def fetch_countries(self, region=None):
        """Fetch country data from REST Countries API"""
        url = "https://restcountries.com/v3.1/all"
        if region:
            url = f"https://restcountries.com/v3.1/region/{region}"
        
        print(f"\n📥 Fetching countries...")
        result = self._fetch(url)
        
        if result['success']:
            countries = result['data']
            print(f"\n✅ Found {len(countries)} countries:\n")
            print("-" * 60)
            
            # Sort by population
            countries.sort(key=lambda x: x.get('population', 0), reverse=True)
            
            for country in countries[:10]:  # Top 10
                name = country['name']['common']
                pop = country.get('population', 0)
                region = country.get('region', 'Unknown')
                capital = country.get('capital', ['N/A'])[0] if country.get('capital') else 'N/A'
                
                print(f"🌍 {name}")
                print(f"   🏛️ Capital: {capital}")
                print(f"   👥 Population: {pop:,}")
                print(f"   🌎 Region: {region}")
                print()
            
            if len(countries) > 10:
                print(f"   ... and {len(countries) - 10} more countries")
        else:
            print(f"❌ Error: {result['error']}")
        
        return result
    
    def search_books(self, query):
        """Search for books using Open Library API"""
        from urllib.parse import quote
        
        print(f"\n📥 Searching books for '{query}'...")
        encoded_query = quote(query)
        result = self._fetch(f"https://openlibrary.org/search.json?q={encoded_query}&limit=10")
        
        if result['success']:
            books = result['data'].get('docs', [])
            total = result['data'].get('numFound', 0)
            
            print(f"\n✅ Found {total} books (showing first {len(books)}):\n")
            print("-" * 60)
            
            for book in books:
                title = book.get('title', 'Unknown')
                author = book.get('author_name', ['Unknown'])[0] if book.get('author_name') else 'Unknown'
                year = book.get('first_publish_year', 'N/A')
                
                print(f"📚 {title}")
                print(f"   ✍️ {author}")
                print(f"   📅 First published: {year}")
                print()
        else:
            print(f"❌ Error: {result['error']}")
        
        return result


def demo():
    """Demonstrate the API data fetcher"""
    fetcher = APIDataFetcher()
    
    print("\n🚀 API Data Fetcher Demo\n")
    
    # Demo 1: JSONPlaceholder Users
    print("\n" + "=" * 60)
    print("Demo 1: JSONPlaceholder Users")
    print("=" * 60)
    fetcher.fetch_json_placeholder_users()
    
    # Demo 2: User Posts
    print("\n" + "=" * 60)
    print("Demo 2: Posts by User 1")
    print("=" * 60)
    fetcher.fetch_user_posts(1)
    
    # Demo 3: Todos
    print("\n" + "=" * 60)
    print("Demo 3: Todos")
    print("=" * 60)
    fetcher.fetch_todos()
    
    # Demo 4: Random Users
    print("\n" + "=" * 60)
    print("Demo 4: Random Users")
    print("=" * 60)
    fetcher.fetch_random_users(3)
    
    print("\n✅ API Data Fetcher Demo Complete!")
    print("Try exploring more APIs!")


if __name__ == "__main__":
    demo()
    
    # Additional demos you can try:
    # fetcher = APIDataFetcher()
    # fetcher.fetch_github_repos("python")
    # fetcher.fetch_countries("europe")
    # fetcher.search_books("python programming")
