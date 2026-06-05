import { useEffect, useState } from "react";
import { apiFetch } from "../services/api";

export type RecipeIngredient = {
  id: number;
  recipe_id: number;
  ingredient_id: number;
  quantity: number;
  unit: string;
};

export type RecipeIngredientPayload =
  Omit<RecipeIngredient, "id">;

export function useRecipeIngredients() {
  const [
    recipeIngredients,
    setRecipeIngredients,
  ] = useState<RecipeIngredient[]>([]);

  const [loading, setLoading] =
    useState(true);

  const loadRecipeIngredients =
    async () => {
      setLoading(true);

      try {
        const data =
          await apiFetch<
            RecipeIngredient[]
          >(
            "/recipe-ingredients"
          );

        setRecipeIngredients(data);
      } catch {
        setRecipeIngredients([]);
      } finally {
        setLoading(false);
      }
    };

  const createRecipeIngredient =
    async (
      payload: RecipeIngredientPayload
    ) => {
      const created =
        await apiFetch<RecipeIngredient>(
          "/recipe-ingredients",
          {
            method: "POST",
            body: JSON.stringify(payload),
          }
        );

      setRecipeIngredients(
        (current) => [
          ...current,
          created,
        ]
      );

      return created;
    };

  const updateRecipeIngredient =
    async (
      id: number,
      payload: RecipeIngredientPayload
    ) => {
      const updated =
        await apiFetch<RecipeIngredient>(
          `/recipe-ingredients/${id}`,
          {
            method: "PUT",
            body: JSON.stringify(payload),
          }
        );

      setRecipeIngredients(
        (current) =>
          current.map((item) =>
            item.id === id
              ? updated
              : item
          )
      );

      return updated;
    };

  const deleteRecipeIngredient =
    async (id: number) => {
      await apiFetch(
        `/recipe-ingredients/${id}`,
        {
          method: "DELETE",
        }
      );

      setRecipeIngredients(
        (current) =>
          current.filter(
            (item) =>
              item.id !== id
          )
      );
    };

  useEffect(() => {
    loadRecipeIngredients();
  }, []);

  return {
    recipeIngredients,
    loading,
    loadRecipeIngredients,
    createRecipeIngredient,
    updateRecipeIngredient,
    deleteRecipeIngredient,
  };
}
