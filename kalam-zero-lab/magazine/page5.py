import io
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
from PIL import Image
from IPython.display import display, Image as IPImage
from google.colab import files

def generate_magazine_page_5_iit_ready():
    # ------------------------------------------------------------------
    # 1. Page Geometry: International A4 at 300 DPI (8.27 x 11.69 in)[cite: 4]
    # ------------------------------------------------------------------
    fig = plt.figure(figsize=(8.27, 11.69), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 141.4)
    ax.axis('off')

    # Palette conforming to GARRF Monograph Identity[cite: 4]
    c_abyss     = "#020712"
    c_card_bg   = "#081326"
    c_subcard   = "#0c1d38"
    c_gold      = "#f59e0b"
    c_gold_glow = "#fbbf24"
    c_cyan      = "#38bdf8"
    c_pzt       = "#f97316"
    c_bond      = "#d97706"
    c_beam      = "#64748b"
    c_white     = "#ffffff"
    c_border    = "#1d3863"
    c_muted     = "#cbd5e1"  # Crisp high-contrast print slate[cite: 4]

    # Base Background Canvas[cite: 4]
    ax.add_patch(patches.Rectangle((0, 0), 100, 141.4, facecolor=c_abyss, zorder=0))
    ax.add_patch(patches.Circle((50, 75), radius=48, color="#0b2447", alpha=0.35, zorder=1))

    # ------------------------------------------------------------------
    # 2. Sacred Watermark: Dharmachakra 24-Spoke Circular Imprint[cite: 4]
    # ------------------------------------------------------------------
    cx_w, cy_w, r_w = 50.0, 72.0, 32.0
    ax.add_patch(patches.Circle((cx_w, cy_w), radius=r_w, facecolor="none",
                                edgecolor="#38bdf8", lw=1.2, alpha=0.08, zorder=1))
    ax.add_patch(patches.Circle((cx_w, cy_w), radius=r_w*0.93, facecolor="none",
                                edgecolor="#38bdf8", lw=0.8, alpha=0.06, zorder=1))
    ax.add_patch(patches.Circle((cx_w, cy_w), radius=r_w*0.28, facecolor="none",
                                edgecolor="#fbbf24", lw=1.1, alpha=0.10, zorder=1))
    ax.add_patch(patches.Circle((cx_w, cy_w), radius=r_w*0.08, facecolor="#38bdf8",
                                edgecolor="none", alpha=0.12, zorder=1))
    for i in range(24):
        theta = np.deg2rad(i * 15.0)
        x_in  = cx_w + (r_w * 0.28) * np.cos(theta)
        y_in  = cy_w + (r_w * 0.28) * np.sin(theta)
        x_out = cx_w + (r_w * 0.93) * np.cos(theta)
        y_out = cy_w + (r_w * 0.93) * np.sin(theta)
        ax.plot([x_in, x_out], [y_in, y_out], color="#38bdf8", lw=0.75, alpha=0.08, zorder=1)

    # ------------------------------------------------------------------
    # 3. Top Header Container Bar (White Fill)[cite: 4]
    # ------------------------------------------------------------------
    header_box = FancyBboxPatch((4, 126.8), 92, 11.8, boxstyle="round,pad=0.5,rounding_size=1.0",
                                facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1.2, zorder=2)
    ax.add_patch(header_box)

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
        ax.text(9.5, 132.6, "G", color=c_gold_glow, fontsize=14, weight="black", ha="center", va="center", zorder=4)

    # Header Typography[cite: 4]
    ax.text(15, 135.0, "Gopalkrishna Advanced Rural Research Foundation (GARRF)",
            color="#07233b", fontsize=10.6, weight="heavy", ha="left", zorder=3)
    ax.text(15, 132.3, "Dr. APJ Abdul Kalam Research Zero Funding Initiative",
            color="#b45309", fontsize=9.0, weight="bold", style="italic", ha="left", zorder=3)
    ax.text(15, 129.7, "Technical Magazine 1 • Issue 1 • Research Monograph Series",
            color="#334155", fontsize=8.0, weight="semibold", ha="left", zorder=3)

    # Dual Flags: Bharat & Singapore[cite: 4]
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
    # 4. Main Content Area Workspace[cite: 4]
    # ------------------------------------------------------------------
    content_area = FancyBboxPatch((4, 14.5), 92, 108.5, boxstyle="round,pad=0.5,rounding_size=1.0",
                                  facecolor=c_card_bg, edgecolor=c_border, linewidth=1.2, zorder=2)
    ax.add_patch(content_area)

    for cx, cy in [(6, 120.5), (94, 120.5), (6, 17.0), (94, 17.0)]:
        ax.plot([cx], [cy], marker="+", color=c_cyan, markersize=7.0, alpha=0.7, zorder=3)

    # Chapter Header
    ax.text(6.5, 118.8, "CHAPTER V • QUANTITATIVE DAMAGE METROLOGY & METRIC INVERSION",
            color=c_gold_glow, fontsize=9.2, weight="heavy", ha="left", zorder=4)
    ax.text(6.5, 114.8, "Progressive Fracture Mechanics & Classical Statistical Indices",
            color=c_white, fontsize=14.2, weight="black", ha="left", zorder=4)
    ax.text(6.5, 111.8, "Mathematical formulation of RMSD, MAPD, and CCD metrics across progressive substrate crack depths.",
            color=c_muted, fontsize=9.0, weight="medium", ha="left", zorder=4)

    # ------------------------------------------------------------------
    # SECTION A: Progressive Fracture Mechanics & Standardized States
    # ------------------------------------------------------------------
    card_frac = FancyBboxPatch((6, 69.2), 88, 40.8, boxstyle="round,pad=0.3,rounding_size=0.8",
                               facecolor=c_subcard, edgecolor="#254778", lw=1.2, zorder=3)
    ax.add_patch(card_frac)

    ax.text(8.5, 106.8, "1. PROGRESSIVE CRACK KINEMATICS (DEPTH STANDARDIZED BY t_s)",
            color=c_gold_glow, fontsize=9.8, weight="heavy", ha="left", zorder=4)

    # Sub-Box 1: Schematic of Progressive health states (Width: 41.5)
    ax.add_patch(patches.Rectangle((7.5, 71.5), 41.5, 33.0, facecolor="#07152b", edgecolor=c_border, lw=1.0, zorder=4))
    ax.text(28.2, 101.5, "Substrate Cross-Section & Crack Progression", color=c_cyan, fontsize=8.6, weight="bold", ha="center", zorder=5)

    # Cross-section block
    sub_x, sub_y, sub_w, sub_h = 10.5, 84.0, 35.5, 14.0
    ax.add_patch(patches.Rectangle((sub_x, sub_y), sub_w, sub_h, facecolor=c_beam, edgecolor="#94a3b8", lw=1.0, zorder=5))
    ax.text(sub_x + 2.0, sub_y + sub_h - 3.0, r"Substrate Thickness $t_s$", color=c_white, fontsize=7.6, weight="bold", zorder=6)

    # Progressive fracture labels
    crack_depths = [0.0, 0.10, 0.30, 0.50, 0.80]
    crack_colors = ["#16a34a", "#0284c7", "#ca8a04", "#ea580c", "#dc2626"]
    crack_names  = ["S₀: 0%", "S₁: 10%", "S₂: 30%", "S₃: 50%", "S₄: 80%"]

    for i, (cd, col, cname) in enumerate(zip(crack_depths, crack_colors, crack_names)):
        cx_pos = sub_x + 5.0 + i * 6.6
        if cd > 0:
            c_depth_pix = cd * sub_h
            ax.add_patch(patches.Polygon([[cx_pos - 0.7, sub_y + sub_h],
                                          [cx_pos, sub_y + sub_h - c_depth_pix],
                                          [cx_pos + 0.7, sub_y + sub_h]],
                                         facecolor=col, edgecolor="#ffffff", lw=0.6, zorder=7))
        else:
            # pristine marker
            ax.plot([cx_pos], [sub_y + sub_h], marker="o", color=col, markersize=3.5, zorder=7)

        ax.text(cx_pos, sub_y + sub_h + 1.2, cname, color=col, fontsize=7.0, weight="bold", ha="center", zorder=8)

    ax.text(28.2, 79.5, r"Crack Depth $d = \xi \cdot t_s$  ($\xi = 0.0 \rightarrow 0.80$, Width $w_c = 0.2$ mm)",
            color=c_gold_glow, fontsize=8.0, weight="bold", ha="center", zorder=6)
    ax.text(28.2, 76.5, r"Stiffness Degradation: $K_{\mathrm{eff}} = K_0 [1 - \gamma_d (d / t_s)^2]$",
            color=c_white, fontsize=8.0, weight="semibold", ha="center", zorder=6)
    ax.text(28.2, 73.2, "Quadratic compliance loss induced by stress concentration.",
            color=c_muted, fontsize=7.4, style="italic", ha="center", zorder=6)

    # Sub-Box 2: Quantitative 5-State fracture metric table (IIT-READY VISUALS)[cite: 13]
    # Standardized visual geometry and padding to prevent collision.
    ax.add_patch(FancyBboxPatch((51.0, 71.5), 41.5, 33.0, boxstyle="round,pad=0.2,rounding_size=0.5",
                                facecolor="#081427", edgecolor="#204575", lw=1.0, zorder=4))
    
    ax.text(71.7, 101.5, "Standardized Fracture Parameter Benchmark", color=c_cyan, fontsize=8.6, weight="bold", ha="center", zorder=5)

    # 5 Column headers, perfectly decoupled.Usable content width (40.5 units) split explicitly[cite: 12].
    headers = ["State", "Depth (d)", "Remaining ts", "ΔK Loss", "Severity"]
    col_x   = [52.5, 59.5, 68.0, 78.5, 86.0]  # standardized coordinates[cite: 12]
    y_start = 96.5

    for h, x_pos in zip(headers, col_x):
        ax.text(x_pos, y_start, h, color=c_gold_glow, fontsize=7.2, weight="bold", zorder=5)

    # Table data using professional bold italic Monograph nomenclature[cite: 13].
    # Percentage values shifted right to decouple visually[cite: 12].
    table_data = [
        ("**_S_**₀ (Pristine)", "0.0 mm",   "100 %", "0.0 %",  "Baseline",  "#16a34a"),
        ("**_S_**₁ (Crack 1)",  "0.10 ts",  "90 %",  "4.0 %",  "Incipient", "#0284c7"),
        ("**_S_**₂ (Crack 2)",  "0.30 ts",  "70 %",  "10.0 %", "Fatigue",   "#ca8a04"),
        ("**_S_**₃ (Crack 3)",  "0.50 ts",  "50 %",  "18.0 %", "Moderate",  "#ea580c"),
        ("**_S_**₄ (Crack 4)",  "0.80 ts",  "20 %",  "30.0 %", "Critical",  "#dc2626")
    ]

    for row_idx, row in enumerate(table_data):
        curr_y = y_start - 4.5 * (row_idx + 1)
        ax.plot([52.0, 91.0], [curr_y + 3.2, curr_y + 3.2], color="#1d3863", lw=0.6, zorder=4)
        for val, x_pos in zip(row[:5], col_x):
            if x_pos == col_x[0] or x_pos == col_x[4]:
                ax.text(x_pos, curr_y, val, color=row[5], fontsize=7.0, weight="bold", zorder=5)
            elif x_pos == col_x[2] or x_pos == col_x[3]:
                # right-justify these percentage columns for decoupled breathing room[cite: 12]
                ax.text(x_pos + 1.5, curr_y, val, color=c_muted, fontsize=6.8, ha="right", zorder=5)
            else:
                ax.text(x_pos, curr_y, val, color=c_muted, fontsize=6.8, zorder=5)

    ax.text(71.7, 73.0, "Reference values benchmarked for t_s = 4.0 mm plate specimens.",
            color=c_muted, fontsize=7.2, style="italic", ha="center", zorder=5)

    # ------------------------------------------------------------------
    # SECTION B: Statistical Damage Metric Derivations (RMSD, MAPD, CCD)
    # ------------------------------------------------------------------
    card_metrics = FancyBboxPatch((6, 42.0), 88, 25.5, boxstyle="round,pad=0.3,rounding_size=0.8",
                                  facecolor=c_subcard, edgecolor=c_border, lw=1.2, zorder=3)
    ax.add_patch(card_metrics)

    ax.text(8.5, 64.5, "2. CLASSICAL STATISTICAL DAMAGE INDICES (FREQUENCY-DOMAIN METROLOGY)",
            color=c_cyan, fontsize=9.6, weight="heavy", ha="left", zorder=4)

    # Column 1: RMSD (Root Mean Square Deviation) - Width: 27.5
    ax.add_patch(FancyBboxPatch((7.5, 43.8), 27.5, 18.5, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(8.8, 59.5, "Root Mean Square Deviation (RMSD):", color=c_gold_glow, fontsize=8.0, weight="bold", zorder=5)
    ax.text(8.8, 55.2, r"$\mathrm{RMSD} = \sqrt{\frac{\sum_{i=1}^{N} (G_i - G_i^0)^2}{\sum_{i=1}^{N} (G_i^0)^2}} \times 100\%$",
            color=c_white, fontsize=8.0, zorder=5)
    ax.text(8.8, 51.5, "• Primary metric for overall spectral change.", color=c_muted, fontsize=7.4, zorder=5)
    ax.text(8.8, 48.8, "• Strongly sensitive to resonant peak shifts.", color=c_muted, fontsize=7.4, zorder=5)
    ax.text(8.8, 46.0, "• Vulnerable to baseline vertical scaling drift.", color=c_cyan, fontsize=7.4, weight="bold", zorder=5)

    # Column 2: MAPD (Mean Absolute Percentage Deviation) - Width: 27.5
    ax.add_patch(FancyBboxPatch((36.2, 43.8), 27.5, 18.5, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(37.5, 59.5, "Mean Absolute Percentage (MAPD):", color=c_gold_glow, fontsize=8.0, weight="bold", zorder=5)
    ax.text(37.5, 55.2, r"$\mathrm{MAPD} = \frac{1}{N} \sum_{i=1}^{N} \left| \frac{G_i - G_i^0}{G_i^0} \right| \times 100\%$",
            color=c_white, fontsize=8.2, zorder=5)
    ax.text(37.5, 51.5, "• Normalized point-by-point relative error.", color=c_muted, fontsize=7.4, zorder=5)
    ax.text(37.5, 48.8, "• Highlights anti-resonant anti-node growth.", color=c_muted, fontsize=7.4, zorder=5)
    ax.text(37.5, 46.0, "• Susceptible to divisor division near nulls.", color=c_cyan, fontsize=7.4, weight="bold", zorder=5)

    # Column 3: CCD (Cross-Correlation Deviation) - Width: 28.5
    ax.add_patch(FancyBboxPatch((65.0, 43.8), 27.5, 18.5, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(66.2, 59.5, "Correlation Deviation (CCD = 1 - r):", color=c_gold_glow, fontsize=8.0, weight="bold", zorder=5)
    ax.text(66.2, 55.2, r"$\mathrm{CCD} = 1 - \frac{\sum (G_i - \overline{G})(G_i^0 - \overline{G}^0)}{\sigma_G \cdot \sigma_{G0}}$",
            color=c_white, fontsize=8.2, zorder=5)
    ax.text(66.2, 51.5, "• Measures waveform shape distortion.", color=c_muted, fontsize=7.4, zorder=5)
    ax.text(66.2, 48.8, "• Immune to uniform vertical gain shifts.", color=c_muted, fontsize=7.4, zorder=5)
    ax.text(66.2, 46.0, "• Insensitive to pure amplitude damping.", color=c_cyan, fontsize=7.4, weight="bold", zorder=5)

    # ------------------------------------------------------------------
    # SECTION C: Operational Limitations & Environmental Inversion Barrier
    # ------------------------------------------------------------------
    card_limit = FancyBboxPatch((6, 20.2), 88, 20.3, boxstyle="round,pad=0.3,rounding_size=0.8",
                                facecolor=c_subcard, edgecolor=c_border, lw=1.2, zorder=3)
    ax.add_patch(card_limit)

    ax.text(8.5, 37.8, "3. OPERATIONAL LIMITATIONS OF CLASSICAL INDICES & THE INVERSION BARRIER",
            color=c_gold_glow, fontsize=9.4, weight="heavy", ha="left", zorder=4)

    # Left Box: Environmental Coupling Barrier (Width: 41.5)
    ax.add_patch(FancyBboxPatch((7.5, 21.2), 41.5, 14.2, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(9.0, 32.6, "1. Environmental Coupling & False Alarms:", color=c_cyan, fontsize=8.4, weight="bold", zorder=5)
    ax.text(9.0, 29.5, "• Temperature variation (ΔT = ±15°C) shifts resonant peaks", color=c_muted, fontsize=7.6, zorder=5)
    ax.text(9.0, 27.2, "  by 1.5–3.0 kHz due to modulus softening E(T) = E₀(1 - α_E ΔT).", color=c_muted, fontsize=7.6, zorder=5)
    ax.text(9.0, 24.8, "• This frequency shift causes classical RMSD to surge > 15%,", color=c_white, fontsize=7.6, weight="bold", zorder=5)
    ax.text(9.0, 22.5, "  falsely registering as severe crack fracture without defect.", color=c_gold_glow, fontsize=7.6, weight="bold", zorder=5)

    # Right Box: Non-Invertibility of Classical Metrics (Width: 42.0)
    ax.add_patch(FancyBboxPatch((50.5, 21.2), 42.0, 14.2, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(52.0, 32.6, "2. The Inverse Problem & Local Minima Trap:", color=c_cyan, fontsize=8.4, weight="bold", zorder=5)
    ax.text(52.0, 29.5, "• Classical metrics compress N = 1,000 spectral points into", color=c_muted, fontsize=7.6, zorder=5)
    ax.text(52.0, 27.2, "  a single scalar scalar number (e.g., RMSD = 12.4%).", color=c_muted, fontsize=7.6, zorder=5)
    ax.text(52.0, 24.8, "• One scalar cannot decouple crack depth d from bond slip tb.", color=c_white, fontsize=7.6, weight="bold", zorder=5)
    ax.text(52.0, 22.5, "• Optimization becomes non-convex, trapped in local minima.", color=c_gold_glow, fontsize=7.6, weight="bold", zorder=5)

    # ------------------------------------------------------------------
    # TRANSITION BADGE: Centered Pill (x = 14 to 86, Standardized visual buffer)
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((14.0, 15.0), 72.0, 4.4, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#08152b", edgecolor="#b45309", lw=0.9, zorder=3))
    
    ax.text(50.0, 17.7, "Frontier Quantum AI Inversion (PI-QNN), Variational Circuits,",
            color=c_gold_glow, fontsize=8.2, weight="bold", style="italic", ha="center", zorder=4)
    ax.text(50.0, 15.8, "and Dimensional Ansatz Architectures continue on Page 6.",
            color=c_gold_glow, fontsize=8.2, weight="bold", style="italic", ha="center", zorder=4)

    # ------------------------------------------------------------------
    # 5. Bottom Running Footer Bar with "Page 5"[cite: 4]
    # ------------------------------------------------------------------
    footer_box = FancyBboxPatch((4, 1.2), 92, 9.6, boxstyle="round,pad=0.3,rounding_size=0.6",
                                facecolor=c_card_bg, edgecolor=c_border, linewidth=1.1, zorder=2)
    ax.add_patch(footer_box)

    ax.text(7, 8.2, "GARRF Technical Magazine 1 • Monograph Series • Archive Ref: GARRF-MAG1-SINGBHA-2026.P05",
            color=c_muted, fontsize=8.0, weight="medium", zorder=4)
    ax.text(7, 5.7, "Official Portal: https://garrf.in  •  LinkedIn: https://www.linkedin.com/company/gopalkrishnaadvancedruralresearchfoundation/",
            color=c_cyan, fontsize=7.6, weight="semibold", zorder=4)
    ax.text(7, 3.0, "Dedicated in Honour of Singapore and Bharat",
            color=c_white, fontsize=8.6, weight="bold", ha="left", zorder=4)
    ax.text(93, 3.0, "Page 5",
            color=c_gold_glow, fontsize=9.5, weight="black", ha="right", zorder=4)

    output_filename = "SingBha_Magazine_Page_5_Final.png"
    plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
    plt.close()

    display(IPImage(filename=output_filename, width=720))
    print(f"Generated successfully: {output_filename} (A4 300 DPIIIT-READY Page 5 Ready)")
    files.download(output_filename)

if __name__ == "__main__":
    generate_magazine_page_5_iit_ready()
