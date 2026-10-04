import io
import urllib.request
from google.colab import files
from IPython.display import Image as IPImage, display
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def generate_magazine_page_15_experimental_protocol_large_font():
  # ------------------------------------------------------------------
  # 1. Page Geometry: International A4 at 300 DPI (8.27 x 11.69 in)
  # ------------------------------------------------------------------
  fig = plt.figure(figsize=(8.27, 11.69), dpi=300)
  ax = fig.add_axes([0, 0, 1, 1])
  ax.set_xlim(0, 100)
  ax.set_ylim(0, 141.4)
  ax.axis('off')

  # Color Palette conforming to GARRF Monograph Identity
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

  # Base Canvas
  ax.add_patch(
      patches.Rectangle((0, 0), 100, 141.4, facecolor=c_abyss, zorder=0)
  )
  ax.add_patch(
      patches.Circle(
          (50, 75), radius=48, color='#0b2447', alpha=0.35, zorder=1
      )
  )

  # ------------------------------------------------------------------
  # 2. Sacred Watermark: Dharmachakra 24-Spoke Circular Imprint
  # ------------------------------------------------------------------
  cx_w, cy_w, r_w = 50.0, 72.0, 32.0
  ax.add_patch(
      patches.Circle(
          (cx_w, cy_w),
          radius=r_w,
          facecolor='none',
          edgecolor='#38bdf8',
          lw=1.2,
          alpha=0.08,
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
          alpha=0.06,
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
          alpha=0.10,
          zorder=1,
      )
  )
  ax.add_patch(
      patches.Circle(
          (cx_w, cy_w),
          radius=r_w * 0.08,
          facecolor='#38bdf8',
          edgecolor='none',
          alpha=0.12,
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
        alpha=0.08,
        zorder=1,
    )

  # ------------------------------------------------------------------
  # 3. Top Header Container Bar (White Fill)
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

  # Header Typography
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

  # Dual Flags: Bharat & Singapore
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

  # ------------------------------------------------------------------
  # 4. Main Content Area Workspace
  # ------------------------------------------------------------------
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

  # Monograph Section 13 Header
  ax.text(
      6.5,
      118.8,
      'SECTION 13 • EXPERIMENTAL TESTING PROTOCOL & HARDWARE INTERFACING',
      color=c_gold_glow,
      fontsize=9.4,
      weight='heavy',
      ha='left',
      zorder=4,
  )
  ax.text(
      6.5,
      114.6,
      'Experimental Protocols: Physical Charge Density Acquisition',
      color=c_white,
      fontsize=14.0,
      weight='black',
      ha='left',
      zorder=4,
  )
  ax.text(
      6.5,
      111.4,
      'Differential virtual ground instrumentation, segmented electrode'
      ' calibration & gradient isolation.',
      color=c_muted,
      fontsize=9.0,
      weight='medium',
      ha='left',
      zorder=4,
  )

  # ------------------------------------------------------------------
  # CARD 1: HARDWARE INTERFACE & VIRTUAL GROUND CIRCUITRY (y=69.0 to 110.0)
  # ------------------------------------------------------------------
  card_hw = FancyBboxPatch(
      (6, 68.8),
      88,
      41.2,
      boxstyle='round,pad=0.3,rounding_size=0.6',
      facecolor=c_subcard,
      edgecolor='#254778',
      lw=1.1,
      zorder=3,
  )
  ax.add_patch(card_hw)

  ax.text(
      8.5,
      106.6,
      '1. DIFFERENTIAL CHARGE CONDITIONING FRONT-END & VIRTUAL GROUND'
      ' ARCHITECTURE',
      color=c_gold_glow,
      fontsize=9.4,
      weight='heavy',
      ha='left',
      zorder=4,
  )

  # Left: Circuit Schematic Diagram
  ax.add_patch(
      FancyBboxPatch(
          (7.5, 70.2),
          43.5,
          34.3,
          boxstyle='round,pad=0.2,rounding_size=0.4',
          facecolor='#081427',
          edgecolor='#204575',
          lw=0.9,
          zorder=4,
      )
  )
  ax.text(
      29.2,
      101.8,
      'Dual-Channel Virtual Ground Transimpedance Topology',
      color=c_cyan,
      fontsize=8.2,
      weight='bold',
      ha='center',
      zorder=5,
  )

  # PZT Segmented Electrodes Block
  pz_x, pz_y = 9.0, 79.5
  ax.add_patch(
      patches.Rectangle(
          (pz_x, pz_y + 8.5),
          6.5,
          8.5,
          facecolor='#1e293b',
          edgecolor='#94a3b8',
          lw=0.8,
          zorder=5,
      )
  )
  ax.text(
      pz_x + 3.25,
      pz_y + 12.75,
      'PZT\nWafer',
      color='#ffffff',
      fontsize=7.0,
      weight='bold',
      ha='center',
      va='center',
      zorder=6,
  )

  # Pads A and B
  ax.add_patch(
      patches.Rectangle(
          (pz_x + 6.5, pz_y + 13.2),
          2.4,
          3.4,
          facecolor=c_gold,
          edgecolor='#ffffff',
          lw=0.6,
          zorder=6,
      )
  )
  ax.add_patch(
      patches.Rectangle(
          (pz_x + 6.5, pz_y + 8.9),
          2.4,
          3.4,
          facecolor=c_cyan,
          edgecolor='#ffffff',
          lw=0.6,
          zorder=6,
      )
  )
  ax.text(
      pz_x + 7.7,
      pz_y + 14.9,
      'Pad A',
      color='#000',
      fontsize=5.8,
      weight='black',
      ha='center',
      va='center',
      zorder=7,
  )
  ax.text(
      pz_x + 7.7,
      pz_y + 10.6,
      'Pad B',
      color='#000',
      fontsize=5.8,
      weight='black',
      ha='center',
      va='center',
      zorder=7,
  )

  # Lead routing to Op-Amp A
  oa_x, oa_y = 23.0, 93.0
  ax.plot(
      [pz_x + 8.9, oa_x],
      [pz_y + 14.9, oa_y + 1.2],
      color=c_gold,
      lw=1.2,
      zorder=5,
  )
  ax.add_patch(
      patches.Polygon(
          [[oa_x, oa_y + 3.5], [oa_x, oa_y - 3.5], [oa_x + 5.2, oa_y]],
          facecolor='#1e293b',
          edgecolor='#ffffff',
          lw=0.8,
          zorder=5,
      )
  )
  ax.text(
      oa_x + 0.8,
      oa_y + 1.0,
      '-',
      color='#ffffff',
      fontsize=7.0,
      weight='bold',
      zorder=6,
  )
  ax.text(
      oa_x + 0.8,
      oa_y - 2.0,
      '+',
      color='#ffffff',
      fontsize=7.0,
      weight='bold',
      zorder=6,
  )
  # Ground connection
  ax.plot(
      [oa_x - 1.0, oa_x],
      [oa_y - 2.0, oa_y - 2.0],
      color='#94a3b8',
      lw=0.8,
      zorder=5,
  )
  ax.plot(
      [oa_x - 1.0, oa_x - 1.0],
      [oa_y - 2.0, oa_y - 3.2],
      color='#94a3b8',
      lw=0.8,
      zorder=5,
  )
  ax.plot(
      [oa_x - 1.8, oa_x - 0.2],
      [oa_y - 3.2, oa_y - 3.2],
      color='#94a3b8',
      lw=1.0,
      zorder=5,
  )
  ax.text(
      oa_x - 1.0,
      oa_y - 4.6,
      '0V',
      color=c_emerald,
      fontsize=6.2,
      weight='bold',
      ha='center',
      zorder=6,
  )
  # Feedback Cf
  ax.plot(
      [oa_x - 0.8, oa_x - 0.8, oa_x + 6.5, oa_x + 6.5],
      [oa_y + 1.2, oa_y + 5.0, oa_y + 5.0, oa_y],
      color='#38bdf8',
      lw=0.8,
      zorder=5,
  )
  ax.add_patch(
      patches.Rectangle(
          (oa_x + 1.8, oa_y + 4.1),
          2.2,
          1.8,
          facecolor='#0284c7',
          edgecolor='#fff',
          lw=0.5,
          zorder=6,
      )
  )
  ax.text(
      oa_x + 2.9,
      oa_y + 5.0,
      r'$C_f$',
      color='#fff',
      fontsize=6.2,
      weight='bold',
      ha='center',
      va='center',
      zorder=7,
  )

  # Lead routing to Op-Amp B
  ob_x, ob_y = 23.0, 82.5
  ax.plot(
      [pz_x + 8.9, ob_x],
      [pz_y + 10.6, ob_y + 1.2],
      color=c_cyan,
      lw=1.2,
      zorder=5,
  )
  ax.add_patch(
      patches.Polygon(
          [[ob_x, ob_y + 3.5], [ob_x, ob_y - 3.5], [ob_x + 5.2, ob_y]],
          facecolor='#1e293b',
          edgecolor='#ffffff',
          lw=0.8,
          zorder=5,
      )
  )
  ax.text(
      ob_x + 0.8,
      ob_y + 1.0,
      '-',
      color='#ffffff',
      fontsize=7.0,
      weight='bold',
      zorder=6,
  )
  ax.text(
      ob_x + 0.8,
      ob_y - 2.0,
      '+',
      color='#ffffff',
      fontsize=7.0,
      weight='bold',
      zorder=6,
  )
  # Ground connection
  ax.plot(
      [ob_x - 1.0, ob_x],
      [ob_y - 2.0, ob_y - 2.0],
      color='#94a3b8',
      lw=0.8,
      zorder=5,
  )
  ax.plot(
      [ob_x - 1.0, ob_x - 1.0],
      [ob_y - 2.0, ob_y - 3.2],
      color='#94a3b8',
      lw=0.8,
      zorder=5,
  )
  ax.plot(
      [ob_x - 1.8, ob_x - 0.2],
      [ob_y - 3.2, ob_y - 3.2],
      color='#94a3b8',
      lw=1.0,
      zorder=5,
  )
  ax.text(
      ob_x - 1.0,
      ob_y - 4.6,
      '0V',
      color=c_emerald,
      fontsize=6.2,
      weight='bold',
      ha='center',
      zorder=6,
  )
  # Feedback Cf
  ax.plot(
      [ob_x - 0.8, ob_x - 0.8, ob_x + 6.5, ob_x + 6.5],
      [ob_y + 1.2, ob_y + 5.0, ob_y + 5.0, ob_y],
      color='#38bdf8',
      lw=0.8,
      zorder=5,
  )
  ax.add_patch(
      patches.Rectangle(
          (ob_x + 1.8, ob_y + 4.1),
          2.2,
          1.8,
          facecolor='#0284c7',
          edgecolor='#fff',
          lw=0.5,
          zorder=6,
      )
  )
  ax.text(
      ob_x + 2.9,
      ob_y + 5.0,
      r'$C_f$',
      color='#fff',
      fontsize=6.2,
      weight='bold',
      ha='center',
      va='center',
      zorder=7,
  )

  # Difference Amplifier Stage (IN-AMP / SUBTRACTOR)
  da_x, da_y = 36.5, 87.5
  ax.plot(
      [oa_x + 5.2, da_x], [oa_y, da_y + 1.5], color=c_gold, lw=1.2, zorder=5
  )
  ax.plot(
      [ob_x + 5.2, da_x], [ob_y, da_y - 1.5], color=c_cyan, lw=1.2, zorder=5
  )
  ax.add_patch(
      patches.Polygon(
          [[da_x, da_y + 3.8], [da_x, da_y - 3.8], [da_x + 5.5, da_y]],
          facecolor='#334155',
          edgecolor='#ffffff',
          lw=0.8,
          zorder=5,
      )
  )
  ax.text(
      da_x + 0.8,
      da_y + 1.1,
      '-',
      color='#ffffff',
      fontsize=7.0,
      weight='bold',
      zorder=6,
  )
  ax.text(
      da_x + 0.8,
      da_y - 2.0,
      '+',
      color='#ffffff',
      fontsize=7.0,
      weight='bold',
      zorder=6,
  )
  ax.plot([da_x + 5.5, da_x + 7.5], [da_y, da_y], color=c_emerald, lw=1.4, zorder=5)
  ax.text(
      da_x + 8.0,
      da_y,
      r'$V_{\mathrm{diff}} \propto \nabla D_3$',
      color=c_emerald,
      fontsize=7.6,
      weight='bold',
      va='center',
      zorder=6,
  )

  # Right: Formula & Circuit Operating Principles
  ax.add_patch(
      FancyBboxPatch(
          (52.0, 70.2),
          40.5,
          34.3,
          boxstyle='round,pad=0.2,rounding_size=0.4',
          facecolor='#081427',
          edgecolor='#204575',
          lw=0.9,
          zorder=4,
      )
  )
  ax.text(
      72.2,
      101.8,
      'Circuit Principles & Conversion Laws',
      color=c_cyan,
      fontsize=8.4,
      weight='bold',
      ha='center',
      zorder=5,
  )

  ax.add_patch(
      FancyBboxPatch(
          (53.5, 89.2),
          37.5,
          9.6,
          boxstyle='round,pad=0.1,rounding_size=0.3',
          facecolor='#050d1a',
          edgecolor='#b45309',
          lw=0.8,
          zorder=5,
      )
  )
  ax.text(
      72.2,
      96.5,
      'DIFFERENTIAL CHARGE-TO-VOLTAGE LAW',
      color=c_gold_glow,
      fontsize=6.8,
      weight='bold',
      ha='center',
      zorder=6,
  )
  ax.text(
      72.2,
      93.4,
      r'$V_{\mathrm{out},A} = -\frac{1}{C_f}\iint_{A} D_3(x,y)\,dA$',
      color=c_white,
      fontsize=7.4,
      weight='bold',
      ha='center',
      zorder=6,
  )
  ax.text(
      72.2,
      90.7,
      r'$\Delta V = V_A - V_B = -\frac{1}{C_f}\iint \nabla D_3 \cdot \Delta'
      r' \vec{r}\,dA$',
      color=c_emerald,
      fontsize=7.2,
      ha='center',
      zorder=6,
  )

  hw_notes = [
      (
          '• Virtual Ground Clamping:',
          'Inverting inputs held at 0V eliminate cable drift.',
          c_white,
      ),
      (
          '• Pure Mechanical Charge:',
          'Zero field (E3 = 0) isolates piezoelectric strain.',
          c_cyan,
      ),
      (
          '• Hardware Drift Rejection:',
          'Outdoor diurnal thermal shift cancels at subtraction.',
          c_emerald,
      ),
  ]
  for i, (h_tit, h_sub, h_c) in enumerate(hw_notes):
    y_pos = 85.8 - i * 4.8
    ax.text(53.5, y_pos, h_tit, color=h_c, fontsize=7.2, weight='bold', zorder=6)
    ax.text(53.5, y_pos - 2.0, h_sub, color=c_muted, fontsize=6.8, zorder=6)

  # ------------------------------------------------------------------
  # CARD 2: STEP-BY-STEP CALIBRATION & TESTING WORKFLOW (y=21.0 to 66.5)
  # ------------------------------------------------------------------
  card_proto = FancyBboxPatch(
      (6, 21.0),
      88,
      45.5,
      boxstyle='round,pad=0.3,rounding_size=0.6',
      facecolor=c_subcard,
      edgecolor='#254778',
      lw=1.1,
      zorder=3,
  )
  ax.add_patch(card_proto)

  ax.text(
      8.5,
      63.8,
      '2. SYSTEMATIC STEP-BY-STEP EXPERIMENTAL EXECUTION PROTOCOL',
      color=c_gold_glow,
      fontsize=9.4,
      weight='heavy',
      ha='left',
      zorder=4,
  )

  # 4-Step Experimental Protocol Cards with calibrated vertical pitch
  steps = [
      (
          'STEP 1: Substrate Preparation & Bonding',
          'Surface ground to 400-grit finish, degreased with IPA. Bonded with'
          ' ultra-thin\nlow-viscosity adhesive (ha < 0.1 mm) under 0.2 MPa'
          ' uniform clamping pressure.',
          c_gold_glow,
      ),
      (
          'STEP 2: Segmented Electrode Patterning & Wiring',
          'Top electrode etched into discrete dual/quadrant pads with isolated'
          ' boundaries.\nMicro-coaxial leads soldered (<260°C, <2s) and routed'
          ' to inverting op-amp nodes.',
          c_cyan,
      ),
      (
          'STEP 3: Baseline Common-Mode Balancing & Nulling',
          'Apply swept sinusoidal excitation (50 - 350 kHz). Trim feedback'
          ' capacitance Cf\nuntil the differential output ΔV ≈ 0 mV across'
          ' undamaged baseline substrate.',
          c_white,
      ),
      (
          'STEP 4: Stress Induction & Charge Gradient Mapping',
          'Subject asset to mechanical loading or fatigue crack growth.'
          ' Monitor localized\ndivergence in ΔV; map sharp peak singularities'
          ' (∇D3) to pinpoint crack coordinates.',
          c_emerald,
      ),
  ]

  for i, (s_title, s_body, s_acc) in enumerate(steps):
    s_y = 52.0 - i * 9.2  # Calibrated pitch ensures Step 4 stays above y=23.0
    ax.add_patch(
        FancyBboxPatch(
            (7.5, s_y),
            85.0,
            8.2,
            boxstyle='round,pad=0.2,rounding_size=0.3',
            facecolor='#081427',
            edgecolor='#204575',
            lw=0.8,
            zorder=4,
        )
    )
    # Step Number Badge
    ax.add_patch(
        FancyBboxPatch(
            (8.8, s_y + 4.8),
            31.0,
            2.7,
            boxstyle='round,pad=0.1,rounding_size=0.2',
            facecolor='#0c234b',
            edgecolor=s_acc,
            lw=0.7,
            zorder=5,
        )
    )
    ax.text(
        24.3,
        s_y + 6.1,
        s_title,
        color=s_acc,
        fontsize=7.2,
        weight='heavy',
        ha='center',
        va='center',
        zorder=6,
    )

    # Step Body Text
    ax.text(
        9.2, s_y + 3.0, s_body, color=c_muted, fontsize=7.1, va='top', zorder=5
    )

  # ------------------------------------------------------------------
  # TRANSITION BADGE: Monograph Transition Pill -> Page 16 (Clearance Protected)
  # ------------------------------------------------------------------
  ax.add_patch(
      FancyBboxPatch(
          (10.0, 15.2),
          80.0,
          3.8,
          boxstyle='round,pad=0.2,rounding_size=0.4',
          facecolor='#08152b',
          edgecolor='#b45309',
          lw=0.9,
          zorder=3,
      )
  )
  ax.text(
      50.0,
      16.9,
      'ANALYTICAL BENCHMARKING & FINITE ELEMENT VALIDATION CONTINUES ON PAGE 16.',
      color=c_gold_glow,
      fontsize=7.6,
      weight='bold',
      style='italic',
      ha='center',
      zorder=4,
  )

  # ------------------------------------------------------------------
  # 5. Bottom Running Footer Bar (Page 15 Normalized)
  # ------------------------------------------------------------------
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
      ' GARRF-MAG1-SINGBHA-2026.P15',
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
      'Page 15',
      color=c_gold_glow,
      fontsize=9.6,
      weight='black',
      ha='right',
      zorder=4,
  )

  output_filename = 'SingBha_Magazine_Page_15_Experimental_Protocol_Audited.png'
  plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
  plt.close()

  display(IPImage(filename=output_filename, width=720))
  print(
      f'Generated successfully: {output_filename} (A4 300 DPI Page 15 - Audited'
      ' & Zero Overlap)'
  )
  files.download(output_filename)


if __name__ == '__main__':
  generate_magazine_page_15_experimental_protocol_large_font()
