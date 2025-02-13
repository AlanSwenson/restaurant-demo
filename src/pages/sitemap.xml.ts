import type { APIRoute } from "astro";

const SITE_URL = "https://restaurant.alanswenson.dev"; // Replace with your actual domain

export const GET: APIRoute = async () => {
  // Get the current date in ISO format
  const date = new Date().toISOString();

  // Add your static routes here
  const staticPages = [
    "",
    "/about",
    "/contact",
    // Add other static routes...
  ];

  // Generate the sitemap XML
  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      ${staticPages
        .map(
          (page) => `
        <url>
          <loc>${SITE_URL}${page}</loc>
          <lastmod>${date}</lastmod>
        </url>`
        )
        .join("")}
    </urlset>`;

  return new Response(sitemap, {
    headers: {
      "Content-Type": "application/xml",
      "Cache-Control": "public, max-age=3600",
    },
  });
};
