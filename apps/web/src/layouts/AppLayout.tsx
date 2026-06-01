import { Link, Outlet } from "react-router-dom"

import { useRealtime } from "../hooks/useRealtime"

export default function AppLayout() {
  const realtime = useRealtime()

  return (
    <div className="min-h-screen bg-amber-50 text-stone-800">
      <header className="border-b border-stone-200 bg-white px-4 py-3 flex justify-between items-center">
        <h1 className="text-2xl font-bold">
          Crumbkeeper
        </h1>

        <span className="text-sm">
          {realtime.connected ? "Live Kitchen" : "Offline"}
        </span>
      </header>

      <main className="pb-20">
        <Outlet />
      </main>

      <nav className="fixed bottom-0 left-0 right-0 border-t border-stone-200 bg-white">
        <div className="flex justify-around py-3 text-sm flex-wrap">
          <Link to="/">Dashboard</Link>
          <Link to="/production">Production</Link>
          <Link to="/schedule">Schedule</Link>
          <Link to="/calendar">Calendar</Link>
          <Link to="/orders">Orders</Link>
          <Link to="/customers">Customers</Link>
          <Link to="/products">Products</Link>
          <Link to="/inventory">Inventory</Link>
          <Link to="/shopping">Shopping</Link>
          <Link to="/storefront">Storefront</Link>
          <Link to="/notifications">Alerts</Link>
          <Link to="/labels">Labels</Link>
          <Link to="/recipes">Recipes</Link>
          <Link to="/settings">Settings</Link>
        </div>
      </nav>
    </div>
  )
}
