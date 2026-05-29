import { apiFetch } from "./api"

export interface HealthResponse {
  status: string
  service: string
}

export async function getHealth() {
  return apiFetch<HealthResponse>(
    "/api/v1/health"
  )
}
