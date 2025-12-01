"""
MINI PROJECT 1: Real-Time Notification System
=============================================
Build a real-time notification system using WebSockets

Requirements:
1. WebSocket server that manages connections
2. Support for different notification channels (user, broadcast)
3. JSON message format for notifications
4. Connection management (connect, disconnect, track users)
5. Simple notification sending mechanism

Features to implement:
- Connect with user ID
- Subscribe to channels
- Send notifications to specific users
- Broadcast notifications to all users
- Handle disconnections gracefully
"""

print("=" * 60)
print("REAL-TIME NOTIFICATION SYSTEM")
print("=" * 60)

# TODO: Implement the notification system

# Suggested structure:

# 1. ConnectionManager class
# --------------------------
# class ConnectionManager:
#     def __init__(self):
#         self.active_connections: Dict[str, WebSocket] = {}  # user_id -> websocket
#         self.channels: Dict[str, Set[str]] = {}  # channel -> set of user_ids
#
#     async def connect(self, user_id: str, websocket: WebSocket):
#         pass
#
#     def disconnect(self, user_id: str):
#         pass
#
#     async def send_to_user(self, user_id: str, message: dict):
#         pass
#
#     async def broadcast(self, message: dict):
#         pass
#
#     async def send_to_channel(self, channel: str, message: dict):
#         pass


# 2. Notification message format
# ------------------------------
# {
#     "type": "notification",
#     "data": {
#         "title": "New Message",
#         "body": "You have a new message from Alice",
#         "timestamp": "2024-01-15T10:30:00Z",
#         "priority": "high"
#     }
# }


# 3. FastAPI WebSocket endpoint
# -----------------------------
# @app.websocket("/ws/notifications/{user_id}")
# async def notification_websocket(websocket: WebSocket, user_id: str):
#     await manager.connect(user_id, websocket)
#     try:
#         while True:
#             data = await websocket.receive_json()
#             # Handle different message types (subscribe, unsubscribe, etc.)
#     except WebSocketDisconnect:
#         manager.disconnect(user_id)


# 4. REST API to send notifications
# ---------------------------------
# @app.post("/notify/{user_id}")
# async def send_notification(user_id: str, notification: Notification):
#     await manager.send_to_user(user_id, notification.dict())
#     return {"status": "sent"}


# BONUS: Add these features
# -------------------------
# - Notification history storage
# - Read/unread status tracking
# - Notification preferences
# - Rate limiting on notifications


print("\nImplement your notification system above!")
