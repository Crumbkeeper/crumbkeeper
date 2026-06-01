import { useEffect, useState } from "react";

const API_URL = "http://127.0.0.1:8000/api/v1/orders";

export function useOrders() {
  const [orders, setOrders] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchOrders = async () => {
    const response = await fetch(API_URL);
    const data = await response.json();

    setOrders(data);
    setLoading(false);
  };

  useEffect(() => {
    fetchOrders();
  }, []);

  const createOrder = async (order: unknown) => {
    await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(order),
    });

    await fetchOrders();
  };

  const updateOrder = async (
    id: number,
    order: unknown
  ) => {
    await fetch(`${API_URL}/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(order),
    });

    await fetchOrders();
  };

  return {
    orders,
    loading,
    createOrder,
    updateOrder,
    refresh: fetchOrders,
  };
}
