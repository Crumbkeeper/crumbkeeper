import { useState } from "react";

export default function ProductsPage() {
  const [products, setProducts] = useState<any[]>([]);

  const [form, setForm] = useState({
    bakery_id: 1,
    recipe_id: null,
    name: "",
    category: "",
    default_price: 0,
    lead_time_hours: 24,
    max_daily_quantity: 10,
    order_cutoff_hours: 24,
    available_days: "",
    active: true,
  });

  const createProduct = async () => {
    const response = await fetch(
      "http://127.0.0.1:8000/api/v1/products",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(form),
      }
    );

    const product = await response.json();

    setProducts([...products, product]);

    setForm({
      ...form,
      name: "",
      category: "",
      default_price: 0,
    });
  };

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
            type="number"
            placeholder="Price"
            onChange={(e) =>
              setForm({
                ...form,
                default_price: Number(e.target.value),
              })
            }
          />

          <button
            onClick={createProduct}
            className="w-full rounded bg-amber-700 text-white p-2"
          >
            Save Product
          </button>
        </div>

        <div className="rounded-xl border p-6 space-y-4">
          <h2 className="text-xl font-semibold">
            Product Catalog
          </h2>

          {products.map((product) => (
            <div
              key={product.id}
              className="rounded-lg border p-4"
            >
              <h3 className="font-semibold">
                {product.name}
              </h3>

              <div>${product.default_price}</div>
              <div>{product.category}</div>
              <div>{product.available_days}</div>
            </div>
          ))}
        </div>

      </div>
    </div>
  );
}