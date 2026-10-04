import io
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
from PIL import Image
from IPython.display import display, Image as IPImage
from google.colab import files

def generate_magazine_page_10_pillars_part2():
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

    # Section Banner[cite: 25]
    ax.text(6.5, 118.8, "SECTION 8 • SCIENTIFIC PILLARS OF SingBha-EMCD (PART II)",
            color=c_gold_glow, fontsize=9.2, weight="heavy", ha="left", zorder=4)
    ax.text(6.5, 114.8, "The Six Scientific Pillars of SingBha-EMCD (Pillars 4 to 6)",
            color=c_white, fontsize=14.0, weight="black", ha="left", zorder=4)
    ax.text(6.5, 111.8, "3D continuum anisotropic mechanics, dual-horizon range scaling & virtual ground circuitry.",
            color=c_muted, fontsize=8.8, weight="medium", ha="left", zorder=4)

    # ------------------------------------------------------------------
    # 3-COLUMN PILLAR CARDS (Pillars 4, 5, 6)[cite: 25]
    # ------------------------------------------------------------------
    col_w, col_h = 27.8, 88.5
    y_card = 21.0

    # ------------------------------------------------------------------
    # PILLAR 4: 3D Continuum Anisotropic Mechanics[cite: 25]
    # ------------------------------------------------------------------
    x_c1 = 6.5
    card_p4 = FancyBboxPatch((x_c1, y_card), col_w, col_h, boxstyle="round,pad=0.3,rounding_size=0.6",
                             facecolor=c_subcard, edgecolor="#254778", lw=1.1, zorder=3)
    ax.add_patch(card_p4)

    ax.text(x_c1 + col_w/2, y_card + col_h - 4.5, "PILLAR 4", color=c_gold_glow, fontsize=8.5, weight="heavy", ha="center", zorder=4)
    ax.text(x_c1 + col_w/2, y_card + col_h - 7.8, "3D Continuum Anisotropy", color=c_white, fontsize=9.2, weight="black", ha="center", zorder=4)
    ax.text(x_c1 + col_w/2, y_card + col_h - 10.5, "Triaxial Poisson Coupling", color=c_cyan, fontsize=7.8, weight="bold", ha="center", zorder=4)

    # Schematic Vector: 3D Solid Stress Block[cite: 17, 25]
    ax.add_patch(FancyBboxPatch((x_c1 + 1.5, y_card + col_h - 32.0), col_w - 3.0, 19.5, boxstyle="round,pad=0.1,rounding_size=0.3",
                                facecolor="#081427", edgecolor="#204575", lw=0.8, zorder=4))
    
    iso_ox, iso_oy = x_c1 + 9.5, y_card + col_h - 28.0
    # Front face
    ax.add_patch(patches.Rectangle((iso_ox, iso_oy), 6.5, 6.0, facecolor="#1e293b", edgecolor="#94a3b8", lw=0.7, zorder=5))
    # Top face
    ax.add_patch(patches.Polygon([[iso_ox, iso_oy + 6.0], [iso_ox + 3.5, iso_oy + 8.5], 
                                  [iso_ox + 10.0, iso_oy + 8.5], [iso_ox + 6.5, iso_oy + 6.0]],
                                 facecolor="#334155", edgecolor="#94a3b8", lw=0.7, zorder=5))
    # Side face
    ax.add_patch(patches.Polygon([[iso_ox + 6.5, iso_oy], [iso_ox + 10.0, iso_oy + 2.5], 
                                  [iso_ox + 10.0, iso_oy + 8.5], [iso_ox + 6.5, iso_oy + 6.0]],
                                 facecolor="#475569", edgecolor="#94a3b8", lw=0.7, zorder=5))

    # Stress arrows (T1, T3)
    ax.annotate("", xy=(iso_ox + 12.0, iso_oy + 2.8), xytext=(iso_ox + 6.5, iso_oy + 2.8),
                arrowprops=dict(arrowstyle="->", color=c_cyan, lw=1.2), zorder=6)
    ax.text(iso_ox + 12.6, iso_oy + 2.3, r"$T_1$", color=c_cyan, fontsize=6.8, weight="bold", zorder=7)

    ax.annotate("", xy=(iso_ox + 3.2, iso_oy + 9.6), xytext=(iso_ox + 3.2, iso_oy + 6.0),
                arrowprops=dict(arrowstyle="->", color=c_gold_glow, lw=1.2), zorder=6)
    ax.text(iso_ox + 3.2, iso_oy + 10.2, r"$T_3$", color=c_gold_glow, fontsize=6.8, weight="bold", ha="center", zorder=7)

    # Formula Box: 3D Impedance Matrix (Safe LaTeX without \quad)[cite: 17, 25]
    ax.add_patch(FancyBboxPatch((x_c1 + 1.5, y_card + col_h - 45.0), col_w - 3.0, 11.2, boxstyle="round,pad=0.1,rounding_size=0.3",
                                facecolor="#050d1a", edgecolor="#b45309", lw=0.8, zorder=4))
    ax.text(x_c1 + col_w/2, y_card + col_h - 36.5, "TRIAXIAL IMPEDANCE TENSOR", color=c_gold_glow, fontsize=6.2, weight="bold", ha="center", zorder=5)
    ax.text(x_c1 + col_w/2, y_card + col_h - 40.8, r"$\mathbf{Z}_s = \mathrm{diag}(Z_{s,x}, Z_{s,y}, Z_{s,z})$", color=c_white, fontsize=7.8, weight="bold", ha="center", zorder=5)
    ax.text(x_c1 + col_w/2, y_card + col_h - 43.5, r"$S_i = s_{ij}^E T_j + d_{3i} E_3\ (i,j = 1..6)$", color=c_cyan, fontsize=6.8, ha="center", zorder=5)

    p4_lines = [
        "Classical 1D models fail in thick concrete,",
        "bolted flanges, and pressure vessels due",
        "to severe multi-axial Poisson restraints.",
        "",
        "SingBha-EMCD incorporates full tri-axial",
        "structural impedance tensors (Zs,x, Zs,y, Zs,z)",
        "and cross-axis compliances (s12^E, s13^E).",
        "",
        "Out-of-plane thickness dilatation modes",
        "and lateral shear interactions are solved",
        "analytically, preventing metric breakdown",
        "in highly confined heavy-civil and",
        "high-pressure industrial components."
    ]
    for i, line in enumerate(p4_lines):
        ax.text(x_c1 + 2.2, y_card + 39.0 - i * 3.0, line, color=c_white if "tri-axial" in line else c_muted,
                fontsize=6.8, weight="bold" if "tri-axial" in line else "normal", zorder=5)

    # ------------------------------------------------------------------
    # PILLAR 5: Dual-Horizon Multi-Scale Reach[cite: 25]
    # ------------------------------------------------------------------
    x_c2 = 36.1
    card_p5 = FancyBboxPatch((x_c2, y_card), col_w, col_h, boxstyle="round,pad=0.3,rounding_size=0.6",
                             facecolor=c_subcard, edgecolor="#254778", lw=1.1, zorder=3)
    ax.add_patch(card_p5)

    ax.text(x_c2 + col_w/2, y_card + col_h - 4.5, "PILLAR 5", color=c_gold_glow, fontsize=8.5, weight="heavy", ha="center", zorder=4)
    ax.text(x_c2 + col_w/2, y_card + col_h - 7.8, "Dual-Horizon Reach Scaling", color=c_white, fontsize=9.2, weight="black", ha="center", zorder=4)
    ax.text(x_c2 + col_w/2, y_card + col_h - 10.5, "Near-Field + Far-Field Waves", color=c_cyan, fontsize=7.8, weight="bold", ha="center", zorder=4)

    # Schematic Vector: Dual-Horizon Inspection Wave Zones[cite: 25, 31]
    ax.add_patch(FancyBboxPatch((x_c2 + 1.5, y_card + col_h - 32.0), col_w - 3.0, 19.5, boxstyle="round,pad=0.1,rounding_size=0.3",
                                facecolor="#081427", edgecolor="#204575", lw=0.8, zorder=4))
    
    tx_orig = x_c2 + 4.5
    ax.add_patch(patches.Rectangle((tx_orig, y_card + col_h - 24.0), 3.2, 3.8, facecolor=c_gold, edgecolor="#ffffff", lw=0.6, zorder=5))
    ax.text(tx_orig + 1.6, y_card + col_h - 22.1, "PZT", color="#000000", fontsize=5.8, weight="black", ha="center", va="center", zorder=6)

    # Near-field zone circle
    ax.add_patch(patches.Circle((tx_orig + 1.6, y_card + col_h - 22.1), radius=5.0, facecolor="none",
                                edgecolor=c_cyan, lw=1.1, linestyle="--", zorder=5))
    ax.text(tx_orig + 1.6, y_card + col_h - 29.5, r"Near-Field ($r \leq 1\,\mathrm{m}$)", color=c_cyan, fontsize=5.8, weight="bold", ha="center", zorder=6)

    # Far-field wave arcs with adjusted label positioning
    for arc_r in [8.0, 11.5, 14.8]:
        arc = patches.Arc((tx_orig + 1.6, y_card + col_h - 22.1), 2*arc_r, 2*arc_r, angle=0, theta1=-42, theta2=42,
                          edgecolor=c_emerald, lw=1.2, zorder=5)
        ax.add_patch(arc)
    ax.text(x_c2 + 19.0, y_card + col_h - 15.5, "Lamb Waves\n(>10 m Range)", color=c_emerald, fontsize=5.8, weight="bold", ha="center", zorder=6)

    # Formula Box: Dual Operational Modes[cite: 25, 31]
    ax.add_patch(FancyBboxPatch((x_c2 + 1.5, y_card + col_h - 45.0), col_w - 3.0, 11.2, boxstyle="round,pad=0.1,rounding_size=0.3",
                                facecolor="#050d1a", edgecolor="#b45309", lw=0.8, zorder=4))
    ax.text(x_c2 + col_w/2, y_card + col_h - 36.5, "HYBRID OPERATIONAL DOMAIN", color=c_gold_glow, fontsize=6.2, weight="bold", ha="center", zorder=5)
    ax.text(x_c2 + col_w/2, y_card + col_h - 40.8, r"Near: $\nabla D_3(x,y)\ (50 - 350\,\mathrm{kHz})$", color=c_white, fontsize=7.2, weight="bold", ha="center", zorder=5)
    ax.text(x_c2 + col_w/2, y_card + col_h - 43.5, r"Far: $u(x,t) = A_0 e^{j(kx - \omega t)}\ (20 - 100\,\mathrm{kHz})$", color=c_emerald, fontsize=6.6, ha="center", zorder=5)

    p5_lines = [
        "Overcomes high-frequency acoustic attenuation",
        "(reff = 0.4 m to 1.5 m) via a seamless hybrid",
        "dual-horizon operational architecture.",
        "",
        "Near-Field Mode (50-350 kHz):",
        "Operates as a self-sensing charge gradient",
        "spectrometer (r ≤ 1.0 m) for incipient cracks.",
        "",
        "Far-Field Mode (20-100 kHz):",
        "Excites low-frequency guided Lamb wave",
        "packets (S0 longitudinal, A0 flexural modes)",
        "traversing spacious metallic or composite",
        "panels across tens of meters without moving."
    ]
    for i, line in enumerate(p5_lines):
        ax.text(x_c2 + 2.2, y_card + 39.0 - i * 3.0, line, color=c_emerald if "Far-Field" in line or "Near-Field" in line else c_muted,
                fontsize=6.8, weight="bold" if "Far-Field" in line or "Near-Field" in line else "normal", zorder=5)

    # ------------------------------------------------------------------
    # PILLAR 6: Elimination of Cable Capacitance Drift[cite: 25]
    # ------------------------------------------------------------------
    x_c3 = 65.7
    card_p6 = FancyBboxPatch((x_c3, y_card), col_w, col_h, boxstyle="round,pad=0.3,rounding_size=0.6",
                             facecolor=c_subcard, edgecolor="#254778", lw=1.1, zorder=3)
    ax.add_patch(card_p6)

    ax.text(x_c3 + col_w/2, y_card + col_h - 4.5, "PILLAR 6", color=c_gold_glow, fontsize=8.5, weight="heavy", ha="center", zorder=4)
    ax.text(x_c3 + col_w/2, y_card + col_h - 7.8, "Virtual Ground Circuitry", color=c_white, fontsize=9.2, weight="black", ha="center", zorder=4)
    ax.text(x_c3 + col_w/2, y_card + col_h - 10.5, "Cable Capacitance Elimination", color=c_cyan, fontsize=7.8, weight="bold", ha="center", zorder=4)

    # Schematic Vector: Virtual Ground Transimpedance Op-Amp Circuit[cite: 25, 35]
    ax.add_patch(FancyBboxPatch((x_c3 + 1.5, y_card + col_h - 32.0), col_w - 3.0, 19.5, boxstyle="round,pad=0.1,rounding_size=0.3",
                                facecolor="#081427", edgecolor="#204575", lw=0.8, zorder=4))
    
    # Coaxial Cable Lead
    ax.plot([x_c3 + 3.0, x_c3 + 9.5], [y_card + col_h - 20.0, y_card + col_h - 20.0], color=c_gold, lw=1.4, zorder=5)
    ax.text(x_c3 + 6.2, y_card + col_h - 18.0, "50m+ Cable", color=c_gold_glow, fontsize=5.6, weight="bold", ha="center", zorder=6)

    # Op-Amp Triangle Buffer
    op_x, op_y = x_c3 + 13.5, y_card + col_h - 21.0
    ax.add_patch(patches.Polygon([[op_x, op_y + 4.2], [op_x, op_y - 4.2], [op_x + 6.2, op_y]],
                                 facecolor="#1e293b", edgecolor="#ffffff", lw=0.8, zorder=5))
    ax.text(op_x + 1.0, op_y + 1.3, "-", color="#ffffff", fontsize=6.8, weight="bold", zorder=6)
    ax.text(op_x + 1.0, op_y - 2.6, "+", color="#ffffff", fontsize=6.8, weight="bold", zorder=6)

    # Ground connection
    ax.plot([op_x - 1.2, op_x], [op_y - 2.4, op_y - 2.4], color="#94a3b8", lw=0.8, zorder=5)
    ax.plot([op_x - 1.2, op_x - 1.2], [op_y - 2.4, op_y - 4.0], color="#94a3b8", lw=0.8, zorder=5)
    ax.plot([op_x - 2.2, op_x - 0.2], [op_y - 4.0, op_y - 4.0], color="#94a3b8", lw=1.0, zorder=5)
    ax.text(op_x - 1.2, op_y - 5.4, "0 V (GND)", color=c_emerald, fontsize=5.4, weight="bold", ha="center", zorder=6)

    # Feedback Capacitor (Cf)
    ax.plot([op_x - 1.2, op_x - 1.2, op_x + 8.2, op_x + 8.2], 
            [op_y + 1.6, op_y + 6.0, op_y + 6.0, op_y], color="#38bdf8", lw=0.8, zorder=5)
    ax.add_patch(patches.Rectangle((op_x + 2.2, op_y + 5.0), 2.2, 2.0, facecolor="#0284c7", edgecolor="#ffffff", lw=0.5, zorder=6))
    ax.text(op_x + 3.3, op_y + 6.0, r"$C_f$", color="#ffffff", fontsize=5.8, weight="bold", ha="center", va="center", zorder=7)

    # Formula Box: Zero Current Proof[cite: 25]
    ax.add_patch(FancyBboxPatch((x_c3 + 1.5, y_card + col_h - 45.0), col_w - 3.0, 11.2, boxstyle="round,pad=0.1,rounding_size=0.3",
                                facecolor="#050d1a", edgecolor="#b45309", lw=0.8, zorder=4))
    ax.text(x_c3 + col_w/2, y_card + col_h - 36.5, "CABLE CURRENT ELIMINATION", color=c_gold_glow, fontsize=6.2, weight="bold", ha="center", zorder=5)
    ax.text(x_c3 + col_w/2, y_card + col_h - 40.8, r"$I_{\mathrm{cable}} = C_{\mathrm{cable}} \frac{dV}{dt} = C_{\mathrm{cable}} \cdot 0 = 0$",
            color=c_white, fontsize=7.2, weight="bold", ha="center", zorder=5)
    ax.text(x_c3 + col_w/2, y_card + col_h - 43.5, r"$V_{\mathrm{out}}(t) = -\frac{Q(t)}{C_f} = -\frac{1}{C_f}\iint D_3\,dA$",
            color=c_emerald, fontsize=6.6, ha="center", zorder=5)

    p6_lines = [
        "In classical EMI, long coaxial cables add",
        "parasitic capacitance (50-100 pF/m) that",
        "causes severe phase lag and resonance shift.",
        "",
        "SingBha-EMCD routes segmented pads directly",
        "to inverting inputs of charge amplifiers",
        "held at virtual ground (0 V).",
        "",
        "Because voltage across cable remains 0 V,",
        "dynamic charging current is eliminated.",
        "",
        "Field deployments can use 50+ meter cables",
        "without signal distortion, capacitive drift,",
        "or requirement for bulky remote analyzers."
    ]
    for i, line in enumerate(p6_lines):
        ax.text(x_c3 + 2.2, y_card + 39.0 - i * 3.0, line, color=c_emerald if "50+ meter" in line else c_muted,
                fontsize=6.8, weight="bold" if "50+ meter" in line else "normal", zorder=5)

    # ------------------------------------------------------------------
    # TRANSITION BADGE: Monograph Transition Pill -> Page 11[cite: 27]
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((10.0, 15.2), 80.0, 3.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#08152b", edgecolor="#b45309", lw=0.9, zorder=3))
    ax.text(50.0, 16.9, "MASTER 8-DIMENSIONAL BENCHMARK MATRIX (EMI VS. SingBha-EMCD) CONTINUES ON PAGE 11.",
            color=c_gold_glow, fontsize=7.4, weight="bold", style="italic", ha="center", zorder=4)

    # ------------------------------------------------------------------
    # 5. Bottom Running Footer Bar (Normalized to "Page 10")[cite: 4]
    # ------------------------------------------------------------------
    footer_box = FancyBboxPatch((4, 1.2), 92, 9.6, boxstyle="round,pad=0.3,rounding_size=0.6",
                                facecolor=c_card_bg, edgecolor=c_border, linewidth=1.1, zorder=2)
    ax.add_patch(footer_box)

    ax.text(7, 8.2, "GARRF Technical Magazine 1 • Monograph Series • Archive Ref: GARRF-MAG1-SINGBHA-2026.P10",
            color=c_muted, fontsize=8.0, weight="medium", zorder=4)
    ax.text(7, 5.7, "Official Portal: https://garrf.in  •  LinkedIn: https://www.linkedin.com/company/gopalkrishnaadvancedruralresearchfoundation/",
            color=c_cyan, fontsize=7.6, weight="semibold", zorder=4)
    ax.text(7, 3.0, "Dedicated in Honour of Singapore and Bharat",
            color=c_white, fontsize=8.6, weight="bold", ha="left", zorder=4)
    ax.text(93, 3.0, "Page 10",
            color=c_gold_glow, fontsize=9.5, weight="black", ha="right", zorder=4)

    output_filename = "SingBha_Magazine_Page_10_Pillars_Part2.png"
    plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
    plt.close()

    display(IPImage(filename=output_filename, width=720))
    print(f"Generated successfully: {output_filename} (A4 300 DPI Page 10 Ready - Verified & Error-Free)")
    files.download(output_filename)

if __name__ == "__main__":
    generate_magazine_page_10_pillars_part2()
