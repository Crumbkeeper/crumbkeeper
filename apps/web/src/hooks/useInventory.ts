import { useEffect, useState } from "react";
import { apiFetch } from "../services/api";

export function useInventory() {
  const [inventory, setInventory] =
    useState<any[]>([]);

  useEffect(() => {
    apiFetch<any[]>("/inventory")
      .then(setInventory)
      .catch(() => setInventory([]));
  }, []);

  return inventory;
}
