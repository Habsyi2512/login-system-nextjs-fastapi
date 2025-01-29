import DashboardGuard from "@/components/DashboardGuard";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <DashboardGuard>
      <div className="min-h-screen bg-gray-100">
        {/* Sidebar atau Navbar bisa ditambahkan di sini */}
        <main className="p-4">{children}</main>
      </div>
    </DashboardGuard>
  );
}

