import { useState } from "react";

export default function SettingsPage() {
  const [bakeryName, setBakeryName] = useState("HoneyBean");
  const [notifications, setNotifications] = useState(true);
  const [offlineMode, setOfflineMode] = useState(true);

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">
        Bakery Settings
      </h1>

      <div className="rounded-xl border p-6 space-y-4">
        <label className="block">
          <div className="font-semibold mb-2">
            Bakery Name
          </div>

          <input
            value={bakeryName}
            onChange={(e) => setBakeryName(e.target.value)}
            className="w-full rounded-lg border p-3"
          />
        </label>

        <label className="flex items-center gap-3">
          <input
            type="checkbox"
            checked={notifications}
            onChange={() =>
              setNotifications(!notifications)
            }
          />
          Enable Notifications
        </label>

        <label className="flex items-center gap-3">
          <input
            type="checkbox"
            checked={offlineMode}
            onChange={() =>
              setOfflineMode(!offlineMode)
            }
          />
          Offline Kitchen Mode
        </label>

        <button className="rounded-lg border px-4 py-2">
          Save Settings
        </button>
      </div>
    </div>
  );
}
