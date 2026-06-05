import { useEffect, useState } from "react";
import { apiFetch } from "../services/api";

export type InventoryItem = {
  id: number;
  product_id: number;
  item_name: string;
  category: string;
  quantity_on_hand: number;
  projected_depletion: number;
  unit: string;
  reorder_threshold: number;
  low_stock: boolean;
};

export type InventoryPayload = Omit<InventoryItem, "id" | "low_stock"> & {
  low_stock?: boolean;
};

export function useInventory() {
  const [inventory, setInventory] = useState<InventoryItem[]>([]);
  const [loading, setLoading] = useState(true);

  const loadInventory = async () => {
    setLoading(true);

    try {
      const data = await apiFetch<InventoryItem[]>("/inventory");
      setInventory(data);
    } catch {
      setInventory([]);
    } finally {
      setLoading(false);
    }
  };

  const createInventoryItem = async (payload: InventoryPayload) => {
    const created = await apiFetch<InventoryItem>("/inventory", {
      method: "POST",
      body: JSON.stringify({
        ...payload,
        low_stock: payload.quantity_on_hand <= payload.reorder_threshold,
      }),
    });

    setInventory((current) => [...current, created]);
    return created;
  };

  const updateInventoryItem = async (
    id: number,
    payload: InventoryPayload
  ) => {
    const updated = await apiFetch<InventoryItem>(`/inventory/${id}`, {
      method: "PUT",
      body: JSON.stringify({
        ...payload,
        low_stock: payload.quantity_on_hand <= payload.reorder_threshold,
      }),
    });

    setInventory((current) =>
      current.map((item) => (item.id === id ? updated : item))
    );

    return updated;
  };

  const deleteInventoryItem = async (id: number) => {
    await apiFetch(`/inventory/${id}`, {
      method: "DELETE",
    });

    setInventory((current) => current.filter((item) => item.id !== id));
  };

  useEffect(() => {
    loadInventory();
  }, []);

  return {
    inventory,
    loading,
    loadInventory,
    createInventoryItem,
    updateInventoryItem,
    deleteInventoryItem,
  };
}
