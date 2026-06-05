import { useState } from "react";
import { useRecipes } from "../hooks/useRecipes";
import { useIngredients } from "../hooks/useIngredients";
import { useRecipeIngredients } from "../hooks/useRecipeIngredients";

export default function RecipesPage() {
  const {
    recipes,
    createRecipe,
    updateRecipe,
    deleteRecipe,
  } = useRecipes();

  const { ingredients } = useIngredients();

  const {
    recipeIngredients,
    createRecipeIngredient,
    deleteRecipeIngredient,
  } = useRecipeIngredients();

  const [editingId, setEditingId] = useState<number | null>(null);
  const [targetYield, setTargetYield] = useState(1);


  const [selectedIngredientId, setSelectedIngredientId] = useState(0);
  const [ingredientQuantity, setIngredientQuantity] = useState(0);
  const [ingredientUnit, setIngredientUnit] = useState("g");

  const emptyForm = {
    name: "",
    category: "",
    flour_grams: 0,
    water_grams: 0,
    starter_grams: 0,
    salt_grams: 0,
    yield_count: 1,
    dough_weight: 0,
    bulk_fermentation_hours: 0,
    cold_retard_hours: 0,
    bake_temperature: 450,
    bake_duration_minutes: 45,
    notes: "",
  };

  const [form, setForm] = useState(emptyForm);

  const resetForm = () => {
    setForm(emptyForm);
    setEditingId(null);
    setSelectedIngredientId(0);
    setIngredientQuantity(0);
    setIngredientUnit("g");
  };

  const loadRecipe = (recipe: any) => {
    setEditingId(recipe.id);

    setForm({
      name: recipe.name || "",
      category: recipe.category || "",
      flour_grams: recipe.flour_grams || 0,
      water_grams: recipe.water_grams || 0,
      starter_grams: recipe.starter_grams || 0,
      salt_grams: recipe.salt_grams || 0,
      yield_count: recipe.yield_count || 1,
      dough_weight: recipe.dough_weight || 0,
      bulk_fermentation_hours: recipe.bulk_fermentation_hours || 0,
      cold_retard_hours: recipe.cold_retard_hours || 0,
      bake_temperature: recipe.bake_temperature || 450,
      bake_duration_minutes: recipe.bake_duration_minutes || 45,
      notes: recipe.notes || "",
    });
  };

  const handleSave = async () => {
    if (!form.name.trim()) return;

    if (editingId) {
      await updateRecipe(editingId, form);
    } else {
      await createRecipe(form);
    }

    resetForm();
  };

  const handleDelete = async () => {
    if (!editingId) return;

    await deleteRecipe(editingId);
    resetForm();
  };

  const handleAddRecipeIngredient = async () => {
    if (!editingId) return;
    if (!selectedIngredientId) return;
    if (ingredientQuantity <= 0) return;

    await createRecipeIngredient({
      recipe_id: editingId,
      ingredient_id: selectedIngredientId,
      quantity: ingredientQuantity,
      unit: ingredientUnit,
    });

    setSelectedIngredientId(0);
    setIngredientQuantity(0);
    setIngredientUnit("g");
  };

  const scaleFactor =
    form.yield_count > 0
      ? targetYield / form.yield_count
      : 1;

  const attachedIngredients = recipeIngredients.filter(
    (item) => item.recipe_id === editingId
  );

  const ingredientName = (ingredientId: number) => {
    const ingredient = ingredients.find(
      (item) => item.id === ingredientId
    );

    return ingredient?.name || "Unknown Ingredient";
  };

  const hydration =
    form.flour_grams > 0
      ? ((form.water_grams / form.flour_grams) * 100).toFixed(1)
      : "0";

  const starterPercent =
    form.flour_grams > 0
      ? ((form.starter_grams / form.flour_grams) * 100).toFixed(1)
      : "0";

  const saltPercent =
    form.flour_grams > 0
      ? ((form.salt_grams / form.flour_grams) * 100).toFixed(1)
      : "0";

  const totalDough =
    form.flour_grams +
    form.water_grams +
    form.starter_grams +
    form.salt_grams;

  const recipeCost =
    attachedIngredients.reduce(
      (total, item) => {
        const ingredient =
          ingredients.find(
            (i) =>
              i.id === item.ingredient_id
          );

        return (
          total +
          (
            item.quantity *
            (ingredient?.cost_per_unit ?? 0)
          )
        );
      },
      0
    );

  const costPerItem =
    form.yield_count > 0
      ? recipeCost / form.yield_count
      : 0;

  const scaledFlour =
    form.flour_grams * scaleFactor;

  const scaledWater =
    form.water_grams * scaleFactor;

  const scaledStarter =
    form.starter_grams * scaleFactor;

  const scaledSalt =
    form.salt_grams * scaleFactor;

  const scaledCost =
    recipeCost * scaleFactor;

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">Recipes</h1>

      <div className="grid gap-8 xl:grid-cols-[500px_1fr]">
        <section className="rounded-xl border bg-white p-6 space-y-6">
          <h2 className="text-xl font-semibold">
            {editingId ? "Edit Recipe" : "Create Recipe"}
          </h2>

          <div className="space-y-3">
            <label className="block">
              <div className="mb-1 text-sm font-medium">Recipe Name</div>
              <input
                className="w-full rounded border p-2"
                value={form.name}
                onChange={(e) =>
                  setForm({ ...form, name: e.target.value })
                }
              />
            </label>

            <label className="block">
              <div className="mb-1 text-sm font-medium">Category</div>
              <input
                className="w-full rounded border p-2"
                value={form.category}
                onChange={(e) =>
                  setForm({ ...form, category: e.target.value })
                }
              />
            </label>
          </div>

          <div>
            <h3 className="font-semibold mb-3">Formula</h3>

            <div className="grid grid-cols-2 gap-3">
              <label>
                <div className="text-sm">Flour (g)</div>
                <input
                  type="number"
                  className="w-full rounded border p-2"
                  value={form.flour_grams}
                  onChange={(e) =>
                    setForm({
                      ...form,
                      flour_grams: Number(e.target.value),
                    })
                  }
                />
              </label>

              <label>
                <div className="text-sm">Water (g)</div>
                <input
                  type="number"
                  className="w-full rounded border p-2"
                  value={form.water_grams}
                  onChange={(e) =>
                    setForm({
                      ...form,
                      water_grams: Number(e.target.value),
                    })
                  }
                />
              </label>

              <label>
                <div className="text-sm">Starter (g)</div>
                <input
                  type="number"
                  className="w-full rounded border p-2"
                  value={form.starter_grams}
                  onChange={(e) =>
                    setForm({
                      ...form,
                      starter_grams: Number(e.target.value),
                    })
                  }
                />
              </label>

              <label>
                <div className="text-sm">Salt (g)</div>
                <input
                  type="number"
                  className="w-full rounded border p-2"
                  value={form.salt_grams}
                  onChange={(e) =>
                    setForm({
                      ...form,
                      salt_grams: Number(e.target.value),
                    })
                  }
                />
              </label>
            </div>
          </div>

          <div className="rounded-xl border bg-amber-50 p-4 space-y-4">
            <h3 className="font-semibold">Recipe Ingredients</h3>

            {!editingId && (
              <div className="text-sm text-stone-600">
                Save or select a recipe before adding ingredients.
              </div>
            )}

            {editingId && (
              <>
                <div className="grid gap-3 md:grid-cols-[1fr_100px_90px]">
                  <label>
                    <div className="text-sm">Ingredient</div>
                    <select
                      className="w-full rounded border p-2"
                      value={selectedIngredientId}
                      onChange={(e) =>
                        setSelectedIngredientId(Number(e.target.value))
                      }
                    >
                      <option value={0}>Select Ingredient</option>

                      {ingredients.map((ingredient) => (
                        <option key={ingredient.id} value={ingredient.id}>
                          {ingredient.name}
                        </option>
                      ))}
                    </select>
                  </label>

                  <label>
                    <div className="text-sm">Quantity</div>
                    <input
                      type="number"
                      className="w-full rounded border p-2"
                      value={ingredientQuantity}
                      onChange={(e) =>
                        setIngredientQuantity(Number(e.target.value))
                      }
                    />
                  </label>

                  <label>
                    <div className="text-sm">Unit</div>
                    <input
                      className="w-full rounded border p-2"
                      value={ingredientUnit}
                      onChange={(e) =>
                        setIngredientUnit(e.target.value)
                      }
                    />
                  </label>
                </div>

                <button
                  onClick={handleAddRecipeIngredient}
                  className="w-full rounded bg-stone-800 text-white p-2"
                >
                  Add Ingredient To Recipe
                </button>

                <div className="space-y-2">
                  {attachedIngredients.length === 0 && (
                    <div className="text-sm text-stone-600">
                      No ingredients attached yet.
                    </div>
                  )}

                  {attachedIngredients.map((item) => (
                    <div
                      key={item.id}
                      className="flex items-center justify-between rounded border bg-white p-3"
                    >
                      <div>
                        <div className="font-medium">
                          {ingredientName(item.ingredient_id)}
                        </div>
                        <div className="text-sm text-stone-600">
                          {item.quantity} {item.unit}
                        </div>
                      </div>

                      <button
                        onClick={() => deleteRecipeIngredient(item.id)}
                        className="rounded bg-red-700 px-3 py-1 text-sm text-white"
                      >
                        Remove
                      </button>
                    </div>
                  ))}
                </div>
              </>
            )}
          </div>

          <div>
            <h3 className="font-semibold mb-3">Production</h3>

            <div className="grid grid-cols-2 gap-3">
              <label>
                <div className="text-sm">Yield Count</div>
                <input
                  type="number"
                  className="w-full rounded border p-2"
                  value={form.yield_count}
                  onChange={(e) =>
                    setForm({
                      ...form,
                      yield_count: Number(e.target.value),
                    })
                  }
                />
              </label>

              <label>
                <div className="text-sm">Dough Weight</div>
                <input
                  type="number"
                  className="w-full rounded border p-2"
                  value={form.dough_weight}
                  onChange={(e) =>
                    setForm({
                      ...form,
                      dough_weight: Number(e.target.value),
                    })
                  }
                />
              </label>

              <label>
                <div className="text-sm">Bulk Fermentation</div>
                <input
                  type="number"
                  className="w-full rounded border p-2"
                  value={form.bulk_fermentation_hours}
                  onChange={(e) =>
                    setForm({
                      ...form,
                      bulk_fermentation_hours: Number(e.target.value),
                    })
                  }
                />
              </label>

              <label>
                <div className="text-sm">Cold Retard</div>
                <input
                  type="number"
                  className="w-full rounded border p-2"
                  value={form.cold_retard_hours}
                  onChange={(e) =>
                    setForm({
                      ...form,
                      cold_retard_hours: Number(e.target.value),
                    })
                  }
                />
              </label>

              <label>
                <div className="text-sm">Bake Temp</div>
                <input
                  type="number"
                  className="w-full rounded border p-2"
                  value={form.bake_temperature}
                  onChange={(e) =>
                    setForm({
                      ...form,
                      bake_temperature: Number(e.target.value),
                    })
                  }
                />
              </label>

              <label>
                <div className="text-sm">Bake Minutes</div>
                <input
                  type="number"
                  className="w-full rounded border p-2"
                  value={form.bake_duration_minutes}
                  onChange={(e) =>
                    setForm({
                      ...form,
                      bake_duration_minutes: Number(e.target.value),
                    })
                  }
                />
              </label>
            </div>
          </div>

          <label className="block">
            <div className="mb-1 text-sm font-medium">Notes</div>
            <textarea
              className="w-full rounded border p-2"
              rows={4}
              value={form.notes}
              onChange={(e) =>
                setForm({ ...form, notes: e.target.value })
              }
            />
          </label>

          <button
            onClick={handleSave}
            className="w-full rounded bg-amber-700 text-white p-2"
          >
            {editingId ? "Save Recipe" : "Create Recipe"}
          </button>

          {editingId && (
            <div className="grid grid-cols-2 gap-3">
              <button
                onClick={resetForm}
                className="rounded border p-2"
              >
                Cancel
              </button>

              <button
                onClick={handleDelete}
                className="rounded bg-red-700 text-white p-2"
              >
                Delete
              </button>
            </div>
          )}
        </section>

        <section className="space-y-4">
          <div className="rounded-xl border bg-white p-6">
            <h2 className="text-xl font-semibold mb-4">
              Recipe Intelligence
            </h2>

            <div>Hydration: {hydration}%</div>
            <div>Starter: {starterPercent}%</div>
            <div>Salt: {saltPercent}%</div>
            <div>Total Dough: {totalDough}g</div>
            <div>
              Recipe Cost: $
              {recipeCost.toFixed(2)}
            </div>
            <div>
              Cost Per Item: $
              {costPerItem.toFixed(2)}
            </div>

            <div className="mt-4">
              <label className="block">
                <div className="text-sm font-medium">Target Yield</div>
                <input
                  type="number"
                  value={targetYield}
                  onChange={(e) =>
                    setTargetYield(Number(e.target.value))
                  }
                  className="w-full rounded border p-2"
                />
              </label>
                          </div>

              <div className="mt-4 border-t pt-4">
                <div className="font-semibold mb-2">
                  Scaled Formula
                </div>

                <div>
                  Flour: {scaledFlour.toFixed(0)}g
                </div>

                <div>
                  Water: {scaledWater.toFixed(0)}g
                </div>

                <div>
                  Starter: {scaledStarter.toFixed(0)}g
                </div>

                <div>
                  Salt: {scaledSalt.toFixed(0)}g
                </div>

                <div className="mt-2">
                  Scaled Cost: $
                  {scaledCost.toFixed(2)}
                </div>
              </div>
          </div>

          <div className="rounded-xl border bg-white p-6">
            <h2 className="text-xl font-semibold mb-4">
              Recipe Library
            </h2>

            <div className="space-y-3">
              {recipes.map((recipe: any) => (
                <button
                  key={recipe.id}
                  onClick={() => loadRecipe(recipe)}
                  className="w-full rounded border p-4 text-left hover:bg-amber-50"
                >
                  <div className="font-semibold">{recipe.name}</div>
                  <div className="text-sm text-stone-600">
                    {recipe.category}
                  </div>
                  <div className="text-sm">
                    Yield: {recipe.yield_count}
                  </div>
                  <div className="text-sm">
                    Hydration:{" "}
                    {recipe.flour_grams > 0
                      ? (
                          (recipe.water_grams / recipe.flour_grams) *
                          100
                        ).toFixed(1)
                      : 0}
                    %
                  </div>
                  <div className="text-sm">
                    Version {recipe.version}
                  </div>
                </button>
              ))}
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}






