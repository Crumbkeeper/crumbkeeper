import { Link } from "react-router-dom"

export default function MorePage() {
  return (
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold">
        More
      </h1>

      <div className="grid gap-3">

        <Link to="/operations" className="rounded-xl border p-4">
          Operations Hub
        </Link>

        <Link to="/schedule" className="rounded-xl border p-4">
          Schedule
        </Link>

        <Link to="/calendar" className="rounded-xl border p-4">
          Calendar
        </Link>

        <Link to="/customers" className="rounded-xl border p-4">
          Customers
        </Link>

        <Link to="/products" className="rounded-xl border p-4">
          Products
        </Link>

        <Link to="/shopping" className="rounded-xl border p-4">
          Shopping
        </Link>

        <Link to="/storefront" className="rounded-xl border p-4">
          Storefront
        </Link>

        <Link to="/labels" className="rounded-xl border p-4">
          Labels
        </Link>

        <Link to="/notifications" className="rounded-xl border p-4">
          Alerts
        </Link>

        <Link to="/settings" className="rounded-xl border p-4">
          Settings
        </Link>

      </div>
    </div>
  )
}
