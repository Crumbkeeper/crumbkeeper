import { useState } from "react";

type Recipe = {
  name: string;
  category: string;
  flour: number;
  water: number;
  starter: number;
  salt: number;
};

export default function RecipesPage() {
  const [targetYield, setTargetYield] = useState(1);

  const recipes: Recipe[] = [
    {
      name: "Doughlene Country Loaf",
      category: "Sourdough",
      flour: 1000,
      water: 750,
      starter: 200,
      salt: 20,
    },
    {
      name: "Jalapeño Cheddar",
      category: "Inclusion Loaf",
      flour: 1000,
      water: 720,
      starter: 200,
      salt: 20,
    },
    {
      name: "Cinnamon Raisin Sandwich",
      category: "Sandwich Bread",
      flour: 900,
      water: 650,
      starter: 180,
      salt: 18,
    },
  ];

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">Recipes</h1>

      <div className="grid gap-8 md:grid-cols-2">
        <div className="rounded-xl border p-6 space-y-4">
          <h2 className="text-xl font-semibold">Create Recipe</h2>

          <input className="w-full border rounded p-2" placeholder="Recipe Name" />
          <input className="w-full border rounded p-2" placeholder="Category" />
          <input className="w-full border rounded p-2" placeholder="Flour (g)" />
          <input className="w-full border rounded p-2" placeholder="Water (g)" />
          <input className="w-full border rounded p-2" placeholder="Starter (g)" />
          <input className="w-full border rounded p-2" placeholder="Salt (g)" />

          <button className="w-full rounded bg-amber-700 text-white p-2">
            Save Recipe
          </button>
        </div>

        <div className="rounded-xl border p-6 space-y-4">
          <h2 className="text-xl font-semibold">Scale Recipe</h2>

          <input
            type="number"
            value={targetYield}
            onChange={(e) => setTargetYield(Number(e.target.value))}
            className="w-full border rounded p-2"
          />

          <div className="space-y-4">
            {recipes.map((recipe) => (
              <div key={recipe.name} className="rounded-lg border p-4">
                <h3 className="font-semibold">{recipe.name}</h3>

                <p className="text-sm text-gray-600">{recipe.category}</p>

                <div className="mt-2 text-sm">
                  Flour: {recipe.flour * targetYield}g
                  <br />
                  Water: {recipe.water * targetYield}g
                  <br />
                  Starter: {recipe.starter * targetYield}g
                  <br />
                  Salt: {recipe.salt * targetYield}g
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}