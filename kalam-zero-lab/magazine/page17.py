import io
import urllib.request
from google.colab import files
from IPython.display import Image as IPImage, display
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def generate_magazine_page_17_ai_ingestion_arjun_fixed():
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

  # Monograph Section 15 Header
  ax.text(
      6.5,
      118.8,
      'SECTION 15 • AI INGESTION ARCHITECTURE & ARJUN KNOWLEDGE BRIDGING',
      color=c_gold_glow,
      fontsize=9.4,
      weight='heavy',
      ha='left',
      zorder=4,
  )
  ax.text(
      6.5,
      114.6,
      'AI Ingestion and ARJUN: Charge-Domain to Semantic Bridging',
      color=c_white,
      fontsize=14.0,
      weight='black',
      ha='left',
      zorder=4,
  )
  ax.text(
      6.5,
      111.4,
      'AI-ready pipelines for spatial gradient vectors, Multi-Domain Asset'
      ' Knowledge Graphs & Arjun reasoning.',
      color=c_muted,
      fontsize=8.8,
      weight='medium',
      ha='left',
      zorder=4,
  )

  # ------------------------------------------------------------------
  # COLUMN 1: AI-READY INGESTION ARCHITECTURE (Left Half)
  # ------------------------------------------------------------------
  col1_x = 6.0
  # Shortened to fit safely within x = 6.0 to 48.0 (No overlap across center)
  ax.text(
      col1_x + 1.0,
      106.6,
      '15.1 DATA INGESTION (ADIA)',
      color=c_white,
      fontsize=9.2,
      weight='heavy',
      ha='left',
      zorder=4,
  )

  # Left Column, Top Card: Gradient Vector Pipeline
  card_adia = FancyBboxPatch(
      (col1_x, 69.0),
      44.0,
      35.0,
      boxstyle='round,pad=0.3,rounding_size=0.6',
      facecolor=c_subcard,
      edgecolor='#254778',
      lw=1.1,
      zorder=3,
  )
  ax.add_patch(card_adia)
  ax.text(
      col1_x + 22.0,
      100.8,
      'ADIA: CHARGE GRADIENT VECTOR PIPELINE',
      color=c_gold_glow,
      fontsize=8.0,
      weight='heavy',
      ha='center',
      zorder=5,
  )

  adia_flow = [
      (
          '1. MULTI-CHANNEL INGEST',
          'Segmented pad data q_A(t), q_B(t) captured at virtual ground.',
          c_cyan,
      ),
      (
          '2. SPATIAL GRADIENT (∇D3)',
          'High-SNR differential isolation of incipient micro-crack'
          ' signature.',
          c_white,
      ),
      (
          '3. FEATURE VECTORING',
          'max|∇D3|, singularity bandwidth, and multi-axial Poisson metrics.',
          c_emerald,
      ),
      (
          '4. AI TRAINING SET GENERATION',
          'Automatic labeling against calibrated load and defect size data.',
          c_white,
      ),
  ]
  for i, (adia_hdr, adia_txt, adia_col) in enumerate(adia_flow):
    adia_y = 96.0 - i * 6.5
    ax.text(
        col1_x + 2.5,
        adia_y,
        adia_hdr,
        color=adia_col,
        fontsize=7.2,
        weight='bold',
        zorder=5,
    )
    ax.text(
        col1_x + 2.5,
        adia_y - 2.0,
        adia_txt,
        color=c_muted,
        fontsize=6.7,
        zorder=5,
    )

  # Left Column, Bottom Card: Multi-Domain Knowledge Graph
  card_makg = FancyBboxPatch(
      (col1_x, 21.0),
      44.0,
      45.0,
      boxstyle='round,pad=0.3,rounding_size=0.6',
      facecolor=c_subcard,
      edgecolor='#254778',
      lw=1.1,
      zorder=3,
  )
  ax.add_patch(card_makg)
  ax.text(
      col1_x + 22.0,
      62.8,
      'MULTI-DOMAIN ASSET KNOWLEDGE GRAPH (MAKG)',
      color=c_gold_glow,
      fontsize=7.8,
      weight='heavy',
      ha='center',
      zorder=5,
  )

  ax.text(
      col1_x + 2.5,
      59.0,
      'Bridging structural mechanics to diagnostic semantic entities.',
      color=c_muted,
      fontsize=7.0,
      ha='left',
      zorder=5,
  )

  makg_nodes = [
      ('• Structural Domain', 'Material: Concrete C40 | Rebar: Fe500', c_white),
      (
          '• Load Domain',
          'Static: Gravity | Dynamic: Metro Traffic (300 Hz)',
          c_cyan,
      ),
      (
          '• Sensor Domain',
          'Location: Pier 4 Node 7 | Type: SingBha Quadrant',
          c_emerald,
      ),
      (
          '• Failure Domain',
          'Failure Mode: Tendon Slippage | Priority: Critical',
          c_white,
      ),
  ]
  for i, (makg_hdr, makg_txt, makg_col) in enumerate(makg_nodes):
    makg_y = 54.5 - i * 6.5
    ax.text(
        col1_x + 2.5,
        makg_y,
        makg_hdr,
        color=makg_col,
        fontsize=7.2,
        weight='bold',
        zorder=5,
    )
    ax.text(
        col1_x + 2.5,
        makg_y - 2.0,
        makg_txt,
        color=c_muted,
        fontsize=6.7,
        zorder=5,
    )

  # ------------------------------------------------------------------
  # COLUMN 2: ARJUN KNOWLEDGE BRIDGING (Right Half)
  # ------------------------------------------------------------------
  col2_x = 52.0
  # Starts cleanly at x = 53.0 with zero collision[cite: 3]
  ax.text(
      col2_x + 1.0,
      106.6,
      '15.2 ARJUN REASONING ENGINE',
      color=c_white,
      fontsize=9.2,
      weight='heavy',
      ha='left',
      zorder=4,
  )

  # Right Column, Top Card: Arjun Rational Reasoning
  card_arjun = FancyBboxPatch(
      (col2_x, 69.0),
      44.0,
      35.0,
      boxstyle='round,pad=0.3,rounding_size=0.6',
      facecolor=c_subcard,
      edgecolor='#254778',
      lw=1.1,
      zorder=3,
  )
  ax.add_patch(card_arjun)
  ax.text(
      col2_x + 22.0,
      100.8,
      'ARJUN RATIONAL REASONING ENGINE',
      color=c_gold_glow,
      fontsize=8.0,
      weight='heavy',
      ha='center',
      zorder=5,
  )

  arjun_rational = [
      (
          '• Knowledge Synthesis:',
          'Combines ∇D3 features, MAKG context, and failure rules.',
          c_cyan,
      ),
      (
          '• Cross-Domain Reasoning:',
          'Transfers delamination logic (composite) to voids (concrete rebar).',
          c_white,
      ),
      (
          '• Explanation Audit Trail:',
          'Generates logical causal trails behind every diagnostic hypothesis.',
          c_emerald,
      ),
  ]
  for i, (arjun_hdr, arjun_txt, arjun_col) in enumerate(arjun_rational):
    arjun_y = 95.5 - i * 8.2
    ax.text(
        col2_x + 2.5,
        arjun_y,
        arjun_hdr,
        color=arjun_col,
        fontsize=7.2,
        weight='bold',
        zorder=5,
    )
    ax.text(
        col2_x + 2.5,
        arjun_y - 2.2,
        arjun_txt,
        color=c_muted,
        fontsize=6.7,
        zorder=5,
    )

  # Right Column, Bottom Card: Diagnostic Explainability
  card_explain = FancyBboxPatch(
      (col2_x, 21.0),
      44.0,
      45.0,
      boxstyle='round,pad=0.3,rounding_size=0.6',
      facecolor=c_subcard,
      edgecolor='#254778',
      lw=1.1,
      zorder=3,
  )
  ax.add_patch(card_explain)
  ax.text(
      col2_x + 22.0,
      62.8,
      "DIAGNOSTIC EXPLAINABILITY & 'WHY' ANALYSIS",
      color=c_gold_glow,
      fontsize=7.8,
      weight='heavy',
      ha='center',
      zorder=5,
  )

  ax.text(
      col2_x + 2.5,
      59.0,
      'ARJUN details the rationale for crack localization.',
      color=c_muted,
      fontsize=7.0,
      ha='left',
      zorder=5,
  )

  # Rational explanation block with safe bounds (width = 39.5)
  rationale_box = FancyBboxPatch(
      (col2_x + 2.0, 24.0),
      40.0,
      30.0,
      boxstyle='round,pad=0.2,rounding_size=0.4',
      facecolor='#081427',
      edgecolor='#b45309',
      lw=0.8,
      zorder=5,
  )
  ax.add_patch(rationale_box)
  ax.text(
      col2_x + 22.0,
      51.2,
      'ARJUN RATIONALE TRACE (ART)',
      color=c_white,
      fontsize=7.2,
      weight='bold',
      ha='center',
      zorder=6,
  )

  # Formatted text lines fitting safely within the box width[cite: 4]
  art_lines = [
      (
          'Condition:',
          '∇D3 peak singularity amplitude > 500% over baseline.',
          c_white,
      ),
      (
          'MAKG Context:',
          'Asset: Girders | Component: Prestress Tendon Span 4.',
          c_cyan,
      ),
      (
          'Failure Rule:',
          'Traction collapse at adhesive boundary (Eq. 13, Monograph P12).',
          c_emerald,
      ),
      (
          '-> Rationale:',
          'Divergence confirms incipient mechanical defect below footprint.',
          c_gold_glow,
      ),
  ]

  for i, (art_hdr, art_txt, art_col) in enumerate(art_lines):
    art_y = 47.5 - i * 4.6
    ax.text(
        col2_x + 4.0,
        art_y,
        art_hdr,
        color=art_col,
        fontsize=6.8,
        weight='bold',
        ha='left',
        zorder=6,
    )
    ax.text(
        col2_x + 4.0,
        art_y - 1.8,
        art_txt,
        color=c_muted,
        fontsize=6.3,
        ha='left',
        zorder=6,
    )

  # The wrapped hypothesis cleanly contained inside box bounds[cite: 4]
  ax.text(
      col2_x + 4.0,
      28.5,
      '** Hypothesis (Localized Flaw Detected):',
      color=c_crimson,
      fontsize=6.7,
      weight='bold',
      ha='left',
      zorder=6,
  )
  ax.text(
      col2_x + 4.0,
      26.5,
      'Localized tendon void / debonding at node (4, 7).',
      color='#fca5a5',
      fontsize=6.4,
      weight='semibold',
      ha='left',
      zorder=6,
  )

  # ------------------------------------------------------------------
  # TRANSITION BADGE: Monograph Transition Pill -> Page 18
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
      'ARJUN RATIONAL REASONING DEMONSTRATIONS ACROSS DEFECT MODES'
      ' CONTINUE ON PAGE 18.',
      color=c_gold_glow,
      fontsize=7.4,
      weight='bold',
      style='italic',
      ha='center',
      zorder=4,
  )

  # ------------------------------------------------------------------
  # 5. Bottom Running Footer Bar (Page 17 Normalized)
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
      ' GARRF-MAG1-SINGBHA-2026.P17',
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
      'Page 17',
      color=c_gold_glow,
      fontsize=9.5,
      weight='black',
      ha='right',
      zorder=4,
  )

  output_filename = 'SingBha_Magazine_Page_17_AI_Rational_Ingestion_Audited.png'
  plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
  plt.close()

  display(IPImage(filename=output_filename, width=720))
  print(
      f'Generated successfully: {output_filename} (A4 300 DPI Page 17 - Audited'
      ' & Zero Overlap)'
  )
  files.download(output_filename)


if __name__ == '__main__':
  generate_magazine_page_17_ai_ingestion_arjun_fixed()
