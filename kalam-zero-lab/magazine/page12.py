import io
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
from PIL import Image
from IPython.display import display, Image as IPImage
from google.colab import files

def generate_magazine_page_12_fracture_singularity():
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

    # Monograph Section 10 Banner[cite: 26]
    ax.text(6.5, 118.8, "SECTION 10 • FRACTURE MECHANICS FORMULATION & SINGULARITIES",
            color=c_gold_glow, fontsize=9.2, weight="heavy", ha="left", zorder=4)
    ax.text(6.5, 114.8, "Surface Micro-Crack Mechanics & Gradient Singularities",
            color=c_white, fontsize=14.0, weight="black", ha="left", zorder=4)
    ax.text(6.5, 111.8, "Traction-free boundary conditions, dynamic stress collapse & mathematical divergence of ∇D3.",
            color=c_muted, fontsize=8.8, weight="medium", ha="left", zorder=4)

    # ------------------------------------------------------------------
    # CARD 1: TRACTION-FREE CRACK BOUNDARIES & STRESS COLLAPSE (Top Half: y=69.0 to 110.0)
    # ------------------------------------------------------------------
    card_tf = FancyBboxPatch((6, 69.0), 88, 41.0, boxstyle="round,pad=0.3,rounding_size=0.6",
                             facecolor=c_subcard, edgecolor="#254778", lw=1.1, zorder=3)
    ax.add_patch(card_tf)

    ax.text(8.5, 106.8, "1. TRACTION-FREE BOUNDARY CONDITIONS & LOCALIZED DYNAMIC STRESS COLLAPSE",
            color=c_gold_glow, fontsize=9.2, weight="heavy", ha="left", zorder=4)

    # Left: Analytical Mechanics & Formula Box (Inner y: 70.5 to 104.5)
    ax.add_patch(FancyBboxPatch((7.5, 70.5), 41.5, 34.0, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(9.0, 101.8, "Traction-Free Crack Face Condition:", color=c_cyan, fontsize=8.0, weight="bold", zorder=5)
    
    # Equation 1: Valid Matplotlib mathtext[cite: 26]
    ax.text(9.0, 97.5, r"$\sigma_{nn}(x_c, y) = 0,\ \tau_{nt}(x_c, y) = 0 \Rightarrow Z_s(x_c) \rightarrow 0$",
            color=c_white, fontsize=7.8, weight="bold", zorder=5)

    # Equation 2: Dynamic Stress Drop[cite: 26]
    ax.text(9.0, 93.2, r"$T_1(x_c^+) - T_1(x_c^-) = -Y_{11}^E d_{31} E_3$",
            color=c_gold_glow, fontsize=8.0, weight="bold", zorder=5)

    # Compact description strictly terminating at y = 72.0 (Leaves 1.5 units padding above inner box bottom)
    tf_desc = [
        "• Incipient Defect Initiation: At flaw coordinate x = x_c,",
        "  structural impedance vanishes across traction-free faces.",
        "• Abrupt Stress Discontinuity: Dynamic stress T1(x)",
        "  collapses instantaneously across the crack interface.",
        "• Classical Failure: Conventional EMI averages this drop",
        "  over full crystal area, losing localized damage (<0.5%)."
    ]
    for i, line in enumerate(tf_desc):
        ax.text(9.0, 88.5 - i * 2.7, line,
                color=c_white if "T1(x)" in line or "Incipient" in line else c_muted,
                fontsize=6.5, weight="bold" if "•" in line else "normal", zorder=5)

    # Right: Vector Schematic of Stress Collapse across Crack (Inner y: 70.5 to 104.5)
    ax.add_patch(FancyBboxPatch((50.5, 70.5), 42.0, 34.0, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(71.5, 101.8, "Stress Distribution T₁(x) Across Crack Mouth", color=c_cyan, fontsize=8.0, weight="bold", ha="center", zorder=5)

    t_px, t_py, t_pw, t_ph = 55.0, 75.5, 33.0, 21.0
    ax.plot([t_px, t_px + t_pw], [t_py + 4.0, t_py + 4.0], color="#64748b", lw=0.8, zorder=5)
    ax.plot([t_px + t_pw/2, t_px + t_pw/2], [t_py, t_py + t_ph], color="#ef4444", lw=1.2, linestyle=":", zorder=5)
    ax.text(t_px + t_pw/2, t_py - 2.2, r"Crack Location $x = x_c$", color=c_crimson, fontsize=6.6, weight="bold", ha="center", zorder=6)

    xs_l = np.linspace(0, 0.48, 50)
    xs_r = np.linspace(0.52, 1.0, 50)
    stress_l = 13.0 * np.cos(np.pi * xs_l * 0.8)
    stress_r = 13.0 * np.cos(np.pi * (1.0 - xs_r) * 0.8)

    ax.plot(t_px + xs_l * t_pw, t_py + 4.0 + stress_l, color=c_cyan, lw=1.5, zorder=6)
    ax.plot(t_px + xs_r * t_pw, t_py + 4.0 + stress_r, color=c_cyan, lw=1.5, zorder=6)
    
    ax.annotate("", xy=(t_px + t_pw/2, t_py + 4.0), xytext=(t_px + t_pw/2, t_py + 4.0 + 12.5),
                arrowprops=dict(arrowstyle="<->", color=c_gold_glow, lw=1.3), zorder=7)
    ax.text(t_px + t_pw/2 + 2.0, t_py + 10.5, r"$\Delta T_1$ Collapse", color=c_gold_glow, fontsize=6.6, weight="bold", zorder=8)
    ax.text(t_px + 2.0, t_py + t_ph - 2.5, "Traction Stress Field T₁(x)", color="#ffffff", fontsize=6.2, zorder=6)

    # ------------------------------------------------------------------
    # CARD 2: SPATIAL GRADIENT SINGULARITY DIVERGENCE (Bottom Half: y=21.0 to 66.5)
    # Complete 2.5 units vertical buffer between Card 1 and Card 2
    # ------------------------------------------------------------------
    card_sing = FancyBboxPatch((6, 21.0), 88, 45.5, boxstyle="round,pad=0.3,rounding_size=0.6",
                              facecolor=c_subcard, edgecolor="#254778", lw=1.1, zorder=3)
    ax.add_patch(card_sing)

    ax.text(8.5, 63.8, "2. SPATIAL GRADIENT SINGULARITY DIVERGENCE & SNR ENHANCEMENT (>24 dB)",
            color=c_gold_glow, fontsize=9.2, weight="heavy", ha="left", zorder=4)

    # Left: Gradient Divergence Vector Plot (Inner y: 22.8 to 60.5)
    ax.add_patch(FancyBboxPatch((7.5, 22.8), 41.5, 37.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(28.2, 57.5, "Singularity Divergence: |∇D₃| at Crack Mouth", color=c_gold_glow, fontsize=8.0, weight="bold", ha="center", zorder=5)

    g_px, g_py, g_pw, g_ph = 12.0, 27.5, 33.0, 26.0
    ax.plot([g_px, g_px + g_pw], [g_py, g_py], color="#64748b", lw=0.8, zorder=5)
    ax.plot([g_px, g_px], [g_py, g_py + g_ph], color="#64748b", lw=0.8, zorder=5)
    ax.text(g_px + g_pw/2, g_py - 2.5, r"Transducer Coordinate $x$ across Patch", color=c_muted, fontsize=6.6, ha="center", zorder=5)
    ax.text(g_px - 2.5, g_py + g_ph/2, r"Gradient $|\nabla D_3|$", color=c_muted, fontsize=6.6, va="center", rotation=90, zorder=5)

    gx_arr = np.linspace(-1, 1, 150)
    sing_spike = 1.2 + 22.0 / (1.0 + (gx_arr / 0.04)**2)
    ax.plot(g_px + (gx_arr + 1)/2 * g_pw, g_py + (sing_spike / 25.0) * g_ph, color=c_emerald, lw=1.8, zorder=6)

    ax.plot([g_px, g_px + g_pw], [g_py + 1.8, g_py + 1.8], color="#ef4444", lw=1.2, linestyle="--", zorder=6)
    ax.text(g_px + 3.0, g_py + 3.2, "Conventional EMI (Diluted <0.5%)", color="#ef4444", fontsize=5.8, weight="bold", zorder=7)

    ax.annotate("Mathematical Singularity\nSpike (>500% Amplitude)", xy=(g_px + g_pw/2, g_py + g_ph - 2.0),
                xytext=(g_px + g_pw/2 + 2.5, g_py + g_ph - 4.5),
                arrowprops=dict(arrowstyle="->", color=c_gold_glow, lw=1.0),
                fontsize=6.0, color=c_gold_glow, weight="bold", zorder=7)

    # Right: Formula Box & Diagnostic Impact List (Inner y: 22.8 to 60.5)
    ax.add_patch(FancyBboxPatch((50.5, 22.8), 42.0, 37.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(71.5, 57.5, "Closed-Form Mathematical Divergence", color=c_cyan, fontsize=8.0, weight="bold", ha="center", zorder=5)

    # Formula Box
    ax.add_patch(FancyBboxPatch((52.0, 44.5), 39.0, 11.2, boxstyle="round,pad=0.1,rounding_size=0.3",
                                facecolor="#050d1a", edgecolor="#b45309", lw=0.8, zorder=5))
    ax.text(71.5, 53.0, "SPATIAL GRADIENT DIVERGENCE THEOREM", color=c_gold_glow, fontsize=6.2, weight="bold", ha="center", zorder=6)
    ax.text(71.5, 49.5, r"$\nabla D_3 = d_{31} \frac{\partial T_1}{\partial x} \hat{i} + d_{32} \frac{\partial T_2}{\partial y} \hat{j}$",
            color=c_white, fontsize=7.6, weight="bold", ha="center", zorder=6)
    ax.text(71.5, 46.5, r"$\lim_{x \rightarrow x_c} |\nabla D_3| \longrightarrow \infty$",
            color=c_emerald, fontsize=8.4, weight="heavy", ha="center", zorder=6)

    # Compact summary safely above bottom pill
    compact_desc = [
        ("• Singularity Detection:", "Differentiating D3 isolates the crack singularity directly.", c_white),
        ("• 24 dB SNR Gain:", "Amplifies micro-crack spikes >300-500% over scalar EMI.", c_emerald),
        ("• Incipient Sensitivity:", "Catches 50 μm fatigue cracks prior to macro-failure.", c_cyan),
        ("• Sub-mm Localization:", "Pinpoints defect coordinate x_c directly beneath wafer.", c_gold_glow),
    ]

    ax.text(52.5, 41.5, "Analytical Diagnostic Impact:", color=c_gold_glow, fontsize=7.0, weight="heavy", zorder=6)
    for i, (b_hdr, b_txt, b_col) in enumerate(compact_desc):
        y_pos = 38.0 - i * 3.8
        ax.text(52.5, y_pos, b_hdr, color=b_col, fontsize=6.5, weight="bold", zorder=6)
        ax.text(52.5, y_pos - 1.6, b_txt, color=c_muted, fontsize=6.2, zorder=6)

    # ------------------------------------------------------------------
    # TRANSITION BADGE: Monograph Transition Pill -> Page 13[cite: 27]
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((10.0, 15.2), 80.0, 3.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#08152b", edgecolor="#b45309", lw=0.9, zorder=3))
    ax.text(50.0, 16.9, "HYBRID WAVEFORM PROPAGATION DYNAMICS (GUIDED LAMB WAVES & TOF) CONTINUE ON PAGE 13.",
            color=c_gold_glow, fontsize=7.4, weight="bold", style="italic", ha="center", zorder=4)

    # ------------------------------------------------------------------
    # 5. Bottom Running Footer Bar (Normalized to "Page 12")[cite: 4]
    # ------------------------------------------------------------------
    footer_box = FancyBboxPatch((4, 1.2), 92, 9.6, boxstyle="round,pad=0.3,rounding_size=0.6",
                                facecolor=c_card_bg, edgecolor=c_border, linewidth=1.1, zorder=2)
    ax.add_patch(footer_box)

    ax.text(7, 8.2, "GARRF Technical Magazine 1 • Monograph Series • Archive Ref: GARRF-MAG1-SINGBHA-2026.P12",
            color=c_muted, fontsize=8.0, weight="medium", zorder=4)
    ax.text(7, 5.7, "Official Portal: https://garrf.in  •  LinkedIn: https://www.linkedin.com/company/gopalkrishnaadvancedruralresearchfoundation/",
            color=c_cyan, fontsize=7.6, weight="semibold", zorder=4)
    ax.text(7, 3.0, "Dedicated in Honour of Singapore and Bharat",
            color=c_white, fontsize=8.6, weight="bold", ha="left", zorder=4)
    ax.text(93, 3.0, "Page 12",
            color=c_gold_glow, fontsize=9.5, weight="black", ha="right", zorder=4)

    output_filename = "SingBha_Magazine_Page_12_Fracture_Singularity_Audited.png"
    plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
    plt.close()

    display(IPImage(filename=output_filename, width=720))
    print(f"Generated successfully: {output_filename} (A4 300 DPI Page 12 - Audited & Zero Overlap)")
    files.download(output_filename)

if __name__ == "__main__":
    generate_magazine_page_12_fracture_singularity()
