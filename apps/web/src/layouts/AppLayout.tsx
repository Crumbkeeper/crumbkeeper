import { Link, Outlet } from "react-router-dom"

export default function AppLayout() {
  return (
    <div className="min-h-screen bg-amber-50 text-stone-800">
      <header className="border-b border-stone-200 bg-white px-4 py-3">
        <h1 className="text-2xl font-bold">
          Crumbkeeper
        </h1>
      </header>

      <main className="pb-20">
        <Outlet />
      </main>

      <nav className="fixed bottom-0 left-0 right-0 border-t border-stone-200 bg-white">
        <div className="flex justify-around py-3 text-sm">
          <Link to="/">Dashboard</Link>
          <Link to="/production">Production</Link>
          <Link to="/orders">Orders</Link>
          <Link to="/recipes">Recipes</Link>
          <Link to="/settings">Settings</Link>
        </div>
      </nav>
    </div>
  )
}
