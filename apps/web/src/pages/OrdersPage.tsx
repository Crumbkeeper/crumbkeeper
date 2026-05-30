import { useState } from "react";

export default function OrdersPage() {
  const [orders, setOrders] = useState<any[]>([]);

  const [form, setForm] = useState({
    customer: "",
    product: "",
    quantity: 1,
    pickup_date: "",
    status: "new",
  });

  const createOrder = () => {
    const order = {
      id: Date.now(),
      ...form,
    };

    setOrders([...orders, order]);

    setForm({
      customer: "",
      product: "",
      quantity: 1,
      pickup_date: "",
      status: "new",
    });
  };

  const advanceStatus = (id: number) => {
    const flow = [
      "new",
      "confirmed",
      "scheduled",
      "in production",
      "baked",
      "ready",
      "completed",
    ];

    setOrders(
      orders.map((order) => {
        if (order.id !== id) return order;

        const current = flow.indexOf(order.status);

        return {
          ...order,
          status: flow[Math.min(current + 1, flow.length - 1)],
        };
      })
    );
  };

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">
        Orders
      </h1>

      <div className="grid md:grid-cols-2 gap-8">

        <div className="rounded-xl border p-6 space-y-4">
          <h2 className="text-xl font-semibold">
            Create Order
          </h2>

          <input
            className="w-full border rounded p-2"
            placeholder="Customer"
            value={form.customer}
            onChange={(e) =>
              setForm({ ...form, customer: e.target.value })
            }
          />

          <input
            className="w-full border rounded p-2"
            placeholder="Product"
            value={form.product}
            onChange={(e) =>
              setForm({ ...form, product: e.target.value })
            }
          />

          <input
            className="w-full border rounded p-2"
            type="number"
            placeholder="Quantity"
            value={form.quantity}
            onChange={(e) =>
              setForm({
                ...form,
                quantity: Number(e.target.value),
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
            onClick={createOrder}
            className="w-full rounded bg-amber-700 text-white p-2"
          >
            Save Order
          </button>
        </div>

        <div className="rounded-xl border p-6 space-y-4">
          <h2 className="text-xl font-semibold">
            Order Queue
          </h2>

          {orders.map((order) => (
            <div
              key={order.id}
              className="rounded-lg border p-4 space-y-2"
            >
              <h3 className="font-semibold">
                {order.customer}
              </h3>

              <div>{order.product}</div>
              <div>Qty: {order.quantity}</div>
              <div>Status: {order.status}</div>

              <button
                onClick={() => advanceStatus(order.id)}
                className="rounded bg-sage-700 text-white px-3 py-1"
              >
                Advance
              </button>
            </div>
          ))}
        </div>

      </div>
    </div>
  );
}