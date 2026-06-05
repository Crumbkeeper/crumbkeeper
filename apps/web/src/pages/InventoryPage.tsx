import { useState } from "react";
import { useInventory } from "../hooks/useInventory";
import type {
  InventoryItem,
  InventoryPayload,
} from "../hooks/useInventory";

const emptyForm: InventoryPayload = {
  product_id: 1,
  item_name: "",
  category: "ingredient",
  quantity_on_hand: 0,
  projected_depletion: 0,
  unit: "g",
  reorder_threshold: 0,
};

export default function InventoryPage() {
  const {
    inventory,
    loading,
    createInventoryItem,
    updateInventoryItem,
    deleteInventoryItem,
  } = useInventory();

  const [form, setForm] = useState<InventoryPayload>(emptyForm);
  const [editingId, setEditingId] = useState<number | null>(null);

  const resetForm = () => {
    setForm(emptyForm);
    setEditingId(null);
  };

  const loadItem = (item: InventoryItem) => {
    setEditingId(item.id);

    setForm({
      product_id: item.product_id,
      item_name: item.item_name,
      category: item.category,
      quantity_on_hand: item.quantity_on_hand,
      projected_depletion: item.projected_depletion,
      unit: item.unit,
      reorder_threshold: item.reorder_threshold,
    });
  };

  const handleSave = async () => {
    if (!form.item_name.trim()) {
      return;
    }

    if (editingId) {
      await updateInventoryItem(editingId, form);
    } else {
      await createInventoryItem(form);
    }

    resetForm();
  };

  const handleDelete = async () => {
    if (!editingId) {
      return;
    }

    await deleteInventoryItem(editingId);
    resetForm();
  };

  const projectedRemaining =
    Number(form.quantity_on_hand) - Number(form.projected_depletion);

  const formLowStock =
    Number(form.quantity_on_hand) <= Number(form.reorder_threshold);

  return (
    <div className="p-6 space-y-8">
      <div>
        <h1 className="text-3xl font-bold">Inventory</h1>
        <p className="text-sm text-stone-600">
          Track bakery ingredients, stock levels, projected use, and reorder
          points.
        </p>
      </div>

      <div className="grid gap-8 lg:grid-cols-[380px_1fr]">
        <section className="rounded-xl border bg-white p-5 space-y-4">
          <h2 className="text-xl font-semibold">
            {editingId ? "Edit Inventory Item" : "Add Inventory Item"}
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

          <label className="block space-y-1">
            <span className="text-sm font-medium">Category</span>
            <select
              className="w-full rounded border p-2"
              value={form.category}
              onChange={(e) =>
                setForm({ ...form, category: e.target.value })
              }
            >
              <option value="ingredient">Ingredient</option>
              <option value="packaging">Packaging</option>
              <option value="finished_good">Finished Good</option>
              <option value="starter">Starter</option>
              <option value="other">Other</option>
            </select>
          </label>

          <div className="grid grid-cols-2 gap-3">
            <label className="block space-y-1">
              <span className="text-sm font-medium">On Hand</span>
              <input
                type="number"
                className="w-full rounded border p-2"
                value={form.quantity_on_hand}
                onChange={(e) =>
                  setForm({
                    ...form,
                    quantity_on_hand: Number(e.target.value),
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

          <div className="grid grid-cols-2 gap-3">
            <label className="block space-y-1">
              <span className="text-sm font-medium">Projected Use</span>
              <input
                type="number"
                className="w-full rounded border p-2"
                value={form.projected_depletion}
                onChange={(e) =>
                  setForm({
                    ...form,
                    projected_depletion: Number(e.target.value),
                  })
                }
              />
            </label>

            <label className="block space-y-1">
              <span className="text-sm font-medium">Reorder At</span>
              <input
                type="number"
                className="w-full rounded border p-2"
                value={form.reorder_threshold}
                onChange={(e) =>
                  setForm({
                    ...form,
                    reorder_threshold: Number(e.target.value),
                  })
                }
              />
            </label>
          </div>

          <div className="rounded-lg bg-amber-50 p-3 text-sm">
            <div>
              Projected Remaining:{" "}
              <strong>
                {projectedRemaining} {form.unit}
              </strong>
            </div>
            <div>
              Status:{" "}
              <strong className={formLowStock ? "text-red-700" : "text-green-700"}>
                {formLowStock ? "Low Stock" : "Stock Healthy"}
              </strong>
            </div>
          </div>

          <button
            onClick={handleSave}
            className="w-full rounded bg-amber-700 p-2 font-semibold text-white"
          >
            {editingId ? "Save Inventory Item" : "Add Inventory Item"}
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
          <h2 className="text-xl font-semibold">Inventory Items</h2>

          {loading && <div>Loading inventory...</div>}

          {!loading && inventory.length === 0 && (
            <div className="rounded-xl border bg-white p-5 text-stone-600">
              No inventory items yet. Add your first bakery ingredient.
            </div>
          )}

          <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
            {inventory.map((item) => {
              const remaining =
                item.quantity_on_hand - item.projected_depletion;

              return (
                <button
                  key={item.id}
                  onClick={() => loadItem(item)}
                  className="rounded-xl border bg-white p-4 text-left shadow-sm hover:bg-amber-50"
                >
                  <div className="flex items-start justify-between gap-3">
                    <div>
                      <h3 className="font-semibold">{item.item_name}</h3>
                      <p className="text-sm text-stone-500">
                        {item.category}
                      </p>
                    </div>

                    <span
                      className={
                        item.low_stock
                          ? "rounded-full bg-red-100 px-2 py-1 text-xs font-semibold text-red-700"
                          : "rounded-full bg-green-100 px-2 py-1 text-xs font-semibold text-green-700"
                      }
                    >
                      {item.low_stock ? "Low" : "Healthy"}
                    </span>
                  </div>

                  <div className="mt-4 space-y-1 text-sm">
                    <div>
                      On Hand:{" "}
                      <strong>
                        {item.quantity_on_hand} {item.unit}
                      </strong>
                    </div>
                    <div>
                      Projected Use:{" "}
                      <strong>
                        {item.projected_depletion} {item.unit}
                      </strong>
                    </div>
                    <div>
                      Remaining:{" "}
                      <strong>
                        {remaining} {item.unit}
                      </strong>
                    </div>
                    <div>
                      Reorder At:{" "}
                      <strong>
                        {item.reorder_threshold} {item.unit}
                      </strong>
                    </div>
                  </div>
                </button>
              );
            })}
          </div>
        </section>
      </div>
    </div>
  );
}

