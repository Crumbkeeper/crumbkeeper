import { useEffect, useState } from "react";
import { apiFetch } from "../services/api";

export type ShoppingItem = {
  id: number;
  inventory_item_id: number | null;
  item_name: string;
  quantity_needed: number;
  unit: string;
  status: string;
  source: string;
  notes: string | null;
};

export type ShoppingPayload = Omit<ShoppingItem, "id">;

export function useShopping() {
  const [items, setItems] = useState<ShoppingItem[]>([]);
  const [loading, setLoading] = useState(true);

  const loadShopping = async () => {
    setLoading(true);

    try {
      const data = await apiFetch<ShoppingItem[]>("/shopping-list");
      setItems(data);
    } catch {
      setItems([]);
    } finally {
      setLoading(false);
    }
  };

  const createShoppingItem = async (payload: ShoppingPayload) => {
    const created = await apiFetch<ShoppingItem>("/shopping-list", {
      method: "POST",
      body: JSON.stringify(payload),
    });

    setItems((current) => [...current, created]);
    return created;
  };

  const updateShoppingItem = async (
    id: number,
    payload: ShoppingPayload
  ) => {
    const updated = await apiFetch<ShoppingItem>(`/shopping-list/${id}`, {
      method: "PUT",
      body: JSON.stringify(payload),
    });

    setItems((current) =>
      current.map((item) => (item.id === id ? updated : item))
    );

    return updated;
  };

  const deleteShoppingItem = async (id: number) => {
    await apiFetch(`/shopping-list/${id}`, {
      method: "DELETE",
    });

    setItems((current) => current.filter((item) => item.id !== id));
  };

  useEffect(() => {
    loadShopping();
  }, []);

  return {
    items,
    loading,
    loadShopping,
    createShoppingItem,
    updateShoppingItem,
    deleteShoppingItem,
  };
}
