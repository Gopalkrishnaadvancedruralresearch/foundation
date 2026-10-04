import io
import ssl
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
from PIL import Image

try:
    from IPython.display import display, Image as IPImage
    from google.colab import files
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

def fetch_image_safely(url, timeout=7):
    """Safely retrieves remote images bypassing SSL verification and bot blocking."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
        return Image.open(io.BytesIO(resp.read()))

def generate_magazine_page_24():
    # ------------------------------------------------------------------
    # 1. Page Geometry: International A4 at 300 DPI (8.27 x 11.69 in)
    # ------------------------------------------------------------------
    fig = plt.figure(figsize=(8.27, 11.69), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 141.4)
    ax.axis('off')

    # Deep Space Monograph Color Palette
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
    c_muted     = "#cbd5e1"

    # Base Canvas Fill
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
    try:
        img_logo = fetch_image_safely("https://garrf.in/kalam-zero-lab/logo.jpeg")
        ax.imshow(img_logo, extent=[5.5, 13.5, 127.8, 137.4], zorder=4)
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

    # Flags (Bharat & Singapore)
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
    # 4. Outer Structural Container
    # ------------------------------------------------------------------
    main_card = FancyBboxPatch((4, 14.0), 92, 109.5, boxstyle="round,pad=0.5,rounding_size=1.0",
                               facecolor=c_card_bg, edgecolor=c_border, linewidth=1.2, zorder=2)
    ax.add_patch(main_card)

    # Section Banner
    ax.text(50, 120.2, "SECTION 23 • THE LIVING FRONTIERS COMPENDIUM & AI DIRECTORY",
            color=c_gold_glow, fontsize=8.2, weight="black", ha="center",
            bbox=dict(boxstyle="round,pad=0.35,rounding_size=0.6", facecolor="#1a1202", edgecolor=c_gold, lw=1.1), zorder=3)

    ax.text(50, 116.6, "World-First Quantum AI, Autonomous Simulators & Intelligent Faculty",
            color=c_white, fontsize=12.2, weight="black", ha="center", zorder=3)
    ax.text(50, 114.2, "The Monograph Capstone (Page 24 of 24) • Open Infrastructure • Dr. APJ Abdul Kalam Zero Funding Lab",
            color=c_cyan, fontsize=7.2, style="italic", ha="center", zorder=3)

    # ------------------------------------------------------------------
    # BLOCK 1: MOST IMPORTANT FLAGSHIP — QUANTUM COMPUTING & AI (y = 92.5 to 112.5)
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((6.0, 92.5), 88.0, 20.0, boxstyle="round,pad=0.4,rounding_size=0.6",
                                facecolor="#03112c", edgecolor=c_purple, linewidth=1.3, zorder=3))

    ax.text(8.0, 109.8, "⚛️ FLAGSHIP DISCOVERY: WORLD-FIRST QUANTUM AI IN MULTIPHYSICS & SHM",
            color=c_gold_glow, fontsize=7.8, weight="black", zorder=4)
    ax.text(8.0, 107.8, "Powered by Annamdas 3D Solvers, Quantum-Classical Algorithms & Optimization Models",
            color=c_cyan, fontsize=6.8, weight="bold", zorder=4)
    ax.plot([8.0, 92.0], [106.6, 106.6], color="#271b4d", lw=0.9, zorder=4)

    q_col1 = [
        "1. QUANTUM AI + EMI LAB:",
        "   Electromechanical Impedance for PZT & Smart Materials.",
        "2. QUANTUM AI + EMR LAB:",
        "   Electromagnetic Radiations for Plasmons / Metamaterials."
    ]
    q_col2 = [
        "3. QUANTUM AI ROAD ESTIMATOR:",
        "   Civic Infrastructure Material & Money Saver App.",
        "4. PZT-EMI INTERACTIONS:",
        "   Nanoscale Defect & Acoustic Wave Dynamics."
    ]
    q_col3 = [
        "5. SINGLE-PHONE EMI EXP:",
        "   Direct Smart-Phone Ultrasonic SHM Interface.",
        "PORTAL ACCESS:",
        "   https://garrf.in/kalam-zero-lab/ ↗"
    ]

    for idx, (t1, t2, t3) in enumerate(zip(q_col1, q_col2, q_col3)):
        y_pos = 104.4 - (idx * 2.5)
        ax.text(8.0,  y_pos, t1, color=c_white if idx % 2 == 1 else c_gold_glow, fontsize=6.2, weight="bold" if idx % 2 == 0 else "normal", zorder=4)
        ax.text(38.0, y_pos, t2, color=c_white if idx % 2 == 1 else c_gold_glow, fontsize=6.2, weight="bold" if idx % 2 == 0 else "normal", zorder=4)
        ax.text(68.0, y_pos, t3, color=c_cyan if idx == 3 else (c_white if idx % 2 == 1 else c_green), fontsize=6.2, weight="bold" if idx % 2 == 0 or idx == 3 else "normal", zorder=4)

    # ------------------------------------------------------------------
    # BLOCK 2: 3-COLUMN RESEARCH ENGINES (y = 57.0 to 91.0)
    # ------------------------------------------------------------------
    # Card A: Drone Club & Industrial Robotics
    ax.add_patch(FancyBboxPatch((6.0, 57.0), 28.0, 34.0, boxstyle="round,pad=0.35,rounding_size=0.5",
                                facecolor=c_card_in, edgecolor=c_cyan, linewidth=1.1, zorder=3))
    ax.text(20.0, 88.5, "AEROSPACE & ROBOTICS", color=c_cyan, fontsize=7.2, weight="black", ha="center", zorder=4)
    ax.text(20.0, 86.6, "Flying Drone Club & CHITTI AI", color=c_gold_glow, fontsize=6.3, weight="bold", ha="center", zorder=4)
    ax.plot([8.0, 32.0], [85.5, 85.5], color=c_border, lw=0.6, zorder=4)

    drone_lines = [
        "• Open Onboarding for families & students",
        "• Interactive 3D Orbit, Hover & In-Hand Play",
        "• Virtual Component Assembly Suite",
        "• Battery-Constrained Live Trips (2 points)",
        "• 6 Specialized Classes (incl. Medical Drone)",
        "• Transparent parts & cost breakdowns",
        "• CHITTI Voice AI: Industrial Manipulator",
        "  kinematics, DoF & PID steering loop control",
        "Links: dronewelcomeclub.html • IndustrialRobot.html"
    ]
    y_dr = 83.5
    for line in drone_lines:
        c_use = c_gold_glow if "Links:" in line else c_white
        f_size = 5.6 if "Links:" in line else 5.8
        ax.text(8.0, y_dr, line, color=c_use, fontsize=f_size, zorder=4)
        y_dr -= 2.9

    # Card B: Semiconductor & Nanotech Suite
    ax.add_patch(FancyBboxPatch((36.0, 57.0), 28.0, 34.0, boxstyle="round,pad=0.35,rounding_size=0.5",
                                facecolor=c_card_in, edgecolor=c_gold, linewidth=1.1, zorder=3))
    ax.text(50.0, 88.5, "SEMICONDUCTOR & NANO", color=c_gold_glow, fontsize=7.2, weight="black", ha="center", zorder=4)
    ax.text(50.0, 86.6, "KRISHNA Cleanroom & Fab Suite", color=c_white, fontsize=6.3, weight="bold", ha="center", zorder=4)
    ax.plot([38.0, 62.0], [85.5, 85.5], color=c_border, lw=0.6, zorder=4)

    semi_lines = [
        "• Foundation: Solid-state physics & bandgaps",
        "• Level 1: ISO cleanrooms & HF safety",
        "• Level 2: 13.5nm EUV plasma & Rayleigh CD",
        "• Level 3: CD-SEM linewidths & AFM metrology",
        "• Level 4: 2.5D TSVs & 3D HBM packaging",
        "• Transistor Twin: Planar vs FinFET vs GAA",
        "• Level 5: Photonic ICs & Superconducting Qubits",
        "• Core Fab: Full-wafer implant, etch & CMP",
        "Link: https://garrf.in/kalam-zero-lab/semic.html"
    ]
    y_sm = 83.5
    for line in semi_lines:
        c_use = c_gold_glow if "Link:" in line else c_white
        f_size = 5.6 if "Link:" in line else 5.8
        ax.text(38.0, y_sm, line, color=c_use, fontsize=f_size, zorder=4)
        y_sm -= 2.9

    # Card C: Masters SHM Suite & Lecture Series
    ax.add_patch(FancyBboxPatch((66.0, 57.0), 28.0, 34.0, boxstyle="round,pad=0.35,rounding_size=0.5",
                                facecolor=c_card_in, edgecolor=c_green, linewidth=1.1, zorder=3))
    ax.text(80.0, 88.5, "MASTERS SHM SUITE", color=c_green, fontsize=7.2, weight="black", ha="center", zorder=4)
    ax.text(80.0, 86.6, "Specialized M.E. / M.Tech Research", color=c_white, fontsize=6.3, weight="bold", ha="center", zorder=4)
    ax.plot([68.0, 92.0], [85.5, 85.5], color=c_border, lw=0.6, zorder=4)

    shm_lines = [
        "• Advanced Civil, Mechanical & Aerospace Focus",
        "• Integrated PZT, EMI, Lamb Waves & NDT",
        "• FFT Digital Signal Processing & Spectra",
        "• Multi-Variable Structural Defect Modeling",
        "• 24/7 AI-Assisted Teaching Environment",
        "• Distinguished Master Lecture Series:",
        "  Prof. Manohar • Prof. Ananth",
        "  Prof. Chandra • Prof. Nanjunda",
        "Protected Link: ProfManohar.html (Ask for Pwd)"
    ]
    y_sh = 83.5
    for line in shm_lines:
        c_use = c_gold_glow if "Protected" in line else c_white
        f_size = 5.6 if "Protected" in line else 5.8
        ax.text(68.0, y_sh, line, color=c_use, fontsize=f_size, zorder=4)
        y_sh -= 2.9

    # ------------------------------------------------------------------
    # BLOCK 3: ARJUN AI CONSOLE & DIALOGUE PORTAL (y = 40.5 to 55.5)
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((6.0, 40.5), 88.0, 15.0, boxstyle="round,pad=0.4,rounding_size=0.6",
                                facecolor="#04132e", edgecolor=c_cyan, linewidth=1.3, zorder=3))

    ax.text(8.0, 52.8, "INTERACTIVE CONSULTATION: ARJUN AI ASSISTANT (24/7 ENGINEERING TUTOR)",
            color=c_cyan, fontsize=7.6, weight="black", zorder=4)
    ax.text(92.0, 52.8, "Direct Console: https://garrf.in/ai_assistants/emi/ ↗",
            color=c_gold_glow, fontsize=6.8, weight="bold", ha="right", zorder=4)
    ax.plot([8.0, 92.0], [51.6, 51.6], color="#173559", lw=0.8, zorder=4)

    arjun_points = [
        ("• SingBha-EMCD Queries:", " Ask Arjun about mathematical charge formulations, zero-drift spatial balances, and TIA circuit dynamics."),
        ("• Waveform & Spectrum Processing:", " Inquire about real-time impedance phase shifts, high-frequency excitation sweeps, and FFT signatures."),
        ("• Multi-Domain SHM Avatars:", " Switch Arjun avatars to analyze bridge piers, subsea transit linings, and composites across India and Singapore.")
    ]
    y_arj = 49.4
    for b_title, b_desc in arjun_points:
        ax.text(8.0, y_arj, b_title, color=c_gold_glow, fontsize=6.4, weight="bold", zorder=4)
        ax.text(32.0, y_arj, b_desc, color=c_white, fontsize=6.2, zorder=4)
        y_arj -= 2.7

    # ------------------------------------------------------------------
    # BLOCK 4: FOUNDER RECOGNITION — YASHOKIRTI AWARD 2026 (y = 28.0 to 39.0)
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((6.0, 28.0), 88.0, 11.2, boxstyle="round,pad=0.35,rounding_size=0.5",
                                facecolor="#0a1833", edgecolor=c_gold, linewidth=1.2, zorder=3))

    ax.text(8.0, 36.6, "ACADEMIC & CIVIC MILESTONE: ER. AVINASH SHIRODE YASHOKIRTI AWARD 2026",
            color=c_gold_glow, fontsize=7.2, weight="black", zorder=4)
    ax.text(92.0, 36.6, "Conferred by: IISc Alumni Association Bangalore",
            color=c_green, fontsize=6.6, weight="bold", ha="right", zorder=4)
    ax.plot([8.0, 92.0], [35.4, 35.4], color="#332a10", lw=0.8, zorder=4)

    ax.text(8.0, 33.6, "Awarded to Dr. Annamdas Venu Gopal Madhav in recognition of foundational research bridging Structural Health Monitoring,",
            color=c_white, fontsize=6.3, zorder=4)
    ax.text(8.0, 31.8, "piezoelectric intelligence, and artificial intelligence at AISIA / Virtual AISIA, fostering barrier-free rural education.",
            color=c_white, fontsize=6.3, zorder=4)
    ax.text(8.0, 30.0, "Official Citation Archive: https://sites.google.com/view/aisia/yasho ↗",
            color=c_cyan, fontsize=6.0, weight="bold", zorder=4)

    # ------------------------------------------------------------------
    # BLOCK 5: OFFICIAL COLOPHON & MONOGRAPH CONCLUSION (y = 15.0 to 26.5)
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((6.0, 15.0), 88.0, 11.5, boxstyle="round,pad=0.35,rounding_size=0.5",
                                facecolor="#020817", edgecolor=c_border, linewidth=1.0, zorder=3))

    ax.text(8.0, 24.2, "TECHNICAL MONOGRAPH COMPILATION COLOPHON (PAGES 1 TO 24)",
            color=c_white, fontsize=7.0, weight="heavy", zorder=4)
    ax.plot([8.0, 92.0], [23.2, 23.2], color="#172b47", lw=0.7, zorder=4)

    ax.text(8.0, 21.6, "Published by Gopalkrishna Advanced Rural Research Foundation (GARRF) • Section 8 Non-Profit Research Organization.",
            color=c_muted, fontsize=6.2, zorder=4)
    ax.text(8.0, 19.8, "Under the Dr. APJ Abdul Kalam Research Zero Funding Initiative • Dedicated to the engineers and students of Bharat & Singapore.",
            color=c_muted, fontsize=6.2, zorder=4)
    ax.text(8.0, 18.0, "All 250+ Virtual Laboratories, Schematics, and AI Tutors are hosted permanently free of commercial subscription paywalls.",
            color=c_gold_glow, fontsize=6.2, weight="semibold", zorder=4)
    ax.text(8.0, 16.2, "Monograph Series Completed: Issue 1, Magazine 1 • Concluding Technical Page 24 • https://garrf.in",
            color=c_cyan, fontsize=6.0, zorder=4)

    # ------------------------------------------------------------------
    # 5. Bottom Running Footer Bar with "Page 24"
    # ------------------------------------------------------------------
    footer_box = FancyBboxPatch((4, 1.2), 92, 9.6, boxstyle="round,pad=0.3,rounding_size=0.6",
                                facecolor=c_card_bg, edgecolor=c_border, linewidth=1.1, zorder=2)
    ax.add_patch(footer_box)

    ax.text(7, 8.2, "GARRF Technical Magazine 1 • Monograph Series • Archive Ref: GARRF-MAG1-SINGBHA-2026.P24 (FINAL)",
            color=c_muted, fontsize=7.1, zorder=4)
    ax.text(7, 5.7, "Arjun AI: https://garrf.in/ai_assistants/emi/  •  Zero Lab: https://garrf.in/kalam-zero-lab/  •  Portal: https://garrf.in",
            color=c_cyan, fontsize=6.4, weight="semibold", zorder=4)
    ax.text(7, 3.0, "Dedicated in Honour of Singapore and Bharat",
            color=c_white, fontsize=7.6, weight="bold", ha="left", zorder=4)
    ax.text(93, 3.0, "Page 24",
            color=c_gold_glow, fontsize=8.5, weight="black", ha="right", zorder=4)

    output_filename = "SingBha_Magazine_Page_24_Final.png"
    plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
    plt.close()

    if IN_COLAB:
        display(IPImage(filename=output_filename, width=720))
        print(f"Generated successfully: {output_filename} (A4 300 DPI Page 24 Final)")
        try:
            files.download(output_filename)
        except Exception:
            pass
    else:
        print(f"Generated successfully: {output_filename}")

if __name__ == "__main__":
    generate_magazine_page_24()
