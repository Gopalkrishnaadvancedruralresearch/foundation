import io
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

def generate_magazine_page_1():
    # ------------------------------------------------------------------
    # 1. Page Geometry: International A4 at 300 DPI (8.27 x 11.69 in)
    # ------------------------------------------------------------------
    fig = plt.figure(figsize=(8.27, 11.69), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 141.4)  # Aspect ratio 1 : sqrt(2)
    ax.axis('off')

    # Color Palette matching the GARRF Monograph Series
    c_abyss     = "#020712"
    c_card_bg   = "#081326"
    c_card_in   = "#0c1d38"
    c_gold      = "#f59e0b"
    c_gold_glow = "#fbbf24"
    c_cyan      = "#38bdf8"
    c_green     = "#10b981"
    c_purple    = "#c084fc"
    c_white     = "#ffffff"
    c_border    = "#1d3863"
    c_muted     = "#cbd5e1"

    # Base Background Canvas
    ax.add_patch(patches.Rectangle((0, 0), 100, 141.4, facecolor=c_abyss, zorder=0))
    ax.add_patch(patches.Circle((50, 75), radius=48, color="#0b2447", alpha=0.35, zorder=1))

    # ------------------------------------------------------------------
    # 2. Sacred Watermark: Dharmachakra 24-Spoke Circular Imprint
    # ------------------------------------------------------------------
    cx_w, cy_w, r_w = 50.0, 72.0, 32.0
    ax.add_patch(patches.Circle((cx_w, cy_w), radius=r_w, facecolor="none",
                                edgecolor="#38bdf8", lw=1.2, alpha=0.10, zorder=1))
    ax.add_patch(patches.Circle((cx_w, cy_w), radius=r_w*0.93, facecolor="none",
                                edgecolor="#38bdf8", lw=0.8, alpha=0.08, zorder=1))
    ax.add_patch(patches.Circle((cx_w, cy_w), radius=r_w*0.28, facecolor="none",
                                edgecolor="#fbbf24", lw=1.1, alpha=0.12, zorder=1))
    ax.add_patch(patches.Circle((cx_w, cy_w), radius=r_w*0.08, facecolor="#38bdf8",
                                edgecolor="none", alpha=0.14, zorder=1))
    for i in range(24):
        theta = np.deg2rad(i * 15.0)
        x_in  = cx_w + (r_w * 0.28) * np.cos(theta)
        y_in  = cy_w + (r_w * 0.28) * np.sin(theta)
        x_out = cx_w + (r_w * 0.93) * np.cos(theta)
        y_out = cy_w + (r_w * 0.93) * np.sin(theta)
        ax.plot([x_in, x_out], [y_in, y_out], color="#38bdf8", lw=0.75, alpha=0.09, zorder=1)

    # ------------------------------------------------------------------
    # 3. Top Header Container Bar (White Fill)
    # ------------------------------------------------------------------
    header_box = FancyBboxPatch((4, 126.8), 92, 11.8, boxstyle="round,pad=0.5,rounding_size=1.0",
                                facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1.2, zorder=2)
    ax.add_patch(header_box)

    # Fetch live GARRF logo
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
        ax.text(9.5, 132.6, "G", color=c_gold_glow, fontsize=13, weight="black", ha="center", va="center", zorder=4)

    # Header Typography
    ax.text(15, 135.0, "Gopalkrishna Advanced Rural Research Foundation (GARRF)",
            color="#07233b", fontsize=10.0, weight="heavy", ha="left", zorder=3)
    ax.text(15, 132.4, "Dr. APJ Abdul Kalam Research Zero Funding Initiative",
            color="#b45309", fontsize=8.4, weight="bold", style="italic", ha="left", zorder=3)
    ax.text(15, 129.8, "Technical Magazine 1 • Issue 1 • Research Monograph Series",
            color="#475569", fontsize=7.2, ha="left", zorder=3)

    # Dual Flags: Bharat (Left) & Singapore (Right)
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
    # 4. Main Content Area: Table of Contents & Monograph Directory
    # ------------------------------------------------------------------
    content_area = FancyBboxPatch((4, 14.5), 92, 108.5, boxstyle="round,pad=0.5,rounding_size=1.0",
                                  facecolor=c_card_bg, edgecolor=c_border, linewidth=1.2, zorder=2)
    ax.add_patch(content_area)

    for cx, cy in [(6, 120.5), (94, 120.5), (6, 17.0), (94, 17.0)]:
        ax.plot([cx], [cy], marker="+", color=c_cyan, markersize=7.0, alpha=0.7, zorder=3)

    # Header Banner inside Content Area
    ax.text(6.5, 118.8, "MONOGRAPH DIRECTORY • TABLE OF CONTENTS",
            color=c_gold_glow, fontsize=8.8, weight="heavy", ha="left", zorder=4)
    ax.text(6.5, 114.8, "Technical Architecture & Complete Monograph Index",
            color=c_white, fontsize=13.6, weight="black", ha="left", zorder=4)
    ax.text(6.5, 111.8, "A structured directory indexing 24 comprehensive pages from continuum formulations to quantum AI frontiers.",
            color=c_muted, fontsize=8.2, weight="medium", ha="left", zorder=4)

    # ------------------------------------------------------------------
    # 2-COLUMN TABLE OF CONTENTS (Pages 2 to 24)
    # ------------------------------------------------------------------
    col_w, col_h = 42.5, 87.5
    y_grid = 21.5

    left_entries = [
        ("Page 2",  "GARRF Committee Tree, 5 Divisions & Lab Manifesto", "Org Roster, 250+ Simulators, 97-3% Reality", c_gold_glow),
        ("Page 3",  "Chapter III: 1D Beam & 2D Plate Admittance Models", "Liang 1D Rod & Bhalla-Soh Biaxial Dynamic Models", c_cyan),
        ("Page 4",  "Chapter IV: 3D Continuum Tensors & Shear-Lag", "Annamdas 3D Solvers, Thickness Dilatation Pole", c_cyan),
        ("Page 5",  "Chapter V: Damage Metrology & Statistical Indices", "RMSD, MAPD, CCD Formulations & Inversion Limits", c_cyan),
        ("Page 6",  "Chapter VI: Frontier Quantum AI Inversion (PI-QNN)", "Variational Quantum Circuits & Hamiltonian Loss", c_purple),
        ("Page 7",  "Chapter VII: Decoupling Benchmarks & Spectral Fit", "Decoupling Micro-Cracks, Bond Slip & Thermal Drift", c_purple),
        ("Page 8",  "Chapter VIII: SingBha EMCD Dual-Domain Architecture", "Impedance-to-Wave Transduction & Guided Packets", c_green),
        ("Page 9",  "Section 8: Scientific Pillars of SingBha-EMCD (Part I)", "Spatial Gradient, Crack Trajectory & Thermal Drift", c_gold_glow),
        ("Page 10", "Section 8: Scientific Pillars of SingBha-EMCD (Part II)", "3D Continuum, Dual-Horizon Reach & Virtual Ground", c_gold_glow),
        ("Page 11", "Section 9: Master 8D Technical Benchmark Matrix", "Classical EMI vs SingBha-EMCD Structural Matrix", c_green),
        ("Page 12", "Section 10: Micro-Crack Mechanics & Singularities", "Traction-Free Boundaries & Mathematical Divergence", c_cyan),
        ("Page 13", "Section 11: Waveform Propagation Dynamics (WFP)", "Lamb Waves, S0/A0 Modes & Dynamic Charge Capture", c_cyan)
    ]

    right_entries = [
        ("Page 14", "Section 12: Applied Engineering Structures Matrix", "Civil, Marine, Aerospace & Spacecraft Systems", c_gold_glow),
        ("Page 15", "Section 13: Experimental Protocol & Virtual Ground", "Front-End TIA Hardware & Systematic 4-Step Guide", c_cyan),
        ("Page 16", "Section 14: Multi-Physics FEA Variational Solvers", "Coupled Matrices, Quarter-Point Tip Mesh & Accuracy", c_cyan),
        ("Page 17", "Section 15: AI Ingestion & ARJUN Knowledge Bridging", "ADIA Pipeline, MAKG Graph Triples & Causal Audit", c_purple),
        ("Page 18", "Section 16: Pedagogical Deep-Dive: Why EMCD Wins", "2 Active PZTs + 10 Taps vs $50k LCR & Node 7 Proof", c_green),
        ("Page 19", "Section 17: Benchmark Matrix & National Economic Scale", "Capital Efficiency: Bharat Rural & Singapore Smart", c_green),
        ("Page 20", "Section 18: MAKG Diagnostic Flow & Verification", "4-Stage Causal Flow & 3 Core Deduction Proofs", c_purple),
        ("Page 21", "Section 19: ARJUN 4-Agent Autonomous Architecture", "Consensus Engine, False-Alarm Rejection & Orders", c_purple),
        ("Page 22", "Section 20: Real-World Deployments & Field Validation", "Bharat Freight Corridor & Singapore MRT Subsea Line", c_cyan),
        ("Page 23", "Section 21-22: Standardization Roadmap & Kalam Charter", "IEEE P21451, IRC/Singapore Norms & Kalam History", c_gold_glow),
        ("Page 24", "Section 23: Grand Finale Innovation Compendium", "Quantum AI Flagship, ARJUN, Drones, Fab & Yashokirti", c_gold_glow)
    ]

    def render_column(entries, x_left, y_top):
        ax.add_patch(FancyBboxPatch((x_left, y_grid), col_w, col_h, boxstyle="round,pad=0.3,rounding_size=0.6",
                                    facecolor=c_card_in, edgecolor=c_border, linewidth=1.1, zorder=3))
        card_step = 7.15
        for idx, (p_num, p_title, p_desc, p_color) in enumerate(entries):
            curr_y = y_top - idx * card_step
            ax.add_patch(FancyBboxPatch((x_left + 1.2, curr_y - 6.2), col_w - 2.4, 6.0, boxstyle="round,pad=0.15,rounding_size=0.3",
                                        facecolor="#050e20", edgecolor="#1a355e", linewidth=0.7, zorder=4))
            ax.add_patch(FancyBboxPatch((x_left + 2.0, curr_y - 2.8), 7.8, 2.2, boxstyle="round,pad=0.1,rounding_size=0.2",
                                        facecolor="#0c234b", edgecolor=p_color, linewidth=0.7, zorder=5))
            ax.text(x_left + 5.9, curr_y - 1.7, p_num, color=p_color, fontsize=5.8, weight="black", ha="center", va="center", zorder=6)
            ax.text(x_left + 10.8, curr_y - 1.7, p_title, color=c_white, fontsize=5.9, weight="bold", ha="left", va="center", zorder=5)
            ax.text(x_left + 2.2, curr_y - 4.5, p_desc, color=c_muted, fontsize=5.3, ha="left", va="center", zorder=5)

    render_column(left_entries, 6.5, 108.0)
    render_column(right_entries, 51.0, 108.0)

    # Transition Pill
    ax.add_patch(FancyBboxPatch((10.0, 15.2), 80.0, 3.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#08152b", edgecolor="#b45309", lw=0.9, zorder=3))
    ax.text(50.0, 16.9, "GARRF ORGANIZATIONAL COMMITTEE TREE, 5 DIVISIONS & MANIFESTO COMMENCE ON PAGE 2.",
            color=c_gold_glow, fontsize=7.4, weight="bold", style="italic", ha="center", zorder=4)

    # ------------------------------------------------------------------
    # 5. Bottom Running Footer Bar with "Page 1"
    # ------------------------------------------------------------------
    footer_box = FancyBboxPatch((4, 1.2), 92, 9.6, boxstyle="round,pad=0.3,rounding_size=0.6",
                                facecolor=c_card_bg, edgecolor=c_border, linewidth=1.1, zorder=2)
    ax.add_patch(footer_box)

    ax.text(7, 8.2, "GARRF Technical Magazine 1 • Monograph Series • Archive Ref: GARRF-MAG1-SINGBHA-2026.P01",
            color=c_muted, fontsize=7.1, zorder=4)
    ax.text(7, 5.7, "Official Portal: https://garrf.in  •  LinkedIn: https://www.linkedin.com/company/gopalkrishnaadvancedruralresearchfoundation/",
            color=c_cyan, fontsize=6.6, weight="semibold", zorder=4)
    ax.text(7, 3.0, "Dedicated in Honour of Singapore and Bharat",
            color=c_white, fontsize=7.6, weight="bold", ha="left", zorder=4)
    ax.text(93, 3.0, "Page 1",
            color=c_gold_glow, fontsize=8.5, weight="black", ha="right", zorder=4)

    output_filename = "SingBha_Magazine_Page_1_Contents.png"
    plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
    plt.close()

    if IN_COLAB:
        display(IPImage(filename=output_filename, width=720))
        print(f"Generated successfully: {output_filename} (A4 300 DPI Magazine Page 1 Ready with Table of Contents)")
        try:
            files.download(output_filename)
        except Exception:
            pass
    else:
        print(f"Generated successfully: {output_filename}")

if __name__ == "__main__":
    generate_magazine_page_1()
