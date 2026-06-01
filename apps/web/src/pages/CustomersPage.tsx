import { useEffect, useState } from "react";

export default function CustomersPage() {
  const [customers, setCustomers] = useState<any[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/v1/customers")
      .then((r) => r.json())
      .then(setCustomers);
  }, []);

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">
        Customers
      </h1>

      <div className="space-y-4">
        {customers.map((customer) => (
          <div
            key={customer.id}
            className="rounded-xl border p-4"
          >
            <h2 className="font-semibold">
              {customer.name}
            </h2>

            <div>{customer.email || "No email"}</div>
            <div>{customer.phone || "No phone"}</div>
            <div>
              Pickup: {customer.preferred_pickup_day || "Unspecified"}
            </div>
            <div>
              Favorites: {customer.favorite_products || "None"}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
