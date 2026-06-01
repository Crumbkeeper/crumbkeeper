import { useState } from "react";
import { useOrders } from "../hooks/useOrders";

const statusFlow = [
  "new",
  "confirmed",
  "scheduled",
  "in production",
  "baked",
  "ready",
  "completed",
];

export default function OrdersPage() {
  const { orders, createOrder, updateOrder } = useOrders();

  const [form, setForm] = useState({
    customer_name: "",
    product_name: "",
    quantity: 1,
    pickup_date: "",
    status: "new",
    fulfillment_type: "pickup",
    payment_status: "pending",
    total_price: 0,
    notes: "",
  });

  const handleCreate = async () => {
    await createOrder(form);

    setForm({
      customer_name: "",
      product_name: "",
      quantity: 1,
      pickup_date: "",
      status: "new",
      fulfillment_type: "pickup",
      payment_status: "pending",
      total_price: 0,
      notes: "",
    });
  };

  const advanceStatus = async (order: any) => {
    const current = statusFlow.indexOf(order.status);

    const next =
      statusFlow[
        Math.min(current + 1, statusFlow.length - 1)
      ];

    await updateOrder(order.id, {
      ...order,
      status: next,
    });
  };

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">Orders</h1>

      <div className="grid md:grid-cols-2 gap-8">

        <div className="rounded-xl border p-6 space-y-4">
          <h2 className="text-xl font-semibold">
            Create Order
          </h2>

          <input
            className="w-full border rounded p-2"
            placeholder="Customer"
            value={form.customer_name}
            onChange={(e) =>
              setForm({
                ...form,
                customer_name: e.target.value,
              })
            }
          />

          <input
            className="w-full border rounded p-2"
            placeholder="Product"
            value={form.product_name}
            onChange={(e) =>
              setForm({
                ...form,
                product_name: e.target.value,
              })
            }
          />

          <input
            className="w-full border rounded p-2"
            type="date"
            value={form.pickup_date}
            onChange={(e) =>
              setForm({
                ...form,
                pickup_date: e.target.value,
              })
            }
          />

          <button
            onClick={handleCreate}
            className="w-full rounded bg-amber-700 text-white p-2"
          >
            Save Order
          </button>
        </div>

        <div className="rounded-xl border p-6 space-y-4">
          {orders.map((order: any) => (
            <div
              key={order.id}
              className="rounded-lg border p-4"
            >
              <h3 className="font-semibold">
                {order.customer_name}
              </h3>

              <div>{order.product_name}</div>
              <div>Status: {order.status}</div>

              <button
                onClick={() => advanceStatus(order)}
                className="rounded bg-amber-700 text-white px-3 py-1 mt-2"
              >
                Advance Status
              </button>
            </div>
          ))}
        </div>

      </div>
    </div>
  );
}
