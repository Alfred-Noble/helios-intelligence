const API_BASE = "http://127.0.0.1:8000";

export async function getAnalytics() {
  const response = await fetch(
    `${API_BASE}/analytics/summary`
  );

  return response.json();
}

export async function getLeads() {
  const response = await fetch(
    `${API_BASE}/leads/`
  );

  return response.json();
}

export async function getProjects() {
  const response = await fetch(
    `${API_BASE}/projects/`
  );

  return response.json();
}

export async function createLead(
  data: {
    full_name: string;
    headline: string;
    company: string;
    industry: string;
    location: string;
    email: string;
  }
) {
  const response = await fetch(
    `${API_BASE}/leads/`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    }
  );

  return response.json();
}