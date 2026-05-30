import { useEffect, useState } from "react";

const API_URL = "http://127.0.0.1:8000/api/v1/production-runs";

export function useProductionRuns() {
  const [runs, setRuns] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchRuns = async () => {
    const response = await fetch(API_URL);
    const data = await response.json();

    setRuns(data);
    setLoading(false);
  };

  useEffect(() => {
    fetchRuns();
  }, []);

  const createRun = async (run: unknown) => {
    await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(run),
    });

    await fetchRuns();
  };

  return {
    runs,
    loading,
    createRun,
    refresh: fetchRuns,
  };
}