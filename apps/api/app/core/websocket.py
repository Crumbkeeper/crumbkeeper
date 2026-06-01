import json
from datetime import datetime

from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(
        self,
        websocket: WebSocket,
    ):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(
        self,
        websocket: WebSocket,
    ):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(
        self,
        event_type: str,
        payload: dict,
    ):
        message = json.dumps({
            "event": event_type,
            "payload": payload,
            "timestamp": datetime.utcnow().isoformat(),
        })

        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()
