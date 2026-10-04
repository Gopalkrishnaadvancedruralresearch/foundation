import io
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
from PIL import Image
from IPython.display import display, Image as IPImage
from google.colab import files

def generate_magazine_page_8_singbha_emcd():
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
    c_emerald   = "#10b981"
    c_crimson   = "#ef4444"
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
    # 3. Top Header Container Bar (White Fill)
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

    # Header Typography
    ax.text(15, 135.0, "Gopalkrishna Advanced Rural Research Foundation (GARRF)",
            color="#07233b", fontsize=10.6, weight="heavy", ha="left", zorder=3)
    ax.text(15, 132.3, "Dr. APJ Abdul Kalam Research Zero Funding Initiative",
            color="#b45309", fontsize=9.0, weight="bold", style="italic", ha="left", zorder=3)
    ax.text(15, 129.7, "Technical Magazine 1 • Issue 1 • Research Monograph Series",
            color="#334155", fontsize=8.0, weight="semibold", ha="left", zorder=3)

    # Dual Flags: Bharat & Singapore
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
    # 4. Main Content Area Workspace
    # ------------------------------------------------------------------
    content_area = FancyBboxPatch((4, 14.5), 92, 108.5, boxstyle="round,pad=0.5,rounding_size=1.0",
                                  facecolor=c_card_bg, edgecolor=c_border, linewidth=1.2, zorder=2)
    ax.add_patch(content_area)

    for cx, cy in [(6, 120.5), (94, 120.5), (6, 17.0), (94, 17.0)]:
        ax.plot([cx], [cy], marker="+", color=c_cyan, markersize=7.0, alpha=0.7, zorder=3)

    # Chapter Header
    ax.text(6.5, 118.8, "CHAPTER VIII • SingBha EMCD ARCHITECTURE & TIME-DOMAIN METROLOGY",
            color=c_gold_glow, fontsize=9.2, weight="heavy", ha="left", zorder=4)
    ax.text(6.5, 114.8, "SingBha Electro-Mechanical Coupled Dynamics & Waveform Evolution",
            color=c_white, fontsize=14.0, weight="black", ha="left", zorder=4)
    ax.text(6.5, 111.8, "Dual-domain impedance-to-guided-wave transduction across progressive fracture health states.",
            color=c_muted, fontsize=8.8, weight="medium", ha="left", zorder=4)

    # ------------------------------------------------------------------
    # SECTION A: SingBha EMCD Analytical Framework & Transduction Physics
    # ------------------------------------------------------------------
    card_emcd = FancyBboxPatch((6, 73.0), 88, 37.0, boxstyle="round,pad=0.3,rounding_size=0.8",
                               facecolor=c_subcard, edgecolor="#254778", lw=1.2, zorder=3)
    ax.add_patch(card_emcd)

    ax.text(8.5, 106.8, "1. SingBha EMCD FORMULATION: COUPLED IMPEDANCE-TO-WAVE DYNAMICS",
            color=c_gold_glow, fontsize=9.6, weight="heavy", ha="left", zorder=4)

    # Sub-Box 1: Analytical Formulation
    ax.add_patch(FancyBboxPatch((7.5, 74.8), 41.5, 30.0, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(9.0, 101.8, "Dual-Domain SingBha Wave Equation:", color=c_cyan, fontsize=8.2, weight="bold", zorder=5)
    ax.text(9.0, 97.2, r"$\mathbf{M}\ddot{\mathbf{u}} + \mathbf{C}\dot{\mathbf{u}} + \mathbf{K}_{\mathrm{eff}}(d)\mathbf{u} = \mathbf{\Theta} V(t) + \mathbf{F}_{\mathrm{EMCD}}(t)$",
            color=c_white, fontsize=7.8, zorder=5)
    ax.text(9.0, 93.0, r"$\mathbf{F}_{\mathrm{EMCD}}(t) = \mathcal{F}^{-1}\left\{ \overline{Y}_{3\mathrm{D}}(\omega) \cdot Z_{\mathrm{probe}}(\omega) V(\omega) \right\}$",
            color=c_gold_glow, fontsize=7.8, zorder=5)
    ax.text(9.0, 88.5, "• Boundary-Coupled Strain Transduction:", color=c_white, fontsize=7.6, weight="bold", zorder=5)
    ax.text(9.0, 85.5, r"  $\varepsilon_{11}(x,t) = \frac{d_{31}}{h} V(t) \ast h_{\mathrm{bond}}(t) - \frac{\tau_b(x,t)}{G_b}$",
            color=c_muted, fontsize=7.6, zorder=5)
    ax.text(9.0, 81.5, r"• Group Velocity Softening: $c_g(d) = c_0 \sqrt{1 - \gamma_d (d/t_s)^2}$",
            color=c_cyan, fontsize=7.6, weight="bold", zorder=5)
    ax.text(9.0, 77.2, "• Direct conversion of high-frequency admittance to A0/S0 Lamb waves.",
            color=c_muted, fontsize=7.0, style="italic", zorder=5)

    # Sub-Box 2: Physical Transducer Interaction Schematic
    ax.add_patch(FancyBboxPatch((50.5, 74.8), 42.0, 30.0, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(71.5, 101.8, "Transducer Coupled Field Geometry", color=c_cyan, fontsize=8.4, weight="bold", ha="center", zorder=5)

    # Substrate Plate
    sub_x, sub_y, sub_w, sub_h = 53.0, 82.0, 37.0, 7.0
    ax.add_patch(patches.Rectangle((sub_x, sub_y), sub_w, sub_h, facecolor="#475569", edgecolor="#94a3b8", lw=1.0, zorder=5))
    ax.text(sub_x + 2.0, sub_y + 2.2, r"Waveguide Substrate $t_s$", color=c_white, fontsize=7.0, weight="bold", zorder=6)

    # Adhesive Bond
    ax.add_patch(patches.Rectangle((56.0, sub_y + sub_h), 12.0, 1.2, facecolor="#d97706", edgecolor="#ffffff", lw=0.4, zorder=6))
    ax.text(62.0, sub_y + sub_h + 0.3, r"Bond $t_b, G_b$", color="#ffffff", fontsize=5.8, ha="center", weight="bold", zorder=7)

    # Actuator PZT
    ax.add_patch(patches.Rectangle((56.0, sub_y + sub_h + 1.2), 12.0, 3.2, facecolor=c_pzt, edgecolor="#ffffff", lw=0.6, zorder=6))
    ax.text(62.0, sub_y + sub_h + 2.6, "SingBha PZT Actuator", color="#ffffff", fontsize=6.4, ha="center", weight="bold", zorder=7)

    # Guided Wave Packets
    ax.annotate("", xy=(77.0, sub_y + sub_h/2), xytext=(68.5, sub_y + sub_h/2),
                arrowprops=dict(arrowstyle="->", color=c_cyan, lw=1.5), zorder=7)
    ax.text(73.5, sub_y + sub_h/2 + 1.6, r"Wave Packet $u(x,t)$", color=c_cyan, fontsize=6.8, ha="center", weight="bold", zorder=7)

    # Crack Notch
    crack_x = 81.5
    ax.add_patch(patches.Polygon([[crack_x - 0.8, sub_y + sub_h],
                                  [crack_x, sub_y + sub_h - 4.5],
                                  [crack_x + 0.8, sub_y + sub_h]],
                                 facecolor=c_crimson, edgecolor="#ffffff", lw=0.6, zorder=7))
    ax.text(crack_x, sub_y + sub_h + 1.5, r"Crack $d$", color=c_crimson, fontsize=6.8, ha="center", weight="bold", zorder=7)

    # Tone Burst Excitation Label
    ax.text(71.5, 76.5, "5.5-Cycle Hanning-Windowed Tone Burst Excitation (150 kHz)",
            color=c_gold_glow, fontsize=7.2, weight="bold", ha="center", zorder=5)

    # ------------------------------------------------------------------
    # SECTION B: Multi-State Waveform Evolution (S0 to S4 Signals)
    # ------------------------------------------------------------------
    card_wave = FancyBboxPatch((6, 36.0), 88, 35.5, boxstyle="round,pad=0.3,rounding_size=0.8",
                               facecolor=c_subcard, edgecolor=c_border, lw=1.2, zorder=3)
    ax.add_patch(card_wave)

    ax.text(8.5, 68.5, "2. TIME-DOMAIN WAVEFORM DISPERSION & ATTENUATION (S₀ → S₄)",
            color=c_cyan, fontsize=9.6, weight="heavy", ha="left", zorder=4)

    # Sub-Box 1: Primary Time-Domain Waveforms
    ax.add_patch(FancyBboxPatch((7.5, 37.5), 53.0, 29.0, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(34.0, 63.8, "SingBha EMCD Experimental Guided-Wave Packets", color=c_gold_glow, fontsize=8.2, weight="bold", ha="center", zorder=5)

    # Axes for Waveforms with dedicated margins
    wx, wy, ww, wh = 13.5, 41.0, 44.5, 19.5
    ax.plot([wx, wx + ww], [wy, wy], color="#64748b", lw=0.8, zorder=5)
    ax.plot([wx, wx], [wy - 1.0, wy + wh], color="#64748b", lw=0.8, zorder=5)
    ax.text(wx + ww/2, wy - 2.5, r"Time of Flight $t$ ($\mu\mathrm{s}$)", color=c_muted, fontsize=6.6, ha="center", zorder=5)
    ax.text(wx - 2.8, wy + wh/2, "Amplitude (V)", color=c_muted, fontsize=6.6, va="center", rotation=90, zorder=5)

    # Waveform traces
    t = np.linspace(0, 100, 300)
    def tone_burst(t_arr, t0, amp):
        sig = np.sin(2 * np.pi * 0.08 * (t_arr - t0)) * np.exp(-((t_arr - t0)/12.0)**2)
        return amp * sig

    w_s0 = tone_burst(t, 25.0, 3.8) + tone_burst(t, 65.0, 2.8)
    w_s4 = tone_burst(t, 29.0, 2.2) + tone_burst(t, 52.0, 1.6) + tone_burst(t, 72.0, 1.2)

    px_w = wx + (t / 100.0) * ww
    py_s0 = wy + wh*0.50 + (w_s0 / 8.0) * (wh*0.45)
    py_s4 = wy + wh*0.50 + (w_s4 / 8.0) * (wh*0.45)

    ax.plot(px_w, py_s0, color="#10b981", lw=1.2, label="Pristine S0", zorder=6)
    ax.plot(px_w, py_s4, color="#ef4444", lw=1.2, linestyle="--", label="Damaged S4", zorder=7)

    # Annotations on Waveform Plot
    ax.annotate("Direct A0 Wave", xy=(wx + 0.28*ww, wy + wh*0.88), xytext=(wx + 0.12*ww, wy + wh*0.92),
                arrowprops=dict(arrowstyle="->", color="#10b981", lw=0.8), fontsize=6.0, color="#10b981", weight="bold", zorder=8)
    ax.annotate("Crack Reflection\n(Echo)", xy=(wx + 0.52*ww, wy + wh*0.68), xytext=(wx + 0.44*ww, wy + wh*0.84),
                arrowprops=dict(arrowstyle="->", color="#ef4444", lw=0.8), fontsize=5.8, color="#ef4444", weight="bold", zorder=8)
    ax.annotate(r"$\Delta t_{\mathrm{delay}}$ (Phase Lag)", xy=(wx + 0.30*ww, wy + wh*0.40), xytext=(wx + 0.35*ww, wy + wh*0.22),
                arrowprops=dict(arrowstyle="->", color=c_cyan, lw=0.8), fontsize=5.8, color=c_cyan, weight="bold", zorder=8)

    ax.text(wx + ww - 1.0, wy + wh - 1.5, "— S₀ Baseline\n-- S₄ Critical", color=c_white, fontsize=6.0, ha="right", zorder=8)

    # Sub-Box 2: Waveform Extraction Parameter Benchmarks
    ax.add_patch(FancyBboxPatch((62.0, 37.5), 30.5, 29.0, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))
    ax.text(77.2, 63.8, "Wave Feature Extraction", color=c_gold_glow, fontsize=8.0, weight="bold", ha="center", zorder=5)

    wave_metrics = [
        ("Time of Flight (TOF):", r"$\Delta t = 4.2\,\mu\mathrm{s}$ lag at S₄"),
        ("Energy Transmission:", r"$E/E_0 = 42.6\%$ (-7.4 dB)"),
        ("Crack Reflection Coeff:", r"$R_c = 0.38$ at 0.80 $t_s$ depth"),
        ("SingBha Wave Metric:", r"$\mathcal{M}_{\mathrm{EMCD}} = \alpha \frac{\Delta t}{t_0} + \beta \frac{\Delta E}{E_0}$"),
        ("Dual Inversion Fid:", r"PI-QNN Fit: $R^2 = 0.994$")
    ]
    for i, (m_lbl, m_val) in enumerate(wave_metrics):
        my = 59.8 - i * 4.6
        ax.text(63.2, my, m_lbl, color=c_cyan, fontsize=6.8, weight="bold", zorder=5)
        ax.text(63.2, my - 2.1, m_val, color=c_white if i == 3 else c_muted, fontsize=6.6, weight="bold" if i == 3 else "normal", zorder=5)

    # ------------------------------------------------------------------
    # SECTION C: Coupled Impedance-Guided Wave Validation Summary
    # ------------------------------------------------------------------
    card_summary = FancyBboxPatch((6, 20.2), 88, 14.8, boxstyle="round,pad=0.3,rounding_size=0.8",
                                  facecolor=c_subcard, edgecolor=c_border, lw=1.2, zorder=3)
    ax.add_patch(card_summary)

    ax.text(8.5, 32.2, "3. SingBha EMCD VALIDATION & MULTI-DOMAIN FUSION SUMMARY",
            color=c_gold_glow, fontsize=9.2, weight="heavy", ha="left", zorder=4)

    ax.add_patch(FancyBboxPatch((7.5, 21.2), 85.0, 8.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#081427", edgecolor="#204575", lw=0.9, zorder=4))

    ax.text(9.2, 27.4, r"• Dual-Domain Synthesis: High-frequency admittance spectra predict guided-wave arrival times with $\pm 0.8\%$ precision.",
            color=c_white, fontsize=7.2, weight="medium", zorder=5)
    ax.text(9.2, 24.8, "• Crack Localization: Time-of-flight echo reflection maps crack position x_c along the waveguide within ±0.6 mm.",
            color=c_muted, fontsize=7.0, zorder=5)
    ax.text(9.2, 22.2, "• Multi-Modal Inversion: Combining EMI spectra with EMCD waveforms eliminates remaining inverse ambiguities.",
            color=c_cyan, fontsize=7.0, weight="bold", zorder=5)

    # ------------------------------------------------------------------
    # TRANSITION BADGE: Continuing Series Pill
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((10.0, 15.2), 80.0, 3.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#08152b", edgecolor="#b45309", lw=0.9, zorder=3))
    ax.text(50.0, 16.9, "SingBha SENSING MATRICES, FIELD DEPLOYMENTS & INDUSTRIAL VALIDATION CONTINUE ON PAGE 9.",
            color=c_gold_glow, fontsize=7.6, weight="bold", style="italic", ha="center", zorder=4)

    # ------------------------------------------------------------------
    # 5. Bottom Running Footer Bar with "Page 8"
    # ------------------------------------------------------------------
    footer_box = FancyBboxPatch((4, 1.2), 92, 9.6, boxstyle="round,pad=0.3,rounding_size=0.6",
                                facecolor=c_card_bg, edgecolor=c_border, linewidth=1.1, zorder=2)
    ax.add_patch(footer_box)

    ax.text(7, 8.2, "GARRF Technical Magazine 1 • Monograph Series • Archive Ref: GARRF-MAG1-SINGBHA-2026.P08",
            color=c_muted, fontsize=8.0, weight="medium", zorder=4)
    ax.text(7, 5.7, "Official Portal: https://garrf.in  •  LinkedIn: https://www.linkedin.com/company/gopalkrishnaadvancedruralresearchfoundation/",
            color=c_cyan, fontsize=7.6, weight="semibold", zorder=4)
    ax.text(7, 3.0, "Dedicated in Honour of Singapore and Bharat",
            color=c_white, fontsize=8.6, weight="bold", ha="left", zorder=4)
    ax.text(93, 3.0, "Page 8",
            color=c_gold_glow, fontsize=9.5, weight="black", ha="right", zorder=4)

    output_filename = "SingBha_Magazine_Page_8_EMCD.png"
    plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
    plt.close()

    display(IPImage(filename=output_filename, width=720))
    print(f"Generated successfully: {output_filename} (A4 300 DPI SingBha EMCD Page 8 Ready)")
    files.download(output_filename)

if __name__ == "__main__":
    generate_magazine_page_8_singbha_emcd()
