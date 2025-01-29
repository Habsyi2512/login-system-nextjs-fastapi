"use client";

import { useAuth } from "@/providers/AuthProvider";
import { useRouter } from "next/navigation";

import React from "react";

export default function Navbar() {
  const router = useRouter();
  const { isAuthenticated, logout } = useAuth();
  return (
    <header className="text-neutral-200">
      <nav className="bg-neutral-900 px-5 py-3">
        {isAuthenticated ? (
          <button onClick={logout}>logout</button>
        ) : (
          <button onClick={() => router.push("/login")}>login</button>
        )}
      </nav>
    </header>
  );
}
