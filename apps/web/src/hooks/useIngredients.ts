import { useEffect, useState } from "react";
import { apiFetch } from "../services/api";

export type Ingredient = {
  id: number;
  bakery_id: number;
  name: string;
  category: string;
  unit: string;
  current_stock: number;
  reorder_threshold: number;
  cost_per_unit: number;
  vendor: string | null;
  notes: string | null;
  active: boolean;
};

export type IngredientPayload =
  Omit<Ingredient, "id">;

export function useIngredients() {
  const [ingredients, setIngredients] =
    useState<Ingredient[]>([]);

  const [loading, setLoading] =
    useState(true);

  const loadIngredients =
    async () => {
      setLoading(true);

      try {
        const data =
          await apiFetch<Ingredient[]>(
            "/ingredients"
          );

        setIngredients(data);
      } catch {
        setIngredients([]);
      } finally {
        setLoading(false);
      }
    };

  const createIngredient =
    async (
      payload: IngredientPayload
    ) => {
      const created =
        await apiFetch<Ingredient>(
          "/ingredients",
          {
            method: "POST",
            body: JSON.stringify(payload),
          }
        );

      setIngredients(
        (current) => [
          ...current,
          created,
        ]
      );

      return created;
    };

  const updateIngredient =
    async (
      id: number,
      payload: IngredientPayload
    ) => {
      const updated =
        await apiFetch<Ingredient>(
          `/ingredients/${id}`,
          {
            method: "PUT",
            body: JSON.stringify(payload),
          }
        );

      setIngredients(
        (current) =>
          current.map((item) =>
            item.id === id
              ? updated
              : item
          )
      );

      return updated;
    };

  const deleteIngredient =
    async (id: number) => {
      await apiFetch(
        `/ingredients/${id}`,
        {
          method: "DELETE",
        }
      );

      setIngredients(
        (current) =>
          current.filter(
            (item) =>
              item.id !== id
          )
      );
    };

  useEffect(() => {
    loadIngredients();
  }, []);

  return {
    ingredients,
    loading,
    loadIngredients,
    createIngredient,
    updateIngredient,
    deleteIngredient,
  };
}
