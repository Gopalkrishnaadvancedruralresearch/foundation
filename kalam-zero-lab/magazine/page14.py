import io
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
from PIL import Image
from IPython.display import display, Image as IPImage
from google.colab import files

def generate_magazine_page_14_applied_structures():
    # ------------------------------------------------------------------
    # 1. Page Geometry: International A4 at 300 DPI (8.27 x 11.69 in)[cite: 4]
    # ------------------------------------------------------------------
    fig = plt.figure(figsize=(8.27, 11.69), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 141.4)  # Explicit (0, 141.4) to maintain upright orientation
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

    # Section 12 Header[cite: 30]
    ax.text(6.5, 118.8, "SECTION 12 • APPLIED ENGINEERING STRUCTURES & MULTI-DOMAIN ASSET CATALOGUE",
            color=c_gold_glow, fontsize=9.2, weight="heavy", ha="left", zorder=4)
    ax.text(6.5, 114.8, "Applied Engineering Structures: Comprehensive Multi-Domain Matrix",
            color=c_white, fontsize=14.0, weight="black", ha="left", zorder=4)
    ax.text(6.5, 111.8, "Field deployment catalogue across four critical heavy-infrastructure sectors using SingBha-EMCD.",
            color=c_muted, fontsize=8.8, weight="medium", ha="left", zorder=4)

    # ------------------------------------------------------------------
    # 2x2 SECTOR GRID ARCHITECTURE (Sectors 1, 2, 3, 4)[cite: 30]
    # ------------------------------------------------------------------
    grid_w, grid_h = 42.5, 41.5

    sectors_data = [
        # Sector 1: Civil Infrastructure[cite: 30]
        {"col": 6.5, "row": 67.5, "num": "SECTOR 1", "title": "Civil Infrastructure Assets",
         "accent": c_gold_glow,
         "items": [
             ("• Prestressed Girders:", "Tendon slippage, web shear cracking, early hydration."),
             ("• Gravity Dams:", "Hydraulic uplift micro-fissuring, ASR chemical expansion."),
             ("• Nuclear Domes:", "Multi-axial thermal stress, liner debonding, tendon voids."),
             ("• Metro Tunnels:", "Segmental lining convergence, shotcrete spallation.")
         ]},
        
        # Sector 2: Mechanical & Marine[cite: 30]
        {"col": 51.0, "row": 67.5, "num": "SECTOR 2", "title": "Mechanical & Marine Systems",
         "accent": c_cyan,
         "items": [
             ("• Petroleum Tanks (50k bbl):", "Annular plate bottom pitting, hoop-stress fatigue."),
             ("• Pressure Vessels (LNG):", "Cyclic thermal shock, stress corrosion under insulation."),
             ("• Offshore Jacket Platforms:", "Tubular K- and T-joint node splash-zone fatigue."),
             ("• Wind Turbine Flanges:", "Bolt pretension loss, interfacial slip under buffeting.")
         ]},

        # Sector 3: Aerospace Systems[cite: 30]
        {"col": 6.5, "row": 22.0, "num": "SECTOR 3", "title": "Aerospace Flight Structures",
         "accent": c_emerald,
         "items": [
             ("• CFRP Composite Fuselage:", "Barely Visible Impact Damage (BVID), ply delamination."),
             ("• Wing Spar Caps:", "Multi-site fastener hole fatigue, skin-to-stiffener debonding."),
             ("• Titanium Fan Blades:", "Leading-edge micro-fretting, blade root spallation."),
             ("• Landing Gear Struts:", "High-impact forged cylinder cracking, pin overload.")
         ]},

        # Sector 4: Spacecraft & Cryogenics[cite: 30]
        {"col": 51.0, "row": 22.0, "num": "SECTOR 4", "title": "Spacecraft & Cryogenic Systems",
         "accent": "#f43f5e",
         "items": [
             ("• Satellite Panels:", "Honeycomb face-sheet separation, launch acoustic fatigue."),
             ("• Deployable Solar Booms:", "Latch deployment lock verification, thermal micro-buckling."),
             ("• Cryo Tanks (LH2/LOX):", "Thermal shock micro-fissuring, orbital vacuum cycles."),
             ("• SiC Space Telescope Trusses:", "Sub-nanometer structural drift across day/night cycles.")
         ]}
    ]

    for sec in sectors_data:
        sx, sy = sec["col"], sec["row"]
        
        # Outer Card Patch[cite: 30]
        ax.add_patch(FancyBboxPatch((sx, sy), grid_w, grid_h, boxstyle="round,pad=0.3,rounding_size=0.6",
                                    facecolor=c_subcard, edgecolor="#254778", lw=1.1, zorder=3))

        # Inner Subcard Container[cite: 30]
        ax.add_patch(FancyBboxPatch((sx + 1.2, sy + 1.5), grid_w - 2.4, grid_h - 3.0, boxstyle="round,pad=0.2,rounding_size=0.4",
                                    facecolor="#081427", edgecolor="#204575", lw=0.8, zorder=4))

        # Sector Header Pill Banner[cite: 30]
        ax.add_patch(FancyBboxPatch((sx + 2.5, sy + grid_h - 6.8), grid_w - 5.0, 4.5, boxstyle="round,pad=0.1,rounding_size=0.2",
                                    facecolor="#0c234b", edgecolor=sec["accent"], lw=0.7, zorder=5))
        ax.text(sx + grid_w/2, sy + grid_h - 3.8, f"{sec['num']} • {sec['title']}",
                color=sec["accent"], fontsize=7.2, weight="heavy", ha="center", va="center", zorder=6)

        # Content Bullet Points[cite: 30]
        y_text_start = sy + grid_h - 9.8
        for i, (item_hdr, item_desc) in enumerate(sec["items"]):
            curr_y = y_text_start - i * 6.8
            ax.text(sx + 3.0, curr_y, item_hdr, color=c_white, fontsize=6.8, weight="bold", zorder=6)
            ax.text(sx + 3.0, curr_y - 2.6, item_desc, color=c_muted, fontsize=6.1, zorder=6)
            
            if i < 3:
                ax.plot([sx + 3.0, sx + grid_w - 3.0], [curr_y - 4.2, curr_y - 4.2], color="#16305a", lw=0.5, zorder=5)

    # ------------------------------------------------------------------
    # TRANSITION BADGE: Monograph Transition Pill -> Page 15[cite: 32]
    # ------------------------------------------------------------------
    ax.add_patch(FancyBboxPatch((10.0, 15.2), 80.0, 3.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor="#08152b", edgecolor="#b45309", lw=0.9, zorder=3))
    ax.text(50.0, 16.9, "STEP-BY-STEP EXPERIMENTAL PROTOCOL & HARDWARE INTERFACING CONTINUES ON PAGE 15.",
            color=c_gold_glow, fontsize=7.4, weight="bold", style="italic", ha="center", zorder=4)

    # ------------------------------------------------------------------
    # 5. Bottom Running Footer Bar (Normalized to "Page 14")[cite: 4, 30]
    # ------------------------------------------------------------------
    footer_box = FancyBboxPatch((4, 1.2), 92, 9.6, boxstyle="round,pad=0.3,rounding_size=0.6",
                                facecolor=c_card_bg, edgecolor=c_border, linewidth=1.1, zorder=2)
    ax.add_patch(footer_box)

    ax.text(7, 8.2, "GARRF Technical Magazine 1 • Monograph Series • Archive Ref: GARRF-MAG1-SINGBHA-2026.P14",
            color=c_muted, fontsize=8.0, weight="medium", zorder=4)
    ax.text(7, 5.7, "Official Portal: https://garrf.in  •  LinkedIn: https://www.linkedin.com/company/gopalkrishnaadvancedruralresearchfoundation/",
            color=c_cyan, fontsize=7.6, weight="semibold", zorder=4)
    ax.text(7, 3.0, "Dedicated in Honour of Singapore and Bharat",
            color=c_white, fontsize=8.6, weight="bold", ha="left", zorder=4)
    ax.text(93, 3.0, "Page 14",
            color=c_gold_glow, fontsize=9.5, weight="black", ha="right", zorder=4)

    output_filename = "SingBha_Magazine_Page_14_Applied_Structures_Upright.png"
    plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
    plt.close()

    display(IPImage(filename=output_filename, width=720))
    print(f"Generated successfully: {output_filename} (A4 300 DPI Page 14 - Upright & Verified)")
    files.download(output_filename)

if __name__ == "__main__":
    generate_magazine_page_14_applied_structures()
