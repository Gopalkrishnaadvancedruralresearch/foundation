import io
import urllib.request
from google.colab import files
from IPython.display import Image as IPImage, display
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def generate_magazine_page_22_large_font():
  # ------------------------------------------------------------------
  # 1. Page Geometry: International A4 at 300 DPI (8.27 x 11.69 in)
  # ------------------------------------------------------------------
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
  c_muted = '#e2e8f0'

  # Base Canvas Background
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

  # ------------------------------------------------------------------
  # 3. Top Header Container Bar (Exact GARRF Monograph Template)
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

  # Alignment Grid Corner Markers
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

  # Section 20 Title Block (Larger, High Impact)
  ax.text(
      6.5,
      118.8,
      'SECTION 20 • REAL-WORLD FIELD DEPLOYMENTS & EMPIRICAL VALIDATION',
      color=c_gold_glow,
      fontsize=9.8,
      weight='heavy',
      ha='left',
      zorder=4,
  )
  ax.text(
      6.5,
      114.6,
      'Field Testing SingBha-EMCD: Viaduct Girders & Subsea Metro Tunnels',
      color=c_white,
      fontsize=14.0,
      weight='black',
      ha='left',
      zorder=4,
  )
  ax.text(
      6.5,
      111.4,
      'Live empirical deployment validation: Proving zero thermal drift and'
      ' 50m cable immunity.',
      color=c_muted,
      fontsize=9.0,
      weight='medium',
      ha='left',
      zorder=4,
  )

  # ------------------------------------------------------------------
  # CASE STUDY 1: BHARAT HIGHWAY VIADUCT (y = 66.5 to 110.0)
  # High-Visibility Cards with Big, Bold Text
  # ------------------------------------------------------------------
  cs1_box = FancyBboxPatch(
      (6.0, 66.5),
      88.0,
      43.5,
      boxstyle='round,pad=0.3,rounding_size=0.5',
      facecolor=c_subcard,
      edgecolor='#254778',
      lw=1.0,
      zorder=3,
  )
  ax.add_patch(cs1_box)

  # CS1 Header Bar
  ax.add_patch(
      FancyBboxPatch(
          (6.8, 105.8),
          86.4,
          3.2,
          boxstyle='round,pad=0.1,rounding_size=0.2',
          facecolor='#0c234b',
          edgecolor=c_gold_glow,
          lw=0.8,
          zorder=4,
      )
  )
  ax.text(
      8.0,
      107.4,
      '20.1 CASE 1: POST-TENSIONED HIGHWAY VIADUCT (BHARAT FREIGHT CORRIDOR)',
      color=c_gold_glow,
      fontsize=8.4,
      weight='heavy',
      va='center',
      zorder=5,
  )

  # Box 1A: Classical EMI Defect (Red Border)
  ax.add_patch(
      FancyBboxPatch(
          (7.5, 68.2),
          41.5,
          36.5,
          boxstyle='round,pad=0.2,rounding_size=0.3',
          facecolor='#081427',
          edgecolor=c_crimson,
          lw=0.9,
          zorder=4,
      )
  )
  ax.text(
      9.0,
      102.2,
      'CLASSICAL EMI: THERMAL FAILURE',
      color='#fca5a5',
      fontsize=7.8,
      weight='black',
      zorder=5,
  )

  c1_pts = [
      (
          '• Asset Type:',
          '60m Prestressed concrete girder with heavy freight loading.',
      ),
      (
          '• Ambient Heat:',
          'Surface temperatures cycled daily from 14°C to 47°C.',
      ),
      (
          '• Drift Error:',
          'EMI resonance shifted >18%, hiding real structural damage.',
      ),
      (
          '• False Alarms:',
          'Triggered constant false alerts; completely impractical at scale.',
      ),
  ]

  y_p = 98.6
  for hdr, bdy in c1_pts:
    ax.text(
        9.0,
        y_p,
        hdr,
        color=c_white,
        fontsize=7.2,
        weight='bold',
        zorder=5,
    )
    ax.text(
        9.0,
        y_p - 2.1,
        bdy,
        color=c_muted,
        fontsize=6.8,
        weight='medium',
        zorder=5,
    )
    y_p -= 5.2

  # Metric Badge 1A
  ax.add_patch(
      FancyBboxPatch(
          (9.0, 69.4),
          38.5,
          4.0,
          boxstyle='round,pad=0.1,rounding_size=0.2',
          facecolor='#2a080c',
          edgecolor=c_crimson,
          lw=0.8,
          zorder=5,
      )
  )
  ax.text(
      28.2,
      71.4,
      'EMI Thermal False Alarm Rate: > 18%',
      color='#fca5a5',
      fontsize=7.4,
      weight='black',
      ha='center',
      va='center',
      zorder=6,
  )

  # Box 1B: SingBha-EMCD Validation (Green Border)
  ax.add_patch(
      FancyBboxPatch(
          (51.0, 68.2),
          41.5,
          36.5,
          boxstyle='round,pad=0.2,rounding_size=0.3',
          facecolor='#081427',
          edgecolor=c_emerald,
          lw=0.9,
          zorder=4,
      )
  )
  ax.text(
      52.5,
      102.2,
      'SINGBHA-EMCD: ZERO THERMAL DRIFT',
      color=c_emerald,
      fontsize=7.8,
      weight='black',
      zorder=5,
  )

  c2_pts = [
      (
          '• Physical Proof:',
          'Spatial gradient ∂ε₃₃ᵀ/∂x ≡ 0 cancels 100% of sun heating.',
      ),
      (
          '• True Crack Found:',
          'Node 7 spiked by +380% (∇D₃) under live moving truck loads.',
      ),
      (
          '• Defect Verified:',
          'Physical inspection confirmed a 0.15 mm rebar crack at G3.',
      ),
      (
          '• Hardware Cost:',
          'Built with <$15 TIA array, replacing ₹35 Lakh imported analyzer.',
      ),
  ]

  y_p = 98.6
  for hdr, bdy in c2_pts:
    ax.text(
        52.5,
        y_p,
        hdr,
        color=c_emerald if 'Crack' in hdr else c_white,
        fontsize=7.2,
        weight='bold',
        zorder=5,
    )
    ax.text(
        52.5,
        y_p - 2.1,
        bdy,
        color=c_muted,
        fontsize=6.8,
        weight='medium',
        zorder=5,
    )
    y_p -= 5.2

  # Metric Badge 1B
  ax.add_patch(
      FancyBboxPatch(
          (52.5, 69.4),
          38.5,
          4.0,
          boxstyle='round,pad=0.1,rounding_size=0.2',
          facecolor='#052e16',
          edgecolor=c_emerald,
          lw=0.8,
          zorder=5,
      )
  )
  ax.text(
      71.7,
      71.4,
      'EMCD Thermal Baseline Drift: < 0.02%',
      color='#6ee7b7',
      fontsize=7.4,
      weight='black',
      ha='center',
      va='center',
      zorder=6,
  )

  # ------------------------------------------------------------------
  # CASE STUDY 2: SINGAPORE SUBSEA METRO TUNNEL (y = 20.2 to 64.5)
  # High-Visibility Cards with Big, Bold Text
  # ------------------------------------------------------------------
  cs2_box = FancyBboxPatch(
      (6.0, 20.2),
      88.0,
      44.5,
      boxstyle='round,pad=0.3,rounding_size=0.5',
      facecolor=c_subcard,
      edgecolor='#254778',
      lw=1.0,
      zorder=3,
  )
  ax.add_patch(cs2_box)

  # CS2 Header Bar
  ax.add_patch(
      FancyBboxPatch(
          (6.8, 60.8),
          86.4,
          3.0,
          boxstyle='round,pad=0.1,rounding_size=0.2',
          facecolor='#0c234b',
          edgecolor=c_cyan,
          lw=0.8,
          zorder=4,
      )
  )
  ax.text(
      8.0,
      62.3,
      '20.2 CASE 2: HIGH-DENSITY MRT SUBSEA TUNNEL (SINGAPORE DOWNTOWN LINE)',
      color=c_cyan,
      fontsize=8.4,
      weight='heavy',
      va='center',
      zorder=5,
  )

  # Box 2A: Cable Shunting Failure (Red Border)
  ax.add_patch(
      FancyBboxPatch(
          (7.5, 33.5),
          41.5,
          26.0,
          boxstyle='round,pad=0.2,rounding_size=0.3',
          facecolor='#081427',
          edgecolor=c_crimson,
          lw=0.9,
          zorder=4,
      )
  )
  ax.text(
      9.0,
      56.6,
      'EMI CABLE LIMIT: COLLAPSE AT 45 METERS',
      color='#fca5a5',
      fontsize=7.6,
      weight='black',
      zorder=5,
  )

  c3_pts = [
      ('• Cable Distance:', 'Sensors required 45m leads to reach equipment bays.'),
      (
          '• Capacitive Shunt:',
          '45m cable capacitance (>4.5 nF) flattened all signals.',
      ),
      (
          '• Total Failure:',
          'Analyzer was blind; unable to distinguish slip from line loss.',
      ),
  ]

  y_p = 53.4
  for hdr, bdy in c3_pts:
    ax.text(
        9.0,
        y_p,
        hdr,
        color=c_white,
        fontsize=7.2,
        weight='bold',
        zorder=5,
    )
    ax.text(
        9.0,
        y_p - 1.9,
        bdy,
        color=c_muted,
        fontsize=6.7,
        weight='medium',
        zorder=5,
    )
    y_p -= 4.7

  # Box 2B: Virtual Ground Triumph (Cyan Border)
  ax.add_patch(
      FancyBboxPatch(
          (51.0, 33.5),
          41.5,
          26.0,
          boxstyle='round,pad=0.2,rounding_size=0.3',
          facecolor='#081427',
          edgecolor=c_cyan,
          lw=0.9,
          zorder=4,
      )
  )
  ax.text(
      52.5,
      56.6,
      'SINGBHA VIRTUAL-GROUND: >50M INTEGRITY',
      color=c_cyan,
      fontsize=7.6,
      weight='black',
      zorder=5,
  )

  c4_pts = [
      (
          '• 0V Ground Clamping:',
          'Op-amp virtual ground holds leads at exactly 0 Volts.',
      ),
      (
          '• Zero Charging Noise:',
          'dv/dt = 0 across lines; completely eliminates cable capacitance.',
      ),
      (
          '• Joint Micro-Slip Found:',
          'Detected segmental lining shear slip with >22 dB SNR over 45m.',
      ),
  ]

  y_p = 53.4
  for hdr, bdy in c4_pts:
    ax.text(
        52.5,
        y_p,
        hdr,
        color=c_cyan if 'Joint' in hdr else c_white,
        fontsize=7.2,
        weight='bold',
        zorder=5,
    )
    ax.text(
        52.5,
        y_p - 1.9,
        bdy,
        color=c_muted,
        fontsize=6.7,
        weight='medium',
        zorder=5,
    )
    y_p -= 4.7

  # Bottom Synthesis Subcard inside Card 2 (Spacious & Large Text)
  ax.add_patch(
      FancyBboxPatch(
          (7.5, 21.2),
          85.0,
          11.0,
          boxstyle='round,pad=0.2,rounding_size=0.3',
          facecolor='#051122',
          edgecolor='#204575',
          lw=0.8,
          zorder=4,
      )
  )
  ax.text(
      9.0,
      29.8,
      '20.3 FIELD TAKEAWAYS: DUAL BREAKTHROUGH OVER CLASSICAL EMI',
      color=c_gold_glow,
      fontsize=7.4,
      weight='heavy',
      zorder=5,
  )
  ax.text(
      9.0,
      27.2,
      '• 100% Thermal Immunity: Spatial subtraction cancels intense diurnal'
      ' solar heating variations.',
      color=c_white,
      fontsize=6.8,
      weight='semibold',
      zorder=5,
  )
  ax.text(
      9.0,
      24.8,
      '• Extended Cable Range: Virtual-ground topology exceeds 50m cable runs'
      ' without high-frequency loss.',
      color=c_cyan,
      fontsize=6.8,
      weight='semibold',
      zorder=5,
  )
  ax.text(
      9.0,
      22.4,
      '• True Economic Scale: Eliminates expensive commercial LCR analyzers'
      ' using accessible components.',
      color=c_emerald,
      fontsize=6.8,
      weight='bold',
      zorder=5,
  )

  # ARJUN Access Callout Banner
  ax.text(
      50.0,
      18.2,
      'Arjun, our AI Assistant, can answer all your questions. Access link'
      ' available on the final page of this monograph.',
      color=c_cyan,
      fontsize=6.6,
      weight='bold',
      style='italic',
      ha='center',
      zorder=5,
  )

  # Transition Badge -> Page 23
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
      'PAGE 23: STANDARDIZATION PROTOCOLS & KALAM ZERO FUNDING CHARTER'
      ' CONTINUES NEXT.',
      color=c_gold_glow,
      fontsize=7.0,
      weight='bold',
      style='italic',
      ha='center',
      zorder=4,
  )

  # ------------------------------------------------------------------
  # 5. Bottom Running Footer Bar (Official Monograph Template)
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
      ' GARRF-MAG1-SINGBHA-2026.P22',
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
      'Page 22',
      color=c_gold_glow,
      fontsize=9.5,
      weight='black',
      ha='right',
      zorder=4,
  )

  # Save and Export High-Resolution Plate
  output_filename = 'SingBha_Magazine_Page_22_Large_Font.png'
  plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
  plt.close()

  display(IPImage(filename=output_filename, width=720))
  print(
      f'Generated successfully: {output_filename} (A4 300 DPI Page 22 - High'
      ' Legibility Edition)'
  )
  files.download(output_filename)


if __name__ == '__main__':
  generate_magazine_page_22_large_font()
