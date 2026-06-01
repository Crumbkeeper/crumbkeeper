import { useEffect, useState } from "react";

const API_URL = "http://127.0.0.1:8000/api/v1/products";

export function useProducts() {
  const [products, setProducts] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchProducts = async () => {
    const response = await fetch(API_URL);
    const data = await response.json();

    setProducts(data);
    setLoading(false);
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  const createProduct = async (product: unknown) => {
    await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(product),
    });

    await fetchProducts();
  };

  const updateProduct = async (
    id: number,
    product: unknown
  ) => {
    await fetch(`${API_URL}/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(product),
    });

    await fetchProducts();
  };

  return {
    products,
    loading,
    createProduct,
    updateProduct,
    refresh: fetchProducts,
  };
}
