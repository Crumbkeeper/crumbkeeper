import { useEffect, useState } from "react";
import { apiFetch } from "../services/api";

export function useHealth() {
  const [healthy, setHealthy] =
    useState(false);

  useEffect(() => {
    apiFetch("/health")
      .then(() => setHealthy(true))
      .catch(() => setHealthy(false));
  }, []);

  return healthy;
}
