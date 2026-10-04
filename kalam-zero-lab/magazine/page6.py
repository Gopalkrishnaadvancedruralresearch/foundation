import io
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
from PIL import Image
from IPython.display import display, Image as IPImage
from google.colab import files

def draw_circuit_1d(ax, x0, y0, w, h):
    """2-Qubit VQC for 1D Beam: Feature Map + Rotations + CNOT"""
    y_q0 = y0 + h * 0.70
    y_q1 = y0 + h * 0.30
    
    # Qubit Labels & Wires
    ax.text(x0 + 1.0, y_q0, r"$|q_0\rangle$", color="#cbd5e1", fontsize=7.2, va="center", weight="bold")
    ax.text(x0 + 1.0, y_q1, r"$|q_1\rangle$", color="#cbd5e1", fontsize=7.2, va="center", weight="bold")
    ax.plot([x0 + 4.2, x0 + w - 1.2], [y_q0, y_q0], color="#64748b", lw=1.0, zorder=5)
    ax.plot([x0 + 4.2, x0 + w - 1.2], [y_q1, y_q1], color="#64748b", lw=1.0, zorder=5)
    
    # Headers
    ax.text(x0 + 6.2, y0 + h - 1.2, "Feature", color="#38bdf8", fontsize=5.8, ha="center")
    ax.text(x0 + 14.0, y0 + h - 1.2, "Variational", color="#f59e0b", fontsize=5.8, ha="center")
    ax.text(x0 + 20.8, y0 + h - 1.2, "Entangle", color="#38bdf8", fontsize=5.8, ha="center")
    
    # Gates Phi
    for yq in [y_q0, y_q1]:
        ax.add_patch(patches.Rectangle((x0 + 4.8, yq - 1.5), 2.8, 3.0, facecolor="#0284c7", edgecolor="#ffffff", lw=0.6, zorder=6))
        ax.text(x0 + 6.2, yq, r"$\Phi_i$", color="#ffffff", fontsize=6.6, ha="center", va="center", weight="bold", zorder=7)
        
        # Gates Ry, Rz
        ax.add_patch(patches.Rectangle((x0 + 9.5, yq - 1.5), 3.8, 3.0, facecolor="#ca8a04", edgecolor="#ffffff", lw=0.6, zorder=6))
        ax.text(x0 + 11.4, yq, r"$R_y(\theta)$", color="#ffffff", fontsize=6.0, ha="center", va="center", weight="bold", zorder=7)
        ax.add_patch(patches.Rectangle((x0 + 14.2, yq - 1.5), 3.8, 3.0, facecolor="#b45309", edgecolor="#ffffff", lw=0.6, zorder=6))
        ax.text(x0 + 16.1, yq, r"$R_z(\phi)$", color="#ffffff", fontsize=6.0, ha="center", va="center", weight="bold", zorder=7)
        
    # CNOT
    ax.plot([x0 + 20.8, x0 + 20.8], [y_q0, y_q1], color="#38bdf8", lw=1.2, zorder=6)
    ax.plot([x0 + 20.8], [y_q0], marker="o", color="#38bdf8", markersize=3.6, zorder=7)
    ax.add_patch(patches.Circle((x0 + 20.8, y_q1), radius=1.1, facecolor="#07152b", edgecolor="#38bdf8", lw=1.0, zorder=7))
    ax.text(x0 + 20.8, y_q1, "+", color="#38bdf8", fontsize=7.2, ha="center", va="center", weight="black", zorder=8)


def draw_circuit_2d(ax, x0, y0, w, h):
    """3-Qubit QCNN for 2D Plate: Cyclic Ring Entanglement"""
    y_qs = [y0 + h * 0.78, y0 + h * 0.50, y0 + h * 0.22]
    labels = [r"$|q_0\rangle$", r"$|q_1\rangle$", r"$|q_2\rangle$"]
    
    for i, yq in enumerate(y_qs):
        ax.text(x0 + 1.0, yq, labels[i], color="#cbd5e1", fontsize=7.2, va="center", weight="bold")
        ax.plot([x0 + 4.2, x0 + w - 1.2], [yq, yq], color="#64748b", lw=1.0, zorder=5)
        
        ax.add_patch(patches.Rectangle((x0 + 4.8, yq - 1.4), 2.6, 2.8, facecolor="#0284c7", edgecolor="#ffffff", lw=0.6, zorder=6))
        ax.text(x0 + 6.1, yq, r"$\Phi_i$", color="#ffffff", fontsize=6.2, ha="center", va="center", weight="bold", zorder=7)
        
        ax.add_patch(patches.Rectangle((x0 + 8.2, yq - 1.4), 3.0, 2.8, facecolor="#ca8a04", edgecolor="#ffffff", lw=0.6, zorder=6))
        ax.text(x0 + 9.7, yq, r"$R_y$", color="#ffffff", fontsize=6.2, ha="center", va="center", weight="bold", zorder=7)

    # CNOT q0 -> q1
    ax.plot([x0 + 13.2, x0 + 13.2], [y_qs[0], y_qs[1]], color="#38bdf8", lw=1.1, zorder=6)
    ax.plot([x0 + 13.2], [y_qs[0]], marker="o", color="#38bdf8", markersize=3.0, zorder=7)
    ax.add_patch(patches.Circle((x0 + 13.2, y_qs[1]), radius=1.0, facecolor="#07152b", edgecolor="#38bdf8", lw=0.9, zorder=7))
    ax.text(x0 + 13.2, y_qs[1], "+", color="#38bdf8", fontsize=6.5, ha="center", va="center", weight="black", zorder=8)
    
    # CNOT q1 -> q2
    ax.plot([x0 + 17.0, x0 + 17.0], [y_qs[1], y_qs[2]], color="#38bdf8", lw=1.1, zorder=6)
    ax.plot([x0 + 17.0], [y_qs[1]], marker="o", color="#38bdf8", markersize=3.0, zorder=7)
    ax.add_patch(patches.Circle((x0 + 17.0, y_qs[2]), radius=1.0, facecolor="#07152b", edgecolor="#38bdf8", lw=0.9, zorder=7))
    ax.text(x0 + 17.0, y_qs[2], "+", color="#38bdf8", fontsize=6.5, ha="center", va="center", weight="black", zorder=8)

    # Circular Return: q2 -> q0 (Arc loop)
    arc_x = x0 + 20.8
    ax.plot([arc_x, arc_x + 2.0, arc_x + 2.0, arc_x], [y_qs[2], y_qs[2] + 1.2, y_qs[0] - 1.2, y_qs[0]], color="#f59e0b", lw=1.1, zorder=6)
    ax.plot([arc_x], [y_qs[2]], marker="o", color="#f59e0b", markersize=3.0, zorder=7)
    ax.add_patch(patches.Circle((arc_x, y_qs[0]), radius=1.0, facecolor="#07152b", edgecolor="#f59e0b", lw=0.9, zorder=7))
    ax.text(arc_x, y_qs[0], "+", color="#f59e0b", fontsize=6.5, ha="center", va="center", weight="black", zorder=8)


def draw_circuit_3d(ax, x0, y0, w, h):
    """4-Qubit PI-QNN for 3D Solid: Triaxial Channels + Full Entanglement Matrix"""
    y_qs = [y0 + h * (0.83 - 0.22 * i) for i in range(4)]
    labels = [r"$|q_0\rangle$", r"$|q_1\rangle$", r"$|q_2\rangle$", r"$|q_3\rangle$"]
    
    for i, yq in enumerate(y_qs):
        ax.text(x0 + 0.8, yq, labels[i], color="#cbd5e1", fontsize=6.8, va="center", weight="bold")
        ax.plot([x0 + 4.0, x0 + w - 1.2], [yq, yq], color="#64748b", lw=0.9, zorder=5)
        
        ax.add_patch(patches.Rectangle((x0 + 4.5, yq - 1.2), 2.2, 2.4, facecolor="#0284c7", edgecolor="#ffffff", lw=0.5, zorder=6))
        ax.text(x0 + 5.6, yq, r"$\Phi$", color="#ffffff", fontsize=5.8, ha="center", va="center", weight="bold", zorder=7)
        
        ax.add_patch(patches.Rectangle((x0 + 7.4, yq - 1.2), 2.6, 2.4, facecolor="#ca8a04", edgecolor="#ffffff", lw=0.5, zorder=6))
        ax.text(x0 + 8.7, yq, r"$R_y$", color="#ffffff", fontsize=5.8, ha="center", va="center", weight="bold", zorder=7)
        
        ax.add_patch(patches.Rectangle((x0 + 10.6, yq - 1.2), 2.6, 2.4, facecolor="#b45309", edgecolor="#ffffff", lw=0.5, zorder=6))
        ax.text(x0 + 11.9, yq, r"$R_z$", color="#ffffff", fontsize=5.8, ha="center", va="center", weight="bold", zorder=7)

    # Entanglement Ladder
    connections = [(0, 1, 14.5), (1, 2, 17.0), (2, 3, 19.5), (3, 0, 22.0)]
    for src, dst, cx in connections:
        y_src = y_qs[src]
        y_dst = y_qs[dst]
        ax.plot([x0 + cx, x0 + cx], [y_src, y_dst], color="#38bdf8", lw=1.0, zorder=6)
        ax.plot([x0 + cx], [y_src], marker="o", color="#38bdf8", markersize=2.6, zorder=7)
        ax.add_patch(patches.Circle((x0 + cx, y_dst), radius=0.9, facecolor="#07152b", edgecolor="#38bdf8", lw=0.8, zorder=7))
        ax.text(x0 + cx, y_dst, "+", color="#38bdf8", fontsize=5.6, ha="center", va="center", weight="black", zorder=8)


def generate_magazine_page_6():
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

    # Canvas Background[cite: 4]
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
    ax.text(6.5, 118.8, "CHAPTER VI • FRONTIER QUANTUM AI INVERSION & MULTI-STATE DECOUPLING",
            color=c_gold_glow, fontsize=9.2, weight="heavy", ha="left", zorder=4)
    ax.text(6.5, 114.8, "PI-QNN Physics-Informed Variational Circuits & Dimensional Ansatz",
            color=c_white, fontsize=14.2, weight="black", ha="left", zorder=4)
    ax.text(6.5, 111.8, "Resolving non-invertible 3D parameters by mapping continuum mechanics onto dynamic quantum states.",
            color=c_muted, fontsize=9.0, weight="medium", ha="left", zorder=4)

    # ------------------------------------------------------------------
    # SECTION A: Quantum AI Pipeline Flowchart
    # ------------------------------------------------------------------
    card_pipeline = FancyBboxPatch((6, 80.5), 88, 29.5, boxstyle="round,pad=0.3,rounding_size=0.8",
                                   facecolor=c_subcard, edgecolor="#254778", lw=1.2, zorder=3)
    ax.add_patch(card_pipeline)

    ax.text(8.5, 106.8, "1. INVERSE PROBLEM RESOLUTION PIPELINE: ADMITTANCE -> HEALTH STATE",
            color=c_gold_glow, fontsize=9.6, weight="heavy", ha="left", zorder=4)

    flow_y = 89.0
    boxes = [
        ("Spectral Data", 8.5, r"$\Delta\overline{Y}(\omega)$ Vector"),
        ("Feature Map", 26.5, r"$\Phi(x)$ Pauli-Z"),
        ("Ansatz [θ]", 44.5, "Variational VQC"),
        ("Measurement", 62.5, r"Expectation $\langle Z_i \rangle$"),
        ("Health State", 80.5, r"$\hat{S}(d, \Delta K, \eta_b)$")
    ]
    b_w, b_h = 13.0, 11.5

    for idx, (label_top, x_p, label_bot) in enumerate(boxes):
        box = FancyBboxPatch((x_p, flow_y), b_w, b_h, boxstyle="round,pad=0.1,rounding_size=0.3",
                             facecolor="#07152b", edgecolor=c_border, lw=1.0, zorder=4)
        ax.add_patch(box)
        ax.text(x_p + b_w/2, flow_y + b_h*0.70, label_top, color=c_cyan, fontsize=7.8, weight="bold", ha="center", zorder=5)
        ax.text(x_p + b_w/2, flow_y + b_h*0.30, label_bot, color=c_white, fontsize=7.4, weight="bold", ha="center", zorder=5)
        
        if idx < len(boxes) - 1:
            ax.annotate("", xy=(x_p + b_w + 4.8, flow_y + b_h/2), xytext=(x_p + b_w + 0.2, flow_y + b_h/2),
                        arrowprops=dict(arrowstyle="->", color=c_gold_glow, lw=1.3), zorder=6)

    ax.text(50.0, 83.2, r"Differential Input Mapping: $\vec{x} = [\mathrm{Re}(\Delta \overline{Y}), \mathrm{Im}(\Delta \overline{Y})]$ where $\Delta \overline{Y} = \overline{Y}_{\mathrm{measured}} - \overline{Y}_0$",
            color=c_white, fontsize=8.2, weight="semibold", ha="center", zorder=5)

    # ------------------------------------------------------------------
    # SECTION B: Dimensional Quantum Circuits (Native Vector Drawing)
    # ------------------------------------------------------------------
    card_ansatz = FancyBboxPatch((6, 37.0), 88, 41.5, boxstyle="round,pad=0.3,rounding_size=0.8",
                                 facecolor=c_subcard, edgecolor=c_border, lw=1.2, zorder=3)
    ax.add_patch(card_ansatz)

    ax.text(8.5, 75.2, "2. DIMENSIONAL ANSATZ ARCHITECTURES & QUANTUM CIRCUIT TOPOLOGY",
            color=c_gold_glow, fontsize=9.6, weight="heavy", ha="left", zorder=4)

    # Box A: 1D Beam (2 Qubits)
    ax.add_patch(FancyBboxPatch((7.5, 38.5), 27.5, 34.5, boxstyle="round,pad=0.2,rounding_size=0.5",
                                facecolor="#07152b", edgecolor=c_cyan, lw=1.0, zorder=4))
    ax.text(21.2, 70.2, "A. 1D Beam (2 Qubits)", color=c_gold_glow, fontsize=8.6, weight="bold", ha="center", zorder=5)
    ax.text(21.2, 67.2, "Stiffness & Damping Inversion", color=c_muted, fontsize=7.4, style="italic", ha="center", zorder=5)
    
    draw_circuit_1d(ax, 8.5, 47.0, 25.5, 17.5)
    
    ax.text(21.2, 43.5, r"$\sum \langle \hat{O}_1 \rangle \rightarrow \hat{d}$ (Crack Depth)", color=c_white, fontsize=7.4, weight="bold", ha="center", zorder=5)
    ax.text(21.2, 40.5, r"$\sum \langle \hat{O}_2 \rangle \rightarrow \hat{\eta}$ (Damping Loss)", color=c_cyan, fontsize=7.4, weight="bold", ha="center", zorder=5)

    # Box B: 2D Plate (3 Qubits)
    ax.add_patch(FancyBboxPatch((36.2, 38.5), 27.5, 34.5, boxstyle="round,pad=0.2,rounding_size=0.5",
                                facecolor="#07152b", edgecolor=c_cyan, lw=1.0, zorder=4))
    ax.text(50.0, 70.2, "B. 2D Plate (3 Qubits)", color=c_gold_glow, fontsize=8.6, weight="bold", ha="center", zorder=5)
    ax.text(50.0, 67.2, "Directional Coupled Field", color=c_muted, fontsize=7.4, style="italic", ha="center", zorder=5)
    
    draw_circuit_2d(ax, 37.2, 47.0, 25.5, 17.5)
    
    ax.text(50.0, 43.5, r"$\sum \langle \hat{O}_i \rangle \rightarrow \hat{d}, \hat{\nu}$ (Poisson Coupling)", color=c_white, fontsize=7.4, weight="bold", ha="center", zorder=5)
    ax.text(50.0, 40.5, r"Cyclic CNOT captures $\overline{Z}_{s,xx} \leftrightarrow \overline{Z}_{s,yy}$", color=c_cyan, fontsize=7.2, weight="bold", ha="center", zorder=5)

    # Box C: 3D Solid (4 Qubits)
    ax.add_patch(FancyBboxPatch((65.0, 38.5), 28.0, 34.5, boxstyle="round,pad=0.2,rounding_size=0.5",
                                facecolor="#07152b", edgecolor=c_cyan, lw=1.0, zorder=4))
    ax.text(79.0, 70.2, "C. 3D Solid (4 Qubits)", color=c_gold_glow, fontsize=8.6, weight="bold", ha="center", zorder=5)
    ax.text(79.0, 67.2, "Triaxial & Thickness Mode", color=c_muted, fontsize=7.4, style="italic", ha="center", zorder=5)
    
    draw_circuit_3d(ax, 66.0, 47.0, 26.0, 17.5)
    
    ax.text(79.0, 43.5, r"$\sum \langle \hat{O}_i \rangle \rightarrow \hat{d}, \hat{\varepsilon}, \hat{t}_b, \hat{\eta}_b$", color=c_white, fontsize=7.4, weight="bold", ha="center", zorder=5)
    ax.text(79.0, 40.5, r"Resolves $\kappa_3$ Dilatation Resonance", color=c_gold_glow, fontsize=7.2, weight="bold", ha="center", zorder=5)

    # ------------------------------------------------------------------
    # SECTION C: Loss Function & PI-QNN Convergence
    # ------------------------------------------------------------------
    card_convergence = FancyBboxPatch((6, 20.0), 88, 15.0, boxstyle="round,pad=0.3,rounding_size=0.8",
                                     facecolor=c_subcard, edgecolor=c_border, lw=1.2, zorder=3)
    ax.add_patch(card_convergence)

    ax.text(8.5, 32.2, "3. HAMILTONIAN LOSS FUNCTION: PI-QNN PHYSICS-INFORMED CONVERGENCE",
            color=c_gold_glow, fontsize=9.2, weight="heavy", ha="left", zorder=4)

    ax.add_patch(FancyBboxPatch((7.5, 21.2), 85.0, 8.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    
    # Mathematical Hamiltonian Loss Equation
    ax.text(50.0, 26.5, r"$\mathcal{H}_{\mathrm{PINN}} = w_1 \sum_{n=1}^{N} \left| \langle \hat{O}_n \rangle_{\vec{\theta}} - \vec{y}_n \right|^2 + w_2 \left| \overline{Y}_{3\mathrm{D}}(\omega; \vec{\theta}) - \overline{Y}_{\mathrm{measured}} \right|^2$",
            color=c_white, fontsize=8.8, ha="center", zorder=5)
    
    ax.text(28.0, 22.8, "Statistical Residual Loss (RMSD)", color=c_cyan, fontsize=7.2, weight="semibold", ha="center", zorder=5)
    ax.text(72.0, 22.8, "Continuum Physics Boundary Constraint (Page 4)", color=c_gold_glow, fontsize=7.2, weight="semibold", ha="center", zorder=5)

    # ------------------------------------------------------------------
    # TRANSITION BADGE: Centered Pill (x = 12 to 88)
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((12.0, 15.2), 76.0, 3.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#08152b", edgecolor="#b45309", lw=0.9, zorder=3))
    ax.text(50.0, 16.9, "QUANTUM AI BENCHMARKS & TRANSDUCER DECOUPLING VALIDATION CONTINUE ON PAGE 7.",
            color=c_gold_glow, fontsize=8.0, weight="bold", style="italic", ha="center", zorder=4)

    # ------------------------------------------------------------------
    # 5. Bottom Running Footer Bar with "Page 6"
    # ------------------------------------------------------------------
    footer_box = FancyBboxPatch((4, 1.2), 92, 9.6, boxstyle="round,pad=0.3,rounding_size=0.6",
                                facecolor=c_card_bg, edgecolor=c_border, linewidth=1.1, zorder=2)
    ax.add_patch(footer_box)

    ax.text(7, 8.2, "GARRF Technical Magazine 1 • Monograph Series • Archive Ref: GARRF-MAG1-SINGBHA-2026.P06",
            color=c_muted, fontsize=8.0, weight="medium", zorder=4)
    ax.text(7, 5.7, "Official Portal: https://garrf.in  •  LinkedIn: https://www.linkedin.com/company/gopalkrishnaadvancedruralresearchfoundation/",
            color=c_cyan, fontsize=7.6, weight="semibold", zorder=4)
    ax.text(7, 3.0, "Dedicated in Honour of Singapore and Bharat",
            color=c_white, fontsize=8.6, weight="bold", ha="left", zorder=4)
    ax.text(93, 3.0, "Page 6",
            color=c_gold_glow, fontsize=9.5, weight="black", ha="right", zorder=4)

    output_filename = "SingBha_Magazine_Page_6_Complete.png"
    plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
    plt.close()

    display(IPImage(filename=output_filename, width=720))
    print(f"Generated successfully: {output_filename} (A4 300 DPI Page 6 Ready)")
    files.download(output_filename)

if __name__ == "__main__":
    generate_magazine_page_6()
