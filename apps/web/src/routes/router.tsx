import {
  createBrowserRouter,
} from "react-router-dom"

import AppLayout from "../layouts/AppLayout"

import CalendarPage from "../pages/CalendarPage"
import CustomersPage from "../pages/CustomersPage"
import DashboardPage from "../pages/DashboardPage"
import InventoryPage from "../pages/InventoryPage"
import LabelsPage from "../pages/LabelsPage"
import NotificationsPage from "../pages/NotificationsPage"
import OrdersPage from "../pages/OrdersPage"
import ProductionPage from "../pages/ProductionPage"
import ProductsPage from "../pages/ProductsPage"
import RecipesPage from "../pages/RecipesPage"
import SchedulePage from "../pages/SchedulePage"
import SettingsPage from "../pages/SettingsPage"
import ShoppingPage from "../pages/ShoppingPage"
import StorefrontPage from "../pages/StorefrontPage"

export const router = createBrowserRouter([
  {
    path: "/",
    element: <AppLayout />,
    children: [
      { index: true, element: <DashboardPage /> },
      { path: "production", element: <ProductionPage /> },
      { path: "schedule", element: <SchedulePage /> },
      { path: "calendar", element: <CalendarPage /> },
      { path: "orders", element: <OrdersPage /> },
      { path: "customers", element: <CustomersPage /> },
      { path: "products", element: <ProductsPage /> },
      { path: "inventory", element: <InventoryPage /> },
      { path: "shopping", element: <ShoppingPage /> },
      { path: "storefront", element: <StorefrontPage /> },
      { path: "notifications", element: <NotificationsPage /> },
      { path: "labels", element: <LabelsPage /> },
      { path: "recipes", element: <RecipesPage /> },
      { path: "settings", element: <SettingsPage /> },
    ],
  },
])
