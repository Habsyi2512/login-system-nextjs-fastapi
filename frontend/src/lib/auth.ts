import { jwtDecode } from "jwt-decode";

export const getToken = () => {
  if (typeof window !== "undefined") {
    const token = document.cookie
      .split("; ")
      .find((row) => row.startsWith("token="))
      ?.split("=")[1];
    return token;
  }
  return null;
};

export const setToken = (token: string) => {
  document.cookie = `token=${token}; path=/; max-age=3600`; // Set cookie dengan expiry 1 jam
};

export const removeToken = () => {
  document.cookie = "token=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT";
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
