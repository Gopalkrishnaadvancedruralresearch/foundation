import io
import ssl
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

def fetch_image_safely(url, timeout=7):
    """Safely retrieves remote images bypassing SSL verification and Cloudflare/bot blocks."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
        return Image.open(io.BytesIO(resp.read()))

def generate_magazine_page_23():
    # ------------------------------------------------------------------
    # 1. Page Geometry: International A4 at 300 DPI (8.27 x 11.69 in)
    # ------------------------------------------------------------------
    fig = plt.figure(figsize=(8.27, 11.69), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 141.4)
    ax.axis('off')

    # Color Palette matching page1.txt & page2.txt
    c_abyss     = "#020712"
    c_card_bg   = "#061328"
    c_card_in   = "#0b1c38"
    c_gold      = "#f59e0b"
    c_gold_glow = "#fbbf24"
    c_cyan      = "#38bdf8"
    c_green     = "#10b981"
    c_white     = "#ffffff"
    c_border    = "#1e3b68"
    c_muted     = "#cbd5e1"

    # Base Canvas
    ax.add_patch(patches.Rectangle((0, 0), 100, 141.4, facecolor=c_abyss, zorder=0))
    ax.add_patch(patches.Circle((50, 72), radius=48, color="#0b2447", alpha=0.35, zorder=1))

    # ------------------------------------------------------------------
    # 2. Watermark: Dharmachakra 24-Spoke Circular Imprint
    # ------------------------------------------------------------------
    cx_w, cy_w, r_w = 50.0, 72.0, 32.0
    ax.add_patch(patches.Circle((cx_w, cy_w), radius=r_w, facecolor="none",
                                edgecolor="#38bdf8", lw=1.2, alpha=0.08, zorder=1))
    ax.add_patch(patches.Circle((cx_w, cy_w), radius=r_w*0.93, facecolor="none",
                                edgecolor="#38bdf8", lw=0.8, alpha=0.06, zorder=1))
    ax.add_patch(patches.Circle((cx_w, cy_w), radius=r_w*0.28, facecolor="none",
                                edgecolor="#fbbf24", lw=1.1, alpha=0.10, zorder=1))
    for i in range(24):
        theta = np.deg2rad(i * 15.0)
        x_in  = cx_w + (r_w * 0.28) * np.cos(theta)
        y_in  = cy_w + (r_w * 0.28) * np.sin(theta)
        x_out = cx_w + (r_w * 0.93) * np.cos(theta)
        y_out = cy_w + (r_w * 0.93) * np.sin(theta)
        ax.plot([x_in, x_out], [y_in, y_out], color="#38bdf8", lw=0.7, alpha=0.07, zorder=1)

    # ------------------------------------------------------------------
    # 3. Top Header Bar (White Fill)
    # ------------------------------------------------------------------
    header_box = FancyBboxPatch((4, 126.8), 92, 11.8, boxstyle="round,pad=0.5,rounding_size=1.0",
                                facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1.2, zorder=2)
    ax.add_patch(header_box)

    # Live Logo Fetch with safe fallback
    logo_drawn = False
    try:
        img_logo = fetch_image_safely("https://garrf.in/kalam-zero-lab/logo.jpeg")
        ax.imshow(img_logo, extent=[5.5, 13.5, 127.8, 137.4], zorder=4)
        logo_drawn = True
    except Exception:
        pass

    if not logo_drawn:
        ax.add_patch(patches.Circle((9.5, 132.6), radius=3.4, facecolor="#030c1b", edgecolor=c_gold, linewidth=1.4, zorder=3))
        ax.text(9.5, 132.6, "G", color=c_gold_glow, fontsize=13, weight="black", ha="center", va="center", zorder=4)

    # Header Typography
    ax.text(15, 135.0, "Gopalkrishna Advanced Rural Research Foundation (GARRF)",
            color="#07233b", fontsize=10.2, weight="heavy", ha="left", zorder=3)
    ax.text(15, 132.3, "Dr. APJ Abdul Kalam Research Zero Funding Initiative",
            color="#b45309", fontsize=8.6, weight="bold", style="italic", ha="left", zorder=3)
    ax.text(15, 129.7, "Technical Magazine 1 • Issue 1 • Research Monograph Series",
            color="#475569", fontsize=7.4, ha="left", zorder=3)

    # Flags (Bharat & Singapore)
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
    # 4. Outer Structural Container
    # ------------------------------------------------------------------
    main_card = FancyBboxPatch((4, 14.0), 92, 109.5, boxstyle="round,pad=0.5,rounding_size=1.0",
                               facecolor=c_card_bg, edgecolor=c_border, linewidth=1.2, zorder=2)
    ax.add_patch(main_card)

    # Section Banner
    ax.text(50, 120.2, "SECTION 21 • STANDARDIZATION ROADMAP & NEW SECTOR HORIZONS",
            color=c_gold_glow, fontsize=8.2, weight="black", ha="center",
            bbox=dict(boxstyle="round,pad=0.35,rounding_size=0.6", facecolor="#1a1202", edgecolor=c_gold, lw=1.1), zorder=3)

    ax.text(50, 116.6, "Emerging Engineering Horizons & Adaptive Civil Compliance",
            color=c_white, fontsize=12.2, weight="black", ha="center", zorder=3)
    ax.text(50, 114.2, "Laying the Theoretical & Experimental Groundwork Adaptable to Indian (IRC) and Singapore Guidelines",
            color=c_cyan, fontsize=7.2, style="italic", ha="center", zorder=3)

    # ------------------------------------------------------------------
    # SECTION 21.1: 3 Compliance & Research Framework Cards
    # ------------------------------------------------------------------
    framework_cards = [
        {
            "x": 6.0,
            "title": "IEEE P21451 READINESS",
            "lines": [
                "• Standardized transducer telemetry",
                "• Open digital TEDS architecture",
                "• Multi-frequency nodal acquisition"
            ]
        },
        {
            "x": 37.0,
            "title": "A NEW RESEARCH SECTOR",
            "lines": [
                "• Potential for extensive literature",
                "• Surpassing classical EMI bounds",
                "• Open computational mechanics"
            ]
        },
        {
            "x": 68.0,
            "title": "CROSS-BORDER ADAPTABILITY",
            "lines": [
                "• Adaptable to IRC SP:108 criteria",
                "• Aligned with Singapore benchmarks",
                "• Universal structural monitoring"
            ]
        }
    ]

    for c in framework_cards:
        ax.add_patch(FancyBboxPatch((c["x"], 102.5), 26.0, 9.6, boxstyle="round,pad=0.3,rounding_size=0.5",
                                    facecolor=c_card_in, edgecolor=c_gold, linewidth=1.0, zorder=3))
        ax.text(c["x"] + 13.0, 109.8, c["title"], color=c_gold_glow, fontsize=7.0, weight="heavy", ha="center", zorder=4)
        ax.plot([c["x"] + 2.5, c["x"] + 23.5], [108.4, 108.4], color=c_border, lw=0.7, zorder=4)
        y_text = 106.6
        for line in c["lines"]:
            ax.text(c["x"] + 13.0, y_text, line, color=c_white, fontsize=6.2, weight="semibold", ha="center", zorder=4)
            y_text -= 1.8

    # ------------------------------------------------------------------
    # SECTION 21.2: Kalam Research Zero Funding Charter + Photograph
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((6.0, 52.0), 54.0, 48.0, boxstyle="round,pad=0.4,rounding_size=0.6",
                                facecolor="#050e20", edgecolor=c_gold, linewidth=1.2, zorder=3))

    ax.text(8.0, 97.4, "21.2 DR. APJ ABDUL KALAM RESEARCH ZERO FUNDING CHARTER",
            color=c_gold_glow, fontsize=7.4, weight="black", zorder=4)
    ax.text(8.0, 95.3, "MISSION: DEMOCRATIZING CIVIL SENSING & RURAL RESILIENCE",
            color=c_cyan, fontsize=6.8, weight="bold", zorder=4)
    ax.plot([8.0, 57.5], [94.0, 94.0], color="#172b47", lw=0.8, zorder=4)

    charter_items = [
        ("• Zero Funding Ethos:", " Pioneering scientific discovery without financial or grant bottlenecks."),
        ("• Rural Infrastructure Inclusion:", " Bringing high-precision vigilance to remote bridges and culverts."),
        ("• Open Hardware Blueprint:", " Royalty-free schematics and embedded firmware for all engineers."),
        ("• Bilateral Scholarly Roots:", " Inspired by foundational research collaborations across Bharat & Singapore."),
        ("• Edge Diagnostic ARJUN AI:", " Low-cost on-site processing eliminating recurring subscription models."),
        ("• Student & Scholar Empowerment:", " Enabling university research labs to build analyzers under $15.")
    ]

    y_point = 91.5
    for title, desc in charter_items:
        ax.text(8.2, y_point, title, color=c_gold_glow, fontsize=6.8, weight="bold", zorder=4)
        ax.text(8.2, y_point - 2.1, desc, color=c_white, fontsize=6.3, zorder=4)
        y_point -= 6.4

    # Right container: Historic Image Box
    ax.add_patch(FancyBboxPatch((62.0, 52.0), 32.0, 48.0, boxstyle="round,pad=0.4,rounding_size=0.6",
                                facecolor="#051024", edgecolor=c_cyan, linewidth=1.2, zorder=3))

    kalam_drawn = False
    try:
        k_img = fetch_image_safely("https://garrf.in/kalam-zero-lab/kalam_garrf.jpg")
        ax.imshow(k_img, extent=[63.0, 93.0, 56.5, 98.0], aspect='auto', zorder=4)
        kalam_drawn = True
    except Exception:
        pass

    if not kalam_drawn:
        ax.add_patch(FancyBboxPatch((64.0, 58.0), 28.0, 38.0, boxstyle="round,pad=0.3",
                                    facecolor="#0b1c38", edgecolor=c_gold, lw=1.0, zorder=4))
        ax.text(78.0, 78.0, "DR. APJ ABDUL KALAM\n&\nDR. ANNAMDAS V. G. M.",
                color=c_white, fontsize=7.2, weight="black", ha="center", va="center", linespacing=1.3, zorder=5)

    # Caption banner below picture
    ax.add_patch(FancyBboxPatch((63.0, 53.0), 30.0, 3.8, boxstyle="round,pad=0.2",
                                facecolor="#020712", edgecolor=c_gold, lw=0.8, zorder=4))
    ax.text(78.0, 54.9, "Visionary Guidance: Dr. APJ Abdul Kalam & Dr. Annamdas",
            color=c_gold_glow, fontsize=5.8, weight="bold", ha="center", va="center", zorder=5)

    # ------------------------------------------------------------------
    # SECTION 22: Monograph Concluding Synthesis & Roadmap
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((6.0, 25.5), 88.0, 24.5, boxstyle="round,pad=0.35,rounding_size=0.6",
                                facecolor=c_card_in, edgecolor=c_green, linewidth=1.3, zorder=3))

    ax.text(8.0, 47.6, "SECTION 22 • MONOGRAPH CONCLUDING SYNTHESIS & FUTURE OUTLOOK",
            color=c_green, fontsize=7.6, weight="black", zorder=4)
    ax.plot([8.0, 92.0], [46.3, 46.3], color="#17384a", lw=0.8, zorder=4)

    synthesis_bullets = [
        ("• Economic Democratization:", " Over 99% cost reduction, transforming expensive specialized test setups into accessible toolkits."),
        ("• Thermal Drift Resistance:", " Validated stable baselines across ambient shifts, addressing classical EMI temperature drift."),
        ("• Extended Lead Feasibility:", " Virtual-ground designs offer promising cable noise suppression for long-distance tunnel monitoring."),
        ("• A Catalytic Research Branch:", " Paving the pathway for an expansive domain of scholarly publications and standard-compliant tools.")
    ]
    y_syn = 43.8
    for title, desc in synthesis_bullets:
        ax.text(8.0, y_syn, title, color=c_gold_glow, fontsize=6.8, weight="heavy", zorder=4)
        ax.text(28.5, y_syn, desc, color=c_white, fontsize=6.4, weight="normal", zorder=4)
        y_syn -= 4.2

    # ------------------------------------------------------------------
    # SECTION 5: AI Assistant Box & Next Page Navigation
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((6.0, 19.5), 88.0, 4.8, boxstyle="round,pad=0.25,rounding_size=0.4",
                                facecolor="#030d1e", edgecolor=c_cyan, linewidth=1.0, zorder=3))
    ax.text(50.0, 22.4, "Arjun, our AI Assistant, can answer all technical and mathematical questions about this monograph.",
            color=c_white, fontsize=6.6, weight="bold", ha="center", zorder=4)
    ax.text(50.0, 20.6, "Access links and query consoles are indexed on the final destination page (Page 24).",
            color=c_cyan, fontsize=6.0, ha="center", zorder=4)

    ax.add_patch(FancyBboxPatch((6.0, 15.0), 88.0, 3.6, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#020712", edgecolor=c_gold, linewidth=1.0, zorder=3))
    ax.text(50.0, 16.8, "PAGE 24: FINAL MONOGRAPH DESTINATION • 6 ARJUN LINK BOXES & COLOPHON CONTINUES NEXT ➔",
            color=c_gold_glow, fontsize=6.4, weight="black", ha="center", va="center", zorder=4)

    # ------------------------------------------------------------------
    # 6. Bottom Running Footer Bar with "Page 23"
    # ------------------------------------------------------------------
    footer_box = FancyBboxPatch((4, 1.2), 92, 9.6, boxstyle="round,pad=0.3,rounding_size=0.6",
                                facecolor=c_card_bg, edgecolor=c_border, linewidth=1.1, zorder=2)
    ax.add_patch(footer_box)

    ax.text(7, 8.2, "GARRF Technical Magazine 1 • Monograph Series • Archive Ref: GARRF-MAG1-SINGBHA-2026.P23",
            color=c_muted, fontsize=7.1, zorder=4)
    ax.text(7, 5.7, "Official Portal: https://garrf.in  •  LinkedIn: gopalkrishnaadvancedruralresearchfoundation  •  Lab: https://garrf.in/kalam-zero-lab/",
            color=c_cyan, fontsize=6.4, weight="semibold", zorder=4)
    ax.text(7, 3.0, "Dedicated in Honour of Singapore and Bharat",
            color=c_white, fontsize=7.6, weight="bold", ha="left", zorder=4)
    ax.text(93, 3.0, "Page 23",
            color=c_gold_glow, fontsize=8.5, weight="black", ha="right", zorder=4)

    output_filename = "SingBha_Magazine_Page_23_CleanDark.png"
    plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
    plt.close()

    if IN_COLAB:
        display(IPImage(filename=output_filename, width=720))
        print(f"Generated successfully: {output_filename} (A4 300 DPI Clean Dark Edition)")
        try:
            files.download(output_filename)
        except Exception:
            pass
    else:
        print(f"Generated successfully: {output_filename}")

if __name__ == "__main__":
    generate_magazine_page_23()
