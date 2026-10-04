import io
import urllib.request
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib.patches import FancyBboxPatch, Polygon

try:
  from google.colab import files
  from IPython.display import Image as IPImage, display

  IN_COLAB = True
except ImportError:
  IN_COLAB = False


def generate_cover_page():
  # ------------------------------------------------------------------
  # 1. Page Canvas Geometry: A4 (8.27 x 11.69 inches) at 300 DPI
  # ------------------------------------------------------------------
  fig = plt.figure(figsize=(8.27, 11.69), dpi=300)
  ax = fig.add_axes([0, 0, 1, 1])
  ax.set_xlim(0, 100)
  ax.set_ylim(0, 141.4)
  ax.axis('off')

  # Color Palette
  c_abyss = '#020914'  # Deep navy-black field
  c_card_bg = '#061326'  # Midnight container surface
  c_gold = '#f59e0b'  # Amber Gold
  c_gold_glow = '#fbbf24'  # Bright Gold
  c_cyan = '#38bdf8'  # Signal Cyan
  c_green = '#10b981'  # Emerald Green
  c_red = '#ef4444'  # Signal Red
  c_white = '#ffffff'  # Crisp White
  c_border = '#142d54'  # Card Border
  c_muted = '#94a3b8'  # Slate typography

  # Base Canvas
  ax.add_patch(
      patches.Rectangle((0, 0), 100, 141.4, facecolor=c_abyss, zorder=0)
  )

  # Ambient radial glow behind central stage
  ax.add_patch(
      patches.Circle((50, 75), radius=46, color='#0b2447', alpha=0.40, zorder=1)
  )

  # ------------------------------------------------------------------
  # 2. Diagonal 45° "GOPALKRISHNA" Watermark Only (No G/K Initials)
  # ------------------------------------------------------------------
  ax.text(
      50.0,
      74.0,
      'GOPALKRISHNA',
      color='#38bdf8',
      fontsize=64,
      fontweight='black',
      ha='center',
      va='center',
      rotation=45,
      alpha=0.28,
      zorder=3,
  )

  ax.text(
      32.0,
      106.0,
      'GOPALKRISHNA',
      color='#38bdf8',
      fontsize=38,
      fontweight='heavy',
      ha='center',
      va='center',
      rotation=45,
      alpha=0.18,
      zorder=3,
  )

  ax.text(
      68.0,
      42.0,
      'GOPALKRISHNA',
      color='#38bdf8',
      fontsize=38,
      fontweight='heavy',
      ha='center',
      va='center',
      rotation=45,
      alpha=0.18,
      zorder=3,
  )

  # ------------------------------------------------------------------
  # 3. Header Container Box (White Fill)[cite: 4]
  # ------------------------------------------------------------------
  header_box = FancyBboxPatch(
      (4, 126.8),
      92,
      11.8,
      boxstyle='round,pad=0.5,rounding_size=1.0',
      facecolor='#ffffff',
      edgecolor='#cbd5e1',
      linewidth=1.2,
      zorder=2,
  )
  ax.add_patch(header_box)

  # Fetch live GARRF logo[cite: 4]
  logo_drawn = False
  logo_url = 'https://garrf.in/kalam-zero-lab/logo.jpeg'
  try:
    req = urllib.request.Request(
        logo_url, headers={'User-Agent': 'Mozilla/5.0'}
    )
    with urllib.request.urlopen(req, timeout=8) as response:
      logo_data = response.read()
      img = Image.open(io.BytesIO(logo_data))
      ax.imshow(img, extent=[5.5, 13.5, 127.8, 137.4], zorder=4)
      logo_drawn = True
  except Exception:
    pass

  if not logo_drawn:
    ax.add_patch(
        patches.Circle(
            (9.5, 132.6),
            radius=3.4,
            facecolor='#030c1b',
            edgecolor=c_gold,
            linewidth=1.4,
            zorder=3,
        )
    )
    ax.text(
        9.5,
        132.6,
        'G',
        color=c_gold_glow,
        fontsize=13,
        weight='black',
        ha='center',
        va='center',
        zorder=4,
    )

  # Header Typography[cite: 4]
  ax.text(
      15,
      135.0,
      'Gopalkrishna Advanced Rural Research Foundation (GARRF)',
      color='#07233b',
      fontsize=10.0,
      weight='heavy',
      ha='left',
      zorder=3,
  )
  ax.text(
      15,
      132.4,
      'Dr. APJ Abdul Kalam Research Zero Funding Initiative',
      color='#b45309',
      fontsize=8.4,
      weight='bold',
      style='italic',
      ha='left',
      zorder=3,
  )
  ax.text(
      15,
      129.8,
      'Technical Magazine 1 • Issue 1 • Research Monograph Series',
      color='#475569',
      fontsize=7.2,
      ha='left',
      zorder=3,
  )

  # Flags: Bharat (Left) & Singapore (Right)[cite: 4]
  flag_y = 129.8
  # Bharat Flag[cite: 4]
  ax.add_patch(
      patches.Rectangle(
          (81.0, flag_y + 2.3), 5.4, 1.15, facecolor='#ff9933', zorder=3
      )
  )
  ax.add_patch(
      patches.Rectangle(
          (81.0, flag_y + 1.15),
          5.4,
          1.15,
          facecolor='#ffffff',
          edgecolor='#cbd5e1',
          lw=0.3,
          zorder=3,
      )
  )
  ax.add_patch(
      patches.Rectangle(
          (81.0, flag_y), 5.4, 1.15, facecolor='#128807', zorder=3
      )
  )
  ax.add_patch(
      patches.Circle(
          (83.7, flag_y + 1.72),
          radius=0.46,
          facecolor='none',
          edgecolor='#000088',
          lw=0.55,
          zorder=4,
      )
  )
  ax.plot(
      [83.7],
      [flag_y + 1.72],
      marker='o',
      color='#000088',
      markersize=0.8,
      zorder=5,
  )

  # Singapore Flag[cite: 4]
  ax.add_patch(
      patches.Rectangle(
          (87.8, flag_y + 1.72), 5.4, 1.72, facecolor='#dc2626', zorder=3
      )
  )
  ax.add_patch(
      patches.Rectangle(
          (87.8, flag_y),
          5.4,
          1.72,
          facecolor='#ffffff',
          edgecolor='#cbd5e1',
          lw=0.3,
          zorder=3,
      )
  )
  ax.add_patch(
      patches.Circle(
          (89.1, flag_y + 2.58), radius=0.58, facecolor='#ffffff', zorder=4
      )
  )
  ax.add_patch(
      patches.Circle(
          (89.4, flag_y + 2.58), radius=0.49, facecolor='#dc2626', zorder=5
      )
  )
  for ang in [0, 72, 144, 216, 288]:
    rad = np.radians(ang)
    ax.plot(
        89.95 + 0.32 * np.cos(rad),
        flag_y + 2.58 + 0.32 * np.sin(rad),
        marker='*',
        color='#ffffff',
        markersize=1.2,
        zorder=6,
    )

  # ------------------------------------------------------------------
  # 4. Monograph Title & "WORLD FIRST" Badge
  # ------------------------------------------------------------------
  ax.text(
      50,
      121.2,
      'WORLD FIRST: 3D CONTINUUM CHARGE DENSITY & QUANTUM AI INTEGRATION IN'
      ' EMI',
      color=c_gold_glow,
      fontsize=7.4,
      weight='black',
      ha='center',
      bbox=dict(
          boxstyle='round,pad=0.35,rounding_size=0.6',
          facecolor='#1a1202',
          edgecolor=c_gold,
          lw=1.2,
      ),
      zorder=4,
  )

  ax.text(
      50,
      114.8,
      'SingBha Electromechanical Charge Density\n(SingBha-EMCD) Technology'
      ' with Wave Form',
      color=c_white,
      fontsize=15.5,
      weight='black',
      ha='center',
      linespacing=1.25,
      zorder=4,
  )

  ax.text(
      50,
      108.4,
      'Structural Health Monitoring & Quantum AI Integration for Bharat',
      color=c_gold_glow,
      fontsize=9.2,
      weight='heavy',
      ha='center',
      zorder=4,
  )

  ax.text(
      50,
      104.2,
      'A World First Paradigm. Uniting Continuum SingBha-EMCD with Quantum AI'
      ' Analytics\nfor Superior Diagnostic Sensitivity & Better Structural'
      ' Health Across Bharat',
      color=c_cyan,
      fontsize=7.2,
      style='italic',
      ha='center',
      linespacing=1.3,
      zorder=4,
  )

  # ------------------------------------------------------------------
  # 5. Central Hero Visualization Box
  # ------------------------------------------------------------------
  hero_box = FancyBboxPatch(
      (4, 46.5),
      92,
      54.5,
      boxstyle='round,pad=0.5,rounding_size=1.0',
      facecolor=c_card_bg,
      edgecolor=c_border,
      linewidth=1.2,
      zorder=2,
  )
  ax.add_patch(hero_box)

  # Margin Telemetry Pins
  for cy in [90, 75, 60]:
    ax.plot([4, 6.5], [cy, cy], color=c_cyan, lw=1.0, alpha=0.6, zorder=3)
    ax.plot(
        [6.5],
        [cy],
        marker='o',
        color=c_cyan,
        markersize=2.5,
        alpha=0.8,
        zorder=3,
    )
    ax.plot([93.5, 96], [cy, cy], color=c_cyan, lw=1.0, alpha=0.6, zorder=3)
    ax.plot(
        [93.5],
        [cy],
        marker='o',
        color=c_cyan,
        markersize=2.5,
        alpha=0.8,
        zorder=3,
    )

  ax.text(
      6.8,
      97.8,
      'FIGURE 1: SINGBHA-EMCD 3D CONTINUUM ENGINE WITH QUANTUM AI INFERENCE',
      color=c_gold_glow,
      fontsize=6.8,
      weight='heavy',
      zorder=4,
  )
  ax.text(
      93.2,
      97.8,
      'QUANTUM-AI SHM',
      color=c_cyan,
      fontsize=6.8,
      weight='heavy',
      ha='right',
      zorder=4,
  )
  ax.plot([6.8, 93.2], [96.4, 96.4], color=c_border, lw=1.0, zorder=4)

  # Concentric Field Rays
  for r_arc in [16, 24, 32]:
    arc = patches.Arc(
        (50, 70),
        2 * r_arc,
        r_arc * 0.8,
        angle=0,
        theta1=20,
        theta2=160,
        edgecolor=c_cyan,
        lw=0.8,
        linestyle='--',
        alpha=0.35,
        zorder=3,
    )
    ax.add_patch(arc)

  # Host Structure Plate in Isometric Perspective
  host_top = Polygon(
      [[18, 64], [67, 77], [82, 69], [33, 56]],
      closed=True,
      facecolor='#11223b',
      edgecolor='#244470',
      lw=1.4,
      zorder=4,
  )
  host_left = Polygon(
      [[18, 64], [33, 56], [33, 50], [18, 58]],
      closed=True,
      facecolor='#091426',
      edgecolor='#1b3357',
      lw=1.1,
      zorder=4,
  )
  host_right = Polygon(
      [[33, 56], [82, 69], [82, 63], [33, 50]],
      closed=True,
      facecolor='#0c1b33',
      edgecolor='#1b3357',
      lw=1.1,
      zorder=4,
  )
  ax.add_patch(host_top)
  ax.add_patch(host_left)
  ax.add_patch(host_right)
  ax.text(
      20,
      52.2,
      'Host Structural Substrate (High-Strength Steel / Concrete Girder / CFRP)',
      color='#7a93ae',
      fontsize=6.6,
      weight='bold',
      zorder=5,
  )

  # Incipient Micro-Crack Notch
  crack = Polygon(
      [[38.5, 60], [40.5, 62], [41.5, 59]],
      closed=True,
      facecolor='#020712',
      edgecolor=c_red,
      lw=1.3,
      zorder=5,
  )
  ax.add_patch(crack)
  ax.text(
      40,
      54.2,
      'Incipient Micro-Crack Mouth\nσnn=0, τnt=0  =>  Zs -> 0',
      color=c_red,
      fontsize=6.4,
      weight='bold',
      ha='center',
      zorder=6,
  )
  ax.annotate(
      '',
      xy=(40, 59.5),
      xytext=(40, 57.0),
      arrowprops=dict(arrowstyle='->', color=c_red, lw=1.2),
      zorder=6,
  )

  # Viscoelastic Adhesive Bondline
  adh_poly = Polygon(
      [[34.5, 68.5], [52, 73.5], [60, 68.5], [42.5, 63.5]],
      closed=True,
      facecolor='#6b3a04',
      edgecolor=c_gold,
      lw=0.9,
      zorder=5,
  )
  ax.add_patch(adh_poly)

  # Segmented PZT Quadrant Transducer (Q1, Q2, Q3, Q4)
  pzt_poly = Polygon(
      [[34.5, 70.0], [52, 75.0], [60, 70.0], [42.5, 65.0]],
      closed=True,
      facecolor='#0d3b66',
      edgecolor=c_cyan,
      lw=1.5,
      zorder=6,
  )
  ax.add_patch(pzt_poly)

  # Pad dividing lines
  ax.plot([43.2, 47.2], [72.5, 67.5], color=c_gold_glow, lw=1.4, zorder=7)
  ax.plot([38.5, 56.0], [67.5, 72.5], color=c_gold_glow, lw=1.4, zorder=7)

  # Quadrant Pad Labels
  ax.text(
      39.5, 69.5, 'Q1', color=c_white, fontsize=6.2, weight='black', zorder=8
  )
  ax.text(
      47.0, 71.5, 'Q2', color=c_white, fontsize=6.2, weight='black', zorder=8
  )
  ax.text(
      47.0, 67.5, 'Q3', color=c_white, fontsize=6.2, weight='black', zorder=8
  )
  ax.text(
      54.5, 69.5, 'Q4', color=c_white, fontsize=6.2, weight='black', zorder=8
  )

  # Near-Field Gradient Singularity Spike (∇D3)
  ax.annotate(
      '',
      xy=(41.5, 79.5),
      xytext=(41.5, 67.2),
      arrowprops=dict(arrowstyle='->', color=c_gold_glow, lw=2.2),
      zorder=9,
  )
  ax.scatter(
      [41.5], [79.5], color=c_gold_glow, s=45, edgecolor=c_white, zorder=10
  )
  ax.text(
      37.5,
      83.2,
      'Near-Field Singularity: ∇D3\nDifferential Spike > 24 dB SNR\n(Local'
      ' Horizon r ≤ 1.0 m)',
      color=c_gold_glow,
      fontsize=6.8,
      weight='bold',
      ha='right',
      zorder=10,
      bbox=dict(
          boxstyle='round,pad=0.25',
          facecolor='#140f02',
          edgecolor=c_gold,
          lw=0.9,
      ),
  )

  # Far-Field Radiating Guided Lamb Waves
  for r in [11, 17, 23, 29]:
    arc = patches.Arc(
        (51, 69),
        width=r * 1.8,
        height=r * 0.9,
        angle=18,
        theta1=290,
        theta2=70,
        color=c_green,
        lw=1.4,
        linestyle='--',
        alpha=0.9,
        zorder=5,
    )
    ax.add_patch(arc)

  ax.text(
      91.5,
      81.5,
      'Far-Field Guided Wavefield\n(Lamb Wave Pitch-Catch r > 1.0 m)\nQuantum'
      ' AI Anomaly Classification',
      color='#6ee7b7',
      fontsize=6.6,
      weight='bold',
      ha='right',
      zorder=8,
      bbox=dict(
          boxstyle='round,pad=0.28',
          facecolor='#031f16',
          edgecolor=c_green,
          lw=0.9,
      ),
  )

  # Virtual Ground Interface Callout
  ax.annotate(
      '',
      xy=(58.5, 68),
      xytext=(68, 57.5),
      arrowprops=dict(arrowstyle='<-', color=c_cyan, lw=1.3),
      zorder=9,
  )
  ax.text(
      69,
      55.5,
      'Virtual Ground Interface (0 V)\nIcable = Ccable · (dV/dt) ≈ 0\nZero Drift'
      ' Across 50+ m Cables',
      color=c_cyan,
      fontsize=6.6,
      weight='bold',
      ha='left',
      zorder=9,
      bbox=dict(
          boxstyle='round,pad=0.25',
          facecolor='#04182e',
          edgecolor=c_cyan,
          lw=0.9,
      ),
  )

  # Master Formulation Banner
  ax.text(
      50,
      48.2,
      'Master Formulation:  D3(x, y, ω) = E3 · [ ε33^T(1-jη) - Y11^E d31² (1 -'
      ' Ψx(x,ω)) - Y22^E d32² (1 - Ψy(y,ω)) ]',
      color='#dbeafe',
      fontsize=6.8,
      style='italic',
      ha='center',
      weight='semibold',
      zorder=8,
  )

  # ------------------------------------------------------------------
  # 6. Architectural Panorama: Real-World SHM Applications
  # ------------------------------------------------------------------
  pano_box = FancyBboxPatch(
      (4, 28.5),
      92,
      16.5,
      boxstyle='round,pad=0.4,rounding_size=0.8',
      facecolor='#050e1f',
      edgecolor=c_border,
      linewidth=1.1,
      zorder=2,
  )
  ax.add_patch(pano_box)

  ax.text(
      50.0,
      43.4,
      'STRUCTURAL HEALTH MONITORING (SHM) & QUANTUM AI HORIZONS FOR BHARAT',
      color=c_gold_glow,
      fontsize=7.0,
      weight='black',
      ha='center',
      zorder=4,
  )
  ax.plot([6.8, 93.2], [42.4, 42.4], color='#172b47', lw=0.8, zorder=4)

  # 6A. Aeroplane in Flight
  plane = Polygon(
      [
          [10, 40.0],
          [17, 40.0],
          [22, 39.0],
          [24, 37.5],
          [20, 37.5],
          [14, 38.5],
          [11, 38.5],
      ],
      closed=True,
      facecolor='#38bdf8',
      edgecolor=c_white,
      lw=0.7,
      zorder=5,
  )
  wing_top = Polygon(
      [[15, 39.0], [17, 41.5], [19, 41.5], [17.5, 39.0]],
      closed=True,
      facecolor='#0284c7',
      edgecolor=c_white,
      lw=0.6,
      zorder=6,
  )
  wing_bot = Polygon(
      [[16, 38.2], [18, 36.2], [19.5, 36.2], [18, 38.2]],
      closed=True,
      facecolor='#0284c7',
      edgecolor=c_white,
      lw=0.6,
      zorder=6,
  )
  ax.add_patch(plane)
  ax.add_patch(wing_top)
  ax.add_patch(wing_bot)
  ax.text(
      17,
      31.8,
      'AEROSPACE COMPOSITE\nFuselage & Wing BVID',
      color=c_cyan,
      fontsize=5.8,
      weight='bold',
      ha='center',
      zorder=5,
  )

  # 6B. High-Rise Commercial Towers
  ax.add_patch(
      patches.Rectangle(
          (30, 36.0),
          6.5,
          5.8,
          facecolor='#0e2447',
          edgecolor='#38bdf8',
          lw=0.8,
          zorder=5,
      )
  )
  for r in range(4):
    for c in range(3):
      ax.add_patch(
          patches.Rectangle(
              (30.8 + c * 1.8, 36.5 + r * 1.2),
              1.1,
              0.7,
              facecolor='#7dd3fc',
              alpha=0.85,
              zorder=6,
          )
      )
  ax.add_patch(
      patches.Rectangle(
          (37.5, 36.0),
          5.5,
          4.6,
          facecolor='#0b1b36',
          edgecolor='#38bdf8',
          lw=0.7,
          zorder=5,
      )
  )
  for r in range(3):
    for c in range(2):
      ax.add_patch(
          patches.Rectangle(
              (38.3 + c * 2.0, 36.5 + r * 1.2),
              1.2,
              0.7,
              facecolor='#fde047',
              alpha=0.75,
              zorder=6,
          )
      )
  ax.text(
      36.5,
      31.8,
      'HIGH-RISE TOWERS\nSeismic Drift & Strain',
      color='#bae6fd',
      fontsize=5.8,
      weight='bold',
      ha='center',
      zorder=5,
  )

  # 6C. Hydroelectric Concrete Gravity Dam
  dam = Polygon(
      [[48, 36.0], [51, 41.2], [57, 41.2], [63, 36.0]],
      closed=True,
      facecolor='#10b981',
      edgecolor='#6ee7b7',
      lw=0.9,
      alpha=0.85,
      zorder=5,
  )
  ax.add_patch(dam)
  for spill_x in [53.0, 55.0, 57.0]:
    ax.plot(
        [spill_x, spill_x + 1.2],
        [40.2, 36.0],
        color='#ecfdf5',
        lw=0.7,
        zorder=6,
    )
  ax.text(
      55.5,
      31.8,
      'CONCRETE GRAVITY DAM\nUplift Fissure & ASR Mapping',
      color='#6ee7b7',
      fontsize=5.8,
      weight='bold',
      ha='center',
      zorder=5,
  )

  # 6D. Steel Truss Arch Bridge
  b_left, b_right, b_y = 69.0, 91.0, 36.8
  ax.plot([b_left, b_right], [b_y, b_y], color='#f59e0b', lw=1.2, zorder=5)
  arch_x = np.linspace(b_left, b_right, 30)
  arch_y = b_y + 4.2 * np.sin(np.pi * (arch_x - b_left) / (b_right - b_left))
  ax.plot(arch_x, arch_y, color='#fbbf24', lw=1.2, zorder=5)
  for tx in np.linspace(b_left + 2, b_right - 2, 7):
    ty = b_y + 4.2 * np.sin(np.pi * (tx - b_left) / (b_right - b_left))
    ax.plot([tx, tx], [b_y, ty], color='#fde047', lw=0.7, alpha=0.85, zorder=6)
  ax.text(
      80,
      31.8,
      'STEEL TRUSS BRIDGES\nFatigue & Prestress Monitoring',
      color=c_gold_glow,
      fontsize=5.8,
      weight='bold',
      ha='center',
      zorder=5,
  )

  # ------------------------------------------------------------------
  # 7. Authorship & Executive Credentials
  # ------------------------------------------------------------------
  author_card = FancyBboxPatch(
      (4, 11.2),
      92,
      16.0,
      boxstyle='round,pad=0.5,rounding_size=1.0',
      facecolor=c_card_bg,
      edgecolor=c_border,
      linewidth=1.2,
      zorder=2,
  )
  ax.add_patch(author_card)

  # Dr. Annamdas Credentials (Left)
  ax.text(
      7,
      25.4,
      'Dr. Venu Gopal Madhav Annamdas',
      color=c_white,
      fontsize=8.6,
      weight='bold',
      zorder=4,
  )
  ax.text(
      7,
      23.6,
      'Founder & Chief Scientific Advisor • founder@garrf.in',
      color=c_gold_glow,
      fontsize=6.8,
      weight='bold',
      zorder=4,
  )
  bio_vgm = (
      '• PhD (NTU Singapore) • Post-Doc (Univ. of Pittsburgh, USA)\n•'
      ' MicroMasters (RIT, USA) • M.E. (IISc Bangalore, India)\n• PMP (USA) •'
      ' Fellow in Piezoelectrics, SHM & Quantum AI'
  )
  ax.text(
      7, 16.2, bio_vgm, color=c_muted, fontsize=6.2, linespacing=1.28, zorder=4
  )

  # Vertical Separator
  ax.plot([51, 51], [12.2, 26.2], color=c_border, lw=1.1, zorder=4)

  # Shantanu Annamdas Credentials (Right)
  ax.text(
      54,
      25.4,
      'Shantanu Vasudev Krishna Annamdas',
      color=c_white,
      fontsize=8.6,
      weight='bold',
      zorder=4,
  )
  ax.text(
      54,
      23.6,
      'Chief Executive Officer • ceo@garrf.in',
      color=c_cyan,
      fontsize=6.8,
      weight='bold',
      zorder=4,
  )
  bio_svk = (
      '• Student, Birla Open Minds International School • Youth STEM'
      ' Innovator\n• Stewardship: 250+ Multiphysics Simulators & AI Virtual Labs'
      ' (garrf.in)\n• Co-Author & Co-Architect of SingBha-EMCD & Quantum AI SHM'
  )
  ax.text(
      54, 16.2, bio_svk, color=c_muted, fontsize=6.2, linespacing=1.28, zorder=4
  )

  # ------------------------------------------------------------------
  # 8. Clean Bottom Footer
  # ------------------------------------------------------------------
  footer_box = FancyBboxPatch(
      (4, 1.2),
      92,
      9.0,
      boxstyle='round,pad=0.3,rounding_size=0.6',
      facecolor=c_card_bg,
      edgecolor=c_border,
      linewidth=1.1,
      zorder=2,
  )
  ax.add_patch(footer_box)

  ax.text(
      7,
      7.6,
      'GARRF Technical Magazine 1 • Monograph Series • Archive Ref:'
      ' GARRF-MAG1-SINGBHA-2026.P01',
      color=c_muted,
      fontsize=7.1,
      zorder=4,
  )

  ax.text(
      7,
      4.8,
      'Official Portal: https://garrf.in  •  LinkedIn:'
      ' https://www.linkedin.com/company/gopalkrishnaadvancedruralresearchfoundation/',
      color=c_cyan,
      fontsize=6.8,
      weight='semibold',
      zorder=4,
  )

  ax.text(
      93,
      3.8,
      'Dedicated in Honour of Singapore and Bharat',
      color=c_white,
      fontsize=7.6,
      weight='bold',
      ha='right',
      zorder=4,
  )

  output_filename = 'SingBha_Cover_Page_A4_Clean_GK.png'
  plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
  plt.close()

  if IN_COLAB:
    display(IPImage(filename=output_filename, width=720))
    print(
        f'Generated successfully: {output_filename} (45° Diagonal Watermark'
        ' Only)'
    )
    files.download(output_filename)
  else:
    print(f'Generated successfully: {output_filename}')


if __name__ == '__main__':
  generate_cover_page()
