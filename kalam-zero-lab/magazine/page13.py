import io
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
from PIL import Image
from IPython.display import display, Image as IPImage
from google.colab import files

def generate_magazine_page_13_waveform_propagation():
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

    # Monograph Section 11 Banner[cite: 27]
    ax.text(6.5, 118.8, "SECTION 11 • WAVEFORM PROPAGATION DYNAMICS (WFP)",
            color=c_gold_glow, fontsize=9.2, weight="heavy", ha="left", zorder=4)
    ax.text(6.5, 114.8, "Spacious Structures: Hybrid Waveform Propagation",
            color=c_white, fontsize=14.0, weight="black", ha="left", zorder=4)
    ax.text(6.5, 111.8, "Guided Lamb waves, multi-mode dispersion (S0, A0) & dynamic surface charge capture q_dyn(t).",
            color=c_muted, fontsize=8.8, weight="medium", ha="left", zorder=4)

    # ------------------------------------------------------------------
    # CARD 1: GUIDED LAMB WAVE MODES & ACTUATION FORMULATION (y=69.0 to 110.0)
    # ------------------------------------------------------------------
    card_wfp = FancyBboxPatch((6, 69.0), 88, 41.0, boxstyle="round,pad=0.3,rounding_size=0.6",
                             facecolor=c_subcard, edgecolor="#254778", lw=1.1, zorder=3)
    ax.add_patch(card_wfp)

    ax.text(8.5, 106.8, "1. GUIDED LAMB WAVE MODAL DYNAMICS & TONE-BURST EXCITATION",
            color=c_gold_glow, fontsize=9.2, weight="heavy", ha="left", zorder=4)

    # Left: Equations & Modal Descriptions (Inner y: 70.5 to 104.5)
    ax.add_patch(FancyBboxPatch((7.5, 70.5), 41.5, 34.0, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(9.0, 101.8, "5-Cycle Hanning-Windowed Actuation:", color=c_cyan, fontsize=8.0, weight="bold", zorder=5)

    ax.text(9.0, 97.5, r"$V_{\mathrm{act}}(t) = 0.5\,V_0 \left[1 - \cos\left(\frac{\omega_c t}{5}\right)\right] \sin(\omega_c t)$",
            color=c_white, fontsize=7.6, weight="bold", zorder=5)
    ax.text(9.0, 93.8, r"Domain: $0 \leq t \leq 5T_c,$  $f_c = 20 - 100\ \mathrm{kHz}$",
            color=c_gold_glow, fontsize=7.0, weight="bold", zorder=5)

    mode_lines = [
        ("• Symmetric Mode (S0):", "Fast longitudinal packet; sensitive to mid-plane voids.", c_emerald),
        ("• Anti-Symmetric Mode (A0):", "Slower flexural wave; high out-of-plane amplitude.", c_cyan),
        ("• Low-Dispersion Tuning:", "Tuned below A1 cut-off for clean, coherent wave packets.", c_white)
    ]
    for i, (m_hdr, m_desc, m_col) in enumerate(mode_lines):
        y_pos = 89.0 - i * 5.0
        ax.text(9.0, y_pos, m_hdr, color=m_col, fontsize=6.8, weight="bold", zorder=5)
        ax.text(9.0, y_pos - 1.8, m_desc, color=c_muted, fontsize=6.2, zorder=5)

    # Right: Modal Dispersion & Waveform Vector Schematic (Inner y: 70.5 to 104.5)
    ax.add_patch(FancyBboxPatch((50.5, 70.5), 42.0, 34.0, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(71.5, 101.8, "Lamb Wave Packets in Spacious Plate", color=c_cyan, fontsize=8.0, weight="bold", ha="center", zorder=5)

    p_x, p_y, p_w, p_h = 54.5, 76.5, 34.0, 19.0
    ax.plot([p_x, p_x + p_w], [p_y + p_h*0.5, p_y + p_h*0.5], color="#475569", lw=0.6, linestyle=":", zorder=5)
    ax.plot([p_x, p_x + p_w], [p_y, p_y], color="#64748b", lw=0.8, zorder=5)
    ax.plot([p_x, p_x], [p_y, p_y + p_h], color="#64748b", lw=0.8, zorder=5)
    ax.text(p_x + p_w/2, p_y - 2.8, r"Time of Flight $t\ (\mu\mathrm{s})$", color=c_muted, fontsize=6.4, ha="center", zorder=5)
    ax.text(p_x - 2.2, p_y + p_h/2, "Stress Amplitude", color=c_muted, fontsize=6.2, va="center", rotation=90, zorder=5)

    t_w = np.linspace(0, 1, 200)
    s0_packet = 1.4 * np.sin(2 * np.pi * 14 * (t_w - 0.22)) * np.exp(-((t_w - 0.22)/0.05)**2)
    a0_packet = 3.6 * np.sin(2 * np.pi * 10 * (t_w - 0.65)) * np.exp(-((t_w - 0.65)/0.09)**2)
    full_wave = s0_packet + a0_packet

    ax.plot(p_x + t_w * p_w, p_y + p_h*0.5 + (full_wave / 6.0) * (p_h*0.45), color=c_cyan, lw=1.4, zorder=6)
    ax.text(p_x + 0.22*p_w, p_y + p_h*0.82, "S₀ Mode (Fast)", color=c_emerald, fontsize=6.2, weight="bold", ha="center", zorder=7)
    ax.text(p_x + 0.65*p_w, p_y + p_h*0.88, "A₀ Mode (High Amp)", color=c_gold_glow, fontsize=6.2, weight="bold", ha="center", zorder=7)

    # ------------------------------------------------------------------
    # CARD 2: DYNAMIC CHARGE CAPTURE q_dyn(t) & ToF LOCALIZATION (y=21.0 to 66.5)
    # ------------------------------------------------------------------
    card_dyn = FancyBboxPatch((6, 21.0), 88, 45.5, boxstyle="round,pad=0.3,rounding_size=0.6",
                             facecolor=c_subcard, edgecolor="#254778", lw=1.1, zorder=3)
    ax.add_patch(card_dyn)

    ax.text(8.5, 63.8, "2. DYNAMIC SURFACE CHARGE INTEGRATION & DEFECT SCATTERING DYNAMICS",
            color=c_gold_glow, fontsize=9.2, weight="heavy", ha="left", zorder=4)

    # Left: Dynamic Charge Formulation (Inner y: 22.8 to 60.5)
    ax.add_patch(FancyBboxPatch((7.5, 22.8), 41.5, 37.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(28.2, 57.5, "Dynamic Charge Capture Equation", color=c_cyan, fontsize=8.0, weight="bold", ha="center", zorder=5)

    # Formula Box: Raised slightly to give generous padding for bullets below
    ax.add_patch(FancyBboxPatch((9.0, 46.0), 38.5, 10.5, boxstyle="round,pad=0.1,rounding_size=0.3",
                                facecolor="#050d1a", edgecolor="#b45309", lw=0.8, zorder=5))
    ax.text(28.2, 54.0, "DYNAMIC SURFACE CHARGE CAPTURE", color=c_gold_glow, fontsize=6.0, weight="bold", ha="center", zorder=6)
    ax.text(28.2, 51.0, r"$q_{\mathrm{dyn}}(t) = \iint_A \left[ d_{31} T_1^{\mathrm{wave}} + d_{32} T_2^{\mathrm{wave}} \right] dA$",
            color=c_white, fontsize=7.2, weight="bold", ha="center", zorder=6)
    ax.text(28.2, 48.0, r"ToF Triangulation: $x_{\mathrm{crack}} = 0.5\,c_g \cdot \Delta t_{\mathrm{echo}}$",
            color=c_emerald, fontsize=6.8, weight="bold", ha="center", zorder=6)

    # Bullets spaced comfortably between y = 25.0 and 42.0
    dyn_desc = [
        ("• Wave-to-Charge Conversion:", "Directly converts stress packets to electrical charge.", c_white),
        ("• Defect Echo Reflections:", "Cracks introduce amplitude drops and distinct ToF echoes.", c_cyan),
        ("• Dual-Horizon Reach:", "Inspects plates across tens of meters without sensor movement.", c_emerald)
    ]
    for i, (d_hdr, d_txt, d_col) in enumerate(dyn_desc):
        y_pos = 41.5 - i * 5.4
        ax.text(9.2, y_pos, d_hdr, color=d_col, fontsize=6.6, weight="bold", zorder=6)
        ax.text(9.2, y_pos - 1.8, d_txt, color=c_muted, fontsize=6.2, zorder=6)

    # Right: Pitch-Catch Time-of-Flight Reflection Schematic (Inner y: 22.8 to 60.5)
    ax.add_patch(FancyBboxPatch((50.5, 22.8), 42.0, 37.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(71.5, 57.5, "Pitch-Catch ToF Defect Triangulation", color=c_cyan, fontsize=8.0, weight="bold", ha="center", zorder=5)

    # Lowered plate schematic to center it vertically within the box
    sch_x, sch_y, sch_w, sch_h = 53.5, 26.0, 36.0, 22.0
    ax.add_patch(patches.Rectangle((sch_x, sch_y + 11.0), sch_w, 4.0, facecolor="#334155", edgecolor="#64748b", lw=0.8, zorder=5))
    ax.text(sch_x + sch_w/2, sch_y + 13.0, "Spacious Structural Waveguide Plate", color="#ffffff", fontsize=6.0, weight="bold", ha="center", va="center", zorder=6)

    # Actuator Tx
    ax.add_patch(patches.Rectangle((sch_x + 2.0, sch_y + 15.0), 4.0, 2.5, facecolor="#f97316", edgecolor="#ffffff", lw=0.6, zorder=6))
    ax.text(sch_x + 4.0, sch_y + 16.2, "Tx", color="#ffffff", fontsize=5.8, weight="bold", ha="center", va="center", zorder=7)

    # Receiver Rx (SingBha-EMCD)
    ax.add_patch(patches.Rectangle((sch_x + sch_w - 6.0, sch_y + 15.0), 4.0, 2.5, facecolor="#0284c7", edgecolor="#ffffff", lw=0.6, zorder=6))
    ax.text(sch_x + sch_w - 4.0, sch_y + 16.2, "Rx", color="#ffffff", fontsize=5.8, weight="bold", ha="center", va="center", zorder=7)

    # Flaw site
    crack_x = sch_x + sch_w*0.52
    ax.plot([crack_x, crack_x], [sch_y + 12.0, sch_y + 15.0], color=c_crimson, lw=2.0, zorder=7)
    ax.text(crack_x, sch_y + 16.5, "Flaw", color=c_crimson, fontsize=6.2, weight="bold", ha="center", zorder=7)

    # Propagating rays
    ax.annotate("", xy=(crack_x - 1.0, sch_y + 13.0), xytext=(sch_x + 6.0, sch_y + 13.0),
                arrowprops=dict(arrowstyle="->", color=c_gold_glow, lw=1.2), zorder=8)
    ax.annotate("", xy=(sch_x + sch_w - 6.0, sch_y + 13.0), xytext=(crack_x + 1.0, sch_y + 13.0),
                arrowprops=dict(arrowstyle="->", color=c_emerald, lw=1.2), zorder=8)
    ax.text(sch_x + 12.0, sch_y + 8.5, "Direct Incident Wave", color=c_gold_glow, fontsize=5.8, weight="bold", zorder=8)
    ax.text(crack_x + 4.0, sch_y + 8.5, "Scattered Wave", color=c_emerald, fontsize=5.8, weight="bold", zorder=8)

    # ------------------------------------------------------------------
    # TRANSITION BADGE: Monograph Transition Pill -> Page 14
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((10.0, 15.2), 80.0, 3.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#08152b", edgecolor="#b45309", lw=0.9, zorder=3))
    ax.text(50.0, 16.9, "APPLIED ENGINEERING STRUCTURES: MULTI-DOMAIN INFRASTRUCTURE MATRIX CONTINUES ON PAGE 14.",
            color=c_gold_glow, fontsize=7.4, weight="bold", style="italic", ha="center", zorder=4)

    # ------------------------------------------------------------------
    # 5. Bottom Running Footer Bar (Normalized to "Page 13")[cite: 4]
    # ------------------------------------------------------------------
    footer_box = FancyBboxPatch((4, 1.2), 92, 9.6, boxstyle="round,pad=0.3,rounding_size=0.6",
                                facecolor=c_card_bg, edgecolor=c_border, linewidth=1.1, zorder=2)
    ax.add_patch(footer_box)

    ax.text(7, 8.2, "GARRF Technical Magazine 1 • Monograph Series • Archive Ref: GARRF-MAG1-SINGBHA-2026.P13",
            color=c_muted, fontsize=8.0, weight="medium", zorder=4)
    ax.text(7, 5.7, "Official Portal: https://garrf.in  •  LinkedIn: https://www.linkedin.com/company/gopalkrishnaadvancedruralresearchfoundation/",
            color=c_cyan, fontsize=7.6, weight="semibold", zorder=4)
    ax.text(7, 3.0, "Dedicated in Honour of Singapore and Bharat",
            color=c_white, fontsize=8.6, weight="bold", ha="left", zorder=4)
    ax.text(93, 3.0, "Page 13",
            color=c_gold_glow, fontsize=9.5, weight="black", ha="right", zorder=4)

    output_filename = "SingBha_Magazine_Page_13_Waveform_Propagation_Audited.png"
    plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
    plt.close()

    display(IPImage(filename=output_filename, width=720))
    print(f"Generated successfully: {output_filename} (A4 300 DPI Page 13 - Fully Audited)")
    files.download(output_filename)

if __name__ == "__main__":
    generate_magazine_page_13_waveform_propagation()
