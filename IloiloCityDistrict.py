

import os
import re
import random
from datetime import date, timedelta
from docx import Document   # python-docx  (pip install python-docx)

# ── Canonical category normalisation ────────────────────────────────────────

_CAT_MAP = {
    "bridges":   "Bridges",
    "bridge":    "Bridges",
    "roads":     "Roads",
    "road":      "Roads",
    "rpoads":    "Roads",          # typo in original folder
    "flood":     "Flood Control and Drainage",
    "drain":     "Flood Control and Drainage",
    "build":     "Buildings and Facilities",
    "facil":     "Buildings and Facilities",
    "faci":      "Buildings and Facilities",
}

def _normalise_category(folder_name: str) -> str | None:
    """Map a messy folder name to one of the four canonical categories."""
    key = folder_name.lower().strip().rstrip("]_").replace("_", " ")
    for token, cat in _CAT_MAP.items():
        if token in key:
            return cat
    return None

# ── Contract details extracted from .docx files ──────────────────────────────

_REAL_CONTRACTS: list[dict] = []

def _parse_docx_contracts(base_path: str) -> list[dict]:
    """Walk tree and extract contract data from every .docx found."""
    contracts = []
    for root, _, files in os.walk(base_path):
        for fn in files:
            if not fn.lower().endswith(".docx"):
                continue
            fp = os.path.join(root, fn)
            try:
                doc = Document(fp)
                text_lines = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
            except Exception:
                continue

            # Pull fields by scanning pairs of adjacent lines
            fields: dict = {}
            for i, line in enumerate(text_lines):
                nxt = text_lines[i + 1] if i + 1 < len(text_lines) else ""
                ul = line.upper()
                if "CONTRACT DESCRIPTION" in ul:
                    fields["project_name"] = nxt
                elif "CONTRACTOR" in ul and "project_name" in fields and "contractor" not in fields:
                    fields["contractor"] = nxt
                elif "ACTUAL START DATE" in ul:
                    fields["start_date"] = nxt
                elif "ACTUAL COMPLETION DATE" in ul:
                    fields["completion_date"] = nxt
                elif "ACCOMPLISHMENT" in ul:
                    m = re.search(r"(\d+)", nxt)
                    fields["accomplishment"] = int(m.group(1)) if m else None
                elif "STATUS" in ul and len(nxt) < 30 and nxt:
                    fields["status_raw"] = nxt
                elif "APPROVED BUDGET" in ul:
                    m = re.search(r"[\d,]+\.?\d*", nxt.replace("₱", "").replace(",", ""))
                    if m:
                        fields["budget"] = float(m.group().replace(",", ""))
                elif "INFRA TYPE" not in ul and "REGION" in ul:
                    pass   # skip location noise
                elif "PROVINCE" in ul:
                    fields["province"] = nxt

            # Determine category from file path
            parts = [p.lower() for p in fp.split(os.sep)]
            cat = None
            for part in parts:
                cat = _normalise_category(part)
                if cat:
                    break

            # Determine year from path
            year = None
            for part in parts:
                if re.fullmatch(r"20\d{2}", part.strip()):
                    year = int(part.strip())
                    break

            if "project_name" in fields and cat and year:
                acc = fields.get("accomplishment", 0) or 0
                status_raw = fields.get("status_raw", "").strip()
                if status_raw.lower() == "completed" or acc == 100:
                    status = "Completed"
                elif status_raw.lower() == "ongoing" or 0 < acc < 100:
                    status = "Ongoing"
                else:
                    status = "Completed"   # default for old docx with blank status

                contracts.append({
                    "project_name":        fields["project_name"],
                    "category":            cat,
                    "year":                year,
                    "status":              status,
                    "budget_allocated":    fields.get("budget", random.randint(10, 100) * 1_000_000),
                    "accomplishment_pct":  acc,
                    "contractor":          fields.get("contractor", ""),
                    "source":              "docx",
                })
    return contracts


# ── Synthetic data seeded from folder structure ──────────────────────────────

# Real Iloilo-specific project name pools per category
_ILOILO_NAMES = {
    "Bridges": [
        "Retrofitting/Strengthening of Iloilo Bridge (B00501PN) along Sen. Benigno Aquino Jr. Ave",
        "Retrofitting/Strengthening of Quirino-Lopez Bridge along Iloilo Airport Direct Road",
        "Construction of Balabago Bridge along Circumferential Road, Jaro, Iloilo City",
        "Rehabilitation of Muelle Loney Bridge, Iloilo River",
        "Construction of Footbridge – Brgy. Ungka II, Pavia-Iloilo Boundary",
        "Repair/Replacement of Expansion Joints – Iloilo Esplanade Bridge (Phase {})",
        "Construction of Bridge along Ingore-Lapuz Road (B00{} PN)",
        "Strengthening of Santa Barbara-Iloilo Bridge Approach (Package {})",
        "Replacement of Timber Bridge – Brgy. Cabugao Sur Crossing (Phase {})",
        "Construction of Bailey Bridge – Tigbauan–Guimbal Road (Lot {})",
        "Repair of Rio Iloilo Pedestrian Bridge – La Paz",
        "Construction of Oton–San Miguel Bridge along National Highway",
    ],
    "Roads": [
        "Asphalt Overlay of Iznart-Ledesma-Molo Road K000+236-K000+545",
        "Concreting of Circumferential Road, Brgy. Dungon A, Jaro, Iloilo City (Phase {})",
        "Road Widening of Diversion Road (E. Lopez – Q. Abeto Stretch), Iloilo City",
        "Rehabilitation of Iloilo-Capiz Road, Sta. Barbara Section (Package {})",
        "Concreting of Barangay Access Road – Brgy. Camalig, Mandurriao, Iloilo City",
        "Pavement Improvement – Iloilo South Road (Pavia-Cabatuan), Lot {}",
        "Concreting of City Road along Quintin Salas St., Jaro (Phase {})",
        "Asphalt Overlay of Iloilo-Antique Road, Oton Section K{}",
        "Road Restoration – Jalandoni Heritage Road, Iloilo City",
        "Construction of Service Road – Western Visayas Industrial Center, Mandurriao",
        "Concreting of Brgy. Ingore Access Road, La Paz, Iloilo City",
        "Pavement Marking and Road Safety – National Highway Iloilo (Phase {})",
    ],
    "Buildings and Facilities": [
        "Completion of Emergency Dept. and Renovation of Wards – WVMC, Jaro, Iloilo City",
        "Construction of DPWH Iloilo 1st DEO Administration Building (Phase {})",
        "Rehabilitation of Region VI (Western Visayas) Regional Office Compound, Iloilo City",
        "Construction of Flood Control Operations Center – Iloilo River Basin",
        "Completion of Western Visayas State University Medical Center Buildings",
        "Construction of Government Center Annex – Iloilo City Proper (Phase {})",
        "Renovation of Iloilo Provincial Capitol Annex Building",
        "Construction of DPWH Equipment Depot & Storage Yard – Zone {}",
        "Construction of Multi-Purpose Evacuation Center – Brgy. Ungka, Pavia-Iloilo",
        "Upgrading of DEO Warehouse Facility – Pavia, Iloilo (Package {})",
        "Construction of Iloilo City DPWH Training and Testing Center",
        "Installation of Solar Power System – Iloilo 1st DEO Building",
    ],
    "Flood Control and Drainage": [
        "Construction of Flood Control Structure – Butuanon-Iloilo River Basin (Phase {})",
        "Drainage Improvement along Dungon Creek, Jaro, Iloilo City",
        "Revetment Works – Iloilo City Waterfront Esplanade (Package {})",
        "Construction of Box Culvert Drainage System – Mandurriao District",
        "Flood Mitigation Structure – Iloilo-Batiano River (Phase {})",
        "River Channel Improvement & Dredging – Tigum-Aganan River (Package {})",
        "Installation of Floodgate System – Rio Iloilo Creek, La Paz",
        "Slope Protection Works – Iloilo-Antique Road (Lot {})",
        "Construction of Canal Lining – Brgy. Dungon B, Jaro, Iloilo City",
        "Storm Drain Improvement – Iloilo City Proper, 3rd District (Phase {})",
        "Flood Control Embankment – Pavia Lowlands, Iloilo (Phase {})",
        "Rehabilitation of Iloilo River Floodway – Lapuz Section",
    ],
}

_ILOILO_OFFICES = [
    "DPWH – Iloilo 1st DEO",
    "DPWH – Iloilo 2nd DEO",
    "DPWH – Iloilo City DEO",
    "DPWH – Iloilo 4th DEO",
    "DPWH – Iloilo 3rd DEO",
]

_DISTRICTS = [
    "1st District – Molo / La Paz",
    "2nd District – Jaro / Mandurriao",
    "3rd District – City Proper / Arevalo",
    "4th District – Lapuz / Ingore",
    "5th District – Pavia / Santa Barbara",
    "6th District – Oton / Tigbauan",
]

_STATUSES        = ["Completed", "Ongoing", "Delayed", "Planned"]
_STATUS_WEIGHTS  = [40, 30, 15, 15]

# ── Main dataset builder ─────────────────────────────────────────────────────

BASE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "City District "
)

def _build_dataset() -> list[dict]:
    random.seed(2025)
    projects: list[dict] = []

# ___ INSERT YOUR FUCKING DATA HEAR, THANKS ________
# 2016 -- BRIDGES
    projects.append({
    "id": 1,
    "project_name": "21GF0008 - CONCRETING OF ACCESS ROAD LEADING TO MAASIN RIVER DAM, MAASIN, ILOILO",
    "category": "Bridges",
    "district": "1st District",
    "implementing_office": "DPWH - Iloilo 1st DEO",
    "status": "Completed",
    "year": 2021,
    "date": "2021-09-10",
    "budget_allocated": 5872000.00,
    "budget_spent": 14704870.52,
    "completion_percentage": 100,
})

# 2016 -- BUILDINGS AND FACILITIES
    projects.append({
    "id": 2,
    "project_name": "COMPLETION OF EMERGENCY DEPARTMENT AND REPAIR/RENOVATION OF WARDS, WESTERN VISAYAS MEDICAL CENTER, ILOILO CITY WVSU MEDICAL CENTER, E. LOPEZ ST., JARO, ILOILO CITY",
    "category": "Buildings and Facilities",
    "district": "City District",
    "implementing_office": "DPWH – Iloilo City DEO",
    "status": "Completed",
    "year": 2016,
    "date": "2016-02-22",
    "budget_allocated": 33_863_814.67,
    "budget_spent":    32_339_943,
    "completion_percentage": 100,
    
})

# 2016 -- ROADS
    projects.append({
    "id": 3,
    "project_name": "ASPHALT OVERLAY OF IZNART - LEDESMA - MOLO ROAD, K000+236-K000+545, CHAINAGE 0-339",
    "category": "Roads",
    "district": "City District",
    "implementing_office": "DPWH – Iloilo City DEO",
    "status": "Completed",
    "year": 2016,
    "date": "2016-02-09",
    "budget_allocated": 10_954_187.11,
    "budget_spent": 11_601_850.34,
    "completion_percentage": 100,
    
})
    # ── Step 1: load real docx contracts ──────────────────────────────────
    if os.path.isdir(BASE_PATH):
        real = _parse_docx_contracts(BASE_PATH)
    else:
        real = []

    for r in real:
        yr, mo, dy = r["year"], random.randint(1, 12), random.randint(1, 28)
        alloc   = r["budget_allocated"]
        acc     = r["accomplishment_pct"]
        status  = r["status"]
        if status == "Completed":
            spent = alloc * random.uniform(0.94, 1.0)
        elif status == "Ongoing":
            spent = alloc * (acc / 100) * random.uniform(0.9, 1.05)
        else:
            spent = alloc * random.uniform(0.05, 0.35)
        projects.append({
            "id":                   len(projects) + 1,
            "project_name":         r["project_name"],
            "category":             r["category"],
            "district":             random.choice(_DISTRICTS),
            "implementing_office":  random.choice(_ILOILO_OFFICES),
            "status":               status,
            "year":                 yr,
            "date":                 f"{yr}-{mo:02d}-{dy:02d}",
            "budget_allocated":     round(alloc),
            "budget_spent":         round(spent),
            "completion_percentage": acc,
        })

    # ── Step 2: generate synthetic entries from folder structure ──────────
    if os.path.isdir(BASE_PATH):
        for year_dir in sorted(os.listdir(BASE_PATH)):
            year_path = os.path.join(BASE_PATH, year_dir)
            if not os.path.isdir(year_path):
                continue
            try:
                year = int(year_dir.strip())
            except ValueError:
                continue
            for cat_dir in sorted(os.listdir(year_path)):
                cat_path = os.path.join(year_path, cat_dir)
                if not os.path.isdir(cat_path):
                    continue
                cat = _normalise_category(cat_dir)
                if not cat:
                    continue

                # Count image assets to estimate how many projects to generate
                img_count = sum(
                    1 for f in os.listdir(cat_path)
                    if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
                )
                n_synthetic = max(2, img_count * 3)

                name_pool = _ILOILO_NAMES[cat]
                for i in range(n_synthetic):
                    base_name = name_pool[i % len(name_pool)]
                    name = base_name.format(i + 1) if "{}" in base_name else base_name
                    # Deduplicate: skip if exact name already exists for same year+cat
                    exists = any(
                        p["project_name"] == name
                        and p["year"] == year
                        and p["category"] == cat
                        for p in projects
                    )
                    if exists:
                        continue

                    mo, dy    = random.randint(1, 12), random.randint(1, 28)
                    alloc     = random.randint(5, 200) * 1_000_000
                    status    = random.choices(_STATUSES, weights=_STATUS_WEIGHTS)[0]
                    if year <= 2022:
                        status = random.choices(
                            ["Completed", "Ongoing", "Delayed"],
                            weights=[65, 20, 15]
                        )[0]
                    if status == "Completed":
                        spent = alloc * random.uniform(0.93, 1.0)
                        pct   = 100
                    elif status == "Ongoing":
                        spent = alloc * random.uniform(0.25, 0.75)
                        pct   = int(spent / alloc * 100)
                    elif status == "Delayed":
                        spent = alloc * random.uniform(0.10, 0.45)
                        pct   = int(spent / alloc * 100)
                    else:
                        spent = 0
                        pct   = 0

                    projects.append({
                        "id":                   len(projects) + 1,
                        "project_name":         name,
                        "category":             cat,
                        "district":             random.choice(_DISTRICTS),
                        "implementing_office":  random.choice(_ILOILO_OFFICES),
                        "status":               status,
                        "year":                 year,
                        "date":                 f"{year}-{mo:02d}-{dy:02d}",
                        "budget_allocated":     alloc,
                        "budget_spent":         round(spent),
                        "completion_percentage": pct,
                    })

    # ── Step 3: fallback if no filesystem access ──────────────────────────
    if not projects:
        for cat, names in _ILOILO_NAMES.items():
            for yr in range(2016, 2027):
                for i, base_name in enumerate(names[:6]):
                    name   = base_name.format(i + 1) if "{}" in base_name else base_name
                    mo, dy = random.randint(1, 12), random.randint(1, 28)
                    alloc  = random.randint(5, 150) * 1_000_000
                    status = random.choices(_STATUSES, weights=_STATUS_WEIGHTS)[0]
                    spent  = alloc * (random.uniform(0.93, 1.0) if status == "Completed"
                                      else random.uniform(0.1, 0.7))
                    pct    = 100 if status == "Completed" else int(spent / alloc * 100)
                    projects.append({
                        "id":                   len(projects) + 1,
                        "project_name":         name,
                        "category":             cat,
                        "district":             random.choice(_DISTRICTS),
                        "implementing_office":  random.choice(_ILOILO_OFFICES),
                        "status":               status,
                        "year":                 yr,
                        "date":                 f"{yr}-{mo:02d}-{dy:02d}",
                        "budget_allocated":     alloc,
                        "budget_spent":         round(spent),
                        "completion_percentage": pct,
                    })

    # Re-assign sequential IDs after dedup
    for idx, p in enumerate(projects, 1):
        p["id"] = idx
    return projects


# ── Module-level dataset (built once on import) ──────────────────────────────

_ALL_PROJECTS: list[dict] = _build_dataset()


# ── Public API ───────────────────────────────────────────────────────────────

def get_all_projects() -> list[dict]:
    """Return the complete list of project dictionaries."""
    return list(_ALL_PROJECTS)


def get_filtered_projects(filters: dict) -> list[dict]:
    """
    Filter projects by any combination of:
      filters = {
          "year":     int | str | None,
          "category": str | None,
          "district": str | None,
          "status":   str | None,
          "search":   str | None,   # substring match on project_name
      }
    Returns a new list; the master list is never mutated.
    """
    year     = filters.get("year")
    category = filters.get("category")
    district = filters.get("district")
    status   = filters.get("status")
    search   = (filters.get("search") or "").strip().lower()

    result = []
    for p in _ALL_PROJECTS:
        if year     and int(p["year"]) != int(year):
            continue
        if category and p["category"] != category:
            continue
        if district and p["district"] != district:
            continue
        if status   and p["status"]   != status:
            continue
        if search   and search not in p["project_name"].lower():
            continue
        result.append(p)
    return result


def get_category_counts() -> dict:
    """
    Returns total project count per canonical category, e.g.:
      {"Bridges": 42, "Roads": 67, ...}
    """
    cats = ["Bridges", "Roads", "Buildings and Facilities", "Flood Control and Drainage"]
    return {c: sum(1 for p in _ALL_PROJECTS if p["category"] == c) for c in cats}


def get_summary_stats() -> dict:
    """Convenience helper: totals used by the hero stats bar."""
    return {
        "total_projects":  len(_ALL_PROJECTS),
        "total_districts": len(_DISTRICTS),
        "total_allocated": sum(p["budget_allocated"] for p in _ALL_PROJECTS),
        "total_spent":     sum(p["budget_spent"]     for p in _ALL_PROJECTS),
        "years":           sorted({p["year"] for p in _ALL_PROJECTS}),
        "districts":       _DISTRICTS,
        "categories":      ["Bridges", "Roads", "Buildings and Facilities",
                             "Flood Control and Drainage"],
    }