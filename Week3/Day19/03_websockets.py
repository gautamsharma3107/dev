"""
Day 19 - WebSockets Concept
===========================
Learn: Real-time bidirectional communication

Key Concepts:
- HTTP vs WebSockets
- WebSocket lifecycle
- Server implementation (FastAPI example)
- Client implementation
- Common use cases and patterns
"""

import asyncio

print("=" * 60)
print("WEBSOCKETS - REAL-TIME COMMUNICATION")
print("=" * 60)

# ========== HTTP VS WEBSOCKETS ==========
print("\n" + "=" * 60)
print("HTTP VS WEBSOCKETS")
print("=" * 60)

print("""
HTTP (Request-Response):
========================
Client                          Server
  │                              │
  │──── Request GET /data ──────>│
  │<─── Response {data} ─────────│
  │                              │
  │──── Request GET /data ──────>│
  │<─── Response {data} ─────────│
  
- One request = one response
- Client always initiates
- Connection closes after response
- Good for: APIs, web pages, REST

WebSocket (Bidirectional):
==========================
Client                          Server
  │                              │
  │──── Upgrade to WebSocket ───>│
  │<─── Connection Established ──│
  │                              │
  │<════ Message ═══════════════>│
  │<════ Message ═══════════════>│
  │<════ Message ═══════════════>│
  │                              │
  │──── Close Connection ───────>│

- Persistent connection
- Both can send messages anytime
- Real-time, low latency
- Good for: Chat, games, live updates
""")

# ========== WEBSOCKET LIFECYCLE ==========
print("\n" + "=" * 60)
print("WEBSOCKET LIFECYCLE")
print("=" * 60)

print("""
1. HANDSHAKE (HTTP Upgrade)
   Client: "I want to upgrade to WebSocket"
   Server: "OK, switching protocols"

2. OPEN CONNECTION
   - Both can send/receive messages
   - Connection stays open
   - Ping/pong for keepalive

3. MESSAGE EXCHANGE
   - Text or binary messages
   - No request/response pattern
   - Either side can initiate

4. CLOSE CONNECTION
   - Either side can close
   - Clean shutdown with close frame
""")

# ========== FASTAPI WEBSOCKET SERVER ==========
print("\n" + "=" * 60)
print("FASTAPI WEBSOCKET SERVER")
print("=" * 60)

server_code = '''
# server.py - FastAPI WebSocket Server
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

# Store active connections
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

# Simple echo WebSocket
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")

# Chat WebSocket with username
@app.websocket("/ws/chat/{username}")
async def chat_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket)
    await manager.broadcast(f"{username} joined the chat!")
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{username}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{username} left the chat")

# Run: uvicorn server:app --reload
'''

print("FastAPI WebSocket Server:")
print(server_code)

# ========== PYTHON WEBSOCKET CLIENT ==========
print("\n" + "=" * 60)
print("PYTHON WEBSOCKET CLIENT")
print("=" * 60)

client_code = '''
# client.py - WebSocket Client using websockets library
import asyncio
import websockets

async def echo_client():
    """Connect to echo server."""
    uri = "ws://localhost:8000/ws"
    
    async with websockets.connect(uri) as websocket:
        # Send message
        await websocket.send("Hello, Server!")
        print(f">>> Sent: Hello, Server!")
        
        # Receive response
        response = await websocket.recv()
        print(f"<<< Received: {response}")

# Run the client
asyncio.run(echo_client())

# ===== CHAT CLIENT =====
async def chat_client(username: str):
    """Interactive chat client."""
    uri = f"ws://localhost:8000/ws/chat/{username}"
    
    async with websockets.connect(uri) as websocket:
        # Task to receive messages
        async def receive_messages():
            async for message in websocket:
                print(f"\\n{message}")
        
        # Task to send messages
        async def send_messages():
            while True:
                message = await asyncio.get_event_loop().run_in_executor(
                    None, input, ""
                )
                await websocket.send(message)
        
        # Run both tasks concurrently
        await asyncio.gather(
            receive_messages(),
            send_messages()
        )

# Run: python client.py
# asyncio.run(chat_client("Alice"))
'''

print("Python WebSocket Client:")
print(client_code)

# ========== JAVASCRIPT CLIENT (BROWSER) ==========
print("\n" + "=" * 60)
print("JAVASCRIPT WEBSOCKET CLIENT (BROWSER)")
print("=" * 60)

js_client_code = '''
// Browser WebSocket client
const socket = new WebSocket('ws://localhost:8000/ws/chat/User1');

// Connection opened
socket.addEventListener('open', (event) => {
    console.log('Connected to server');
    socket.send('Hello, everyone!');
});

// Listen for messages
socket.addEventListener('message', (event) => {
    console.log('Received:', event.data);
    // Update UI with new message
    addMessageToChat(event.data);
});

// Connection closed
socket.addEventListener('close', (event) => {
    console.log('Disconnected from server');
});

// Handle errors
socket.addEventListener('error', (event) => {
    console.error('WebSocket error:', event);
});

// Send message function
function sendMessage(message) {
    if (socket.readyState === WebSocket.OPEN) {
        socket.send(message);
    } else {
        console.error('WebSocket is not connected');
    }
}

// Close connection
function disconnect() {
    socket.close();
}
'''

print("JavaScript WebSocket Client:")
print(js_client_code)

# ========== WEBSOCKET WITH JSON MESSAGES ==========
print("\n" + "=" * 60)
print("WEBSOCKET WITH JSON MESSAGES")
print("=" * 60)

json_websocket_code = '''
# server.py - WebSocket with JSON messages
from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
import json

app = FastAPI()

class Message(BaseModel):
    type: str
    data: dict

@app.websocket("/ws/json")
async def json_websocket(websocket: WebSocket):
    await websocket.accept()
    
    try:
        while True:
            # Receive JSON message
            raw_data = await websocket.receive_text()
            message = json.loads(raw_data)
            
            # Process based on message type
            if message["type"] == "ping":
                await websocket.send_json({
                    "type": "pong",
                    "data": {"timestamp": time.time()}
                })
            
            elif message["type"] == "subscribe":
                channel = message["data"]["channel"]
                # Add to subscription list
                await websocket.send_json({
                    "type": "subscribed",
                    "data": {"channel": channel}
                })
            
            elif message["type"] == "message":
                # Broadcast message
                await websocket.send_json({
                    "type": "message",
                    "data": message["data"]
                })
                
    except Exception as e:
        print(f"Error: {e}")
'''

print("WebSocket with JSON messages:")
print(json_websocket_code)

# ========== WEBSOCKET ROOMS/CHANNELS ==========
print("\n" + "=" * 60)
print("WEBSOCKET ROOMS/CHANNELS")
print("=" * 60)

rooms_code = '''
# Room-based chat server
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict, List

app = FastAPI()

class RoomManager:
    def __init__(self):
        self.rooms: Dict[str, List[WebSocket]] = {}
    
    async def join_room(self, room: str, websocket: WebSocket):
        await websocket.accept()
        if room not in self.rooms:
            self.rooms[room] = []
        self.rooms[room].append(websocket)
    
    def leave_room(self, room: str, websocket: WebSocket):
        if room in self.rooms:
            self.rooms[room].remove(websocket)
            if not self.rooms[room]:
                del self.rooms[room]
    
    async def broadcast_to_room(self, room: str, message: str):
        if room in self.rooms:
            for connection in self.rooms[room]:
                await connection.send_text(message)

rooms = RoomManager()

@app.websocket("/ws/room/{room_name}/{username}")
async def room_endpoint(websocket: WebSocket, room_name: str, username: str):
    await rooms.join_room(room_name, websocket)
    await rooms.broadcast_to_room(room_name, f"{username} joined {room_name}")
    
    try:
        while True:
            data = await websocket.receive_text()
            await rooms.broadcast_to_room(room_name, f"{username}: {data}")
    except WebSocketDisconnect:
        rooms.leave_room(room_name, websocket)
        await rooms.broadcast_to_room(room_name, f"{username} left {room_name}")
'''

print("Room-based WebSocket server:")
print(rooms_code)

# ========== WEBSOCKET WITH AUTHENTICATION ==========
print("\n" + "=" * 60)
print("WEBSOCKET WITH AUTHENTICATION")
print("=" * 60)

auth_websocket_code = '''
# Authenticated WebSocket
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query
from typing import Optional
import jwt

app = FastAPI()
SECRET_KEY = "your-secret-key"

async def get_current_user(token: str) -> Optional[dict]:
    """Validate token and return user."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"user_id": payload["sub"], "username": payload["name"]}
    except jwt.InvalidTokenError:
        return None

@app.websocket("/ws/secure")
async def secure_websocket(
    websocket: WebSocket,
    token: str = Query(...)  # Token from query string
):
    # Authenticate before accepting
    user = await get_current_user(token)
    if not user:
        await websocket.close(code=4001)  # Custom close code
        return
    
    await websocket.accept()
    await websocket.send_text(f"Welcome, {user['username']}!")
    
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"{user['username']}: {data}")
    except WebSocketDisconnect:
        print(f"User {user['username']} disconnected")

# Client connects: ws://localhost:8000/ws/secure?token=eyJhbG...
'''

print("Authenticated WebSocket:")
print(auth_websocket_code)

# ========== COMMON USE CASES ==========
print("\n" + "=" * 60)
print("COMMON WEBSOCKET USE CASES")
print("=" * 60)

print("""
1. REAL-TIME CHAT
   - Group chats, direct messages
   - Typing indicators
   - Read receipts

2. LIVE NOTIFICATIONS
   - Push notifications
   - Activity feeds
   - System alerts

3. COLLABORATIVE EDITING
   - Google Docs-style editing
   - Whiteboard applications
   - Code collaboration

4. GAMING
   - Multiplayer games
   - Real-time game state
   - Player movements

5. LIVE DATA
   - Stock tickers
   - Sports scores
   - IoT sensor data
   - Dashboard updates

6. STREAMING
   - Live audio/video chat signals
   - Screen sharing coordination
""")

# ========== SIMPLE SIMULATION ==========
print("\n" + "=" * 60)
print("SIMULATING WEBSOCKET COMMUNICATION")
print("=" * 60)

async def simulate_websocket():
    """Simulate WebSocket-like communication."""
    
    class MockWebSocket:
        """Mock WebSocket for demonstration."""
        def __init__(self, name):
            self.name = name
            self.messages = asyncio.Queue()
        
        async def send(self, message):
            print(f"  [{self.name}] Sent: {message}")
            await asyncio.sleep(0.1)
        
        async def receive(self, message):
            print(f"  [{self.name}] Received: {message}")
    
    # Simulate client-server communication
    client = MockWebSocket("Client")
    server = MockWebSocket("Server")
    
    print("\nSimulated WebSocket communication:")
    print("-" * 40)
    
    # Connection handshake
    await client.send("HTTP Upgrade to WebSocket")
    await server.receive("HTTP Upgrade to WebSocket")
    await server.send("101 Switching Protocols")
    await client.receive("101 Switching Protocols")
    print("  [Connection Established]")
    
    # Message exchange
    await client.send("Hello, Server!")
    await server.receive("Hello, Server!")
    await server.send("Hello, Client!")
    await client.receive("Hello, Client!")
    
    await server.send("Server Push: New data available!")
    await client.receive("Server Push: New data available!")
    
    # Close
    await client.send("Close Connection")
    print("  [Connection Closed]")

asyncio.run(simulate_websocket())

# ========== BEST PRACTICES ==========
print("\n" + "=" * 60)
print("WEBSOCKET BEST PRACTICES")
print("=" * 60)

print("""
✅ DO:
   - Implement heartbeat/ping-pong for connection health
   - Handle reconnection on client side
   - Use JSON for structured messages
   - Authenticate before accepting connection
   - Limit message size
   - Handle errors gracefully

❌ DON'T:
   - Don't use WebSockets for everything (REST is fine for CRUD)
   - Don't keep connections open indefinitely without heartbeat
   - Don't send sensitive data without encryption (use wss://)
   - Don't forget to handle disconnections

📝 WHEN TO USE:
   - Need real-time updates (< 1 second)
   - Server needs to push to client
   - Bidirectional communication required
   - High-frequency data exchange
""")

print("\n" + "=" * 60)
print("✅ WebSockets Concept - Complete!")
print("=" * 60)
