import { useRealtime } from "../hooks/useRealtime";

export default function NotificationsPage() {
  const { events } = useRealtime();

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">
        Notifications
      </h1>

      <div className="space-y-4">
        {events.length === 0 && (
          <div className="rounded-xl border p-4">
            No alerts
          </div>
        )}

        {events.map((event, index) => (
          <div
            key={index}
            className="rounded-xl border p-4"
          >
            <div className="font-semibold">
              {event.event}
            </div>

            <div className="text-sm">
              {event.timestamp}
            </div>

            <pre className="text-xs mt-2">
              {JSON.stringify(event.payload, null, 2)}
            </pre>
          </div>
        ))}
      </div>
    </div>
  );
}
