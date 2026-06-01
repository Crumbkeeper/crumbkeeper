import { useInventory } from "../hooks/useInventory";

export default function InventoryPage() {
  const inventory = useInventory();

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">
        Inventory
      </h1>

      <div className="space-y-4">
        {inventory.map((item: any) => (
          <div
            key={item.id}
            className="rounded-xl border p-4"
          >
            <h2 className="font-semibold">
              {item.item_name}
            </h2>

            <div>
              On Hand: {item.quantity_on_hand} {item.unit}
            </div>

            <div>
              Projected Use: {item.projected_depletion}
            </div>

            <div>
              Reorder At: {item.reorder_threshold}
            </div>

            <div
              className={
                item.low_stock
                  ? "text-red-600 font-semibold"
                  : "text-green-600"
              }
            >
              {item.low_stock
                ? "Low Stock"
                : "Stock Healthy"}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
