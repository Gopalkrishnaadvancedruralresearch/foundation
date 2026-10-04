import io
import urllib.request
from google.colab import files
from IPython.display import Image as IPImage, display
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def generate_magazine_page_19_benchmark_and_impact():
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
  c_muted = '#cbd5e1'

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

  # Header Titles
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

  # Section 17 Title Block
  ax.text(
      6.5,
      118.8,
      'SECTION 17 • BENCHMARK COMPARISON MATRIX & NATIONAL ECONOMIC IMPACT',
      color=c_gold_glow,
      fontsize=9.4,
      weight='heavy',
      ha='left',
      zorder=4,
  )
  ax.text(
      6.5,
      114.6,
      'Comparative Validation: Classical EMI vs. SingBha-EMCD Paradigms',
      color=c_white,
      fontsize=13.6,
      weight='black',
      ha='left',
      zorder=4,
  )
  ax.text(
      6.5,
      111.4,
      'Rigorous quantitative benchmarking against commercial LCR analyzers &'
      ' transformative economic viability for Bharat & Singapore.',
      color=c_muted,
      fontsize=8.4,
      weight='medium',
      ha='left',
      zorder=4,
  )

  # ------------------------------------------------------------------
  # CARD 1: THE BENCHMARK COMPARISON MATRIX (y = 66.5 to 110.0)
  # A structured, non-overlapping comparison table
  # ------------------------------------------------------------------
  table_box = FancyBboxPatch(
      (6.0, 66.5),
      88.0,
      43.5,
      boxstyle='round,pad=0.3,rounding_size=0.5',
      facecolor=c_subcard,
      edgecolor='#254778',
      lw=1.0,
      zorder=3,
  )
  ax.add_patch(table_box)

  # Header Bar for Matrix
  ax.add_patch(
      FancyBboxPatch(
          (6.8, 105.8),
          86.4,
          3.2,
          boxstyle='round,pad=0.1,rounding_size=0.2',
          facecolor='#0c234b',
          edgecolor=c_gold_glow,
          lw=0.7,
          zorder=4,
      )
  )
  ax.text(
      8.0,
      107.4,
      'TABLE 17.1: SYSTEMIC SPECIFICATION COMPARISON MATRIX',
      color=c_gold_glow,
      fontsize=7.6,
      weight='heavy',
      va='center',
      zorder=5,
  )

  # Table Column Header Coordinates
  # Cols: Metric / Feature (x=7.5..34.0), Classical EMI (x=35.0..62.0), SingBha-EMCD (x=63.0..93.0)
  th_y = 102.5
  ax.add_patch(
      FancyBboxPatch(
          (7.2, th_y - 1.2),
          26.8,
          3.0,
          boxstyle='round,pad=0.1,rounding_size=0.1',
          facecolor='#081427',
          edgecolor='#334155',
          lw=0.5,
          zorder=4,
      )
  )
  ax.add_patch(
      FancyBboxPatch(
          (35.0, th_y - 1.2),
          27.0,
          3.0,
          boxstyle='round,pad=0.1,rounding_size=0.1',
          facecolor='#1f1118',
          edgecolor=c_crimson,
          lw=0.6,
          zorder=4,
      )
  )
  ax.add_patch(
      FancyBboxPatch(
          (63.0, th_y - 1.2),
          30.0,
          3.0,
          boxstyle='round,pad=0.1,rounding_size=0.1',
          facecolor='#092327',
          edgecolor=c_emerald,
          lw=0.6,
          zorder=4,
      )
  )

  ax.text(
      8.2,
      th_y + 0.3,
      'PERFORMANCE PARAMETER',
      color=c_cyan,
      fontsize=5.8,
      weight='black',
      zorder=5,
  )
  ax.text(
      36.0,
      th_y + 0.3,
      'CLASSICAL SCALAR EMI (KEYSIGHT)',
      color='#fca5a5',
      fontsize=5.8,
      weight='black',
      zorder=5,
  )
  ax.text(
      64.0,
      th_y + 0.3,
      'SINGBHA-EMCD VECTOR TOPOLOGY',
      color='#6ee7b7',
      fontsize=5.8,
      weight='black',
      zorder=5,
  )

  # Table Rows (8 Rigorous Comparative Rows)
  matrix_rows = [
      (
          'Diagnostic Metric',
          'Lumped Scalar Conductance G(ω)',
          'Spatial Gradient Singularity ∇D₃',
      ),
      (
          'Incipient Crack Sensitivity',
          '< 0.5% perturbation (swamped)',
          '> +380% singular spike (>24 dB SNR)',
      ),
      (
          'Diurnal Temperature Drift',
          '10% – 25% peak shift (false alarms)',
          'Zero thermal drift (∂ε₃₃ᵀ/∂x ≡ 0)',
      ),
      (
          'Cable Length Tolerance',
          '< 3 – 5 m (capacitive shunting)',
          '> 50 m (virtual ground 0V clamped)',
      ),
      (
          'Damage Mode Directionality',
          'Blind to crack vector / tensor',
          'Directional vector dipole separation',
      ),
      (
          'Transducer Hardware Count',
          'N active PZTs ($15 – $40 each)',
          '1–2 PZTs + N passive metallic taps',
      ),
      (
          'Instrumentation Unit Cost',
          '$25,000 – $50,000 (Commercial LCR)',
          '< $15 USD (DIY TIA Array + ADC)',
      ),
      (
          'AI Engine Ingestion Fitness',
          'Complex baseline tables required',
          'Direct ARJUN Causal Graph reasoning',
      ),
  ]

  r_y_start = 97.2
  for i, (param, emi_val, emcd_val) in enumerate(matrix_rows):
    curr_ry = r_y_start - i * 3.7
    row_bg = '#07162c' if i % 2 == 0 else '#091c38'
    ax.add_patch(
        FancyBboxPatch(
            (7.2, curr_ry - 1.0),
            85.8,
            3.2,
            boxstyle='round,pad=0.1,rounding_size=0.1',
            facecolor=row_bg,
            edgecolor='#1d3863',
            lw=0.4,
            zorder=4,
        )
    )

    ax.text(
        8.2,
        curr_ry + 0.5,
        param,
        color=c_white,
        fontsize=5.3,
        weight='bold',
        zorder=5,
    )
    ax.text(
        36.0,
        curr_ry + 0.5,
        emi_val,
        color='#cbd5e1',
        fontsize=5.1,
        weight='medium',
        zorder=5,
    )
    ax.text(
        64.0,
        curr_ry + 0.5,
        emcd_val,
        color=c_gold_glow if i == 6 else ('#a7f3d0' if i != 2 else c_cyan),
        fontsize=5.2,
        weight='bold',
        zorder=5,
    )

  # ------------------------------------------------------------------
  # CARD 2: NATIONAL ECONOMIC & INFRASTRUCTURE IMPACT (y = 20.2 to 64.5)
  # Bilateral Strategic Impact: Bharat & Singapore Perspectives
  # ------------------------------------------------------------------
  impact_box = FancyBboxPatch(
      (6.0, 20.2),
      88.0,
      44.5,
      boxstyle='round,pad=0.3,rounding_size=0.5',
      facecolor=c_subcard,
      edgecolor='#254778',
      lw=1.0,
      zorder=3,
  )
  ax.add_patch(impact_box)

  # Header Bar for Economic Section
  ax.add_patch(
      FancyBboxPatch(
          (6.8, 60.8),
          86.4,
          3.0,
          boxstyle='round,pad=0.1,rounding_size=0.2',
          facecolor='#0c234b',
          edgecolor=c_emerald,
          lw=0.7,
          zorder=4,
      )
  )
  ax.text(
      8.0,
      62.3,
      '17.2 BILATERAL STRATEGIC & ECONOMIC IMPACT: BHARAT & SINGAPORE'
      ' HORIZONS',
      color=c_emerald,
      fontsize=7.4,
      weight='heavy',
      va='center',
      zorder=5,
  )

  # Two Large Pillars: Left (Bharat Scale), Right (Singapore Resilience)
  p_w = 41.5
  p_h = 23.5
  p_y = 35.8

  # Pillar 1: Bharat National Scale
  ax.add_patch(
      FancyBboxPatch(
          (7.5, p_y),
          p_w,
          p_h,
          boxstyle='round,pad=0.2,rounding_size=0.3',
          facecolor='#081427',
          edgecolor='#f59e0b',
          lw=0.8,
          zorder=4,
      )
  )
  ax.text(
      8.5,
      p_y + p_h - 2.2,
      'BHARAT: RURAL & CRITICAL ASSET SCALE',
      color=c_gold_glow,
      fontsize=6.4,
      weight='black',
      zorder=5,
  )

  bharat_points = [
      (
          '• Vast Infrastructure Footprint:',
          'Bharat possesses >140,000 km of national highways, 68,000 km of'
          ' railway track, and thousands of post-tensioned bridges spanning'
          ' monsoon terrains.',
      ),
      (
          '• The Economic Bottleneck:',
          'Imported LCR analyzers cost ₹25–40 Lakhs each. Scaling classical EMI'
          ' across rural culverts and flyovers is economically impossible.',
      ),
      (
          '• The SingBha Revolution:',
          'At <₹1,200 ($15 USD) per node, SingBha-EMCD democratizes continuous'
          ' structural monitoring, fulfilling Dr. Kalam\'s Zero-Cost rural'
          ' engineering mission.',
      ),
  ]
  by_cur = p_y + p_h - 4.5
  for b_hdr, b_txt in bharat_points:
    ax.text(
        8.5,
        by_cur,
        b_hdr,
        color=c_white,
        fontsize=5.3,
        weight='bold',
        zorder=5,
    )
    by_cur -= 1.3
    # Two-line clean wrapping
    lines = [
        b_txt[:48],
        b_txt[48:96]
        + (
            '...'
            if len(b_txt) > 96 and not b_txt[48:].startswith(' ')
            else b_txt[96:]
        ),
    ]
    for ln in lines:
      if ln.strip():
        ax.text(
            8.5,
            by_cur,
            ln.strip(),
            color='#94a3b8',
            fontsize=4.9,
            weight='medium',
            zorder=5,
        )
        by_cur -= 1.15
    by_cur -= 0.6

  # Pillar 2: Singapore Smart Urban Resilience
  ax.add_patch(
      FancyBboxPatch(
          (51.0, p_y),
          p_w,
          p_h,
          boxstyle='round,pad=0.2,rounding_size=0.3',
          facecolor='#081427',
          edgecolor=c_cyan,
          lw=0.8,
          zorder=4,
      )
  )
  ax.text(
      52.0,
      p_y + p_h - 2.2,
      'SINGAPORE: HIGH-DENSITY DIGITAL RESILIENCE',
      color=c_cyan,
      fontsize=6.4,
      weight='black',
      zorder=5,
  )

  singapore_points = [
      (
          '• Dense Urban Megastructures:',
          'Singapore manages ultra-critical high-density assets: the MRT'
          ' underground rail network, deep tunnel sewerage, and coastal'
          ' viaducts.',
      ),
      (
          '• Tropical Thermal Swings:',
          'Equatorial humidity and solar heat cycling degrade conventional EMI'
          ' with continuous false alarms. EMCD provides zero thermal drift'
          ' fidelity.',
      ),
      (
          '• Smart Nation Digital Twin:',
          'Vector charge gradients directly integrate into city-scale Building'
          ' Information Modeling (BIM) platforms and autonomous ARJUN AI agent'
          ' networks.',
      ),
  ]
  sy_cur = p_y + p_h - 4.5
  for s_hdr, s_txt in singapore_points:
    ax.text(
        52.0,
        sy_cur,
        s_hdr,
        color=c_white,
        fontsize=5.3,
        weight='bold',
        zorder=5,
    )
    sy_cur -= 1.3
    lines = [
        s_txt[:48],
        s_txt[48:96]
        + (
            '...'
            if len(s_txt) > 96 and not s_txt[48:].startswith(' ')
            else s_txt[96:]
        ),
    ]
    for ln in lines:
      if ln.strip():
        ax.text(
            52.0,
            sy_cur,
            ln.strip(),
            color='#94a3b8',
            fontsize=4.9,
            weight='medium',
            zorder=5,
        )
        sy_cur -= 1.15
    sy_cur -= 0.6

  # Bottom Synthesis Subcard inside Card 2
  ax.add_patch(
      FancyBboxPatch(
          (7.5, 21.2),
          85.0,
          13.0,
          boxstyle='round,pad=0.2,rounding_size=0.3',
          facecolor='#051122',
          edgecolor='#204575',
          lw=0.7,
          zorder=4,
      )
  )
  ax.text(
      8.5,
      32.2,
      '17.3 EXECUTIVE SYNTHESIS: CAPITAL EFFICIENCY & LIFESPAN EXTENSION',
      color=c_gold_glow,
      fontsize=6.2,
      weight='heavy',
      zorder=5,
  )
  ax.text(
      8.5,
      30.2,
      '• 99.8% Capital Cost Reduction: Transforming structural health monitoring'
      ' from a multimillion-dollar luxury into an ambient utility.',
      color=c_white,
      fontsize=5.4,
      weight='semibold',
      zorder=5,
  )
  ax.text(
      8.5,
      28.2,
      '• Proactive Disaster Prevention: Detecting 0.1 mm micro-crack'
      ' singularities 18 months before visible spalling prevents catastrophic'
      ' bridge collapses.',
      color=c_muted,
      fontsize=5.2,
      zorder=5,
  )
  ax.text(
      8.5,
      26.2,
      '• Collaborative Bilateral Heritage: Bridging Bharat\'s scale with'
      ' Singapore\'s advanced cyber-physical integration under the Kalam Zero'
      ' Funding charter.',
      color=c_cyan,
      fontsize=5.2,
      zorder=5,
  )
  ax.text(
      8.5,
      24.0,
      '• ARJUN Ingestion Readiness: Clean vector gradient data feeds directly'
      ' into the Multi-Domain Asset Knowledge Graph (MAKG) on Page 20.',
      color=c_emerald,
      fontsize=5.2,
      weight='bold',
      zorder=5,
  )

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

  # Transition Badge -> Page 20
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
      'PAGE 20: MULTI-DOMAIN ASSET KNOWLEDGE GRAPH (MAKG) & ARJUN REASONING'
      ' ARCHITECTURE.',
      color=c_gold_glow,
      fontsize=6.6,
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
      ' GARRF-MAG1-SINGBHA-2026.P19',
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
      'Page 19',
      color=c_gold_glow,
      fontsize=9.5,
      weight='black',
      ha='right',
      zorder=4,
  )

  # Save and Export High-Resolution Plate
  output_filename = 'SingBha_Magazine_Page_19_Benchmark_Matrix.png'
  plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
  plt.close()

  display(IPImage(filename=output_filename, width=720))
  print(
      f'Generated successfully: {output_filename} (A4 300 DPI Page 19 -'
      ' Benchmark Matrix & National Impact)'
  )
  files.download(output_filename)


if __name__ == '__main__':
  generate_magazine_page_19_benchmark_and_impact()
