import {
  createBrowserRouter,
} from "react-router-dom"

import AppLayout from "../layouts/AppLayout"

import DashboardPage from "../pages/DashboardPage"
import OrdersPage from "../pages/OrdersPage"
import ProductionPage from "../pages/ProductionPage"
import RecipesPage from "../pages/RecipesPage"
import SettingsPage from "../pages/SettingsPage"

export const router = createBrowserRouter([
  {
    path: "/",
    element: <AppLayout />,
    children: [
      {
        index: true,
        element: <DashboardPage />,
      },
      {
        path: "production",
        element: <ProductionPage />,
      },
      {
        path: "orders",
        element: <OrdersPage />,
      },
      {
        path: "recipes",
        element: <RecipesPage />,
      },
      {
        path: "settings",
        element: <SettingsPage />,
      },
    ],
  },
])
