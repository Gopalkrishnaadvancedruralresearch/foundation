import io
import urllib.request
from google.colab import files
from IPython.display import Image as IPImage, display
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def generate_magazine_page_18_clean():
  # 1. Page Geometry: International A4 at 300 DPI (8.27 x 11.69 in)
  fig = plt.figure(figsize=(8.27, 11.69), dpi=300)
  ax = fig.add_axes([0, 0, 1, 1])
  ax.set_xlim(0, 100)
  ax.set_ylim(0, 141.4)
  ax.axis('off')

  # Monograph Palette Identity
  c_abyss = '#020712'
  c_card_bg = '#081326'
  c_subcard = '#0c1d38'
  c_gold = '#f59e0b'
  c_gold_glow = '#fbbf24'
  c_cyan = '#38bdf8'
  c_emerald = '#10b981'
  c_crimson = '#ef4444'
  c_white = '#ffffff'
  c_border = '#1d3863'
  c_muted = '#cbd5e1'
  c_yellow_node = '#facc15'
  c_gray_wire = '#94a3b8'

  # Base Canvas Background
  ax.add_patch(
      patches.Rectangle((0, 0), 100, 141.4, facecolor=c_abyss, zorder=0)
  )
  ax.add_patch(
      patches.Circle(
          (50, 75), radius=48, color='#0b2447', alpha=0.35, zorder=1
      )
  )

  # 2. Sacred Watermark: Dharmachakra 24-Spoke Circular Imprint
  cx_w, cy_w, r_w = 50.0, 72.0, 32.0
  ax.add_patch(
      patches.Circle(
          (cx_w, cy_w),
          radius=r_w,
          facecolor='none',
          edgecolor='#38bdf8',
          lw=1.2,
          alpha=0.07,
          zorder=1,
      )
  )
  ax.add_patch(
      patches.Circle(
          (cx_w, cy_w),
          radius=r_w * 0.93,
          facecolor='none',
          edgecolor='#38bdf8',
          lw=0.8,
          alpha=0.05,
          zorder=1,
      )
  )
  ax.add_patch(
      patches.Circle(
          (cx_w, cy_w),
          radius=r_w * 0.28,
          facecolor='none',
          edgecolor='#fbbf24',
          lw=1.1,
          alpha=0.08,
          zorder=1,
      )
  )
  ax.add_patch(
      patches.Circle(
          (cx_w, cy_w),
          radius=r_w * 0.08,
          facecolor='#38bdf8',
          edgecolor='none',
          alpha=0.10,
          zorder=1,
      )
  )
  for i in range(24):
    theta = np.deg2rad(i * 15.0)
    x_in = cx_w + (r_w * 0.28) * np.cos(theta)
    y_in = cy_w + (r_w * 0.28) * np.sin(theta)
    x_out = cx_w + (r_w * 0.93) * np.cos(theta)
    y_out = cy_w + (r_w * 0.93) * np.sin(theta)
    ax.plot(
        [x_in, x_out],
        [y_in, y_out],
        color='#38bdf8',
        lw=0.75,
        alpha=0.07,
        zorder=1,
    )

  # 3. Top Header Container Bar (Exact GARRF Monograph Template)[cite: 12]
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

  logo_drawn = False
  logo_url = 'https://garrf.in/kalam-zero-lab/logo.jpeg'
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
        fontsize=14,
        weight='black',
        ha='center',
        va='center',
        zorder=4,
    )

  # Header Titles[cite: 12]
  ax.text(
      15,
      135.0,
      'Gopalkrishna Advanced Rural Research Foundation (GARRF)',
      color='#07233b',
      fontsize=10.8,
      weight='heavy',
      ha='left',
      zorder=3,
  )
  ax.text(
      15,
      132.3,
      'Dr. APJ Abdul Kalam Research Zero Funding Initiative',
      color='#b45309',
      fontsize=9.2,
      weight='bold',
      style='italic',
      ha='left',
      zorder=3,
  )
  ax.text(
      15,
      129.7,
      'Technical Magazine 1 • Issue 1 • Research Monograph Series',
      color='#334155',
      fontsize=8.2,
      weight='semibold',
      ha='left',
      zorder=3,
  )

  # Dual Flags: Bharat & Singapore[cite: 12]
  flag_y = 129.6
  ax.add_patch(
      patches.Rectangle(
          (81.2, flag_y + 2.4), 5.4, 1.2, facecolor='#ff9933', zorder=3
      )
  )
  ax.add_patch(
      patches.Rectangle(
          (81.2, flag_y + 1.2),
          5.4,
          1.2,
          facecolor='#ffffff',
          edgecolor='#cbd5e1',
          lw=0.3,
          zorder=3,
      )
  )
  ax.add_patch(
      patches.Rectangle((81.2, flag_y), 5.4, 1.2, facecolor='#128807', zorder=3)
  )
  ax.add_patch(
      patches.Circle(
          (83.9, flag_y + 1.8),
          radius=0.48,
          facecolor='none',
          edgecolor='#000088',
          lw=0.55,
          zorder=4,
      )
  )
  ax.plot(
      [83.9],
      [flag_y + 1.8],
      marker='o',
      color='#000088',
      markersize=0.8,
      zorder=5,
  )

  ax.add_patch(
      patches.Rectangle(
          (88.0, flag_y + 1.8), 5.4, 1.8, facecolor='#dc2626', zorder=3
      )
  )
  ax.add_patch(
      patches.Rectangle(
          (88.0, flag_y),
          5.4,
          1.8,
          facecolor='#ffffff',
          edgecolor='#cbd5e1',
          lw=0.3,
          zorder=3,
      )
  )
  ax.add_patch(
      patches.Circle(
          (89.3, flag_y + 2.7), radius=0.62, facecolor='#ffffff', zorder=4
      )
  )
  ax.add_patch(
      patches.Circle(
          (89.6, flag_y + 2.7), radius=0.53, facecolor='#dc2626', zorder=5
      )
  )
  for ang in [0, 72, 144, 216, 288]:
    rad = np.radians(ang)
    ax.plot(
        90.15 + 0.35 * np.cos(rad),
        2.7 + flag_y + 0.35 * np.sin(rad),
        marker='*',
        color='#ffffff',
        markersize=1.3,
        zorder=6,
    )

  # 4. Main Content Area Workspace
  content_area = FancyBboxPatch(
      (4, 14.5),
      92,
      108.5,
      boxstyle='round,pad=0.5,rounding_size=1.0',
      facecolor=c_card_bg,
      edgecolor=c_border,
      linewidth=1.2,
      zorder=2,
  )
  ax.add_patch(content_area)

  # Corner Grid Alignment Ticks[cite: 12]
  for cx, cy in [(6, 120.5), (94, 120.5), (6, 17.0), (94, 17.0)]:
    ax.plot(
        [cx],
        [cy],
        marker='+',
        color=c_cyan,
        markersize=7.0,
        alpha=0.7,
        zorder=3,
    )

  # Section 16 Title Block
  ax.text(
      6.5,
      118.8,
      'SECTION 16 • PEDAGOGICAL DEEP-DIVE: WHY EMCD OVER SCALAR EMI?',
      color=c_gold_glow,
      fontsize=9.4,
      weight='heavy',
      ha='left',
      zorder=4,
  )
  ax.text(
      6.5,
      114.6,
      'SingBha-EMCD: Distributed Ground Topology & Flaw Gradient Sensing',
      color=c_white,
      fontsize=13.6,
      weight='black',
      ha='left',
      zorder=4,
  )
  ax.text(
      6.5,
      111.4,
      'Fundamental Definition & Setup: Replacing multiple bulky PZTs with'
      ' distributed electrode tap nodes.',
      color=c_muted,
      fontsize=8.6,
      weight='medium',
      ha='left',
      zorder=4,
  )

  # CARD 1: DEFINITION & CORE PRINCIPLE BANNER (y = 103.2 to 110.0)
  def_card = FancyBboxPatch(
      (6.0, 103.2),
      88.0,
      6.8,
      boxstyle='round,pad=0.2,rounding_size=0.4',
      facecolor='#0b1d3a',
      edgecolor=c_cyan,
      lw=0.9,
      zorder=3,
  )
  ax.add_patch(def_card)
  ax.text(
      7.5,
      108.2,
      'WHAT IS SINGBHA-EMCD?',
      color=c_cyan,
      fontsize=7.4,
      weight='heavy',
      zorder=4,
  )
  ax.text(
      7.5,
      106.1,
      'Electromechanical Charge Divergence (EMCD) is a structural diagnostic'
      ' technique that detects micro-cracks by measuring the',
      color=c_white,
      fontsize=6.2,
      weight='medium',
      zorder=4,
  )
  ax.text(
      7.5,
      104.7,
      'spatial rate-of-change of electric displacement (∇D₃) across a conductive'
      ' host structure, rather than measuring lumped scalar impedance.',
      color=c_white,
      fontsize=6.2,
      weight='medium',
      zorder=4,
  )
  ax.text(
      7.5,
      103.5,
      'Instead of gluing dozens of expensive standalone PZTs, EMCD uses 1-2'
      ' active piezoceramics with an array of passive metallic electrode nodes.',
      color=c_gold_glow,
      fontsize=5.9,
      weight='bold',
      zorder=4,
  )

  # CARD 2: THE 3D TECHNICAL SCHEMATIC (y = 66.5 to 102.0)
  vis_box = FancyBboxPatch(
      (6.0, 66.5),
      88.0,
      35.2,
      boxstyle='round,pad=0.3,rounding_size=0.5',
      facecolor=c_subcard,
      edgecolor='#254778',
      lw=1.0,
      zorder=3,
  )
  ax.add_patch(vis_box)

  ax.text(
      8.0,
      99.8,
      '16.1 TOPOGRAPHICAL ARCHITECTURE: ACTIVE PIEZO-NODES & PASSIVE'
      ' ELECTRODE MATRIX',
      color=c_gold_glow,
      fontsize=7.6,
      weight='heavy',
      zorder=4,
  )

  # Perspective Drawing of Host Plate (Isometric View)
  plate_poly = patches.Polygon(
      [(8.5, 71.0), (62.0, 71.0), (74.0, 93.0), (20.5, 93.0)],
      closed=True,
      facecolor='#1e293b',
      edgecolor='#475569',
      lw=1.1,
      zorder=4,
  )
  ax.add_patch(plate_poly)

  # Plate Thickness Rim
  ax.add_patch(
      patches.Polygon(
          [(8.5, 70.0), (62.0, 70.0), (62.0, 71.0), (8.5, 71.0)],
          closed=True,
          facecolor='#0f172a',
          edgecolor='#334155',
          lw=0.8,
          zorder=4,
      )
  )
  ax.text(
      10.0,
      69.0,
      'Conductive Host Structure (Steel Flange / Prestressed Rebar Ground'
      ' Plane)',
      color='#94a3b8',
      fontsize=5.8,
      weight='bold',
      zorder=5,
  )

  # Active Transducer 1 (PZT 1: Actuator / Wave Injector)
  pzt1_pts = [(12.0, 74.0), (17.5, 74.0), (19.5, 78.5), (14.0, 78.5)]
  ax.add_patch(
      patches.Polygon(
          pzt1_pts,
          closed=True,
          facecolor='#020617',
          edgecolor='#f59e0b',
          lw=1.5,
          zorder=6,
      )
  )
  ax.text(
      15.5,
      76.2,
      'PZT 1\n(Actuator)',
      color='#ffffff',
      fontsize=5.6,
      weight='black',
      ha='center',
      va='center',
      zorder=7,
  )

  # Active Transducer 2 (PZT 2: Far-Field Boundary Listener)
  pzt2_pts = [(62.0, 86.5), (67.5, 86.5), (69.5, 91.0), (64.0, 91.0)]
  ax.add_patch(
      patches.Polygon(
          pzt2_pts,
          closed=True,
          facecolor='#020617',
          edgecolor=c_cyan,
          lw=1.5,
          zorder=6,
      )
  )
  ax.text(
      65.5,
      88.7,
      'PZT 2\n(Listener)',
      color='#ffffff',
      fontsize=5.6,
      weight='black',
      ha='center',
      va='center',
      zorder=7,
  )

  # 10 Yellow Electrode Tap Nodes (Yellow Circles with Red Centers)
  electrode_nodes = [
      (25.0, 88.0, '1'),
      (35.0, 89.0, '2'),
      (22.0, 81.0, '3'),
      (32.0, 81.5, '4'),
      (42.0, 85.0, '5'),
      (45.0, 78.0, '6'),
      (52.0, 83.5, '7'),  # Flaw location
      (54.0, 75.5, '8'),
      (33.0, 74.0, '9'),
      (60.0, 80.0, '10'),
  ]

  g_hub_x, g_hub_y = 76.5, 75.0

  for nx, ny, nid in electrode_nodes:
    is_node_7 = nid == '7'

    # Stress wave ray paths from PZT 1
    ax.plot(
        [16.0, nx],
        [76.5, ny],
        color=c_gold_glow,
        lw=0.4,
        alpha=0.3,
        linestyle=':',
        zorder=5,
    )

    # Passive Electrode Node Tap
    ax.add_patch(
        patches.Circle(
            (nx, ny),
            1.2,
            facecolor=c_yellow_node,
            edgecolor='#ca8a04',
            lw=0.8,
            zorder=6,
        )
    )
    ax.plot(
        nx,
        ny,
        marker='o',
        color=c_crimson if not is_node_7 else '#ff0000',
        markersize=2.2,
        zorder=7,
    )
    ax.text(
        nx,
        ny - 2.2,
        f'N{nid}',
        color='#ffffff',
        fontsize=5.0,
        weight='heavy',
        ha='center',
        zorder=7,
    )

    # Red Ground Return Line to Instrument Hub
    rad_c = 0.12 if ny < 82.0 else -0.12
    arrow = FancyArrowPatch(
        (nx, ny),
        (g_hub_x, g_hub_y),
        connectionstyle=f'arc3,rad={rad_c}',
        color='#ef4444',
        lw=0.7,
        alpha=0.65,
        arrowstyle='-',
        zorder=5,
    )
    ax.add_patch(arrow)

  # Incipient Crack Singular Flaw right at Node 7
  crack_x, crack_y = 52.8, 83.5
  ax.plot(
      [crack_x, crack_x + 1.2, crack_x + 0.6, crack_x + 2.0],
      [crack_y + 1.5, crack_y, crack_y - 1.2, crack_y - 2.5],
      color='#ff2222',
      lw=2.2,
      zorder=9,
  )
  ax.text(
      crack_x + 2.5,
      crack_y + 0.8,
      'Micro-Crack Mouth at Node 7\n(Traction σ_xx → 0 Traps Charge)',
      color='#fca5a5',
      fontsize=5.2,
      weight='heavy',
      zorder=9,
  )

  # Legend in Top-Left of Visual Card
  ax.add_patch(
      FancyBboxPatch(
          (7.5, 87.0),
          15.0,
          10.5,
          boxstyle='round,pad=0.2,rounding_size=0.2',
          facecolor='#040d1a',
          edgecolor='#1e3a5f',
          lw=0.6,
          zorder=6,
      )
  )
  ax.text(
      8.2,
      95.5,
      'TOPOLOGY LEGEND:',
      color=c_cyan,
      fontsize=4.8,
      weight='heavy',
      zorder=7,
  )
  ax.plot(
      9.0,
      93.5,
      marker='s',
      color='#020617',
      markeredgecolor=c_gold,
      markersize=4.0,
      zorder=7,
  )
  ax.text(
      10.8,
      93.5,
      'Active PZT (Only 2)',
      color='#ffffff',
      fontsize=4.8,
      va='center',
      zorder=7,
  )
  ax.add_patch(
      patches.Circle(
          (9.0, 91.0),
          0.9,
          facecolor=c_yellow_node,
          edgecolor='#ca8a04',
          lw=0.5,
          zorder=7,
      )
  )
  ax.text(
      10.8,
      91.0,
      'Electrode Nodes (N1-10)',
      color=c_yellow_node,
      fontsize=4.8,
      va='center',
      zorder=7,
  )
  ax.plot(
      [8.0, 10.0],
      [88.5, 88.5],
      color=c_crimson,
      lw=1.2,
      zorder=7,
  )
  ax.text(
      10.8,
      88.5,
      'Ground Return Loop',
      color='#fca5a5',
      fontsize=4.8,
      va='center',
      zorder=7,
  )

  # MEASUREMENT SYSTEM INSTRUMENT BOX
  meas_x, meas_y, meas_w, meas_h = 76.0, 71.0, 16.5, 23.0
  ax.add_patch(
      FancyBboxPatch(
          (meas_x, meas_y),
          meas_w,
          meas_h,
          boxstyle='round,pad=0.2,rounding_size=0.4',
          facecolor='#081427',
          edgecolor=c_emerald,
          lw=1.1,
          zorder=6,
      )
  )
  ax.text(
      meas_x + meas_w / 2,
      meas_y + meas_h - 2.0,
      'MEASUREMENT\nSYSTEM',
      color=c_emerald,
      fontsize=6.2,
      weight='heavy',
      ha='center',
      zorder=7,
  )

  # Top Electrode Actuation Lead (Gray Lead: V_exc)
  ax.plot(
      [meas_x + meas_w / 2, meas_x + meas_w / 2, 16.0, 16.0],
      [meas_y + meas_h, 97.0, 97.0, 78.5],
      color=c_gray_wire,
      lw=1.4,
      zorder=7,
  )
  ax.text(
      45.0,
      97.8,
      'Top Electrode Actuation Lead (Gray Lead: V_exc)',
      color=c_gray_wire,
      fontsize=5.2,
      weight='bold',
      ha='center',
      zorder=8,
  )

  # Oscilloscope Display Screen inside Measurement Box
  disp_x, disp_y, disp_w, disp_h = (
      meas_x + 1.2,
      meas_y + meas_h - 9.8,
      meas_w - 2.4,
      6.0,
  )
  ax.add_patch(
      patches.Rectangle(
          (disp_x, disp_y),
          disp_w,
          disp_h,
          facecolor='#020712',
          edgecolor='#1e3a5f',
          lw=0.8,
          zorder=7,
      )
  )
  ax.plot(
      [disp_x, disp_x + disp_w],
      [disp_y + disp_h / 2, disp_y + disp_h / 2],
      color='#1e3a5f',
      lw=0.4,
      linestyle=':',
      zorder=7,
  )
  ax.plot(
      [disp_x + disp_w / 2, disp_x + disp_w / 2],
      [disp_y, disp_y + disp_h],
      color='#1e3a5f',
      lw=0.4,
      linestyle=':',
      zorder=7,
  )

  # Active Sine Wave trace on screen
  scr_xs = np.linspace(disp_x + 0.5, disp_x + disp_w - 0.5, 50)
  scr_ys = (
      disp_y
      + disp_h / 2
      + 1.8 * np.sin(2 * np.pi * 2.5 * (scr_xs - disp_x) / disp_w)
  )
  ax.plot(scr_xs, scr_ys, color=c_cyan, lw=1.1, zorder=8)
  ax.text(
      disp_x + 1.0,
      disp_y + disp_h - 1.2,
      'SINE GEN',
      color=c_gold_glow,
      fontsize=3.8,
      weight='bold',
      zorder=8,
  )

  # Controls: 3 Buttons & 2 Knobs
  btn_y = disp_y - 2.0
  btn_colors = [c_crimson, c_emerald, c_gold]
  btn_labels = ['RUN', 'CAL', 'MUX']
  for b_idx in range(3):
    bx = disp_x + 1.6 + b_idx * 4.4
    ax.add_patch(
        patches.Circle(
            (bx, btn_y),
            0.9,
            facecolor=btn_colors[b_idx],
            edgecolor='#ffffff',
            lw=0.4,
            zorder=7,
        )
    )
    ax.text(
        bx,
        btn_y - 1.6,
        btn_labels[b_idx],
        color='#94a3b8',
        fontsize=3.6,
        weight='bold',
        ha='center',
        zorder=8,
    )

  knob_y = btn_y - 3.8
  for k_idx in range(2):
    kx = disp_x + 3.4 + k_idx * 7.2
    ax.add_patch(
        patches.Circle(
            (kx, knob_y),
            1.2,
            facecolor='#1e293b',
            edgecolor='#94a3b8',
            lw=0.6,
            zorder=7,
        )
    )
    ax.plot(
        [kx, kx + 0.7],
        [knob_y, knob_y + 0.7],
        color=c_cyan,
        lw=0.8,
        zorder=8,
    )
    ax.text(
        kx,
        knob_y - 1.8,
        'VOLT' if k_idx == 0 else 'FREQ',
        color='#94a3b8',
        fontsize=3.6,
        weight='bold',
        ha='center',
        zorder=8,
    )

  # Multiplexed Ground Return Label
  ax.text(
      meas_x + meas_w / 2,
      meas_y + 1.6,
      'Multiplexed Ground\nInput (Virtual 0V)',
      color=c_crimson,
      fontsize=5.0,
      weight='bold',
      ha='center',
      zorder=7,
  )

  # Math Box inside Card 2
  ax.add_patch(
      FancyBboxPatch(
          (76.5, 66.5),
          15.5,
          4.2,
          boxstyle='round,pad=0.1,rounding_size=0.1',
          facecolor='#040c1a',
          edgecolor=c_gold,
          lw=0.6,
          zorder=7,
      )
  )
  ax.text(
      84.2,
      68.8,
      r'$\Delta q_i = q_{\mathrm{PZT1}} - q_{Ni}$',
      color=c_gold_glow,
      fontsize=6.0,
      weight='heavy',
      ha='center',
      zorder=8,
  )
  ax.text(
      84.2,
      67.2,
      r'$\nabla D_3 \propto \partial \sigma_{xx}/\partial x$',
      color=c_emerald,
      fontsize=5.0,
      ha='center',
      zorder=8,
  )

  # ------------------------------------------------------------------
  # CARD 3: TEST EQUIPMENT COMPARISON (y = 44.5 to 65.0)
  # Multi-line two-step rendering ensures zero cross-column text bleeding
  # ------------------------------------------------------------------
  equip_box = FancyBboxPatch(
      (6.0, 44.5),
      88.0,
      20.5,
      boxstyle='round,pad=0.3,rounding_size=0.5',
      facecolor=c_subcard,
      edgecolor='#254778',
      lw=1.0,
      zorder=3,
  )
  ax.add_patch(equip_box)

  ax.add_patch(
      FancyBboxPatch(
          (6.8, 61.5),
          86.4,
          2.8,
          boxstyle='round,pad=0.1,rounding_size=0.2',
          facecolor='#0c234b',
          edgecolor=c_emerald,
          lw=0.7,
          zorder=4,
      )
  )
  ax.text(
      8.0,
      62.9,
      '16.2 INSTRUMENTATION BENCHMARK: COSTLY COMMERCIAL ANALYZERS VS. DIY'
      ' EMCD HARDWARE',
      color=c_emerald,
      fontsize=7.4,
      weight='heavy',
      va='center',
      zorder=5,
  )

  # Column A: Costly Commercial Analyzer (Red Box)
  ax.add_patch(
      FancyBboxPatch(
          (7.5, 45.8),
          41.5,
          15.0,
          boxstyle='round,pad=0.2,rounding_size=0.3',
          facecolor='#081427',
          edgecolor='#ef4444',
          lw=0.8,
          zorder=4,
      )
  )
  ax.text(
      8.5,
      58.8,
      '1) COSTLY COMMERCIAL SETUP (CLASSICAL EMI)',
      color='#fca5a5',
      fontsize=6.2,
      weight='heavy',
      zorder=5,
  )

  col_a_entries = [
      (
          '• Equipment:',
          'Keysight E4990A / Wayne Kerr 6500B',
          c_white,
          56.4,
      ),
      (
          '• Estimated Cost:',
          '$25,000 – $50,000 USD (Prohibitive)',
          c_crimson,
          53.5,
      ),
      (
          '• Operating Mode:',
          'Sweeps single patch; reads bulk admittance Y(ω)',
          c_muted,
          50.6,
      ),
      (
          '• Key Weakness:',
          'Cable shunt (>3m) & diurnal thermal drift (>15%)',
          c_muted,
          47.7,
      ),
  ]
  for hdr, val, col, y_pos in col_a_entries:
    ax.text(
        8.5,
        y_pos,
        hdr,
        color=col,
        fontsize=5.4,
        weight='bold',
        zorder=5,
    )
    ax.text(
        8.5,
        y_pos - 1.1,
        val,
        color='#94a3b8',
        fontsize=4.9,
        weight='medium',
        zorder=5,
    )

  # Column B: Low-Cost DIY EMCD Equipment (Green Box)
  ax.add_patch(
      FancyBboxPatch(
          (51.0, 45.8),
          41.5,
          15.0,
          boxstyle='round,pad=0.2,rounding_size=0.3',
          facecolor='#081427',
          edgecolor=c_emerald,
          lw=0.8,
          zorder=4,
      )
  )
  ax.text(
      52.0,
      58.8,
      '2) LOW-COST DIY EMCD SETUP (KALAM ZERO INITIATIVE)',
      color=c_emerald,
      fontsize=6.2,
      weight='heavy',
      zorder=5,
  )

  col_b_entries = [
      (
          '• Equipment:',
          'Transimpedance Amp (TIA) + MUX + 16-bit ADC',
          c_white,
          56.4,
      ),
      (
          '• Estimated Cost:',
          '<$15 USD total components (Standard op-amps)',
          c_gold_glow,
          53.5,
      ),
      (
          '• Operating Mode:',
          'Pads held at Virtual Ground (0V); reads charge Δq',
          c_muted,
          50.6,
      ),
      (
          '• Key Advantage:',
          'Zero cable shunt noise; 100% thermal drift immunity',
          c_cyan,
          47.7,
      ),
  ]
  for hdr, val, col, y_pos in col_b_entries:
    ax.text(
        52.0,
        y_pos,
        hdr,
        color=col,
        fontsize=5.4,
        weight='bold',
        zorder=5,
    )
    ax.text(
        52.0,
        y_pos - 1.1,
        val,
        color='#94a3b8',
        fontsize=4.9,
        weight='medium',
        zorder=5,
    )

  # CARD 4: ARJUN PEDAGOGICAL INFERENCE (y = 20.2 to 43.0)
  arjun_box = FancyBboxPatch(
      (6.0, 20.2),
      88.0,
      23.0,
      boxstyle='round,pad=0.3,rounding_size=0.5',
      facecolor=c_subcard,
      edgecolor='#254778',
      lw=1.0,
      zorder=3,
  )
  ax.add_patch(arjun_box)

  ax.add_patch(
      FancyBboxPatch(
          (6.8, 39.8),
          86.4,
          2.6,
          boxstyle='round,pad=0.1,rounding_size=0.2',
          facecolor='#0c234b',
          edgecolor=c_gold_glow,
          lw=0.7,
          zorder=4,
      )
  )
  ax.text(
      8.0,
      41.1,
      '16.3 ARJUN AI ASSISTANT: PEDAGOGICAL CAUSAL LOGIC (WHY EMCD WINS)',
      color=c_gold_glow,
      fontsize=7.4,
      weight='heavy',
      va='center',
      zorder=5,
  )

  step_w = 27.2
  step_gap = 1.6
  step_h = 17.5
  step_y = 21.5

  step_contents = [
      {
          'title': 'STEP 1 • STUDENT QUESTION',
          'title_color': c_white,
          'body_lines': [
              'Why not just stick 10 standard',
              'PZTs and do classical EMI at',
              'each spot? Wouldn\'t a patch near',
              'Node 7 detect the crack anyway?',
          ],
          'rationale_prefix': 'ARJUN RATIONALE:',
          'rationale_lines': [
              'It will see a tiny baseline shift',
              '(<0.5%), but daily temperature',
              'swings (>15%) completely bury it',
              'in frequent false alarms.',
          ],
          'rationale_color': c_crimson,
      },
      {
          'title': 'STEP 2 • CHARGE TRAPPING',
          'title_color': c_cyan,
          'body_lines': [
              'How does the distributed ground',
              'network reveal the flaw location?',
              'Stress waves from PZT 1 lose shear',
              'coupling at crack lips (σxx → 0).',
          ],
          'rationale_prefix': 'ARJUN RATIONALE:',
          'rationale_lines': [
              'Charge is trapped locally.',
              'Differential readout (q_PZT1 - q_N7)',
              'creates a +380% divergence spike',
              '(>24 dB signal-to-noise boost).',
          ],
          'rationale_color': c_emerald,
      },
      {
          'title': 'STEP 3 • CAUSAL DEDUCTION',
          'title_color': c_emerald,
          'body_lines': [
              'How does ARJUN prove it is a real',
              'crack and not a broken cable lead?',
              'ARJUN cross-references PZT 2 (the',
              'far-field listener) for shadow loss.',
          ],
          'rationale_prefix': 'ARJUN RATIONALE:',
          'rationale_lines': [
              'Attenuated transmission across',
              'ray PZT1-N7-PZT2 confirms physical',
              'fatigue flaw at (x_7, y_7) with',
              '97.4% diagnostic confidence.',
          ],
          'rationale_color': c_gold_glow,
      },
  ]

  for s_i, sc in enumerate(step_contents):
    s_x = 7.5 + s_i * (step_w + step_gap)

    ax.add_patch(
        FancyBboxPatch(
            (s_x, step_y),
            step_w,
            step_h,
            boxstyle='round,pad=0.2,rounding_size=0.3',
            facecolor='#081427',
            edgecolor='#204575',
            lw=0.8,
            zorder=4,
        )
    )

    ax.text(
        s_x + 1.2,
        step_y + step_h - 1.8,
        sc['title'],
        color=sc['title_color'],
        fontsize=6.1,
        weight='heavy',
        zorder=5,
    )

    cur_y = step_y + step_h - 3.4
    for line in sc['body_lines']:
      ax.text(
          s_x + 1.2,
          cur_y,
          line,
          color='#94a3b8',
          fontsize=5.0,
          weight='medium',
          zorder=5,
      )
      cur_y -= 1.2

    cur_y -= 0.3
    ax.text(
        s_x + 1.2,
        cur_y,
        sc['rationale_prefix'],
        color=sc['rationale_color'],
        fontsize=5.2,
        weight='black',
        zorder=5,
    )
    cur_y -= 1.25

    for r_line in sc['rationale_lines']:
      ax.text(
          s_x + 1.2,
          cur_y,
          r_line,
          color=sc['rationale_color'],
          fontsize=4.9,
          weight='bold',
          zorder=5,
      )
      cur_y -= 1.15

  # ARJUN AI Access Link Banner
  ax.text(
      50.0,
      18.2,
      'Arjun, our AI Assistant, can answer all your questions. Access link'
      ' available on the final page of this monograph.',
      color=c_cyan,
      fontsize=6.0,
      weight='semibold',
      style='italic',
      ha='center',
      zorder=5,
  )

  # Transition Badge -> Page 19
  ax.add_patch(
      FancyBboxPatch(
          (10.0, 15.0),
          80.0,
          2.6,
          boxstyle='round,pad=0.2,rounding_size=0.4',
          facecolor='#08152b',
          edgecolor='#b45309',
          lw=0.8,
          zorder=3,
      )
  )
  ax.text(
      50.0,
      16.3,
      'BENCHMARK COMPARISON MATRIX & NATIONAL ECONOMIC IMPACT (PAGES 19 TO 24)'
      ' CONTINUES NEXT.',
      color=c_gold_glow,
      fontsize=6.6,
      weight='bold',
      style='italic',
      ha='center',
      zorder=4,
  )

  # 5. Bottom Running Footer Bar (Official Monograph Template)[cite: 12]
  footer_box = FancyBboxPatch(
      (4, 1.2),
      92,
      9.6,
      boxstyle='round,pad=0.3,rounding_size=0.6',
      facecolor=c_card_bg,
      edgecolor=c_border,
      linewidth=1.1,
      zorder=2,
  )
  ax.add_patch(footer_box)

  ax.text(
      7,
      8.2,
      'GARRF Technical Magazine 1 • Monograph Series • Archive Ref:'
      ' GARRF-MAG1-SINGBHA-2026.P18',
      color=c_muted,
      fontsize=8.0,
      weight='medium',
      zorder=4,
  )
  ax.text(
      7,
      5.7,
      'Official Portal: https://garrf.in  •  LinkedIn:'
      ' https://www.linkedin.com/company/gopalkrishnaadvancedruralresearchfoundation/',
      color=c_cyan,
      fontsize=7.6,
      weight='semibold',
      zorder=4,
  )
  ax.text(
      7,
      3.0,
      'Dedicated in Honour of Singapore and Bharat',
      color=c_white,
      fontsize=8.6,
      weight='bold',
      ha='left',
      zorder=4,
  )
  ax.text(
      93,
      3.0,
      'Page 18',
      color=c_gold_glow,
      fontsize=9.5,
      weight='black',
      ha='right',
      zorder=4,
  )

  # Save and Export High-Resolution Plate
  output_filename = 'SingBha_Magazine_Page_18_Perfect_Template.png'
  plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
  plt.close()

  display(IPImage(filename=output_filename, width=720))
  print(
      f'Generated successfully: {output_filename} (A4 300 DPI Page 18 - Clean'
      ' Execution)'
  )
  files.download(output_filename)


if __name__ == '__main__':
  generate_magazine_page_18_clean()
