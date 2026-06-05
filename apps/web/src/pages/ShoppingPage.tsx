import { useState } from "react";
import { useShopping } from "../hooks/useShopping";
import type {
  ShoppingItem,
  ShoppingPayload,
} from "../hooks/useShopping";

const emptyForm: ShoppingPayload = {
  inventory_item_id: null,
  item_name: "",
  quantity_needed: 0,
  unit: "g",
  status: "needed",
  source: "manual",
  notes: "",
};

export default function ShoppingPage() {
  const {
    items,
    loading,
    createShoppingItem,
    updateShoppingItem,
    deleteShoppingItem,
  } = useShopping();

  const [form, setForm] = useState<ShoppingPayload>(emptyForm);
  const [editingId, setEditingId] = useState<number | null>(null);

  const resetForm = () => {
    setForm(emptyForm);
    setEditingId(null);
  };

  const loadItem = (item: ShoppingItem) => {
    setEditingId(item.id);

    setForm({
      inventory_item_id: item.inventory_item_id,
      item_name: item.item_name,
      quantity_needed: item.quantity_needed,
      unit: item.unit,
      status: item.status,
      source: item.source,
      notes: item.notes || "",
    });
  };

  const handleSave = async () => {
    if (!form.item_name.trim()) {
      return;
    }

    if (editingId) {
      await updateShoppingItem(editingId, form);
    } else {
      await createShoppingItem(form);
    }

    resetForm();
  };

  const handleDelete = async () => {
    if (!editingId) {
      return;
    }

    await deleteShoppingItem(editingId);
    resetForm();
  };

  const markPurchased = async (item: ShoppingItem) => {
    await updateShoppingItem(item.id, {
      inventory_item_id: item.inventory_item_id,
      item_name: item.item_name,
      quantity_needed: item.quantity_needed,
      unit: item.unit,
      status: "purchased",
      source: item.source,
      notes: item.notes,
    });
  };

  return (
    <div className="p-6 space-y-8">
      <div>
        <h1 className="text-3xl font-bold">Shopping List</h1>
        <p className="text-sm text-stone-600">
          Manage manual purchases and inventory-generated low-stock needs.
        </p>
      </div>

      <div className="grid gap-8 lg:grid-cols-[380px_1fr]">
        <section className="rounded-xl border bg-white p-5 space-y-4">
          <h2 className="text-xl font-semibold">
            {editingId ? "Edit Shopping Item" : "Add Shopping Item"}
          </h2>

          <label className="block space-y-1">
            <span className="text-sm font-medium">Item Name</span>
            <input
              className="w-full rounded border p-2"
              placeholder="Bread Flour"
              value={form.item_name}
              onChange={(e) =>
                setForm({ ...form, item_name: e.target.value })
              }
            />
          </label>

          <div className="grid grid-cols-2 gap-3">
            <label className="block space-y-1">
              <span className="text-sm font-medium">Needed</span>
              <input
                type="number"
                className="w-full rounded border p-2"
                value={form.quantity_needed}
                onChange={(e) =>
                  setForm({
                    ...form,
                    quantity_needed: Number(e.target.value),
                  })
                }
              />
            </label>

            <label className="block space-y-1">
              <span className="text-sm font-medium">Unit</span>
              <select
                className="w-full rounded border p-2"
                value={form.unit}
                onChange={(e) =>
                  setForm({ ...form, unit: e.target.value })
                }
              >
                <option value="g">g</option>
                <option value="kg">kg</option>
                <option value="oz">oz</option>
                <option value="lb">lb</option>
                <option value="units">units</option>
                <option value="bags">bags</option>
                <option value="jars">jars</option>
              </select>
            </label>
          </div>

          <label className="block space-y-1">
            <span className="text-sm font-medium">Status</span>
            <select
              className="w-full rounded border p-2"
              value={form.status}
              onChange={(e) =>
                setForm({ ...form, status: e.target.value })
              }
            >
              <option value="needed">Needed</option>
              <option value="low">Low</option>
              <option value="stocked">Stocked</option>
              <option value="purchased">Purchased</option>
            </select>
          </label>

          <label className="block space-y-1">
            <span className="text-sm font-medium">Notes</span>
            <textarea
              className="w-full rounded border p-2"
              placeholder="Brand, supplier, package size, etc."
              value={form.notes || ""}
              onChange={(e) =>
                setForm({ ...form, notes: e.target.value })
              }
            />
          </label>

          <button
            onClick={handleSave}
            className="w-full rounded bg-amber-700 p-2 font-semibold text-white"
          >
            {editingId ? "Save Shopping Item" : "Add Shopping Item"}
          </button>

          {editingId && (
            <div className="grid grid-cols-2 gap-3">
              <button
                onClick={resetForm}
                className="rounded border p-2 font-semibold"
              >
                Cancel
              </button>

              <button
                onClick={handleDelete}
                className="rounded bg-red-700 p-2 font-semibold text-white"
              >
                Delete
              </button>
            </div>
          )}
        </section>

        <section className="space-y-4">
          <h2 className="text-xl font-semibold">Shopping Items</h2>

          {loading && <div>Loading shopping list...</div>}

          {!loading && items.length === 0 && (
            <div className="rounded-xl border bg-white p-5 text-stone-600">
              No shopping items yet. Add one manually or let low inventory
              generate it.
            </div>
          )}

          <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
            {items.map((item) => (
              <div
                key={item.id}
                className="rounded-xl border bg-white p-4 shadow-sm"
              >
                <button
                  onClick={() => loadItem(item)}
                  className="w-full text-left"
                >
                  <div className="flex items-start justify-between gap-3">
                    <div>
                      <h3 className="font-semibold">{item.item_name}</h3>
                      <p className="text-sm text-stone-500">
                        {item.source === "inventory"
                          ? "Generated from Inventory"
                          : "Manual Item"}
                      </p>
                    </div>

                    <span
                      className={
                        item.status === "purchased"
                          ? "rounded-full bg-green-100 px-2 py-1 text-xs font-semibold text-green-700"
                          : item.status === "low"
                          ? "rounded-full bg-yellow-100 px-2 py-1 text-xs font-semibold text-yellow-700"
                          : "rounded-full bg-red-100 px-2 py-1 text-xs font-semibold text-red-700"
                      }
                    >
                      {item.status}
                    </span>
                  </div>

                  <div className="mt-4 text-sm">
                    Needed:{" "}
                    <strong>
                      {item.quantity_needed} {item.unit}
                    </strong>
                  </div>

                  {item.notes && (
                    <div className="mt-2 text-sm text-stone-600">
                      {item.notes}
                    </div>
                  )}
                </button>

                {item.status !== "purchased" && (
                  <button
                    onClick={() => markPurchased(item)}
                    className="mt-4 w-full rounded border p-2 text-sm font-semibold"
                  >
                    Mark Purchased
                  </button>
                )}
              </div>
            ))}
          </div>
        </section>
      </div>
    </div>
  );
}
