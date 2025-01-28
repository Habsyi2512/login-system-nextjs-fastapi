"use client";

import React, { useEffect } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/providers/AuthProvider"; // Pastikan path ini benar

export default function Page() {
  const { isAuthenticated } = useAuth(); // Mengambil status autentikasi
  const router = useRouter();

  useEffect(() => {
    // Jika pengguna belum login, arahkan mereka ke halaman login
    if (!isAuthenticated) {
      router.push("/login");
    }
  }, [isAuthenticated, router]);

  // Jika pengguna sudah login, tampilkan dashboard
  if (!isAuthenticated) {
    return <div>Loading...</div>; // Bisa ditambahkan loading atau placeholder
  }

  return (
    <div>
      <h1>Halaman Dashboard</h1>
      <p>
        Selamat datang di dashboard yang hanya bisa diakses oleh pengguna yang
        sudah login.
      </p>
    </div>
  );
}
