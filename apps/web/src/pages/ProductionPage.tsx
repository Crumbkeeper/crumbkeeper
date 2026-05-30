import { useState } from "react";
import { useProductionRuns } from "../hooks/useProductionRuns";

export default function ProductionPage() {
  const { runs, createRun } = useProductionRuns();

  const [form, setForm] = useState({
    task_name: "",
    scheduled_time: "",
    linked_order_id: null,
    status: "scheduled",
  });

  const handleCreate = async () => {
    await createRun(form);

    setForm({
      task_name: "",
      scheduled_time: "",
      linked_order_id: null,
      status: "scheduled",
    });
  };

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">
        Production
      </h1>

      <div className="grid md:grid-cols-2 gap-8">

        <div className="rounded-xl border p-6 space-y-4">
          <h2 className="text-xl font-semibold">
            Create Production Task
          </h2>

          <input
            className="w-full border rounded p-2"
            placeholder="Task"
            value={form.task_name}
            onChange={(e) =>
              setForm({ ...form, task_name: e.target.value })
            }
          />

          <input
            className="w-full border rounded p-2"
            type="time"
            value={form.scheduled_time}
            onChange={(e) =>
              setForm({
                ...form,
                scheduled_time: e.target.value,
              })
            }
          />

          <button
            onClick={handleCreate}
            className="w-full rounded bg-amber-700 text-white p-2"
          >
            Save Task
          </button>
        </div>

        <div className="rounded-xl border p-6 space-y-4">
          <h2 className="text-xl font-semibold">
            Production Timeline
          </h2>

          {runs.map((run: any) => (
            <div
              key={run.id}
              className="rounded-lg border p-4"
            >
              <h3 className="font-semibold">
                {run.task_name}
              </h3>

              <div>{run.scheduled_time}</div>
              <div>Status: {run.status}</div>
            </div>
          ))}
        </div>

      </div>
    </div>
  );
}