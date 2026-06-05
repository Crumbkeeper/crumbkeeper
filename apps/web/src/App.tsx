import { BrowserRouter, NavLink, Route, Routes } from "react-router-dom";

import DashboardPage from "./pages/DashboardPage";
import ProductionPage from "./pages/ProductionPage";
import OrdersPage from "./pages/OrdersPage";
import RecipesPage from "./pages/RecipesPage";
import ProductsPage from "./pages/ProductsPage";
import InventoryPage from "./pages/InventoryPage";
import IngredientsPage from "./pages/IngredientsPage";
import ShoppingPage from "./pages/ShoppingPage";
import CustomersPage from "./pages/CustomersPage";
import SchedulePage from "./pages/SchedulePage";
import StorefrontPage from "./pages/StorefrontPage";
import NotificationsPage from "./pages/NotificationsPage";
import LabelsPage from "./pages/LabelsPage";
import CalendarPage from "./pages/CalendarPage";
import CapacityPage from "./pages/CapacityPage";
import ForecastPage from "./pages/ForecastPage";
import PlannerPage from "./pages/PlannerPage";
import TodayPage from "./pages/TodayPage";
import AnalyticsPage from "./pages/AnalyticsPage";
import EventsPage from "./pages/EventsPage";
import MorePage from "./pages/MorePage";
import OperationsHubPage from "./pages/OperationsHubPage";
import SettingsPage from "./pages/SettingsPage";

const navItems = [
  ["Dashboard", "/"],
  ["Today", "/today"],
  ["Orders", "/orders"],
  ["Production", "/production"],
  ["Recipes", "/recipes"],
  ["Products", "/products"],
  ["Ingredients", "/ingredients"],
  ["Inventory", "/inventory"],
  ["Shopping", "/shopping"],
  ["Customers", "/customers"],
  ["Schedule", "/schedule"],
  ["Storefront", "/storefront"],
  ["Notifications", "/notifications"],
  ["Labels", "/labels"],
  ["Calendar", "/calendar"],
  ["Capacity", "/capacity"],
  ["Forecast", "/forecast"],
  ["Planner", "/planner"],
  ["Analytics", "/analytics"],
  ["Events", "/events"],
  ["Operations", "/operations"],
  ["Settings", "/settings"],
  ["More", "/more"],
];

function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-amber-50 text-stone-900">
        <header className="border-b border-amber-200 bg-white/80 px-4 py-4 shadow-sm">
          <h1 className="text-3xl font-bold text-stone-800">Crumbkeeper</h1>
          <p className="text-sm text-stone-600">Bakery operations dashboard</p>
        </header>

        <div className="flex">
          <aside className="hidden w-64 shrink-0 border-r border-amber-200 bg-white/70 p-4 md:block">
            <nav className="flex flex-col gap-2">
              {navItems.map(([label, path]) => (
                <NavLink
                  key={path}
                  to={path}
                  end={path === "/"}
                  className={({ isActive }) =>
                    `rounded-xl px-3 py-2 text-sm font-medium ${
                      isActive
                        ? "bg-stone-800 text-amber-50"
                        : "text-stone-700 hover:bg-amber-100"
                    }`
                  }
                >
                  {label}
                </NavLink>
              ))}
            </nav>
          </aside>

          <main className="flex-1 p-4">
            <Routes>
              <Route path="/" element={<DashboardPage />} />
              <Route path="/today" element={<TodayPage />} />
              <Route path="/orders" element={<OrdersPage />} />
              <Route path="/production" element={<ProductionPage />} />
              <Route path="/recipes" element={<RecipesPage />} />
              <Route path="/products" element={<ProductsPage />} />
              <Route path="/inventory" element={<InventoryPage />} />
              <Route path="/ingredients" element={<IngredientsPage />} />
              <Route path="/shopping" element={<ShoppingPage />} />
              <Route path="/customers" element={<CustomersPage />} />
              <Route path="/schedule" element={<SchedulePage />} />
              <Route path="/storefront" element={<StorefrontPage />} />
              <Route path="/notifications" element={<NotificationsPage />} />
              <Route path="/labels" element={<LabelsPage />} />
              <Route path="/calendar" element={<CalendarPage />} />
              <Route path="/capacity" element={<CapacityPage />} />
              <Route path="/forecast" element={<ForecastPage />} />
              <Route path="/planner" element={<PlannerPage />} />
              <Route path="/analytics" element={<AnalyticsPage />} />
              <Route path="/events" element={<EventsPage />} />
              <Route path="/operations" element={<OperationsHubPage />} />
              <Route path="/settings" element={<SettingsPage />} />
              <Route path="/more" element={<MorePage />} />
            </Routes>
          </main>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;



