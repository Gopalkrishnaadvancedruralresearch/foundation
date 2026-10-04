import io
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
from PIL import Image
from IPython.display import display, Image as IPImage
from google.colab import files

def generate_magazine_page_4_final():
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
    c_pzt       = "#f97316"
    c_bond      = "#d97706"
    c_beam      = "#64748b"
    c_white     = "#ffffff"
    c_border    = "#1d3863"
    c_muted     = "#cbd5e1"  # High-contrast slate for print legibility[cite: 4]

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
    ax.text(6.5, 118.8, "CHAPTER IV • 3D CONTINUUM TENSORS & INTERFACIAL PHYSICS",
            color=c_gold_glow, fontsize=9.2, weight="heavy", ha="left", zorder=4)
    ax.text(6.5, 114.8, "3D Directional Sum Model, Thickness Resonance & Shear-Lag",
            color=c_white, fontsize=14.2, weight="black", ha="left", zorder=4)
    ax.text(6.5, 111.8, "Triaxial elastodynamics, high-frequency thickness mode proof, and interfacial viscoelastic mechanics.",
            color=c_muted, fontsize=9.0, weight="medium", ha="left", zorder=4)

    # ------------------------------------------------------------------
    # SECTION A: 3D Continuum Schematic & Exact Directional Sum Model
    # ------------------------------------------------------------------
    card_3d = FancyBboxPatch((6, 68.8), 88, 41.2, boxstyle="round,pad=0.3,rounding_size=0.8",
                             facecolor=c_subcard, edgecolor="#254778", lw=1.2, zorder=3)
    ax.add_patch(card_3d)

    ax.text(8.5, 106.8, "1. 3D CONTINUUM MODEL (ANNAMDAS & SOH, 2007) — TRIAXIAL SOLID",
            color=c_gold_glow, fontsize=9.8, weight="heavy", ha="left", zorder=4)

    # Sub-Box 1: Isometric 3D Continuum Schematic (Width: 30.5)
    ax.add_patch(patches.Rectangle((8.5, 71.2), 30.5, 33.2, facecolor="#07152b", edgecolor=c_border, lw=1.0, zorder=4))
    ax.text(23.7, 101.5, "3D Volumetric Continuum", color=c_cyan, fontsize=8.6, weight="bold", ha="center", zorder=5)

    # Volumetric 3D Cube (Front, Top, Right faces)
    bX, bY, bW, bH = 11.5, 75.8, 14.5, 13.0
    sX, sY = 5.8, 5.5
    ax.add_patch(patches.Rectangle((bX, bY), bW, bH, facecolor="#475569", edgecolor="#94a3b8", lw=1.0, zorder=5))
    top_poly = patches.Polygon([[bX, bY + bH], [bX + sX, bY + bH + sY], [bX + bW + sX, bY + bH + sY], [bX + bW, bY + bH]],
                               facecolor="#64748b", edgecolor="#94a3b8", lw=1.0, zorder=5)
    ax.add_patch(top_poly)
    right_poly = patches.Polygon([[bX + bW, bY], [bX + bW + sX, bY + sY], [bX + bW + sX, bY + bH + sY], [bX + bW, bY + bH]],
                                 facecolor="#334155", edgecolor="#94a3b8", lw=1.0, zorder=5)
    ax.add_patch(right_poly)

    # PZT Block on Top Surface (Transducer 2l x 2w x 2h)
    pzt_fx, pzt_fy, pzt_fw, pzt_fh = 15.5, bY + bH - 0.5, 6.5, 2.6
    ax.add_patch(patches.Rectangle((pzt_fx, pzt_fy), pzt_fw, pzt_fh, facecolor=c_pzt, edgecolor="#ffffff", lw=0.6, zorder=6))
    pzt_top = patches.Polygon([[pzt_fx, pzt_fy + pzt_fh], [pzt_fx + 2.4, pzt_fy + pzt_fh + 2.0],
                               [pzt_fx + pzt_fw + 2.4, pzt_fy + pzt_fh + 2.0], [pzt_fx + pzt_fw, pzt_fy + pzt_fh]],
                              facecolor="#ea580c", edgecolor="#ffffff", lw=0.6, zorder=6)
    ax.add_patch(pzt_top)

    # Directional Impedance Vector Arrows
    ax.annotate("", xy=(pzt_fx + pzt_fw + 4.2, pzt_fy + 1.2), xytext=(pzt_fx + pzt_fw, pzt_fy + 1.2),
                arrowprops=dict(arrowstyle="->", color=c_gold_glow, lw=1.3), zorder=7)
    ax.text(pzt_fx + pzt_fw + 4.6, pzt_fy + 0.8, r"$\mathbf{Z}_{xx}$", color=c_gold_glow, fontsize=8.0, weight="bold", zorder=7)

    ax.annotate("", xy=(pzt_fx + 4.2, pzt_fy + pzt_fh + 3.2), xytext=(pzt_fx + 2.8, pzt_fy + pzt_fh + 1.5),
                arrowprops=dict(arrowstyle="->", color=c_gold_glow, lw=1.3), zorder=7)
    ax.text(pzt_fx + 4.8, pzt_fy + pzt_fh + 2.6, r"$\mathbf{Z}_{yy}$", color=c_gold_glow, fontsize=8.0, weight="bold", zorder=7)

    ax.annotate("", xy=(pzt_fx + 3.2, pzt_fy - 3.2), xytext=(pzt_fx + 3.2, pzt_fy),
                arrowprops=dict(arrowstyle="->", color=c_gold_glow, lw=1.3), zorder=7)
    ax.text(pzt_fx + 4.0, pzt_fy - 2.8, r"$\mathbf{Z}_{zz}$", color=c_gold_glow, fontsize=8.0, weight="bold", zorder=7)

    ax.text(23.7, 72.8, r"Triaxial Tensor: $T_1, T_2, T_3, \tau_{ij} \neq 0$", color=c_muted, fontsize=7.8, weight="semibold", ha="center", zorder=5)

    # Sub-Box 2: Exact Analytical Formulation (Width: 52.0)
    ax.add_patch(FancyBboxPatch((40.5, 71.2), 52.0, 33.2, boxstyle="round,pad=0.2,rounding_size=0.5",
                                facecolor="#081427", edgecolor="#204575", lw=1.0, zorder=4))
    
    ax.text(42.2, 101.5, "Closed-Form Admittance Solution (Annamdas & Soh):", color=c_cyan, fontsize=9.2, weight="bold", zorder=5)
    
    # 3D Equation with proper margin clearance
    ax.text(42.2, 95.8, r"$\overline{Y}_{3\mathrm{D}}(\omega) = j\omega \frac{2lw}{h} \left[ \overline{\varepsilon}_{33}^T - \mathbf{d}\mathbf{c}^E\mathbf{d}^T + \sum_{m=1}^{3} \mathcal{D}_m \left(\frac{\overline{Z}_{a,mm}}{\overline{Z}_{s,mm} + \overline{Z}_{a,mm}}\right) \frac{\tan(\kappa_m l_m)}{\kappa_m l_m} \right]$",
            color=c_white, fontsize=8.6, zorder=5)
    
    ax.text(42.2, 91.2, r"• Directional Sum: $\mathbf{Z}_{s,3\mathrm{D}} = \overline{Z}_{s,xx} + \overline{Z}_{s,yy} + \overline{Z}_{s,zz} + \overline{Z}_{\mathrm{shear}}$.",
            color=c_muted, fontsize=8.4, weight="medium", zorder=5)
    ax.text(42.2, 87.5, r"• Triaxial Wavenumbers: $\kappa_1 = \omega\sqrt{\rho/c_{11}^E}, \; \kappa_2 = \omega\sqrt{\rho/c_{22}^E}, \; \kappa_3 = \omega\sqrt{\rho/c_{33}^E}$.",
            color=c_muted, fontsize=8.2, weight="medium", zorder=5)
    ax.text(42.2, 83.8, r"• Coupling: $\mathcal{D}_1 = d_{31}(c_{11}^E + c_{12}^E) + d_{33}c_{13}^E, \; \mathcal{D}_3 = 2d_{31}c_{13}^E + d_{33}c_{33}^E$.",
            color=c_muted, fontsize=8.2, weight="medium", zorder=5)
    ax.text(42.2, 80.0, r"• Dielectric Subtraction: $\mathbf{d}\mathbf{c}^E\mathbf{d}^T = \sum_{i=1}^3 \sum_{j=1}^3 d_{3i} c_{ij}^E d_{3j}$ couples 3D stresses.",
            color=c_muted, fontsize=8.2, weight="medium", zorder=5)
    ax.text(42.2, 76.5, "• Scope: Accurately evaluates true 3D solid blocks,",
            color=c_muted, fontsize=8.0, style="italic", zorder=5)
    ax.text(42.2, 73.5, "  mass concrete & embedded aggregate transducers.",
            color=c_muted, fontsize=8.0, style="italic", zorder=5)

    # ------------------------------------------------------------------
    # SECTION B: Thickness Resonance Proof & FEM Discretization Barrier
    # ------------------------------------------------------------------
    card_proof = FancyBboxPatch((6, 42.0), 88, 25.5, boxstyle="round,pad=0.3,rounding_size=0.8",
                                facecolor=c_subcard, edgecolor=c_border, lw=1.2, zorder=3)
    ax.add_patch(card_proof)

    ax.text(8.5, 64.5, "2. HIGH-FREQUENCY THICKNESS RESONANCE PROOF (600 – 900 kHz) & FEM BARRIER",
            color=c_cyan, fontsize=9.6, weight="heavy", ha="left", zorder=4)

    # Left Column: Mathematical Pole Proof (Width: 41.5)
    ax.add_patch(FancyBboxPatch((7.5, 43.8), 41.5, 18.5, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(9.2, 59.5, "Why 1D and 2D Models Miss the Thickness Mode:", color=c_gold_glow, fontsize=8.6, weight="bold", zorder=5)
    ax.text(9.2, 56.5, r"• Plane Stress ($T_3 = 0$) forces $\partial^2 u_z / \partial z^2 = 0$,",
            color=c_muted, fontsize=8.2, weight="medium", zorder=5)
    ax.text(9.2, 53.8, "  erasing the out-of-plane wavenumber eigenvalue.",
            color=c_muted, fontsize=8.2, weight="medium", zorder=5)
    ax.text(9.2, 50.5, r"• 3D Mode $m=3$ contains $\tan(\kappa_3 h) / (\kappa_3 h)$, with $\kappa_3 = \omega \sqrt{\rho / c_{33}^E}$.",
            color=c_white, fontsize=8.2, weight="bold", zorder=5)
    ax.text(9.2, 47.5, r"• Pole at $\kappa_3 h \rightarrow \pi/2$ predicts the 600–900 kHz peak",
            color=c_cyan, fontsize=8.2, weight="bold", zorder=5)
    ax.text(9.2, 45.0, "  within 2% to 4% of physical experimental data.",
            color=c_cyan, fontsize=8.2, weight="bold", zorder=5)

    # Right Column: FEM High-Frequency Barrier (Width: 42.0)
    ax.add_patch(FancyBboxPatch((50.5, 43.8), 42.0, 18.5, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(52.0, 59.5, "FEM Discretization Barrier (CFL Meshing Limit):", color=c_gold_glow, fontsize=8.6, weight="bold", zorder=5)
    ax.text(52.0, 56.5, r"• Spatial Limit: $\Delta x \leq \lambda_{\mathrm{min}} / 10 = c / (10 \cdot f_{\mathrm{max}})$.",
            color=c_muted, fontsize=8.2, weight="medium", zorder=5)
    ax.text(52.0, 53.5, r"• At $f = 1$ MHz ($c \approx 3000$ m/s), $\lambda = 3$ mm $\rightarrow \Delta x \leq 0.3$ mm.",
            color=c_muted, fontsize=8.2, weight="medium", zorder=5)
    ax.text(52.0, 50.5, "• Requires millions of solid elements, inducing dispersion.",
            color=c_muted, fontsize=8.0, weight="medium", zorder=5)
    ax.text(52.0, 47.5, "• Continuum equations solve eigenvalues in < 15 ms",
            color=c_gold_glow, fontsize=8.0, weight="bold", zorder=5)
    ax.text(52.0, 45.0, "  with zero artificial numerical damping.",
            color=c_gold_glow, fontsize=8.0, weight="bold", zorder=5)

    # ------------------------------------------------------------------
    # SECTION C: Interfacial Adhesive Shear-Lag & Temperature Mechanics
    # ------------------------------------------------------------------
    card_bond = FancyBboxPatch((6, 20.2), 88, 20.3, boxstyle="round,pad=0.3,rounding_size=0.8",
                               facecolor=c_subcard, edgecolor=c_border, lw=1.2, zorder=3)
    ax.add_patch(card_bond)

    ax.text(8.5, 37.8, "3. INTERFACIAL ADHESIVE SHEAR-LAG & ENVIRONMENTAL TEMPERATURE DECOUPLING",
            color=c_gold_glow, fontsize=9.4, weight="heavy", ha="left", zorder=4)

    # Left Box: Viscoelastic Adhesive Shear-Lag
    ax.add_patch(FancyBboxPatch((7.5, 21.2), 41.5, 14.2, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(9.0, 32.6, "Adhesive Shear-Lag Mechanics (tb, Gb, ηb):", color=c_cyan, fontsize=8.6, weight="bold", zorder=5)
    ax.text(9.0, 29.2, r"$\tau(x) = \frac{\overline{G}_b}{t_b} [ u_s(x) - u_p(x) ], \quad \Gamma = \sqrt{\frac{\overline{G}_b}{t_b \overline{Y}_{11}^E h}}$",
            color=c_white, fontsize=9.2, zorder=5)
    ax.text(9.0, 25.8, r"• Complex Modulus: $\overline{G}_b = G_b (1 + j\eta_b)$; captures shear damping.",
            color=c_muted, fontsize=8.0, weight="medium", zorder=5)
    ax.text(9.0, 22.8, r"• Impedance: $\overline{Z}_{s,\mathrm{eff}} = (\frac{\overline{G}_b}{\Gamma t_b}) \tanh(\Gamma l) [\frac{Z_s}{Z_s + Z_{\mathrm{bond}}}]$.",
            color=c_muted, fontsize=7.8, weight="medium", zorder=5)

    # Right Box: Environmental Temperature Decoupling
    ax.add_patch(FancyBboxPatch((50.5, 21.2), 42.0, 14.2, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(52.0, 32.6, "Temperature Drift Decoupling (ΔT):", color=c_cyan, fontsize=8.6, weight="bold", zorder=5)
    ax.text(52.0, 29.2, r"$E(T) = E_0 [1 - \alpha_E \Delta T], \quad \overline{\varepsilon}_{33}^T(T) = \overline{\varepsilon}_{33}^T [1 + \alpha_\varepsilon \Delta T]$",
            color=c_white, fontsize=9.2, zorder=5)
    ax.text(52.0, 25.8, r"• Elastic Softening: $\alpha_E \approx 4.5 \times 10^{-4}$/°C shifts modal peaks.",
            color=c_muted, fontsize=8.0, weight="medium", zorder=5)
    ax.text(52.0, 22.8, "• EOM Filter decouples thermal drift from true crack damage.",
            color=c_muted, fontsize=8.0, weight="medium", zorder=5)

    # ------------------------------------------------------------------
    # TRANSITION BADGE: Centered Pill (x = 14 to 86, Clear of '+' Accents)
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((14.0, 15.0), 72.0, 4.4, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#08152b", edgecolor="#b45309", lw=0.9, zorder=3))
    
    ax.text(50.0, 17.7, "Quantitative Damage Metrology (RMSD, MAPD, CCD) & Metric Derivations",
            color=c_gold_glow, fontsize=8.2, weight="bold", style="italic", ha="center", zorder=4)
    ax.text(50.0, 15.8, "alongside Experimental Crack Progression continue on Page 5.",
            color=c_gold_glow, fontsize=8.2, weight="bold", style="italic", ha="center", zorder=4)

    # ------------------------------------------------------------------
    # 5. Bottom Running Footer Bar with "Page 4"[cite: 4]
    # ------------------------------------------------------------------
    footer_box = FancyBboxPatch((4, 1.2), 92, 9.6, boxstyle="round,pad=0.3,rounding_size=0.6",
                                facecolor=c_card_bg, edgecolor=c_border, linewidth=1.1, zorder=2)
    ax.add_patch(footer_box)

    ax.text(7, 8.2, "GARRF Technical Magazine 1 • Monograph Series • Archive Ref: GARRF-MAG1-SINGBHA-2026.P04",
            color=c_muted, fontsize=8.0, weight="medium", zorder=4)
    ax.text(7, 5.7, "Official Portal: https://garrf.in  •  LinkedIn: https://www.linkedin.com/company/gopalkrishnaadvancedruralresearchfoundation/",
            color=c_cyan, fontsize=7.6, weight="semibold", zorder=4)
    ax.text(7, 3.0, "Dedicated in Honour of Singapore and Bharat",
            color=c_white, fontsize=8.6, weight="bold", ha="left", zorder=4)
    ax.text(93, 3.0, "Page 4",
            color=c_gold_glow, fontsize=9.5, weight="black", ha="right", zorder=4)

    output_filename = "SingBha_Magazine_Page_4_Final.png"
    plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
    plt.close()

    display(IPImage(filename=output_filename, width=720))
    print(f"Generated successfully: {output_filename} (A4 300 DPI Perfect Page 4 Ready)")
    files.download(output_filename)

if __name__ == "__main__":
    generate_magazine_page_4_final()
