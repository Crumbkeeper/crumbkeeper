import { useState } from "react";
import { useProducts } from "../hooks/useProducts";
import { useRecipes } from "../hooks/useRecipes";

export default function ProductsPage() {
  const { products, createProduct } = useProducts();
  const { recipes } = useRecipes();

  const [form, setForm] = useState({
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
  });

  const handleCreate = async () => {
    await createProduct(form);

    setForm({
      ...form,
      recipe_id: null,
      name: "",
      category: "",
      default_price: 0,
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
            Create Product
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
                recipe_id: Number(e.target.value) || null,
              })
            }
          >
            <option value="">Select Recipe</option>

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
                default_price: Number(e.target.value),
              })
            }
          />

          <button
            onClick={handleCreate}
            className="w-full rounded bg-amber-700 text-white p-2"
          >
            Save Product
          </button>
        </div>

        <div className="rounded-xl border p-6 space-y-4">
          <h2 className="text-xl font-semibold">
            Product Catalog
          </h2>

          {products.map((product: any) => {
            const recipe = linkedRecipe(product.recipe_id);

            return (
              <div
                key={product.id}
                className="rounded-lg border p-4"
              >
                <h3 className="font-semibold">
                  {product.name}
                </h3>

                <div>${product.default_price}</div>
                <div>{product.category}</div>

                <div className="text-sm text-stone-600">
                  Recipe: {(recipe as any)?.name || "Unlinked"}
                </div>
              </div>
            );
          })}
        </div>

      </div>
    </div>
  );
}
