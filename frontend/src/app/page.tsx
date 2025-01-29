"use client";

import { useAuth } from "@/providers/AuthProvider";

export default function Home() {
  const { logout } = useAuth();
  return (
    <div>
      <p>Halaman Utama</p>
      <button onClick={logout}>logout</button>
    </div>
  );
}
