import { useState } from "react";

export default function SchedulePage() {
  const [dueDate, setDueDate] = useState("");
  const [schedule, setSchedule] = useState<any>(null);

  const generate = async () => {
    const response = await fetch(
      `http://127.0.0.1:8000/api/v1/schedule/plan?due_date=${dueDate}`,
      {
        method: "POST",
      }
    );

    const data = await response.json();
    setSchedule(data);
  };

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">
        Bake Scheduler
      </h1>

      <input
        type="datetime-local"
        className="w-full border rounded p-2"
        value={dueDate}
        onChange={(e) =>
          setDueDate(e.target.value)
        }
      />

      <button
        onClick={generate}
        className="w-full rounded bg-amber-700 text-white p-2"
      >
        Generate Timeline
      </button>

      {schedule && (
        <div className="space-y-3">
          {Object.entries(schedule).map(([step, time]) => (
            <div
              key={step}
              className="rounded-xl border p-4"
            >
              <strong>{step}</strong>
              <div>{String(time)}</div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
