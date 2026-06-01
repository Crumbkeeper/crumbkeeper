import { useEffect, useState } from "react";

export default function StorefrontPage() {
  const [products, setProducts] = useState<any[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/v1/products")
      .then((r) => r.json())
      .then(setProducts);
  }, []);

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">
        HoneyBean Storefront
      </h1>

      <p className="text-stone-600">
        Place bakery pickup orders
      </p>

      <div className="grid gap-6 md:grid-cols-2">
        {products.map((product) => (
          <div
            key={product.id}
            className="rounded-xl border p-6 space-y-3"
          >
            <h2 className="text-xl font-semibold">
              {product.name}
            </h2>

            <div>{product.category}</div>
            <div>${product.default_price}</div>
            <div>
              Lead Time: {product.lead_time_hours}h
            </div>

            <button
              className="w-full rounded bg-amber-700 text-white p-2"
            >
              Order Now
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
