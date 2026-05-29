import { useOrders } from "../hooks/useOrders";
import { useProductionRuns } from "../hooks/useProductionRuns";
import { useInventory } from "../hooks/useInventory";
import { useRealtime } from "../hooks/useRealtime";

export default function DashboardPage() {
  const orders = useOrders();
  const runs = useProductionRuns();
  const inventory = useInventory();
  const realtime = useRealtime();

  return (
    <div
      style={{
        padding: "2rem",
        display: "grid",
        gap: "1.5rem",
      }}
    >
      <h1>Today Mode</h1>

      <section>
        <h2>Realtime Status</h2>
        <p>{realtime ? "Live" : "Offline"}</p>
      </section>

      <section>
        <h2>Production Queue</h2>
        <p>{runs.length} active runs</p>
      </section>

      <section>
        <h2>Orders Due</h2>
        <p>{orders.length} total orders</p>
      </section>

      <section>
        <h2>Inventory Status</h2>
        <p>{inventory.length} tracked items</p>
      </section>
    </div>
  );
}
