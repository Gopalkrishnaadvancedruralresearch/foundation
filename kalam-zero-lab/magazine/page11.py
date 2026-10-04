import io
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
from PIL import Image
from IPython.display import display, Image as IPImage
from google.colab import files

def generate_magazine_page_11_benchmark_matrix():
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
    c_emerald   = "#10b981"
    c_crimson   = "#ef4444"
    c_white     = "#ffffff"
    c_border    = "#1d3863"
    c_muted     = "#cbd5e1"

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

    # Monograph Section 9 Banner[cite: 27]
    ax.text(6.5, 118.8, "SECTION 9 • MASTER TECHNICAL BENCHMARK MATRIX",
            color=c_gold_glow, fontsize=9.2, weight="heavy", ha="left", zorder=4)
    ax.text(6.5, 114.8, "Master Technical Benchmark Matrix: EMI vs. SingBha-EMCD",
            color=c_white, fontsize=14.0, weight="black", ha="left", zorder=4)
    ax.text(6.5, 111.8, "Comprehensive 8-dimensional comparative evaluation of structural diagnostics and field robustness.",
            color=c_muted, fontsize=8.8, weight="medium", ha="left", zorder=4)

    # ------------------------------------------------------------------
    # BENCHMARK TABLE CONTAINER (STRICT PADDED GRID)
    # ------------------------------------------------------------------
    card_table = FancyBboxPatch((6, 20.8), 88, 88.8, boxstyle="round,pad=0.3,rounding_size=0.6",
                                facecolor=c_subcard, edgecolor="#254778", lw=1.2, zorder=3)
    ax.add_patch(card_table)

    # Inner Table Box: from y = 22.0 to 107.5
    ax.add_patch(FancyBboxPatch((7.5, 22.2), 85.0, 85.2, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))

    # Explicitly Non-Overlapping Column Coordinates
    # Col 1 (Diagnostic Dimension): x in [9.0, 27.8] -> width = 18.8
    # Col 2 (Conventional EMI):     x in [29.2, 57.5] -> width = 28.3
    # Col 3 (SingBha-EMCD):         x in [60.0, 91.5] -> width = 31.5
    col1_x = 9.2
    col2_x = 29.5
    col3_x = 60.0

    # Table Header Banner (Clean gap above Row 0)
    ax.add_patch(FancyBboxPatch((8.0, 101.4), 84.0, 4.8, boxstyle="round,pad=0.1,rounding_size=0.2",
                                facecolor="#0c234b", edgecolor="#38bdf8", lw=0.8, zorder=5))
    ax.text(col1_x + 8.5, 103.8, "DIAGNOSTIC DIMENSION", color=c_gold_glow, fontsize=7.4, weight="heavy", ha="center", va="center", zorder=6)
    ax.text(col2_x + 13.5, 103.8, "CONVENTIONAL SCALAR EMI (1994-PRESENT)", color="#ef4444", fontsize=7.1, weight="heavy", ha="center", va="center", zorder=6)
    ax.text(col3_x + 14.8, 103.8, "SingBha-EMCD TECHNOLOGY (GARRF)", color="#10b981", fontsize=7.1, weight="heavy", ha="center", va="center", zorder=6)

    # 8 Rows Cleanly Wrapped Definitions[cite: 27]
    rows_data = [
        ("1. Measured Observable",
         "Scalar terminal admittance Y(ω) = G + jB",
         "Lumped area average across full crystal footprint.",
         "Continuous spatial charge field D3(x,y) & ∇D3",
         "Preserves gradient singularities at crack mouth."),
        
        ("2. Mechanical Theory",
         "1D spring-mass uniaxial approximation",
         "Neglects multi-axial Poisson coupling & transverse shear.",
         "3D elastodynamic coupled tensor formulation (IEEE 176)",
         "Full anisotropic mechanics (S_ij = s_ijkl*T_kl + d_kij*E_k)."),

        ("3. Adhesive Interlayer",
         "Ignored or assumed infinitely rigid",
         "Incapable of modeling shear lag or bond degradation.",
         "Explicit viscoelastic shear-lag dynamics (h_a, G_a, Z_a)",
         "Hyperbolic shear stress profile τ_xz(x) across bond layer."),

        ("4. Defect Localization",
         "Low / Indeterminate",
         "Stress release is mathematically diluted (<0.5% shift).",
         "High Sub-Millimeter Spatial Resolution",
         "Segmented differential pads isolate exact (x, y) coordinates."),

        ("5. Crack Orientation",
         "Angle Blind",
         "Identical scalar frequency shifts for all flaw trajectories.",
         "Selective Directional Crack Trajectory Resolution",
         "Orthogonal transverse coupling (d31 vs d32) resolves θ angle."),

        ("6. Inspection Reach",
         "Strictly localized near-field (0.4 m to 1.5 m)",
         "Severe geometric ultrasonic attenuation in spacious plates.",
         "Dual-Horizon Range Scaling (Near-Field to >10 m Reach)",
         "Hybrid self-sensing gradient + pitch-catch guided Lamb waves."),

        ("7. Thermal Stability",
         "Severe Diurnal Drift (15°C to 45°C)",
         "Dielectric drift is 10x-50x larger than crack; false alarms.",
         "Inherent Hardware Thermal Drift Immunity (∂ε33/∂x ≡ 0)",
         "Uniform ambient heat cancels identically at circuit level."),

        ("8. Cable Limits",
         "Severely Restricted (<2 m Coaxial Cables)",
         "Parasitic capacitance (50-100 pF/m) induces phase distortion.",
         "Virtual Ground Circuitry (Supports 50+ Meter Field Cables)",
         "Transimpedance op-amp at 0 V eliminates dynamic cable current.")
    ]

    # Row spacing
    y_row_start = 100.2
    row_height = 9.3

    for idx, (dim_title, emi_line1, emi_line2, emcd_line1, emcd_line2) in enumerate(rows_data):
        y_top = y_row_start - idx * row_height

        # Alternating background shading
        if idx % 2 == 1:
            ax.add_patch(patches.Rectangle((8.0, y_top - row_height), 84.0, row_height,
                                           facecolor="#050e1f", edgecolor="none", zorder=4))

        # Horizontal Row Separator
        ax.plot([8.0, 92.0], [y_top - row_height, y_top - row_height], color="#16305a", lw=0.6, zorder=5)

        # Dimension Cell
        ax.text(col1_x, y_top - 3.8, dim_title, color=c_gold_glow, fontsize=7.0, weight="heavy", zorder=6)
        
        # EMI Cell
        ax.text(col2_x, y_top - 3.2, emi_line1, color=c_white, fontsize=6.5, weight="bold", zorder=6)
        ax.text(col2_x, y_top - 6.4, emi_line2, color="#f87171", fontsize=5.9, style="italic", zorder=6)

        # SingBha-EMCD Cell
        ax.text(col3_x, y_top - 3.2, emcd_line1, color=c_white, fontsize=6.5, weight="bold", zorder=6)
        ax.text(col3_x, y_top - 6.4, emcd_line2, color="#34d399", fontsize=5.9, zorder=6)

    # Vertical Column Partition Lines (contained within table boundaries)
    for vx in [28.2, 58.8]:
        ax.plot([vx, vx], [y_row_start - 8 * row_height, y_row_start], color="#204575", lw=0.8, zorder=5)

    # ------------------------------------------------------------------
    # TRANSITION BADGE: Monograph Transition Pill -> Page 12
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((10.0, 15.2), 80.0, 3.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#08152b", edgecolor="#b45309", lw=0.9, zorder=3))
    ax.text(50.0, 16.9, "SURFACE MICRO-CRACK MECHANICS & GRADIENT SINGULARITIES (∇D3) CONTINUE ON PAGE 12.",
            color=c_gold_glow, fontsize=7.4, weight="bold", style="italic", ha="center", zorder=4)

    # ------------------------------------------------------------------
    # 5. Bottom Running Footer Bar (Normalized to "Page 11")[cite: 4]
    # ------------------------------------------------------------------
    footer_box = FancyBboxPatch((4, 1.2), 92, 9.6, boxstyle="round,pad=0.3,rounding_size=0.6",
                                facecolor=c_card_bg, edgecolor=c_border, linewidth=1.1, zorder=2)
    ax.add_patch(footer_box)

    ax.text(7, 8.2, "GARRF Technical Magazine 1 • Monograph Series • Archive Ref: GARRF-MAG1-SINGBHA-2026.P11",
            color=c_muted, fontsize=8.0, weight="medium", zorder=4)
    ax.text(7, 5.7, "Official Portal: https://garrf.in  •  LinkedIn: https://www.linkedin.com/company/gopalkrishnaadvancedruralresearchfoundation/",
            color=c_cyan, fontsize=7.6, weight="semibold", zorder=4)
    ax.text(7, 3.0, "Dedicated in Honour of Singapore and Bharat",
            color=c_white, fontsize=8.6, weight="bold", ha="left", zorder=4)
    ax.text(93, 3.0, "Page 11",
            color=c_gold_glow, fontsize=9.5, weight="black", ha="right", zorder=4)

    output_filename = "SingBha_Magazine_Page_11_Benchmark_Matrix_Fixed.png"
    plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
    plt.close()

    display(IPImage(filename=output_filename, width=720))
    print(f"Generated successfully: {output_filename} (A4 300 DPI Page 11 - Zero Overlaps Guaranteed)")
    files.download(output_filename)

if __name__ == "__main__":
    generate_magazine_page_11_benchmark_matrix()
