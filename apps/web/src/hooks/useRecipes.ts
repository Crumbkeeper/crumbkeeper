import { useEffect, useState } from "react";

const API_URL = "http://127.0.0.1:8000/api/v1/recipes";

export function useRecipes() {
  const [recipes, setRecipes] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchRecipes = async () => {
    const response = await fetch(API_URL);
    const data = await response.json();

    setRecipes(data);
    setLoading(false);
  };

  useEffect(() => {
    fetchRecipes();
  }, []);

  const createRecipe = async (recipe: unknown) => {
    await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(recipe),
    });

    await fetchRecipes();
  };

  return {
    recipes,
    loading,
    createRecipe,
    refresh: fetchRecipes,
  };
}
