import { useEffect, useState } from "react";
import { apiFetch } from "../services/api";

export function useOrders() {
  const [orders, setOrders] = useState<any[]>([]);

  useEffect(() => {
    apiFetch<any[]>("/orders")
      .then(setOrders)
      .catch(() => setOrders([]));
  }, []);

  return orders;
}
