import { useState } from "react";
import {
  useIngredients,
  type Ingredient,
  type IngredientPayload,
} from "../hooks/useIngredients";

const emptyForm: IngredientPayload = {
  bakery_id: 1,
  name: "",
  category: "Other",
  unit: "g",
  current_stock: 0,
  reorder_threshold: 0,
  cost_per_unit: 0,
  vendor: "",
  notes: "",
  active: true,
};

export default function IngredientsPage() {
  const {
    ingredients,
    createIngredient,
    updateIngredient,
    deleteIngredient,
  } = useIngredients();

  const [editingId, setEditingId] =
    useState<number | null>(null);

  const [form, setForm] =
    useState<IngredientPayload>(emptyForm);

  const resetForm = () => {
    setForm(emptyForm);
    setEditingId(null);
  };

  const loadIngredient = (
    ingredient: Ingredient
  ) => {
    setEditingId(ingredient.id);

    setForm({
      bakery_id: ingredient.bakery_id,
      name: ingredient.name,
      category: ingredient.category,
      unit: ingredient.unit,
      current_stock: ingredient.current_stock,
      reorder_threshold: ingredient.reorder_threshold,
      cost_per_unit: ingredient.cost_per_unit,
      vendor: ingredient.vendor || "",
      notes: ingredient.notes || "",
      active: ingredient.active,
    });
  };

  const handleSave = async () => {
    if (!form.name.trim()) return;

    if (editingId) {
      await updateIngredient(editingId, form);
    } else {
      await createIngredient(form);
    }

    resetForm();
  };

  const handleDelete = async () => {
    if (!editingId) return;

    await deleteIngredient(editingId);
    resetForm();
  };

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">
        Ingredients
      </h1>

      <div className="grid gap-8 md:grid-cols-2">

        <div className="rounded-xl border p-6 space-y-4">

          <h2 className="text-xl font-semibold">
            {editingId
              ? "Edit Ingredient"
              : "Create Ingredient"}
          </h2>

          <label>
            Ingredient Name
          </label>

          <input
            className="w-full border rounded p-2"
            value={form.name}
            onChange={(e) =>
              setForm({
                ...form,
                name: e.target.value,
              })
            }
          />

          <label>Category</label>

          <select
            className="w-full border rounded p-2"
            value={form.category}
            onChange={(e) =>
              setForm({
                ...form,
                category: e.target.value,
              })
            }
          >
            <option>Flour</option>
            <option>Water</option>
            <option>Starter</option>
            <option>Salt</option>
            <option>Sweetener</option>
            <option>Fat</option>
            <option>Dairy</option>
            <option>Egg</option>
            <option>Topping</option>
            <option>Inclusion</option>
            <option>Paper Goods</option>
            <option>Cleaning & Sanitation</option>
            <option>Other Food</option>
            <option>Packaging</option>
            <option>Other</option>
          </select>

          <label>Unit</label>

          <input
            className="w-full border rounded p-2"
            value={form.unit}
            onChange={(e) =>
              setForm({
                ...form,
                unit: e.target.value,
              })
            }
          />

          <label>Current Stock</label>

          <input
            type="number"
            className="w-full border rounded p-2"
            value={form.current_stock}
            onChange={(e) =>
              setForm({
                ...form,
                current_stock: Number(e.target.value),
              })
            }
          />

          <label>Reorder Threshold</label>

          <input
            type="number"
            className="w-full border rounded p-2"
            value={form.reorder_threshold}
            onChange={(e) =>
              setForm({
                ...form,
                reorder_threshold: Number(e.target.value),
              })
            }
          />

          <label>Cost Per Unit</label>

          <input
            type="number"
            className="w-full border rounded p-2"
            value={form.cost_per_unit}
            onChange={(e) =>
              setForm({
                ...form,
                cost_per_unit: Number(e.target.value),
              })
            }
          />

          <label>Vendor</label>

          <input
            className="w-full border rounded p-2"
            value={form.vendor || ""}
            onChange={(e) =>
              setForm({
                ...form,
                vendor: e.target.value,
              })
            }
          />

          <label>Notes</label>

          <textarea
            className="w-full border rounded p-2"
            value={form.notes || ""}
            onChange={(e) =>
              setForm({
                ...form,
                notes: e.target.value,
              })
            }
          />

          <label className="flex items-center gap-2">
            <input
              type="checkbox"
              checked={form.active}
              onChange={(e) =>
                setForm({
                  ...form,
                  active: e.target.checked,
                })
              }
            />
            Active Ingredient
          </label>

          <button
            onClick={handleSave}
            className="w-full rounded bg-amber-700 text-white p-2"
          >
            {editingId
              ? "Save Ingredient"
              : "Create Ingredient"}
          </button>

          {editingId && (
            <button
              onClick={handleDelete}
              className="w-full rounded bg-red-700 text-white p-2"
            >
              Delete Ingredient
            </button>
          )}

        </div>

        <div className="rounded-xl border p-6 space-y-4">

          <h2 className="text-xl font-semibold">
            Ingredient Library
          </h2>

          {ingredients.map(
            (ingredient) => (
              <div
                key={ingredient.id}
                onClick={() =>
                  loadIngredient(ingredient)
                }
                className="cursor-pointer rounded-lg border p-4"
              >
                <div className="font-semibold">
                  {ingredient.name}
                </div>

                <div>
                  Category: {ingredient.category}
                </div>

                <div>
                  Stock: {ingredient.current_stock} {ingredient.unit}
                </div>

                <div>
                  Reorder At: {ingredient.reorder_threshold}
                </div>

                <div>
                  Vendor: {ingredient.vendor}
                </div>

                <div>
                  Status: {
                    ingredient.active
                      ? "Active"
                      : "Inactive"
                  }
                </div>
              </div>
            )
          )}

        </div>

      </div>
    </div>
  );
}


