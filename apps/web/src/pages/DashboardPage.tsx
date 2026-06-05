import { useMemo } from "react";
import { useOrders } from "../hooks/useOrders";
import { useProductionRuns } from "../hooks/useProductionRuns";
import { useInventory } from "../hooks/useInventory";
import { useRealtime } from "../hooks/useRealtime";

export default function DashboardPage() {
  const { orders } = useOrders();
  const { runs } = useProductionRuns();
  const { inventory } = useInventory();
  const realtime = useRealtime();

  const tasks = useMemo(() => {
    return runs.length
      ? runs.map((run: any) => run.task_name)
      : ["No active production tasks"];
  }, [runs]);

  const timeline = useMemo(() => {
    return runs.length
      ? runs.map((run: any) => ({
          time: run.scheduled_time,
          task: run.task_name,
        }))
      : [
          { time: "6:00 AM", task: "Feed Doughlene" },
          { time: "9:00 AM", task: "Mix Dough" },
          { time: "1:00 PM", task: "Shape" }
        ];
  }, [runs]);

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-4xl font-bold">Today Mode</h1>

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
        <div className="rounded-xl border p-4">
          <h2 className="font-semibold">Realtime</h2>
          <p>{realtime.connected ? "Live Kitchen" : "Offline"}</p>
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
          <h2 className="text-xl font-semibold mb-4">Active Tasks</h2>

          <div className="space-y-3">
            {tasks.map((task: string) => (
              <div key={task} className="rounded-lg border p-3">
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
            {timeline.map((item: any) => (
              <p key={item.time}>
                {item.time} - {item.task}
              </p>
            ))}
          </div>
        </section>
      </div>
    </div>
  );
}
