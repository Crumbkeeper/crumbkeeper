import { useState } from "react";
import { useOrders } from "../hooks/useOrders";

const labelTypes = [
  "Pickup Label",
  "Ingredient Label",
  "Brand Seal",
  "Storage Label",
  "Compliance Label",
];

export default function LabelsPage() {
  const { orders } = useOrders();
  const [selected, setSelected] = useState("Pickup Label");

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">
        Labels + Printing
      </h1>

      <select
        className="w-full border rounded p-2"
        value={selected}
        onChange={(e) =>
          setSelected(e.target.value)
        }
      >
        {labelTypes.map((type) => (
          <option key={type}>{type}</option>
        ))}
      </select>

      <div className="space-y-4">
        {orders.map((order: any) => (
          <div
            key={order.id}
            className="rounded-xl border p-6 bg-white"
          >
            <h2 className="text-xl font-semibold">
              HoneyBean Bakery
            </h2>

            <div>Label Type: {selected}</div>
            <div>Product: {order.product_name}</div>
            <div>Customer: {order.customer_name}</div>
            <div>Pickup: {order.pickup_date}</div>
            <div>Store refrigerated if applicable</div>
            <div>
              Cottage Food Operation
            </div>
          </div>
        ))}
      </div>

      <button
        onClick={() => window.print()}
        className="w-full rounded bg-amber-700 text-white p-2"
      >
        Print
      </button>
    </div>
  );
}
