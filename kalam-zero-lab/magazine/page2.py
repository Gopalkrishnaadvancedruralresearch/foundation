import io
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
from PIL import Image
from IPython.display import display, Image as IPImage
from google.colab import files

def generate_magazine_page_2():
    # ------------------------------------------------------------------
    # 1. Page Geometry: International A4 at 300 DPI (8.27 x 11.69 in)
    # ------------------------------------------------------------------
    fig = plt.figure(figsize=(8.27, 11.69), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 141.4)
    ax.axis('off')

    # Color Palette matching the Monograph
    c_abyss     = "#020712"
    c_card_bg   = "#061328"
    c_card_in   = "#0b1c38"
    c_gold      = "#f59e0b"
    c_gold_glow = "#fbbf24"
    c_cyan      = "#38bdf8"
    c_green     = "#10b981"
    c_purple    = "#c084fc"
    c_white     = "#ffffff"
    c_border    = "#1e3b68"
    c_muted     = "#cbd5e1"  # Crisp high-contrast text for A4 print legibility

    # Base Canvas
    ax.add_patch(patches.Rectangle((0, 0), 100, 141.4, facecolor=c_abyss, zorder=0))
    ax.add_patch(patches.Circle((50, 72), radius=48, color="#0b2447", alpha=0.35, zorder=1))

    # ------------------------------------------------------------------
    # 2. Sacred Watermark: Dharmachakra 24-Spoke Circular Imprint
    # ------------------------------------------------------------------
    cx_w, cy_w, r_w = 50.0, 72.0, 32.0
    ax.add_patch(patches.Circle((cx_w, cy_w), radius=r_w, facecolor="none",
                                edgecolor="#38bdf8", lw=1.2, alpha=0.08, zorder=1))
    ax.add_patch(patches.Circle((cx_w, cy_w), radius=r_w*0.93, facecolor="none",
                                edgecolor="#38bdf8", lw=0.8, alpha=0.06, zorder=1))
    ax.add_patch(patches.Circle((cx_w, cy_w), radius=r_w*0.28, facecolor="none",
                                edgecolor="#fbbf24", lw=1.1, alpha=0.10, zorder=1))
    for i in range(24):
        theta = np.deg2rad(i * 15.0)
        x_in  = cx_w + (r_w * 0.28) * np.cos(theta)
        y_in  = cy_w + (r_w * 0.28) * np.sin(theta)
        x_out = cx_w + (r_w * 0.93) * np.cos(theta)
        y_out = cy_w + (r_w * 0.93) * np.sin(theta)
        ax.plot([x_in, x_out], [y_in, y_out], color="#38bdf8", lw=0.7, alpha=0.07, zorder=1)

    # ------------------------------------------------------------------
    # 3. Top Header Bar (White Fill)
    # ------------------------------------------------------------------
    header_box = FancyBboxPatch((4, 126.8), 92, 11.8, boxstyle="round,pad=0.5,rounding_size=1.0",
                                facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1.2, zorder=2)
    ax.add_patch(header_box)

    # Live Logo Fetch
    logo_drawn = False
    logo_url = "https://garrf.in/kalam-zero-lab/logo.jpeg"
    try:
        req = urllib.request.Request(logo_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=8) as response:
            logo_data = response.read()
            img = Image.open(io.BytesIO(logo_data))
            ax.imshow(img, extent=[5.5, 13.5, 127.8, 137.4], zorder=4)
            logo_drawn = True
    except Exception:
        pass

    if not logo_drawn:
        ax.add_patch(patches.Circle((9.5, 132.6), radius=3.4, facecolor="#030c1b", edgecolor=c_gold, linewidth=1.4, zorder=3))
        ax.text(9.5, 132.6, "G", color=c_gold_glow, fontsize=13, weight="black", ha="center", va="center", zorder=4)

    # Header Typography
    ax.text(15, 135.0, "Gopalkrishna Advanced Rural Research Foundation (GARRF)",
            color="#07233b", fontsize=10.2, weight="heavy", ha="left", zorder=3)
    ax.text(15, 132.3, "Dr. APJ Abdul Kalam Research Zero Funding Initiative",
            color="#b45309", fontsize=8.6, weight="bold", style="italic", ha="left", zorder=3)
    ax.text(15, 129.7, "Technical Magazine 1 • Issue 1 • Research Monograph Series",
            color="#475569", fontsize=7.4, ha="left", zorder=3)

    # Flags
    flag_y = 129.6
    ax.add_patch(patches.Rectangle((81.2, flag_y + 2.4), 5.4, 1.2, facecolor="#ff9933", zorder=3))
    ax.add_patch(patches.Rectangle((81.2, flag_y + 1.2), 5.4, 1.2, facecolor="#ffffff", edgecolor="#cbd5e1", lw=0.3, zorder=3))
    ax.add_patch(patches.Rectangle((81.2, flag_y),       5.4, 1.2, facecolor="#128807", zorder=3))
    ax.add_patch(patches.Circle((83.9, flag_y + 1.8), radius=0.48, facecolor="none", edgecolor="#000088", lw=0.55, zorder=4))
    ax.plot([83.9], [flag_y + 1.8], marker="o", color="#000088", markersize=0.8, zorder=5)

    ax.add_patch(patches.Rectangle((88.0, flag_y + 1.8), 5.4, 1.8, facecolor="#dc2626", zorder=3))
    ax.add_patch(patches.Rectangle((88.0, flag_y),       5.4, 1.8, facecolor="#ffffff", edgecolor="#cbd5e1", lw=0.3, zorder=3))
    ax.add_patch(patches.Circle((89.3, flag_y + 2.7), radius=0.62, facecolor="#ffffff", zorder=4))
    ax.add_patch(patches.Circle((89.6, flag_y + 2.7), radius=0.53, facecolor="#dc2626", zorder=5))
    for ang in [0, 72, 144, 216, 288]:
        rad = np.radians(ang)
        ax.plot(90.15 + 0.35*np.cos(rad), 2.7 + flag_y + 0.35*np.sin(rad), marker="*", color="#ffffff", markersize=1.3, zorder=6)

    # ------------------------------------------------------------------
    # 4. Page 2 Outer Structural Container
    # ------------------------------------------------------------------
    main_card = FancyBboxPatch((4, 14.0), 92, 109.5, boxstyle="round,pad=0.5,rounding_size=1.0",
                               facecolor=c_card_bg, edgecolor=c_border, linewidth=1.2, zorder=2)
    ax.add_patch(main_card)

    # Section Banner
    ax.text(50, 120.2, "GARRF ORGANIZATIONAL COMMITTEE TREE & 5 RESEARCH DIVISIONS",
            color=c_gold_glow, fontsize=8.2, weight="black", ha="center",
            bbox=dict(boxstyle="round,pad=0.35,rounding_size=0.6", facecolor="#1a1202", edgecolor=c_gold, lw=1.1), zorder=3)

    ax.text(50, 116.6, "One Foundation • Many Branches • One Purpose",
            color=c_white, fontsize=13.0, weight="black", ha="center", zorder=3)
    ax.text(50, 114.2, "Official Living Tree Roster (garrf.in/committee.html) • Section 8 Non-Profit Research Foundation",
            color=c_cyan, fontsize=7.6, style="italic", ha="center", zorder=3)

    # ------------------------------------------------------------------
    # SECTION 1: Board of Patrons & Executive Leadership (y = 104.5 to 112.5)
    # ------------------------------------------------------------------
    # Left: Patrons
    ax.add_patch(FancyBboxPatch((6.0, 105.0), 26.0, 7.5, boxstyle="round,pad=0.3,rounding_size=0.5",
                                facecolor=c_card_in, edgecolor=c_gold, linewidth=1.1, zorder=3))
    ax.text(19.0, 110.8, "BOARD OF PATRONS", color=c_gold_glow, fontsize=7.2, weight="black", ha="center", zorder=4)
    ax.text(19.0, 108.6, "Mr. Annamdas Lakshmi Narayana", color=c_white, fontsize=6.8, weight="bold", ha="center", zorder=4)
    ax.text(19.0, 106.6, "& Mrs. Annamdas Janaki", color=c_white, fontsize=6.8, weight="bold", ha="center", zorder=4)

    # Right: Leadership & Scientific Guidance
    ax.add_patch(FancyBboxPatch((33.5, 105.0), 60.5, 7.5, boxstyle="round,pad=0.3,rounding_size=0.5",
                                facecolor=c_card_in, edgecolor=c_cyan, linewidth=1.1, zorder=3))
    ax.text(63.75, 110.8, "LEADERSHIP & SCIENTIFIC GUIDANCE", color=c_cyan, fontsize=7.2, weight="black", ha="center", zorder=4)
    
    # 3 distinct columns with separate y-coordinates for names and roles
    ax.text(43.0, 108.6, "Prof. N. Sundararajan", color=c_white, fontsize=6.8, weight="bold", ha="center", zorder=4)
    ax.text(43.0, 106.6, "Honorary Advisor (Ret. NTU)", color=c_muted, fontsize=6.0, ha="center", zorder=4)

    ax.text(63.5, 108.6, "Prof. Soh Chee Kiong", color=c_white, fontsize=6.8, weight="bold", ha="center", zorder=4)
    ax.text(63.5, 106.6, "Honorary Advisor (Ret. NTU, NUS)", color=c_muted, fontsize=6.0, ha="center", zorder=4)

    ax.text(84.0, 108.6, "Dr. V. G. M. Annamdas", color=c_gold_glow, fontsize=6.8, weight="bold", ha="center", zorder=4)
    ax.text(84.0, 106.6, "Chief Scientific Advisor (IISc/NTU)", color=c_muted, fontsize=6.0, ha="center", zorder=4)

    # ------------------------------------------------------------------
    # SECTION 2: Official Committee Roster (y = 80.0 to 103.5)
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((6.0, 80.5), 88.0, 23.0, boxstyle="round,pad=0.35,rounding_size=0.6",
                                facecolor="#050e20", edgecolor="#234273", linewidth=1.1, zorder=3))

    ax.text(8.0, 101.4, "INTERNATIONAL COLLABORATORS & ADVISORS (GLOBAL NETWORK):",
            color=c_gold_glow, fontsize=7.2, weight="black", zorder=4)
    
    int_col1 = [
        "• Prof. Sridhar Idapalapati (NTU / Cambridge)",
        "• Dr. Zhang Lei (A*STAR Singapore / NTU)",
        "• Annamdas Harish Kumar (USA / Illinois)",
        "• Dr. Alok Kumar Gupta (Norway / IISc)"
    ]
    int_col2 = [
        "• Dr. Deepesh Upadrashta (Singapore / NTU)",
        "• Mr. Sukesh M V (Singapore / Professional Eng)",
        "• Dr. Sivanand Somasundaram (NTU Singapore)",
        "• Ashok Kadavakollu, MBA (USA / Robotics)"
    ]
    int_col3 = [
        "• Mr. Soma Srinivas (USA / IIT Bombay / Verizon)",
        "• Ms. Gavini Srujana (USA / IEEE Event Secretary)",
        "• Dr. Narasimalu Srikanth (NTU / Ocean Energy)",
        "• Mr. Ranga Reddy (Europe / IISc Alumnus)"
    ]
    
    for idx, (l1, l2, l3) in enumerate(zip(int_col1, int_col2, int_col3)):
        y_pos = 98.6 - (idx * 2.0)
        ax.text(8.0,  y_pos, l1, color=c_white, fontsize=6.4, zorder=4)
        ax.text(38.0, y_pos, l2, color=c_white, fontsize=6.4, zorder=4)
        ax.text(68.0, y_pos, l3, color=c_white, fontsize=6.4, zorder=4)

    ax.plot([8.0, 92.0], [90.5, 90.5], color="#172b47", lw=0.8, zorder=4)

    ax.text(8.0, 88.8, "NATIONAL ADVISORS & STUDENT CHAPTER HEADS (BHARAT NETWORK):",
            color=c_cyan, fontsize=7.2, weight="black", zorder=4)
    
    nat_col1 = ["• Dr. K.N.V. Chandra Shekhar (IITB/Hopkins)", "• Dr. Nivethitha Somu (IITB / NTU Singapore)"]
    nat_col2 = ["• Mr. Sushant (IISc Bangalore / Research Eng)", "• P Arvind (Local Language Coordinator)"]
    nat_col3 = ["• Dr. M Venu (Dean ISDC, Inst. Aero Eng)", "• Mr. Sunkara Madhu Babu, M.Tech (AICTE)"]

    for idx, (n1, n2, n3) in enumerate(zip(nat_col1, nat_col2, nat_col3)):
        y_pos = 86.4 - (idx * 1.9)
        ax.text(8.0,  y_pos, n1, color=c_muted, fontsize=6.3, zorder=4)
        ax.text(38.0, y_pos, n2, color=c_muted, fontsize=6.3, zorder=4)
        ax.text(68.0, y_pos, n3, color=c_muted, fontsize=6.3, zorder=4)

    ax.text(8.0, 82.2, "Student Chapter Heads: R Sai Vaishnav Nandan (Karnataka / Manipal Inst. Tech)  •  Koushik Vulli (Andhra Pradesh / GITAM)",
            color=c_gold_glow, fontsize=6.3, weight="bold", zorder=4)

    # ------------------------------------------------------------------
    # SECTION 3: The 5 Strategic Divisions (y = 51.0 to 78.5)
    # ------------------------------------------------------------------
    ax.text(50, 77.2, "GARRF 5 STRATEGIC DIVISIONS & RESEARCH CENTRES",
            color=c_white, fontsize=7.6, weight="black", ha="center", zorder=4)

    divisions = [
        {
            "name": "AI, Engineering &\nResearch Innovation",
            "hub": "Virtual AISIA ↗",
            "status": "IN PROGRESS",
            "c_status": c_gold_glow,
            "bullets": ["AI & Machine Learning", "SHM & Smart Infra", "Digital Twins & Sensors", "Robotics & Automation", "Data Analytics & R&D"],
            "x": 14.5
        },
        {
            "name": "Student Research\n& Innovation Centre",
            "hub": "Kalam Research ↗",
            "status": "IN PROGRESS",
            "c_status": c_green,
            "bullets": ["Internships & Projects", "M.Tech/PhD Research", "Research Publications", "Hackathons & Patents", "Methodology Training"],
            "x": 32.25
        },
        {
            "name": "Rural Innovation &\nSustainable Dev.",
            "hub": "Rural Development",
            "status": "UPCOMING",
            "c_status": c_purple,
            "bullets": ["Smart Villages & Agri", "Renewable Clean Energy", "Water Management", "Climate Sustainability", "Rural Health & Welfare"],
            "x": 50.0
        },
        {
            "name": "Education & Capacity\nBuilding Centre",
            "hub": "Capacity Building",
            "status": "UPCOMING",
            "c_status": c_cyan,
            "bullets": ["Faculty Programs (FDP)", "Workshops & Training", "Online Certification", "STEM School Outreach", "Science Communication"],
            "x": 67.75
        },
        {
            "name": "Women Research\nInitiative & Empow.",
            "hub": "Women in STEM",
            "status": "UPCOMING",
            "c_status": c_muted,
            "bullets": ["Women in STEM Drive", "Fellowships & Grants", "Leadership Mentorship", "Digital Literacy Hubs", "Rural Startup Support"],
            "x": 85.5
        }
    ]

    for div in divisions:
        # Box container (Height 23.5)
        ax.add_patch(FancyBboxPatch((div["x"] - 8.2, 51.5), 16.4, 23.5, boxstyle="round,pad=0.3,rounding_size=0.5",
                                   facecolor=c_card_in, edgecolor=div["c_status"], linewidth=1.1, zorder=3))

        # Status badge at the top
        ax.text(div["x"], 73.2, div["status"], color=div["c_status"],
                fontsize=5.8, weight="black", ha="center",
                bbox=dict(boxstyle="round,pad=0.18", facecolor="#020712", edgecolor=div["c_status"], lw=0.6), zorder=4)

        # Title
        ax.text(div["x"], 69.8, div["name"], color=c_white, fontsize=6.6, weight="bold", ha="center", linespacing=1.15, zorder=4)
        
        # Hub link
        ax.text(div["x"], 66.8, div["hub"], color=c_gold_glow, fontsize=5.8, weight="bold", ha="center", zorder=4)
        ax.plot([div["x"] - 6.8, div["x"] + 6.8], [65.6, 65.6], color=c_border, lw=0.6, zorder=4)

        # Bullets (Explicitly positioned vertically with no overlap)
        y_b = 64.0
        for b in div["bullets"]:
            ax.text(div["x"] - 7.0, y_b, f"• {b}", color=c_muted, fontsize=5.6, ha="left", zorder=4)
            y_b -= 2.2

    # ------------------------------------------------------------------
    # SECTION 4: Kalam Virtual Simulators, National Disparity & Manifesto (y = 15.0 to 49.5)
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((6.0, 15.5), 88.0, 33.5, boxstyle="round,pad=0.45,rounding_size=0.8",
                                facecolor="#051024", edgecolor=c_green, linewidth=1.3, zorder=3))

    # Header Titles (Clearly spaced)
    ax.text(8.0, 46.8, "BHARAT'S LEADING PRIVATE VIRTUAL SIMULATOR DEVELOPER: 250+ MULTIPHYSICS SIMULATORS",
            color=c_green, fontsize=7.6, weight="black", zorder=4)
    ax.text(8.0, 44.8, "Active Foundation Portal: https://garrf.in/kalam-zero-lab/",
            color=c_gold_glow, fontsize=7.1, weight="bold", zorder=4)
    ax.plot([8.0, 92.0], [43.8, 43.8], color="#17384a", lw=0.8, zorder=4)

    ax.text(8.0, 42.0, "Spread Across Several Engineering Disciplines (Hosted 100% Free under Kalam Zero Funding Initiative):",
            color=c_white, fontsize=7.1, weight="bold", zorder=4)

    # Multi-line Disciplines (Font 6.4, cleanly separated)
    disciplines = [
        "• Civil & Structural Mechanics: Beam Deflection, Truss Finite Elements, Elastodynamic Wave Propagation",
        "• Mechanical & Dynamic Vibrations: Modal Analysis, Damped Oscillations, Gear & Rotor Dynamics",
        "• Electrical & Transducer Electronics: Piezoelectric Impedance, Transimpedance Amps, Signal Conditioning",
        "• AI, Robotics & Autonomous Systems: Neural Network Classification, Quantum AI Damage Identification",
        "• Fluid Dynamics & Applied Physics: Wave Optics, Hydraulics, Continuum Charge Distributions"
    ]
    y_disc = 40.0
    for line in disciplines:
        ax.text(8.0, y_disc, line, color=c_cyan, fontsize=6.4, weight="semibold", zorder=4)
        y_disc -= 1.8

    ax.plot([8.0, 92.0], [30.4, 30.4], color="#17384a", lw=0.8, zorder=4)

    # The 97% - 3% National Research Reality (Wrapped to prevent any horizontal cut-off)
    nat_lines = [
        "THE NATIONAL RESEARCH REALITY:",
        "In India, 97% of total research funding goes to just 3% of elite institutions, while the remaining 97% of other",
        "engineering colleges, state universities, and rural institutions must share a mere 3% of funding.",
        "Operating under the Dr. APJ Abdul Kalam Research Zero Funding Initiative, GARRF bridges this disparity",
        "by developing and hosting 250+ multiphysics virtual simulators completely free of commercial paywalls."
    ]
    y_nat = 28.6
    ax.text(8.0, y_nat, nat_lines[0], color=c_white, fontsize=6.6, weight="bold", zorder=4)
    for line in nat_lines[1:]:
        y_nat -= 1.6
        ax.text(8.0, y_nat, line, color=c_muted, fontsize=6.4, zorder=4)

    # Founder's Manifesto Quote Box (Prominent Gold, Italic)
    ax.plot([8.0, 92.0], [21.0, 21.0], color="#2d4a2d", lw=0.8, zorder=4)
    ax.text(8.0, 19.2, '“India does not need Great People, it needs People who make India Great.',
            color=c_gold_glow, fontsize=7.4, weight="bold", style="italic", zorder=4)
    ax.text(8.0, 17.4, ' You are one of those and I am one of those.”',
            color=c_gold_glow, fontsize=7.4, weight="bold", style="italic", zorder=4)
    ax.text(92.0, 17.4, '— Dr. Annamdas Venu Gopal Madhav, Founder GARRF',
            color=c_gold, fontsize=7.0, weight="bold", ha="right", zorder=4)

    # ------------------------------------------------------------------
    # 5. Bottom Running Footer Bar with "Page 2"
    # ------------------------------------------------------------------
    footer_box = FancyBboxPatch((4, 1.2), 92, 9.6, boxstyle="round,pad=0.3,rounding_size=0.6",
                                facecolor=c_card_bg, edgecolor=c_border, linewidth=1.1, zorder=2)
    ax.add_patch(footer_box)

    ax.text(7, 8.2, "GARRF Technical Magazine 1 • Monograph Series • Archive Ref: GARRF-MAG1-SINGBHA-2026.P02",
            color=c_muted, fontsize=7.1, zorder=4)
    ax.text(7, 5.7, "Official Portal: https://garrf.in  •  Committee Roster: https://garrf.in/committee.html  •  Lab: https://garrf.in/kalam-zero-lab/",
            color=c_cyan, fontsize=6.4, weight="semibold", zorder=4)
    ax.text(7, 3.0, "Dedicated in Honour of Singapore and Bharat",
            color=c_white, fontsize=7.6, weight="bold", ha="left", zorder=4)
    ax.text(93, 3.0, "Page 2",
            color=c_gold_glow, fontsize=8.5, weight="black", ha="right", zorder=4)

    output_filename = "SingBha_Magazine_Page_2_CleanA4.png"
    plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
    plt.close()

    display(IPImage(filename=output_filename, width=720))
    print(f"Generated successfully: {output_filename} (A4 300 DPI Clean Edition)")
    files.download(output_filename)

if __name__ == "__main__":
    generate_magazine_page_2()
