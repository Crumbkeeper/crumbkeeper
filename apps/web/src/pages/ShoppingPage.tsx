import { useEffect, useState } from "react";

export default function ShoppingPage() {
  const [items, setItems] = useState<any[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/v1/shopping-list")
      .then((r) => r.json())
      .then(setItems);
  }, []);

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">
        Shopping List
      </h1>

      <div className="space-y-4">
        {items.map((item) => (
          <div
            key={item.ingredient}
            className="rounded-xl border p-4"
          >
            <h2 className="font-semibold">
              {item.ingredient}
            </h2>

            <div>
              Needed: {item.needed} {item.unit}
            </div>

            <div
              className={
                item.status === "buy"
                  ? "text-red-600"
                  : item.status === "low"
                  ? "text-yellow-600"
                  : "text-green-600"
              }
            >
              {item.status}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
