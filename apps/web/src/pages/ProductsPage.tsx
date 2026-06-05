import { useState } from "react";
import { useProducts } from "../hooks/useProducts";
import { useRecipes } from "../hooks/useRecipes";

export default function ProductsPage() {
  const {
    products,
    createProduct,
    updateProduct,
    deleteProduct,
  } = useProducts();

  const { recipes } = useRecipes();

  const emptyForm = {
    bakery_id: 1,
    recipe_id: null as number | null,
    name: "",
    category: "",
    default_price: 0,
    lead_time_hours: 24,
    max_daily_quantity: 10,
    order_cutoff_hours: 24,
    available_days: "",
    active: true,
  };

  const [form, setForm] = useState(emptyForm);
  const [editingId, setEditingId] = useState<number | null>(null);

  const resetForm = () => {
    setForm(emptyForm);
    setEditingId(null);
  };

  const handleSave = async () => {
    if (!form.name.trim()) {
      return;
    }

    if (editingId) {
      await updateProduct(editingId, form);
    } else {
      await createProduct(form);
    }

    resetForm();
  };

  const handleDelete = async () => {
    if (!editingId) {
      return;
    }

    await deleteProduct(editingId);
    resetForm();
  };

  const loadProduct = (product: any) => {
    setEditingId(product.id);

    setForm({
      bakery_id: product.bakery_id,
      recipe_id: product.recipe_id,
      name: product.name,
      category: product.category,
      default_price: product.default_price,
      lead_time_hours: product.lead_time_hours,
      max_daily_quantity: product.max_daily_quantity,
      order_cutoff_hours: product.order_cutoff_hours,
      available_days: product.available_days || "",
      active: product.active,
    });
  };

  const linkedRecipe = (recipeId: number | null) =>
    recipes.find((r: any) => r.id === recipeId);

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">
        Products
      </h1>

      <div className="grid md:grid-cols-2 gap-8">

        <div className="rounded-xl border p-6 space-y-4">
          <h2 className="text-xl font-semibold">
            {editingId
              ? "Edit Product"
              : "Create Product"}
          </h2>

          <input
            className="w-full border rounded p-2"
            placeholder="Product Name"
            value={form.name}
            onChange={(e) =>
              setForm({
                ...form,
                name: e.target.value,
              })
            }
          />

          <input
            className="w-full border rounded p-2"
            placeholder="Category"
            value={form.category}
            onChange={(e) =>
              setForm({
                ...form,
                category: e.target.value,
              })
            }
          />

          <select
            className="w-full border rounded p-2"
            value={form.recipe_id ?? ""}
            onChange={(e) =>
              setForm({
                ...form,
                recipe_id:
                  Number(e.target.value) || null,
              })
            }
          >
            <option value="">
              Select Recipe
            </option>

            {recipes.map((recipe: any) => (
              <option
                key={recipe.id}
                value={recipe.id}
              >
                {recipe.name}
              </option>
            ))}
          </select>

          <input
            className="w-full border rounded p-2"
            type="number"
            placeholder="Price"
            value={form.default_price}
            onChange={(e) =>
              setForm({
                ...form,
                default_price: Number(
                  e.target.value
                ),
              })
            }
          />

          <input
            className="w-full border rounded p-2"
            type="number"
            placeholder="Lead Time Hours"
            value={form.lead_time_hours}
            onChange={(e) =>
              setForm({
                ...form,
                lead_time_hours: Number(
                  e.target.value
                ),
              })
            }
          />

          <input
            className="w-full border rounded p-2"
            type="number"
            placeholder="Max Daily Quantity"
            value={form.max_daily_quantity}
            onChange={(e) =>
              setForm({
                ...form,
                max_daily_quantity: Number(
                  e.target.value
                ),
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
            Active Product
          </label>

          <button
            onClick={handleSave}
            className="w-full rounded bg-amber-700 text-white p-2"
          >
            {editingId
              ? "Save Product"
              : "Add Product"}
          </button>

          {editingId && (
            <div className="grid grid-cols-2 gap-2">

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
        </div>

        <div className="rounded-xl border p-6 space-y-4">
          <h2 className="text-xl font-semibold">
            Product Catalog
          </h2>

          {products.map((product: any) => {
            const recipe = linkedRecipe(
              product.recipe_id
            );

            return (
              <button
                key={product.id}
                onClick={() =>
                  loadProduct(product)
                }
                className="w-full text-left rounded-lg border p-4 hover:bg-amber-50"
              >
                <h3 className="font-semibold">
                  {product.name}
                </h3>

                <div>
                  ${product.default_price}
                </div>

                <div>
                  {product.category}
                </div>

                <div className="text-sm text-stone-600">
                  Recipe:{" "}
                  {(recipe as any)?.name ||
                    "Unlinked"}
                </div>

                <div className="text-sm">
                  Lead Time:{" "}
                  {product.lead_time_hours}h
                </div>

                <div className="text-sm">
                  Daily Limit:{" "}
                  {product.max_daily_quantity}
                </div>

                <div
                  className={
                    product.active
                      ? "text-green-700"
                      : "text-red-700"
                  }
                >
                  {product.active
                    ? "Active"
                    : "Inactive"}
                </div>
              </button>
            );
          })}
        </div>

      </div>
    </div>
  );
}
