# GRADE.md — news-image-01 (news-image-20261124)

## Entry
- Competition: Sum up 24 November's world news in one image (news-image-20261124)
- Prize: $100, 50 paid places (1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20)
- Entry fee: none (free, verified from live requirements 2026-11-24)
- Deadline: 2026-11-26T00:00:00Z = **26 Nov 2026 07:00 WIB**
- Blind rounds: 4 — next round 24 Nov 19:00 WIB, then 25 Nov 07:00 WIB,
  25 Nov 19:00 WIB, final 26 Nov 07:00 WIB. Submit before 19:00 WIB today
  to be judged in round 1.
- Entries at build time: ~3,073 (rising fast)

## Image (entry.png)
- 1024×1024 px, RGB, **135,204 bytes** (cap 1 MiB), PNG valid (all chunks verified)
- sha256: `6d3bf63856f323ebafc293396fa4da0e3afb1d986007cae7711967c70386e746`
- Front page "THE WORLD IN ONE DAY — TUESDAY, 24 NOVEMBER 2026"
- Lead: Nvidia reinstates Jensen Huang, shares +31%, Nasdaq +6%
  (Reuters/AP, 23 Nov; follow-through 24 Nov)
- Grid: Ukraine hits Russian warship in Libya; Trump lands in the
  Philippines; 12,000 flee a Manchester concert; US loses measles-free status
- Footer: EU 22nd Russia sanctions package; FIFA: US to host 2031 Women's
  World Cup; O'Hare ground stop
- Sources checked: Reuters, AP, BBC (24 Nov 2026 news cycle)

## Local verification (2026-11-24)
- `main.py` run twice (MAKEFUN_OUTPUT_DIR=/tmp/out1, /tmp/out2):
  both wrote entry.png, sha256 identical to the repo file (see above)
- PNG verified with PIL (load + verify, all chunks ok)
- `grade-local` not available for program/v1: the kit says its scorer is
  not published, so the gate is graded server-side only. Local checks
  above are the full verification possible here.
- Repo total: 139,585 bytes, 6 files (main.py, entry.png, LICENSE, README.md,
  GRADE.md, .makefun/owner.json)

## Files
- main.py — stdlib-only copy program (validates PNG/JPEG magic + 1 MiB cap,
  verifies copied bytes match). Written and revised in-session (2 writes).
- entry.png — drawn with PIL (DejaVu fonts), deterministic render.
- LICENSE — MIT (from kit starter)
- README.md — 3 live make.fun badges (gsinggih94/news-image-01)
- .makefun/owner.json — wallet 2AdFVhhazVawUXW9qhhm2Sx4c27EdcpmpasSvyZVswcf
  (repo owner gsinggih94 differs from make.fun login swulandary249)

## Still manual (user)
1. Create public repo `gsinggih94/news-image-01` on GitHub (created after
   2026-11-24T00:00:00Z) and upload all 6 files from news-image-01.zip —
   check `.makefun/owner.json` really uploaded (dot folder is easy to miss).
2. Set repo About: Website `https://make.fun/bounty/news-image-20261124`,
   Topics `makefun` (required), `ai-agents`, `bounties` (recommended),
   Description naming make.fun.
3. Send me the commit SHA (40 chars). I will build the transcript bundle
   and submit as @sri-wulandari before 26 Nov 07:00 WIB.
