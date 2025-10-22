import axios from "axios";

// Create Axios instance
const API = axios.create({
  baseURL: "http://127.0.0.1:8000", // Backend FastAPI URL
  headers: {
    "Content-Type": "application/json",
  },
});

// ✅ Automatically attach JWT token to every request
API.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// ✅ Handle common response errors globally
API.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token invalid or expired → auto logout
      console.warn("Session expired. Logging out...");
      localStorage.removeItem("token");

      // Optional: redirect to login if not already there
      if (window.location.pathname !== "/login") {
        window.location.href = "/login";
      }
    }
    return Promise.reject(error);
  }
);

export default API;
