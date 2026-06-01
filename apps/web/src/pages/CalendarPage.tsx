import { useOrders } from "../hooks/useOrders";

export default function CalendarPage() {
  const { orders } = useOrders();

  const grouped = orders.reduce(
    (acc: any, order: any) => {
      if (!acc[order.pickup_date]) {
        acc[order.pickup_date] = [];
      }

      acc[order.pickup_date].push(order);

      return acc;
    },
    {}
  );

  return (
    <div className="p-6 space-y-8">
      <h1 className="text-3xl font-bold">
        Bakery Calendar
      </h1>

      {Object.entries(grouped).map(
        ([date, items]: any) => (
          <div
            key={date}
            className="rounded-xl border p-6"
          >
            <h2 className="text-xl font-semibold">
              {date}
            </h2>

            <div className="space-y-3 mt-4">
              {items.map((order: any) => (
                <div
                  key={order.id}
                  className="rounded-lg border p-3"
                >
                  {order.customer_name} - {order.product_name}
                </div>
              ))}
            </div>
          </div>
        )
      )}
    </div>
  );
}
