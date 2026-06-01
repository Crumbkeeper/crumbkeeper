import { useState } from "react";
import { useProductionRuns } from "../hooks/useProductionRuns";

const stageFlow = [
  "prep",
  "mix",
  "bulk ferment",
  "shape",
  "proof",
  "bake",
  "cooling",
  "complete",
];

export default function ProductionPage() {
  const { runs, createRun, updateRun } =
    useProductionRuns();

  const [form, setForm] = useState({
    task_name: "",
    scheduled_time: "",
    linked_order_id: null,
    stage: "prep",
    priority: "normal",
    batch_size: 1,
    dough_weight: 0,
    notes: "",
    status: "scheduled",
  });

  const handleCreate = async () => {
    await createRun(form);

    setForm({
      task_name: "",
      scheduled_time: "",
      linked_order_id: null,
      stage: "prep",
      priority: "normal",
      batch_size: 1,
      dough_weight: 0,
      notes: "",
      status: "scheduled",
    });
  };

  const advanceStage = async (run: any) => {
    const current =
      stageFlow.indexOf(run.stage);

    const next =
      stageFlow[
        Math.min(current + 1, stageFlow.length - 1)
      ];

    await updateRun(run.id, {
      ...run,
      stage: next,
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
              setForm({
                ...form,
                task_name: e.target.value,
              })
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

          <input
            className="w-full border rounded p-2"
            type="number"
            placeholder="Dough Weight"
            value={form.dough_weight}
            onChange={(e) =>
              setForm({
                ...form,
                dough_weight: Number(e.target.value),
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
              <div>Stage: {run.stage}</div>
              <div>{run.dough_weight}g</div>

              <button
                onClick={() => advanceStage(run)}
                className="rounded bg-amber-700 text-white px-3 py-1 mt-2"
              >
                Advance Stage
              </button>
            </div>
          ))}
        </div>

      </div>
    </div>
  );
}
