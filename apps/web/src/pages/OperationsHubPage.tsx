import { Link } from "react-router-dom"

export default function OperationsHubPage() {
  return (
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold">
        Operations Hub
      </h1>

      <div className="grid gap-3">

        <Link to="/today" className="rounded-xl border p-4">
          Today Mode
        </Link>

        <Link to="/capacity" className="rounded-xl border p-4">
          Capacity Planning
        </Link>

        <Link to="/forecast" className="rounded-xl border p-4">
          Forecasting
        </Link>

        <Link to="/planner" className="rounded-xl border p-4">
          Production Planner
        </Link>

        <Link to="/events" className="rounded-xl border p-4">
          Events
        </Link>

        <Link to="/analytics" className="rounded-xl border p-4">
          Analytics
        </Link>

      </div>
    </div>
  )
}
