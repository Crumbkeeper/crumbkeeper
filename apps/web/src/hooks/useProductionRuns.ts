import { useEffect, useState } from "react";
import { apiFetch } from "../services/api";

export function useProductionRuns() {
  const [runs, setRuns] = useState<any[]>([]);

  useEffect(() => {
    apiFetch<any[]>("/production-runs")
      .then(setRuns)
      .catch(() => setRuns([]));
  }, []);

  return runs;
}
