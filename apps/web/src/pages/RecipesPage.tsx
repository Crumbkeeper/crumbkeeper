import { useState } from "react";
import { useRecipes } from "../hooks/useRecipes";

export default function RecipesPage() {
  const { recipes, createRecipe } = useRecipes();

  const [targetYield, setTargetYield] = useState(1);

  const [form, setForm] = useState({
    name: "",
    category: "",
    flour_grams: 0,
    water_grams: 0,
    starter_grams: 0,
    salt_grams: 0,
    yield_count: 1,
  });

  const handleCreate = async () => {
    await createRecipe(form);

    setForm({
      name: "",
      category: "",
      flour_grams: 0,
      water_grams: 0,
      starter_grams: 0,
      salt_grams: 0,
      yield_count: 1,
    });
  };

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">Recipes</h1>

      <div className="grid gap-8 md:grid-cols-2">

        <div className="rounded-xl border p-6 space-y-4">
          <h2 className="text-xl font-semibold">
            Create Recipe
          </h2>

          <input
            className="w-full border rounded p-2"
            placeholder="Recipe Name"
            value={form.name}
            onChange={(e) =>
              setForm({ ...form, name: e.target.value })
            }
          />

          <input
            className="w-full border rounded p-2"
            placeholder="Category"
            value={form.category}
            onChange={(e) =>
              setForm({ ...form, category: e.target.value })
            }
          />

          <input
            className="w-full border rounded p-2"
            placeholder="Flour (g)"
            type="number"
            onChange={(e) =>
              setForm({ ...form, flour_grams: Number(e.target.value) })
            }
          />

          <input
            className="w-full border rounded p-2"
            placeholder="Water (g)"
            type="number"
            onChange={(e) =>
              setForm({ ...form, water_grams: Number(e.target.value) })
            }
          />

          <input
            className="w-full border rounded p-2"
            placeholder="Starter (g)"
            type="number"
            onChange={(e) =>
              setForm({ ...form, starter_grams: Number(e.target.value) })
            }
          />

          <input
            className="w-full border rounded p-2"
            placeholder="Salt (g)"
            type="number"
            onChange={(e) =>
              setForm({ ...form, salt_grams: Number(e.target.value) })
            }
          />

          <button
            onClick={handleCreate}
            className="w-full rounded bg-amber-700 text-white p-2"
          >
            Save Recipe
          </button>
        </div>

        <div className="rounded-xl border p-6 space-y-4">
          <h2 className="text-xl font-semibold">
            Saved Recipes
          </h2>

          <input
            type="number"
            value={targetYield}
            onChange={(e) => setTargetYield(Number(e.target.value))}
            className="w-full border rounded p-2"
          />

          <div className="space-y-4">
            {recipes.map((recipe: any) => (
              <div
                key={recipe.id}
                className="rounded-lg border p-4"
              >
                <h3 className="font-semibold">
                  {recipe.name}
                </h3>

                <p className="text-sm text-gray-600">
                  {recipe.category}
                </p>

                <div className="mt-2 text-sm">
                  Flour: {recipe.flour_grams * targetYield}g
                  <br />
                  Water: {recipe.water_grams * targetYield}g
                  <br />
                  Starter: {recipe.starter_grams * targetYield}g
                  <br />
                  Salt: {recipe.salt_grams * targetYield}g
                </div>
              </div>
            ))}
          </div>
        </div>

      </div>
    </div>
  );
}