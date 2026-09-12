# Current state

- 2026-09-12: Static directory repair on `maintenance/schools-static-20260912`.
- Baseline reproduced missing homepage entry, root-relative missing assets, absent title/landmarks/category navigation and 320px horizontal overflow. Evidence is recorded in the portfolio audit.
- All 338 archived school destinations stay in their original order; `maps.txt` is unchanged. The directory is explicitly dated 2020.
- Added dependency-free Prawn styling, native keyboard/category links, inline CSS and a no-JavaScript homepage redirect. No school/provider requests, database writes or hosting settings changes.
- Validation: all five offline regression checks pass. Browser checks at 320, 390 and 1440px pass without JavaScript, including skip focus, category navigation, back-to-top and the nested homepage redirect. Direct file opening passes; desktop/mobile screenshots reviewed. All five category lists match the original destinations/order.
- PR #34: the hosted static check passed. The older Labeler workflow failed because it requested absent `.github/labeler.yml`; it now uses the existing shared-format `.github/labels.yml` with contents-read and pull-request-write permissions, matching the working labeler. Hosted checks and GitHub Pages production bytes must pass before closeout. This is not a Vercel app or a Supabase migration.
