import io
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
from PIL import Image
from IPython.display import display, Image as IPImage
from google.colab import files

def generate_magazine_page_3_perfect_layout():
    # ------------------------------------------------------------------
    # 1. Page Geometry: International A4 at 300 DPI (8.27 x 11.69 in)
    # ------------------------------------------------------------------
    fig = plt.figure(figsize=(8.27, 11.69), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 141.4)
    ax.axis('off')

    # Color Palette conforming to GARRF Monograph Identity
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
    c_muted     = "#cbd5e1"  # Crisp high-contrast print white-slate

    # Base Background Canvas
    ax.add_patch(patches.Rectangle((0, 0), 100, 141.4, facecolor=c_abyss, zorder=0))
    ax.add_patch(patches.Circle((50, 75), radius=48, color="#0b2447", alpha=0.35, zorder=1))

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
    # 3. Top Header Container Bar (White Fill)[cite: 5]
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

    # Header Typography[cite: 5]
    ax.text(15, 135.0, "Gopalkrishna Advanced Rural Research Foundation (GARRF)",
            color="#07233b", fontsize=10.6, weight="heavy", ha="left", zorder=3)
    ax.text(15, 132.3, "Dr. APJ Abdul Kalam Research Zero Funding Initiative",
            color="#b45309", fontsize=9.0, weight="bold", style="italic", ha="left", zorder=3)
    ax.text(15, 129.7, "Technical Magazine 1 • Issue 1 • Research Monograph Series",
            color="#334155", fontsize=8.0, weight="semibold", ha="left", zorder=3)

    # Dual Flags: Bharat & Singapore[cite: 5]
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
    # 4. Main Content Area Workspace[cite: 5]
    # ------------------------------------------------------------------
    content_area = FancyBboxPatch((4, 14.5), 92, 108.5, boxstyle="round,pad=0.5,rounding_size=1.0",
                                  facecolor=c_card_bg, edgecolor=c_border, linewidth=1.2, zorder=2)
    ax.add_patch(content_area)

    for cx, cy in [(6, 120.5), (94, 120.5), (6, 17.0), (94, 17.0)]:
        ax.plot([cx], [cy], marker="+", color=c_cyan, markersize=7.0, alpha=0.7, zorder=3)

    # Chapter Header
    ax.text(6.5, 118.8, "CHAPTER III • ANALYTICAL CONTINUUM ELASTODYNAMICS",
            color=c_gold_glow, fontsize=9.2, weight="heavy", ha="left", zorder=4)
    ax.text(6.5, 114.8, "1D Beam & 2D Plate Formulations of PZT Transducers",
            color=c_white, fontsize=14.5, weight="black", ha="left", zorder=4)
    ax.text(6.5, 111.8, "Closed-form electromechanical admittance models derived from dynamic stress-strain tensors.",
            color=c_muted, fontsize=9.2, weight="medium", ha="left", zorder=4)

    # ------------------------------------------------------------------
    # SECTION A: Technical Drawings (1D Beam & 2D Plate)
    # ------------------------------------------------------------------
    card_drawings = FancyBboxPatch((6, 75.0), 88, 34.5, boxstyle="round,pad=0.3,rounding_size=0.8",
                                   facecolor=c_subcard, edgecolor="#254778", lw=1.2, zorder=3)
    ax.add_patch(card_drawings)

    ax.text(8.5, 106.0, "SCHEMATICS: 1D UNIAXIAL BEAM & 2D BIAXIAL PLATE KINEMATICS",
            color=c_cyan, fontsize=9.8, weight="bold", ha="left", zorder=4)

    # Legend
    ax.add_patch(patches.Rectangle((60, 105.2), 2.8, 1.6, facecolor=c_pzt, edgecolor="#ffffff", lw=0.6, zorder=4))
    ax.text(63.5, 105.8, "PZT-5H", color=c_white, fontsize=8.2, weight="bold", zorder=4)
    ax.add_patch(patches.Rectangle((74, 105.2), 2.8, 1.6, facecolor=c_bond, edgecolor="#ffffff", lw=0.6, zorder=4))
    ax.text(77.5, 105.8, "Bond (tb)", color=c_white, fontsize=8.2, weight="bold", zorder=4)
    ax.add_patch(patches.Rectangle((88, 105.2), 2.8, 1.6, facecolor=c_beam, edgecolor="#ffffff", lw=0.6, zorder=4))
    ax.text(91.5, 105.8, "Substrate", color=c_white, fontsize=8.2, weight="bold", zorder=4)

    # 1D Beam Schematic
    ax.add_patch(patches.Rectangle((8.5, 77.0), 41.0, 26.5, facecolor="#07152b", edgecolor=c_border, lw=1.0, zorder=4))
    ax.text(29.0, 100.5, "1D Slender Beam (Liang et al.)", color=c_gold_glow, fontsize=9.0, weight="bold", ha="center", zorder=5)

    ax.add_patch(patches.Rectangle((10.5, 82.5), 2.2, 13.0, facecolor="#334155", edgecolor="#64748b", lw=1.0, zorder=5))
    ax.add_patch(patches.Rectangle((12.7, 86.0), 34.0, 5.5, facecolor=c_beam, edgecolor="#94a3b8", lw=0.9, zorder=5))
    ax.add_patch(patches.Rectangle((24.0, 91.5), 11.0, 1.0, facecolor=c_bond, edgecolor="#ffffff", lw=0.5, zorder=6))
    ax.add_patch(patches.Rectangle((24.0, 92.5), 11.0, 3.0, facecolor=c_pzt, edgecolor="#ffffff", lw=0.8, zorder=6))
    ax.annotate("", xy=(21.5, 94.0), xytext=(24.0, 94.0), arrowprops=dict(arrowstyle="<-", color=c_cyan, lw=1.3), zorder=7)
    ax.annotate("", xy=(37.5, 94.0), xytext=(35.0, 94.0), arrowprops=dict(arrowstyle="->", color=c_cyan, lw=1.3), zorder=7)
    ax.text(29.5, 96.8, "u(x) ↔ Dynamic Normal Stress T₁", color=c_cyan, fontsize=8.2, weight="bold", ha="center", zorder=7)
    ax.text(29.0, 78.5, "Uniaxial Boundary: T₂ = T₃ = 0 (Free Transverse Strain)", color=c_muted, fontsize=8.0, weight="semibold", ha="center", zorder=5)

    # 2D Plate Schematic
    ax.add_patch(patches.Rectangle((51.5, 77.0), 41.0, 26.5, facecolor="#07152b", edgecolor=c_border, lw=1.0, zorder=4))
    ax.text(72.0, 100.5, "2D Biaxial Plate (Bhalla & Soh)", color=c_gold_glow, fontsize=9.0, weight="bold", ha="center", zorder=5)

    plate_poly = patches.Polygon([[55.0, 82.5], [81.0, 82.5], [88.5, 93.0], [62.5, 93.0]],
                                 facecolor=c_beam, edgecolor="#94a3b8", lw=1.0, zorder=5)
    ax.add_patch(plate_poly)
    pzt_2d = patches.Polygon([[67.0, 86.0], [76.0, 86.0], [78.5, 90.5], [69.5, 90.5]],
                             facecolor=c_pzt, edgecolor="#ffffff", lw=0.8, zorder=6)
    ax.add_patch(pzt_2d)
    ax.annotate("", xy=(79.8, 88.2), xytext=(76.0, 88.2), arrowprops=dict(arrowstyle="->", color=c_cyan, lw=1.3), zorder=7)
    ax.annotate("", xy=(72.5, 92.8), xytext=(72.5, 90.5), arrowprops=dict(arrowstyle="->", color=c_cyan, lw=1.3), zorder=7)
    ax.text(72.0, 95.8, "Biaxial Dynamic Strain: S₁, S₂ (ν Coupling)", color=c_cyan, fontsize=8.2, weight="bold", ha="center", zorder=7)
    ax.text(72.0, 78.5, "Plane Stress: T₃ = 0 (Impedances: Z_s,xx, Z_s,yy)", color=c_muted, fontsize=8.0, weight="semibold", ha="center", zorder=5)

    # ------------------------------------------------------------------
    # SECTION B: Rigorous Closed-Form Mathematical Formulations (Large Print)
    # ------------------------------------------------------------------
    card_math_container = FancyBboxPatch((6, 23.5), 88, 49.5, boxstyle="round,pad=0.3,rounding_size=0.8",
                                         facecolor=c_subcard, edgecolor=c_border, lw=1.2, zorder=3)
    ax.add_patch(card_math_container)

    ax.text(8.5, 70.0, "EXACT CLOSED-FORM ELECTROMECHANICAL ADMITTANCE FORMULATIONS",
            color=c_gold_glow, fontsize=10.2, weight="heavy", ha="left", zorder=4)

    # CARD 1: 1D Liang Formulation
    ax.add_patch(FancyBboxPatch((7.5, 47.5), 85, 20.5, boxstyle="round,pad=0.2,rounding_size=0.5",
                                facecolor="#081427", edgecolor="#204575", lw=1.0, zorder=4))
    ax.text(9.5, 64.8, "1. 1D Liang et al. Formulation (Uniaxial Slender Beam):",
            color=c_cyan, fontsize=9.8, weight="bold", zorder=5)
    
    # 1D Equation (11.8 pt)
    ax.text(9.5, 59.2, r"$\overline{Y}_{1\mathrm{D}}(\omega) = j\omega \frac{2wl}{h} \left[ \overline{\varepsilon}_{33}^T - d_{31}^2 \overline{Y}_{11}^E + d_{31}^2 \overline{Y}_{11}^E \left( \frac{Z_{a,1\mathrm{D}}}{Z_{s,1\mathrm{D}} + Z_{a,1\mathrm{D}}} \right) \frac{\tan(\kappa l)}{\kappa l} \right]$",
            color=c_white, fontsize=11.8, zorder=5)
    
    ax.text(9.5, 54.8, r"• Uniaxial Wavenumber: $\kappa = \omega \sqrt{\rho / \overline{Y}_{11}^E}$. Boundary Stress Assumption: $T_2 = T_3 = 0$.",
            color=c_muted, fontsize=9.6, weight="medium", zorder=5)
    ax.text(9.5, 51.6, r"• Actuator Mechanical Impedance: $Z_{a,1\mathrm{D}} = \frac{wh \overline{Y}_{11}^E \kappa}{j\omega \tan(\kappa l)}$, with $Z_{s,1\mathrm{D}}$ as structural impedance.",
            color=c_muted, fontsize=9.6, weight="medium", zorder=5)
    ax.text(9.5, 48.6, "• Physical Scope: Valid for slender rods and beams with negligible lateral Poisson constraint.",
            color=c_muted, fontsize=9.4, style="italic", zorder=5)

    # CARD 2: 2D Bhalla-Soh Formulation
    ax.add_patch(FancyBboxPatch((7.5, 25.0), 85, 20.8, boxstyle="round,pad=0.2,rounding_size=0.5",
                                facecolor="#081427", edgecolor="#204575", lw=1.0, zorder=4))
    ax.text(9.5, 42.6, "2. 2D Bhalla-Soh Dual-Axis Formulation (Biaxially Coupled Plate):",
            color=c_cyan, fontsize=9.8, weight="bold", zorder=5)
    
    # 2D Equation (11.2 pt)
    ax.text(9.5, 37.0, r"$\overline{Y}_{2\mathrm{D}}(\omega) = j\omega \frac{4lw}{h} \left[ \overline{\varepsilon}_{33}^T - \frac{2d_{31}^2 \overline{Y}^E}{1-\nu} + \frac{d_{31}^2 \overline{Y}^E}{1-\nu} \left\{ \left( \frac{\overline{Z}_{a,xx}}{\overline{Z}_{s,xx} + \overline{Z}_{a,xx}} \right) \frac{\tan(\kappa l)}{\kappa l} + \left( \frac{\overline{Z}_{a,yy}}{\overline{Z}_{s,yy} + \overline{Z}_{a,yy}} \right) \frac{\tan(\kappa w)}{\kappa w} \right\} \right]$",
            color=c_white, fontsize=11.2, zorder=5)
    
    ax.text(9.5, 32.5, r"• Biaxial Planar Wavenumber: $\kappa = \omega \sqrt{\frac{\rho(1 - \nu^2)}{\overline{Y}^E}}$. Plane Stress Condition: $T_3 = 0$.",
            color=c_muted, fontsize=9.6, weight="medium", zorder=5)
    ax.text(9.5, 29.3, r"• Directional Impedances: $\overline{Z}_{a,xx} = \frac{2wh \overline{Y}^E \kappa}{j\omega (1 - \nu) \tan(\kappa l)}$ and $\overline{Z}_{a,yy} = \frac{2lh \overline{Y}^E \kappa}{j\omega (1 - \nu) \tan(\kappa w)}$.",
            color=c_muted, fontsize=9.6, weight="medium", zorder=5)
    ax.text(9.5, 26.3, "• Physical Scope: Fully resolves orthogonal plate reflections; omits normal stress waves through thickness.",
            color=c_muted, fontsize=9.4, style="italic", zorder=5)

    # ------------------------------------------------------------------
    # TRANSITION PILL: Perfectly contained within inner margins (x = 10 to 90)
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((10.0, 15.5), 80.0, 6.4, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#08152b", edgecolor="#b45309", lw=0.9, zorder=3))
    
    ax.text(50.0, 20.3, "The Complete 3D Directional Sum Continuum Model (Annamdas & Soh),",
            color=c_gold_glow, fontsize=8.4, weight="bold", style="italic", ha="center", zorder=4)
    ax.text(50.0, 18.5, "High-Frequency Thickness Dilatation Proof (600–900 kHz),",
            color=c_gold_glow, fontsize=8.4, weight="bold", style="italic", ha="center", zorder=4)
    ax.text(50.0, 16.7, "and Interfacial Viscoelastic Shear-Lag Mechanics continue on Page 4.",
            color=c_gold_glow, fontsize=8.4, weight="bold", style="italic", ha="center", zorder=4)

    # ------------------------------------------------------------------
    # 5. Bottom Running Footer Bar with "Page 3"[cite: 5]
    # ------------------------------------------------------------------
    footer_box = FancyBboxPatch((4, 1.2), 92, 9.6, boxstyle="round,pad=0.3,rounding_size=0.6",
                                facecolor=c_card_bg, edgecolor=c_border, linewidth=1.1, zorder=2)
    ax.add_patch(footer_box)

    ax.text(7, 8.2, "GARRF Technical Magazine 1 • Monograph Series • Archive Ref: GARRF-MAG1-SINGBHA-2026.P03",
            color=c_muted, fontsize=8.0, weight="medium", zorder=4)
    ax.text(7, 5.7, "Official Portal: https://garrf.in  •  LinkedIn: https://www.linkedin.com/company/gopalkrishnaadvancedruralresearchfoundation/",
            color=c_cyan, fontsize=7.6, weight="semibold", zorder=4)
    ax.text(7, 3.0, "Dedicated in Honour of Singapore and Bharat",
            color=c_white, fontsize=8.6, weight="bold", ha="left", zorder=4)
    ax.text(93, 3.0, "Page 3",
            color=c_gold_glow, fontsize=9.5, weight="black", ha="right", zorder=4)

    output_filename = "SingBha_Magazine_Page_3_PerfectLayout.png"
    plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
    plt.close()

    display(IPImage(filename=output_filename, width=720))
    print(f"Generated successfully: {output_filename} (A4 300 DPI Perfect Layout Page 3 Ready)")
    files.download(output_filename)

if __name__ == "__main__":
    generate_magazine_page_3_perfect_layout()
