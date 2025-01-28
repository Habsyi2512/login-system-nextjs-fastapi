import { NextResponse, NextRequest } from "next/server";
import { getToken, isTokenValid } from "@/lib/auth";

export function middleware(req: NextRequest) {
  // const token = getToken();
  // console.log("Token in middleware:", token);
  const path = req.nextUrl.pathname;

  // if (path.startsWith("/dashboard") && (!token || !isTokenValid())) {
  //   return NextResponse.redirect(new URL("/login", req.url));
  // }

  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*", "/profile/:path*"],
};
