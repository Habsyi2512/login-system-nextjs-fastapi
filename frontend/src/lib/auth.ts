import { jwtDecode } from "jwt-decode";

export const getToken = () => {
  if (typeof window !== "undefined") {
    const token = localStorage.getItem("token");
    console.log("Token from localStorage: ", token);
    return token;
  }
  return null;
};

export const setToken = (token: string) => {
  localStorage.setItem("token", token);
};

export const removeToken = () => {
  localStorage.removeItem("token");
};

export const isTokenValid = () => {
  const token = getToken();
  if (!token) return false;

  try {
    const decoded = jwtDecode(token);
    return decoded.exp! * 1000 > Date.now();
  } catch {
    return false;
  }
};
