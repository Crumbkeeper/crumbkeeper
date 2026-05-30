import { useOrders } from "../hooks/useOrders";
import { useProductionRuns } from "../hooks/useProductionRuns";
import { useInventory } from "../hooks/useInventory";
import { useRealtime } from "../hooks/useRealtime";

export default function DashboardPage() {
  const { orders } = useOrders();
  const { runs } = useProductionRuns();
  const inventory = useInventory();
  const realtime = useRealtime();

  const tasks = [
    "Feed Doughlene",
    "Stretch + Fold Round 2",
    "Shape Cinnamon Raisin",
    "Prep Bagel Boil",
  ];

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-4xl font-bold">
        Today Mode
      </h1>

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

        <div className="rounded-xl border p-4">
          <h2 className="font-semibold">Realtime</h2>
          <p>{realtime ? "Live Kitchen" : "Offline"}</p>
        </div>

        <div className="rounded-xl border p-4">
          <h2 className="font-semibold">Active Runs</h2>
          <p>{runs.length}</p>
        </div>

        <div className="rounded-xl border p-4">
          <h2 className="font-semibold">Orders Due</h2>
          <p>{orders.length}</p>
        </div>

        <div className="rounded-xl border p-4">
          <h2 className="font-semibold">Inventory Alerts</h2>
          <p>{inventory.length}</p>
        </div>

      </div>

      <div className="grid gap-8 md:grid-cols-2">

        <section className="rounded-xl border p-6">
          <h2 className="text-xl font-semibold mb-4">
            Active Tasks
          </h2>

          <div className="space-y-3">
            {tasks.map((task) => (
              <div
                key={task}
                className="rounded-lg border p-3"
              >
                {task}
              </div>
            ))}
          </div>
        </section>

        <section className="rounded-xl border p-6">
          <h2 className="text-xl font-semibold mb-4">
            Production Timeline
          </h2>

          <div className="space-y-2 text-sm">
            <p>6:00 AM — Feed Starter</p>
            <p>9:00 AM — Mix Dough</p>
            <p>10:00 AM — Stretch + Fold</p>
            <p>1:00 PM — Shape</p>
            <p>7:00 PM — Cold Retard</p>
          </div>
        </section>

      </div>
    </div>
  );
}