import { useEffect, useState } from "react";

export function useRealtime() {
  const [connected, setConnected] =
    useState(false);

  useEffect(() => {
    const socket = new WebSocket(
      "ws://127.0.0.1:8000/ws"
    );

    socket.onopen = () => {
      setConnected(true);
    };

    socket.onclose = () => {
      setConnected(false);
    };

    return () => {
      socket.close();
    };
  }, []);

  return connected;
}
