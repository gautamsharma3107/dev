"""
Day 41 - WebSockets for Real-Time Apps
======================================
Learn: WebSocket protocol, real-time communication, and Python implementations

Key Concepts:
- WebSocket vs HTTP
- Bidirectional communication
- Real-time applications
- Python WebSocket libraries
"""

# ========== WEBSOCKETS OVERVIEW ==========
print("=" * 60)
print("WEBSOCKETS BASICS")
print("=" * 60)

"""
What are WebSockets?
- Full-duplex communication protocol over TCP
- Persistent connection between client and server
- Both parties can send messages at any time
- Ideal for real-time applications

HTTP vs WebSocket:

HTTP (Request-Response):
Client ──── Request ────> Server
Client <─── Response ──── Server
(Connection closed)

WebSocket (Bidirectional):
Client <──────────────────> Server
        Persistent Connection
        Both can send anytime

WebSocket Use Cases:
- Chat applications
- Live notifications
- Real-time dashboards
- Online gaming
- Live sports scores
- Collaborative editing
- Stock tickers
"""

# ========== WEBSOCKET PROTOCOL ==========
print("\n" + "=" * 60)
print("WEBSOCKET PROTOCOL")
print("=" * 60)

protocol_info = """
WebSocket Handshake:
1. Client sends HTTP Upgrade request
2. Server responds with 101 Switching Protocols
3. Connection upgraded to WebSocket

HTTP Request (Client):
    GET /chat HTTP/1.1
    Host: server.example.com
    Upgrade: websocket
    Connection: Upgrade
    Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
    Sec-WebSocket-Version: 13

HTTP Response (Server):
    HTTP/1.1 101 Switching Protocols
    Upgrade: websocket
    Connection: Upgrade
    Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=

After handshake:
- Connection is persistent
- Messages sent as frames
- Either side can close connection
"""
print(protocol_info)

# ========== SIMPLE WEBSOCKET SIMULATION ==========
print("\n" + "=" * 60)
print("WEBSOCKET CONCEPTS (Simulation)")
print("=" * 60)

import queue
import threading
import time
from typing import Callable, Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class WebSocketMessage:
    type: str  # 'text', 'binary', 'ping', 'pong', 'close'
    data: str
    timestamp: datetime = field(default_factory=datetime.now)

class SimulatedWebSocket:
    """Simulated WebSocket for learning (no actual network)"""
    
    def __init__(self, ws_id: str):
        self.id = ws_id
        self.is_open = False
        self.incoming_queue = queue.Queue()
        self.outgoing_queue = queue.Queue()
        self.on_message: Optional[Callable] = None
        self.on_close: Optional[Callable] = None
    
    def open(self):
        """Open the connection"""
        self.is_open = True
        print(f"🟢 WebSocket {self.id} opened")
    
    def close(self):
        """Close the connection"""
        self.is_open = False
        print(f"🔴 WebSocket {self.id} closed")
        if self.on_close:
            self.on_close()
    
    def send(self, message: str):
        """Send message to other end"""
        if not self.is_open:
            raise Exception("WebSocket is not open")
        
        msg = WebSocketMessage(type='text', data=message)
        self.outgoing_queue.put(msg)
        print(f"📤 [{self.id}] Sent: {message}")
    
    def receive(self) -> Optional[WebSocketMessage]:
        """Receive message from other end"""
        try:
            msg = self.incoming_queue.get_nowait()
            print(f"📥 [{self.id}] Received: {msg.data}")
            return msg
        except queue.Empty:
            return None

class WebSocketServer:
    """Simulated WebSocket server"""
    
    def __init__(self, host: str = "localhost", port: int = 8765):
        self.host = host
        self.port = port
        self.clients: Dict[str, SimulatedWebSocket] = {}
        self.running = False
        self.on_connect: Optional[Callable] = None
        self.on_message: Optional[Callable] = None
        self.on_disconnect: Optional[Callable] = None
    
    def start(self):
        """Start the server"""
        self.running = True
        print(f"🖥️  WebSocket Server started on ws://{self.host}:{self.port}")
    
    def stop(self):
        """Stop the server"""
        self.running = False
        for client in list(self.clients.values()):
            client.close()
        self.clients.clear()
        print("🖥️  WebSocket Server stopped")
    
    def accept_connection(self, client_id: str) -> SimulatedWebSocket:
        """Accept a new client connection"""
        ws = SimulatedWebSocket(client_id)
        ws.open()
        self.clients[client_id] = ws
        
        if self.on_connect:
            self.on_connect(client_id, ws)
        
        return ws
    
    def broadcast(self, message: str, exclude: Optional[str] = None):
        """Send message to all connected clients"""
        for client_id, ws in self.clients.items():
            if client_id != exclude and ws.is_open:
                ws.send(message)

# Demonstrate WebSocket concepts
print("\n--- WebSocket Server Demo ---")

server = WebSocketServer()
server.start()

# Connection handler
def on_connect(client_id, ws):
    print(f"✨ Client {client_id} connected")
    ws.send("Welcome to the server!")

server.on_connect = on_connect

# Accept connections
client1 = server.accept_connection("client-1")
client2 = server.accept_connection("client-2")

# Broadcast message
print("\nBroadcasting message to all clients:")
server.broadcast("Hello everyone!")

# Cleanup
client1.close()
client2.close()
server.stop()

# ========== PYTHON WEBSOCKETS LIBRARY ==========
print("\n" + "=" * 60)
print("PYTHON WEBSOCKETS LIBRARY")
print("=" * 60)

print("""
Installation:
    pip install websockets

The websockets library provides async WebSocket support.
""")

websockets_server = '''
# server.py - WebSocket Server with websockets library
import asyncio
import websockets
import json

# Store connected clients
connected_clients = set()

async def handler(websocket, path):
    """Handle WebSocket connections"""
    # Register client
    connected_clients.add(websocket)
    print(f"Client connected. Total: {len(connected_clients)}")
    
    try:
        async for message in websocket:
            print(f"Received: {message}")
            
            # Parse message
            data = json.loads(message)
            
            # Handle different message types
            if data["type"] == "chat":
                # Broadcast to all clients
                broadcast_msg = json.dumps({
                    "type": "chat",
                    "user": data["user"],
                    "message": data["message"]
                })
                
                await asyncio.gather(
                    *[client.send(broadcast_msg) for client in connected_clients]
                )
            
            elif data["type"] == "ping":
                await websocket.send(json.dumps({"type": "pong"}))
                
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        # Unregister client
        connected_clients.discard(websocket)
        print(f"Client disconnected. Total: {len(connected_clients)}")

# Start server
async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever

# Run: python server.py
asyncio.run(main())
'''
print("WebSocket Server Example:")
print(websockets_server)

websockets_client = '''
# client.py - WebSocket Client with websockets library
import asyncio
import websockets
import json

async def chat_client():
    uri = "ws://localhost:8765"
    
    async with websockets.connect(uri) as websocket:
        print("Connected to server")
        
        # Send a message
        message = json.dumps({
            "type": "chat",
            "user": "Alice",
            "message": "Hello, everyone!"
        })
        await websocket.send(message)
        print(f"Sent: {message}")
        
        # Receive messages
        async for message in websocket:
            data = json.loads(message)
            print(f"Received: {data}")
            
            if data["type"] == "chat":
                print(f"{data['user']}: {data['message']}")

# Run: python client.py
asyncio.run(chat_client())
'''
print("\nWebSocket Client Example:")
print(websockets_client)

# ========== FASTAPI WEBSOCKETS ==========
print("\n" + "=" * 60)
print("FASTAPI WEBSOCKETS")
print("=" * 60)

print("""
FastAPI has built-in WebSocket support.
Easy to integrate with REST endpoints.
""")

fastapi_websocket = '''
# main.py - FastAPI WebSocket Server
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI()

# Connection manager for multiple clients
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        print(f"Client connected. Total: {len(self.active_connections)}")
    
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        print(f"Client disconnected. Total: {len(self.active_connections)}")
    
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
    
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

# Simple WebSocket endpoint
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    await manager.broadcast(f"Client {client_id} joined the chat")
    
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            
            # Broadcast to all clients
            await manager.broadcast(f"{client_id}: {data}")
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client {client_id} left the chat")

# Serve simple HTML client for testing
@app.get("/")
async def get():
    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
    <head><title>WebSocket Chat</title></head>
    <body>
        <h1>WebSocket Chat</h1>
        <input type="text" id="clientId" placeholder="Your name">
        <button onclick="connect()">Connect</button>
        <br><br>
        <input type="text" id="messageText" placeholder="Message">
        <button onclick="sendMessage()">Send</button>
        <ul id="messages"></ul>
        
        <script>
            var ws;
            
            function connect() {
                var clientId = document.getElementById("clientId").value;
                ws = new WebSocket(`ws://localhost:8000/ws/${clientId}`);
                
                ws.onmessage = function(event) {
                    var messages = document.getElementById('messages');
                    var li = document.createElement('li');
                    li.appendChild(document.createTextNode(event.data));
                    messages.appendChild(li);
                };
            }
            
            function sendMessage() {
                var input = document.getElementById("messageText");
                ws.send(input.value);
                input.value = '';
            }
        </script>
    </body>
    </html>
    """)

# Run: uvicorn main:app --reload
'''
print("FastAPI WebSocket Example:")
print(fastapi_websocket)

# ========== REAL-TIME CHAT ROOM ==========
print("\n" + "=" * 60)
print("REAL-TIME CHAT ROOM EXAMPLE")
print("=" * 60)

class ChatRoom:
    """Simulated chat room with WebSocket-like behavior"""
    
    def __init__(self, name: str):
        self.name = name
        self.users: Dict[str, List[str]] = {}  # user_id -> messages
        self.message_history: List[Dict] = []
    
    def join(self, user_id: str):
        """User joins the chat room"""
        if user_id not in self.users:
            self.users[user_id] = []
            self._broadcast_system(f"{user_id} joined the room")
            print(f"👋 {user_id} joined '{self.name}'")
    
    def leave(self, user_id: str):
        """User leaves the chat room"""
        if user_id in self.users:
            del self.users[user_id]
            self._broadcast_system(f"{user_id} left the room")
            print(f"👋 {user_id} left '{self.name}'")
    
    def send_message(self, user_id: str, message: str):
        """Send a message to the room"""
        if user_id not in self.users:
            raise Exception(f"{user_id} is not in the room")
        
        msg = {
            "type": "message",
            "user": user_id,
            "text": message,
            "timestamp": datetime.now().isoformat()
        }
        
        self.message_history.append(msg)
        self._broadcast(msg)
        print(f"💬 [{user_id}]: {message}")
    
    def _broadcast(self, message: Dict):
        """Broadcast message to all users"""
        for user_id in self.users:
            self.users[user_id].append(message)
    
    def _broadcast_system(self, text: str):
        """Broadcast system message"""
        msg = {
            "type": "system",
            "text": text,
            "timestamp": datetime.now().isoformat()
        }
        self.message_history.append(msg)
        self._broadcast(msg)
    
    def get_messages(self, user_id: str) -> List[Dict]:
        """Get pending messages for user"""
        if user_id not in self.users:
            return []
        messages = self.users[user_id].copy()
        self.users[user_id] = []
        return messages

# Demonstrate chat room
print("\n--- Chat Room Demo ---")

room = ChatRoom("General")

# Users join
room.join("Alice")
room.join("Bob")
room.join("Charlie")

# Send messages
room.send_message("Alice", "Hey everyone!")
room.send_message("Bob", "Hi Alice! How are you?")
room.send_message("Charlie", "Good morning!")

# User leaves
room.leave("Charlie")

# More messages
room.send_message("Alice", "Bye Charlie!")

print(f"\nTotal messages: {len(room.message_history)}")

# ========== WEBSOCKET VS HTTP COMPARISON ==========
print("\n" + "=" * 60)
print("WEBSOCKET VS HTTP COMPARISON")
print("=" * 60)

comparison = """
┌─────────────────────┬────────────────────────┬────────────────────────┐
│ Feature             │ HTTP                   │ WebSocket              │
├─────────────────────┼────────────────────────┼────────────────────────┤
│ Connection          │ New for each request   │ Persistent             │
│ Communication       │ Request-Response       │ Bidirectional          │
│ Initiation          │ Client only            │ Both client & server   │
│ Protocol            │ HTTP/HTTPS             │ WS/WSS                 │
│ Overhead            │ Higher (headers)       │ Lower after handshake  │
│ Use Case            │ CRUD, REST APIs        │ Real-time apps         │
│ Stateless           │ Yes                    │ No (stateful)          │
│ Scalability         │ Easier                 │ More complex           │
│ Firewall            │ Usually allowed        │ May need configuration │
└─────────────────────┴────────────────────────┴────────────────────────┘

🎯 USE HTTP WHEN:
- Traditional request-response patterns
- CRUD operations
- RESTful APIs
- File downloads
- Simple data fetching

🎯 USE WEBSOCKET WHEN:
- Real-time updates needed
- Live chat applications
- Gaming (multiplayer)
- Live notifications
- Stock tickers / dashboards
- Collaborative editing
- IoT device communication

⚠️ WEBSOCKET CONSIDERATIONS:
- More complex to scale (sticky sessions)
- Need to handle reconnection
- Load balancers need WebSocket support
- State management is more complex
- May need fallback (long polling)
"""
print(comparison)

# ========== SOCKET.IO ALTERNATIVE ==========
print("\n" + "=" * 60)
print("SOCKET.IO ALTERNATIVE")
print("=" * 60)

socketio_example = '''
# Socket.IO provides higher-level abstraction with fallbacks
# Install: pip install python-socketio

# server.py
import socketio
from aiohttp import web

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

@sio.event
async def connect(sid, environ):
    print(f"Client connected: {sid}")
    await sio.emit('welcome', {'message': 'Welcome!'}, room=sid)

@sio.event
async def disconnect(sid):
    print(f"Client disconnected: {sid}")

@sio.event
async def chat_message(sid, data):
    print(f"Message from {sid}: {data}")
    # Broadcast to all clients
    await sio.emit('chat_message', {
        'user': data['user'],
        'message': data['message']
    })

@sio.event
async def join_room(sid, data):
    room = data['room']
    sio.enter_room(sid, room)
    await sio.emit('room_message', 
        {'message': f'User joined {room}'}, 
        room=room
    )

if __name__ == '__main__':
    web.run_app(app, port=8000)

# Socket.IO Benefits:
# - Automatic reconnection
# - Fallback to long polling
# - Rooms and namespaces
# - Built-in acknowledgments
# - Broadcasting made easy
'''
print("Socket.IO Example:")
print(socketio_example)

# ========== BEST PRACTICES ==========
print("\n" + "=" * 60)
print("WEBSOCKET BEST PRACTICES")
print("=" * 60)

best_practices = """
✅ BEST PRACTICES:

1. Connection Management:
   - Implement heartbeat/ping-pong
   - Handle reconnection gracefully
   - Set connection timeouts
   - Clean up closed connections

2. Security:
   - Use WSS (WebSocket Secure) in production
   - Validate origin headers
   - Authenticate on connection
   - Rate limit connections and messages

3. Error Handling:
   - Catch and log all errors
   - Send meaningful error messages
   - Implement graceful degradation
   - Have fallback mechanism (long polling)

4. Performance:
   - Keep messages small
   - Use binary data when appropriate
   - Implement message batching
   - Consider message compression

5. Scalability:
   - Use Redis for pub/sub across instances
   - Implement sticky sessions or Redis adapter
   - Monitor connection counts
   - Set reasonable connection limits

Example reconnection logic (JavaScript client):
```javascript
let reconnectAttempts = 0;
const maxReconnectAttempts = 5;

function connect() {
    const ws = new WebSocket('wss://example.com/ws');
    
    ws.onopen = () => {
        reconnectAttempts = 0;
        console.log('Connected');
    };
    
    ws.onclose = () => {
        if (reconnectAttempts < maxReconnectAttempts) {
            const delay = Math.pow(2, reconnectAttempts) * 1000;
            setTimeout(connect, delay);
            reconnectAttempts++;
        }
    };
    
    ws.onerror = (error) => {
        console.error('WebSocket error:', error);
    };
}
```
"""
print(best_practices)

print("\n" + "=" * 60)
print("✅ WebSockets for Real-Time Apps - Complete!")
print("=" * 60)
