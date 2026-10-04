import io
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
from PIL import Image
from IPython.display import display, Image as IPImage
from google.colab import files

def generate_magazine_page_9_pillars_part1():
    # ------------------------------------------------------------------
    # 1. Page Geometry: International A4 at 300 DPI (8.27 x 11.69 in)[cite: 4]
    # ------------------------------------------------------------------
    fig = plt.figure(figsize=(8.27, 11.69), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 141.4)
    ax.axis('off')

    # Color Palette conforming to GARRF Monograph Identity[cite: 4]
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

    # Monograph Section Banner (Decoupled from fixed page count)[cite: 24]
    ax.text(6.5, 118.8, "SECTION 8 • SCIENTIFIC PILLARS OF SingBha-EMCD (PART I)",
            color=c_gold_glow, fontsize=9.2, weight="heavy", ha="left", zorder=4)
    ax.text(6.5, 114.8, "The Six Scientific Pillars of SingBha-EMCD (Pillars 1 to 3)",
            color=c_white, fontsize=14.0, weight="black", ha="left", zorder=4)
    ax.text(6.5, 111.8, "Physical mechanisms overcoming scalar dilution, defect angle blindness & diurnal thermal drift.",
            color=c_muted, fontsize=8.8, weight="medium", ha="left", zorder=4)

    # ------------------------------------------------------------------
    # 3-COLUMN PILLAR CARDS (Pillar 1, Pillar 2, Pillar 3)[cite: 24]
    # ------------------------------------------------------------------
    col_w, col_h = 27.8, 88.5
    y_card = 21.0

    # ------------------------------------------------------------------
    # PILLAR 1: Spatial Gradient (grad D3) vs. Bulk Dilution[cite: 24]
    # ------------------------------------------------------------------
    x_c1 = 6.5
    card_p1 = FancyBboxPatch((x_c1, y_card), col_w, col_h, boxstyle="round,pad=0.3,rounding_size=0.6",
                             facecolor=c_subcard, edgecolor="#254778", lw=1.1, zorder=3)
    ax.add_patch(card_p1)

    ax.text(x_c1 + col_w/2, y_card + col_h - 4.5, "PILLAR 1", color=c_gold_glow, fontsize=8.5, weight="heavy", ha="center", zorder=4)
    ax.text(x_c1 + col_w/2, y_card + col_h - 7.8, r"Spatial Gradient ($\nabla D_3$)", color=c_white, fontsize=9.5, weight="black", ha="center", zorder=4)
    ax.text(x_c1 + col_w/2, y_card + col_h - 10.5, "vs. Bulk Terminal Dilution", color=c_cyan, fontsize=7.8, weight="bold", ha="center", zorder=4)

    # Schematic Vector: Segmented Electrode Virtual Ground[cite: 24]
    ax.add_patch(FancyBboxPatch((x_c1 + 1.5, y_card + col_h - 32.0), col_w - 3.0, 19.5, boxstyle="round,pad=0.1,rounding_size=0.3",
                                facecolor="#081427", edgecolor="#204575", lw=0.8, zorder=4))
    
    ax.add_patch(patches.Rectangle((x_c1 + 3.2, y_card + col_h - 22.0), 9.5, 7.5, facecolor="#0284c7", edgecolor="#ffffff", lw=0.6, zorder=5))
    ax.text(x_c1 + 7.9, y_card + col_h - 18.2, "Pad A\n($Q_A$)", color="#ffffff", fontsize=6.8, weight="bold", ha="center", va="center", zorder=6)

    ax.add_patch(patches.Rectangle((x_c1 + 15.0, y_card + col_h - 22.0), 9.5, 7.5, facecolor="#b45309", edgecolor="#ffffff", lw=0.6, zorder=5))
    ax.text(x_c1 + 19.7, y_card + col_h - 18.2, "Pad B\n($Q_B$)", color="#ffffff", fontsize=6.8, weight="bold", ha="center", va="center", zorder=6)

    ax.plot([x_c1 + 13.85, x_c1 + 13.85], [y_card + col_h - 23.5, y_card + col_h - 28.5], color=c_crimson, lw=1.8, zorder=6)
    ax.text(x_c1 + 13.85, y_card + col_h - 30.2, "Crack Singularity", color=c_crimson, fontsize=6.2, weight="bold", ha="center", zorder=6)

    # Formula Box: Differential Charge Gradient[cite: 24]
    ax.add_patch(FancyBboxPatch((x_c1 + 1.5, y_card + col_h - 45.0), col_w - 3.0, 11.2, boxstyle="round,pad=0.1,rounding_size=0.3",
                                facecolor="#050d1a", edgecolor="#b45309", lw=0.8, zorder=4))
    ax.text(x_c1 + col_w/2, y_card + col_h - 36.5, "DIFFERENTIAL CHARGE GRADIENT", color=c_gold_glow, fontsize=6.2, weight="bold", ha="center", zorder=5)
    ax.text(x_c1 + col_w/2, y_card + col_h - 41.0, r"$\Delta Q = Q_A - Q_B$", color=c_white, fontsize=8.2, weight="bold", ha="center", zorder=5)
    ax.text(x_c1 + col_w/2, y_card + col_h - 43.5, r"$= \iint_A D_3\,dA - \iint_B D_3\,dA$", color=c_cyan, fontsize=7.2, ha="center", zorder=5)

    p1_lines = [
        "Conventional EMI averages localized",
        "stress release across the entire crystal",
        "electrode capacitance (<0.5% shift).",
        "",
        "SingBha-EMCD measures differential",
        "charge across segmented electrode",
        "pads held strictly at virtual ground.",
        "",
        "Localized stress collapse directly",
        "above an incipient crack induces a",
        "sharp 300% to 500% differential spike",
        "(>24 dB SNR gain), catching micro-",
        "cracks at inception before failure."
    ]
    for i, line in enumerate(p1_lines):
        ax.text(x_c1 + 2.2, y_card + 39.0 - i * 3.0, line, color=c_white if "300% to 500%" in line else c_muted,
                fontsize=6.8, weight="bold" if "300% to 500%" in line else "normal", zorder=5)

    # ------------------------------------------------------------------
    # PILLAR 2: Directional Crack Trajectory Resolution[cite: 24]
    # ------------------------------------------------------------------
    x_c2 = 36.1
    card_p2 = FancyBboxPatch((x_c2, y_card), col_w, col_h, boxstyle="round,pad=0.3,rounding_size=0.6",
                             facecolor=c_subcard, edgecolor="#254778", lw=1.1, zorder=3)
    ax.add_patch(card_p2)

    ax.text(x_c2 + col_w/2, y_card + col_h - 4.5, "PILLAR 2", color=c_gold_glow, fontsize=8.5, weight="heavy", ha="center", zorder=4)
    ax.text(x_c2 + col_w/2, y_card + col_h - 7.8, "Directional Crack Trajectory", color=c_white, fontsize=9.2, weight="black", ha="center", zorder=4)
    ax.text(x_c2 + col_w/2, y_card + col_h - 10.5, "Orthogonal Stress Decoupling", color=c_cyan, fontsize=7.8, weight="bold", ha="center", zorder=4)

    # Schematic Vector: Directional Tensor Decoupling[cite: 24]
    ax.add_patch(FancyBboxPatch((x_c2 + 1.5, y_card + col_h - 32.0), col_w - 3.0, 19.5, boxstyle="round,pad=0.1,rounding_size=0.3",
                                facecolor="#081427", edgecolor="#204575", lw=0.8, zorder=4))
    
    ax.annotate("", xy=(x_c2 + 22.0, y_card + col_h - 22.0), xytext=(x_c2 + 6.0, y_card + col_h - 22.0),
                arrowprops=dict(arrowstyle="->", color=c_cyan, lw=1.4), zorder=5)
    ax.text(x_c2 + 23.5, y_card + col_h - 22.4, r"$x\ (d_{31})$", color=c_cyan, fontsize=6.8, weight="bold", zorder=6)

    ax.annotate("", xy=(x_c2 + 14.0, y_card + col_h - 14.0), xytext=(x_c2 + 14.0, y_card + col_h - 30.0),
                arrowprops=dict(arrowstyle="->", color=c_gold_glow, lw=1.4), zorder=5)
    ax.text(x_c2 + 14.0, y_card + col_h - 12.8, r"$y\ (d_{32})$", color=c_gold_glow, fontsize=6.8, weight="bold", ha="center", zorder=6)

    ax.plot([x_c2 + 9.0, x_c2 + 19.0], [y_card + col_h - 27.0, y_card + col_h - 17.0], color=c_emerald, lw=1.8, linestyle="--", zorder=6)
    ax.text(x_c2 + 18.0, y_card + col_h - 27.0, r"$\theta_{\mathrm{flaw}}$", color=c_emerald, fontsize=7.2, weight="bold", zorder=6)

    # Formula Box: Directional Vector Field[cite: 24]
    ax.add_patch(FancyBboxPatch((x_c2 + 1.5, y_card + col_h - 45.0), col_w - 3.0, 11.2, boxstyle="round,pad=0.1,rounding_size=0.3",
                                facecolor="#050d1a", edgecolor="#b45309", lw=0.8, zorder=4))
    ax.text(x_c2 + col_w/2, y_card + col_h - 36.5, "DIRECTIONAL VECTOR FIELD", color=c_gold_glow, fontsize=6.2, weight="bold", ha="center", zorder=5)
    ax.text(x_c2 + col_w/2, y_card + col_h - 41.0, r"$\nabla D_3 = d_{31}\frac{\partial T_1}{\partial x}\hat{i} + d_{32}\frac{\partial T_2}{\partial y}\hat{j}$",
            color=c_white, fontsize=7.6, weight="bold", ha="center", zorder=5)
    ax.text(x_c2 + col_w/2, y_card + col_h - 43.5, r"$\theta = \arctan\left(\frac{\partial D_3 / \partial y}{\partial D_3 / \partial x}\right)$",
            color=c_cyan, fontsize=7.0, ha="center", zorder=5)

    p2_lines = [
        "Because d31 and d32 couple independently",
        "along orthogonal structural axes,",
        "directional derivatives resolve flaw paths.",
        "",
        "Scalar admittance collapses all strain",
        "fields into an ambiguous 1D scalar curve.",
        "",
        "Longitudinal fatigue cracks trigger",
        "sharp gradient peaks in ∂D3/∂x while",
        "producing zero shift in ∂D3/∂y.",
        "",
        "This resolves the exact crack trajectory",
        "relative to principal structural load axes,",
        "differentiating web vs. flange fractures."
    ]
    for i, line in enumerate(p2_lines):
        ax.text(x_c2 + 2.2, y_card + 39.0 - i * 3.0, line, color=c_white if "∂D3/∂x" in line else c_muted,
                fontsize=6.8, weight="bold" if "∂D3/∂x" in line else "normal", zorder=5)

    # ------------------------------------------------------------------
    # PILLAR 3: Inherent Hardware Thermal Drift Immunity[cite: 24]
    # ------------------------------------------------------------------
    x_c3 = 65.7
    card_p3 = FancyBboxPatch((x_c3, y_card), col_w, col_h, boxstyle="round,pad=0.3,rounding_size=0.6",
                             facecolor=c_subcard, edgecolor="#254778", lw=1.1, zorder=3)
    ax.add_patch(card_p3)

    ax.text(x_c3 + col_w/2, y_card + col_h - 4.5, "PILLAR 3", color=c_gold_glow, fontsize=8.5, weight="heavy", ha="center", zorder=4)
    ax.text(x_c3 + col_w/2, y_card + col_h - 7.8, "Hardware Thermal Drift Immunity", color=c_white, fontsize=9.0, weight="black", ha="center", zorder=4)
    ax.text(x_c3 + col_w/2, y_card + col_h - 10.5, "Uniform Spatial Cancellation", color=c_cyan, fontsize=7.8, weight="bold", ha="center", zorder=4)

    # Schematic Vector: Uniform Temperature Profile[cite: 24]
    ax.add_patch(FancyBboxPatch((x_c3 + 1.5, y_card + col_h - 32.0), col_w - 3.0, 19.5, boxstyle="round,pad=0.1,rounding_size=0.3",
                                facecolor="#081427", edgecolor="#204575", lw=0.8, zorder=4))
    
    for h_idx in range(5):
        hy = y_card + col_h - 29.5 + h_idx * 3.2
        ax.plot([x_c3 + 4.0, x_c3 + col_w - 4.0], [hy, hy], color="#f97316", lw=1.0, linestyle=":", alpha=0.8, zorder=5)
    
    ax.text(x_c3 + col_w/2, y_card + col_h - 16.5, r"Diurnal Swing: $\Delta T = 20^\circ\mathrm{C} - 45^\circ\mathrm{C}$",
            color=c_gold_glow, fontsize=6.8, weight="bold", ha="center", zorder=6)
    ax.text(x_c3 + col_w/2, y_card + col_h - 20.0, r"$\Delta\varepsilon_{33}^T(T) = \mathrm{Uniform\ Across\ Patch}$",
            color="#ffffff", fontsize=6.6, ha="center", zorder=6)
    ax.text(x_c3 + col_w/2, y_card + col_h - 24.5, r"Spatial Differential $\equiv 0$",
            color=c_emerald, fontsize=8.0, weight="heavy", ha="center", zorder=6)

    # Formula Box: Hardware Cancellation Proof[cite: 24]
    ax.add_patch(FancyBboxPatch((x_c3 + 1.5, y_card + col_h - 45.0), col_w - 3.0, 11.2, boxstyle="round,pad=0.1,rounding_size=0.3",
                                facecolor="#050d1a", edgecolor="#b45309", lw=0.8, zorder=4))
    ax.text(x_c3 + col_w/2, y_card + col_h - 36.5, "HARDWARE CANCELLATION PROOF", color=c_gold_glow, fontsize=6.2, weight="bold", ha="center", zorder=5)
    ax.text(x_c3 + col_w/2, y_card + col_h - 41.0, r"$\frac{\partial \varepsilon_{33}^T}{\partial x} \equiv 0, \quad \frac{\partial \varepsilon_{33}^T}{\partial y} \equiv 0$",
            color=c_white, fontsize=7.8, weight="bold", ha="center", zorder=5)
    ax.text(x_c3 + col_w/2, y_card + col_h - 43.5, r"$\Delta Q_{\mathrm{thermal}} = Q_A(T) - Q_B(T) = 0$",
            color=c_emerald, fontsize=7.0, weight="bold", ha="center", zorder=5)

    p3_lines = [
        "Diurnal ambient swings (15°C to 45°C)",
        "alter dielectric permittivity ε33^T(T),",
        "causing massive baseline drift in EMI.",
        "",
        "Thermal shifts in classical impedance",
        "are 10x to 50x larger than crack signals,",
        "triggering chronic outdoor false alarms.",
        "",
        "Because thermal expansion is spatially",
        "uniform across the small wafer,",
        "hardware subtraction on segmented pads",
        "cancels temperature drift identically.",
        "",
        "Zero baseline software filtering required."
    ]
    for i, line in enumerate(p3_lines):
        ax.text(x_c3 + 2.2, y_card + 39.0 - i * 3.0, line, color=c_emerald if "Zero baseline" in line else c_muted,
                fontsize=6.8, weight="bold" if "Zero baseline" in line else "normal", zorder=5)

    # ------------------------------------------------------------------
    # TRANSITION BADGE: Monograph Transition Pill -> Page 10[cite: 26]
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((10.0, 15.2), 80.0, 3.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#08152b", edgecolor="#b45309", lw=0.9, zorder=3))
    ax.text(50.0, 16.9, "SCIENTIFIC PILLARS 4 TO 6 (3D ANISOTROPY, DUAL-HORIZON & VIRTUAL GROUND) CONTINUE ON PAGE 10.",
            color=c_gold_glow, fontsize=7.4, weight="bold", style="italic", ha="center", zorder=4)

    # ------------------------------------------------------------------
    # 5. Bottom Running Footer Bar (Normalized to "Page 9")[cite: 4]
    # ------------------------------------------------------------------
    footer_box = FancyBboxPatch((4, 1.2), 92, 9.6, boxstyle="round,pad=0.3,rounding_size=0.6",
                                facecolor=c_card_bg, edgecolor=c_border, linewidth=1.1, zorder=2)
    ax.add_patch(footer_box)

    ax.text(7, 8.2, "GARRF Technical Magazine 1 • Monograph Series • Archive Ref: GARRF-MAG1-SINGBHA-2026.P09",
            color=c_muted, fontsize=8.0, weight="medium", zorder=4)
    ax.text(7, 5.7, "Official Portal: https://garrf.in  •  LinkedIn: https://www.linkedin.com/company/gopalkrishnaadvancedruralresearchfoundation/",
            color=c_cyan, fontsize=7.6, weight="semibold", zorder=4)
    ax.text(7, 3.0, "Dedicated in Honour of Singapore and Bharat",
            color=c_white, fontsize=8.6, weight="bold", ha="left", zorder=4)
    ax.text(93, 3.0, "Page 9",
            color=c_gold_glow, fontsize=9.5, weight="black", ha="right", zorder=4)

    output_filename = "SingBha_Magazine_Page_9_Pillars_Part1.png"
    plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
    plt.close()

    display(IPImage(filename=output_filename, width=720))
    print(f"Generated successfully: {output_filename} (A4 300 DPI Page 9 Ready - Normalized Pagination)")
    files.download(output_filename)

if __name__ == "__main__":
    generate_magazine_page_9_pillars_part1()
