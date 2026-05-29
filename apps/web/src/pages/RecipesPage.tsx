import { useState } from "react";
import { useRecipes } from "../hooks/useRecipes";

export default function RecipesPage() {
  const { recipes, createRecipe } = useRecipes();

  const [targetYield, setTargetYield] = useState(1);
  const [editingId, setEditingId] = useState<number | null>(null);

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

    setEditingId(null);
  };

  const loadRecipe = (recipe: any) => {
    setEditingId(recipe.id);

    setForm({
      name: recipe.name,
      category: recipe.category,
      flour_grams: recipe.flour_grams,
      water_grams: recipe.water_grams,
      starter_grams: recipe.starter_grams,
      salt_grams: recipe.salt_grams,
      yield_count: recipe.yield_count,
    });
  };

  const calculateHydration = (recipe: any) =>
    ((recipe.water_grams / recipe.flour_grams) * 100).toFixed(1);

  const calculateStarter = (recipe: any) =>
    ((recipe.starter_grams / recipe.flour_grams) * 100).toFixed(1);

  const calculateSalt = (recipe: any) =>
    ((recipe.salt_grams / recipe.flour_grams) * 100).toFixed(1);

  const totalDough = (recipe: any) =>
    recipe.flour_grams +
    recipe.water_grams +
    recipe.starter_grams +
    recipe.salt_grams;

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">Recipes</h1>

      <div className="grid gap-8 md:grid-cols-2">

        <div className="rounded-xl border p-6 space-y-4">
          <h2 className="text-xl font-semibold">
            {editingId ? "Edit Recipe" : "Create Recipe"}
          </h2>

          <input className="w-full border rounded p-2"
            placeholder="Recipe Name"
            value={form.name}
            onChange={(e) => setForm({ ...form, name: e.target.value })}
          />

          <input className="w-full border rounded p-2"
            placeholder="Category"
            value={form.category}
            onChange={(e) => setForm({ ...form, category: e.target.value })}
          />

          <input className="w-full border rounded p-2"
            placeholder="Flour"
            type="number"
            onChange={(e) => setForm({ ...form, flour_grams: Number(e.target.value) })}
          />

          <input className="w-full border rounded p-2"
            placeholder="Water"
            type="number"
            onChange={(e) => setForm({ ...form, water_grams: Number(e.target.value) })}
          />

          <input className="w-full border rounded p-2"
            placeholder="Starter"
            type="number"
            onChange={(e) => setForm({ ...form, starter_grams: Number(e.target.value) })}
          />

          <input className="w-full border rounded p-2"
            placeholder="Salt"
            type="number"
            onChange={(e) => setForm({ ...form, salt_grams: Number(e.target.value) })}
          />

          <button
            onClick={handleCreate}
            className="w-full rounded bg-amber-700 text-white p-2"
          >
            {editingId ? "Save Revision" : "Save Recipe"}
          </button>
        </div>

        <div className="rounded-xl border p-6 space-y-4">
          <h2 className="text-xl font-semibold">Recipe Intelligence</h2>

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
                className="rounded-lg border p-4 cursor-pointer"
                onClick={() => loadRecipe(recipe)}
              >
                <h3 className="font-semibold">
                  {recipe.name} — v{recipe.version}
                </h3>

                <p className="text-sm text-gray-600">
                  {recipe.category}
                </p>

                <div className="mt-3 text-sm space-y-1">
                  <div>Hydration: {calculateHydration(recipe)}%</div>
                  <div>Starter: {calculateStarter(recipe)}%</div>
                  <div>Salt: {calculateSalt(recipe)}%</div>
                  <div>Total Dough: {totalDough(recipe) * targetYield}g</div>
                </div>
              </div>
            ))}
          </div>
        </div>

      </div>
    </div>
  );
}