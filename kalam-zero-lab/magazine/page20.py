import io
import urllib.request
from google.colab import files
from IPython.display import Image as IPImage, display
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def generate_magazine_page_20_readable():
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
  c_purple = '#c084fc'

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

  # Section 18 Header
  ax.text(
      6.5,
      118.8,
      'SECTION 18 • MULTI-DOMAIN ASSET KNOWLEDGE GRAPH (MAKG) ARCHITECTURE',
      color=c_gold_glow,
      fontsize=9.4,
      weight='heavy',
      ha='left',
      zorder=4,
  )
  ax.text(
      6.5,
      114.6,
      'Grounding the Node 7 Crack into ARJUN Causal Diagnostic Logic',
      color=c_white,
      fontsize=13.6,
      weight='black',
      ha='left',
      zorder=4,
  )
  ax.text(
      6.5,
      111.4,
      'How the AI engine ingests the spatial charge gradient singularity from'
      ' Page 18 and proves true flaw root cause.',
      color=c_muted,
      fontsize=8.5,
      weight='medium',
      ha='left',
      zorder=4,
  )

  # ------------------------------------------------------------------
  # CARD 1: THE CAUSAL DIAGNOSTIC PIPELINE (y = 66.5 to 110.0)
  # 4 Large, Clear, Step-by-Step Flow Cards with Legible Fonts
  # ------------------------------------------------------------------
  flow_box = FancyBboxPatch(
      (6.0, 66.5),
      88.0,
      43.5,
      boxstyle='round,pad=0.3,rounding_size=0.5',
      facecolor=c_subcard,
      edgecolor='#254778',
      lw=1.0,
      zorder=3,
  )
  ax.add_patch(flow_box)

  # Header Bar inside Card 1
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
      '18.1 CONTINUING FROM PAGE 18: CAUSAL TRACE OF THE FLAW DETECTED AT'
      ' NODE 7',
      color=c_gold_glow,
      fontsize=7.6,
      weight='heavy',
      va='center',
      zorder=5,
  )

  # 4 Horizontal Flow Stages
  col_w = 20.2
  col_gap = 1.6
  col_h = 36.5
  col_y = 68.2

  stages = [
      {
          'num': 'STAGE 1: SIGNAL',
          'title': 'EMCD Spike at Node 7',
          'color': c_cyan,
          'pts': [
              (
                  '• Page 18 Context:',
                  'The sensing pad at Node 7 records a +380% divergence spike.',
              ),
              (
                  '• Charge Difference:',
                  'Δq_N7 = q_PZT1 - q_N7 exceeds normal threshold by >24 dB.',
              ),
              (
                  '• Classical Failure:',
                  'Standard EMI averages this out to <0.5%, missing the flaw.',
              ),
          ],
      },
      {
          'num': 'STAGE 2: ASSET MAP',
          'title': 'BIM Digital Twin Link',
          'color': c_gold_glow,
          'pts': [
              (
                  '• Geographic Coordinate:',
                  'MAKG maps Node 7 to Span-4, Deck Flange, at x = 58.0 m.',
              ),
              (
                  '• Critical Subsystem:',
                  'Directly adjacent to Post-Tensioned Anchorage G3.',
              ),
              (
                  '• Cable Integrity:',
                  'Virtual ground (0V) sensing rules out cable noise artifacts.',
              ),
          ],
      },
      {
          'num': 'STAGE 3: MECHANICS',
          'title': 'Physical Proof & Heat',
          'color': c_purple,
          'pts': [
              (
                  '• Traction Discontinuity:',
                  'Crack lips force boundary stress to zero (σ_xx → 0).',
              ),
              (
                  '• Thermal Rejection:',
                  'Diurnal sun heat shifts ∂ε₃₃ᵀ/∂x ≡ 0; ruled out as cause.',
              ),
              (
                  '• Trapped Charge:',
                  'Local shear loss traps displacement current at crack mouth.',
              ),
          ],
      },
      {
          'num': 'STAGE 4: VERDICT',
          'title': 'Far-Field & Work Order',
          'color': c_emerald,
          'pts': [
              (
                  '• PZT 2 Listener:',
                  'Far-field sensor verifies >18 dB transmission shadow.',
              ),
              (
                  '• Flaw Confirmation:',
                  '97.4% deterministic certainty of active fatigue crack.',
              ),
              (
                  '• Action Triggered:',
                  'Automated work order issued with exact mm coordinates.',
              ),
          ],
      },
  ]

  for s_i, st in enumerate(stages):
    sx = 7.2 + s_i * (col_w + col_gap)

    # Stage Box
    ax.add_patch(
        FancyBboxPatch(
            (sx, col_y),
            col_w,
            col_h,
            boxstyle='round,pad=0.2,rounding_size=0.3',
            facecolor='#081427',
            edgecolor=st['color'],
            lw=0.9,
            zorder=4,
        )
    )

    # Stage Header
    ax.text(
        sx + col_w / 2,
        col_y + col_h - 2.4,
        st['num'],
        color=st['color'],
        fontsize=6.4,
        weight='heavy',
        ha='center',
        zorder=5,
    )
    ax.text(
        sx + col_w / 2,
        col_y + col_h - 4.6,
        st['title'],
        color=c_white,
        fontsize=6.8,
        weight='bold',
        ha='center',
        zorder=5,
    )

    # Bullet Points (Clearly readable at 6.2 - 6.6 pt)
    by = col_y + col_h - 7.6
    for b_hdr, b_desc in st['pts']:
      ax.text(
          sx + 1.2,
          by,
          b_hdr,
          color=st['color'],
          fontsize=6.2,
          weight='bold',
          zorder=5,
      )
      by -= 1.6
      # Multi-line wrapped text
      lines = [
          b_desc[:28],
          b_desc[28:56]
          + (
              '...'
              if len(b_desc) > 56 and not b_desc[28:].startswith(' ')
              else b_desc[56:]
          ),
      ]
      for ln in lines:
        if ln.strip():
          ax.text(
              sx + 1.2,
              by,
              ln.strip(),
              color='#cbd5e1',
              fontsize=5.8,
              weight='medium',
              zorder=5,
          )
          by -= 1.45
      by -= 0.8

    # Arrow connecting stages
    if s_i < 3:
      ax.annotate(
          '',
          xy=(sx + col_w + col_gap - 0.2, col_y + col_h / 2),
          xytext=(sx + col_w + 0.2, col_y + col_h / 2),
          arrowprops=dict(
              arrowstyle='->', color=c_gold_glow, lw=1.2, mutation_scale=10
          ),
          zorder=6,
      )

  # ------------------------------------------------------------------
  # CARD 2: REASONING RULES & DEDUCTION PROOFS (y = 20.2 to 64.5)
  # 3 Wide Horizontal Strips - Spacious & Highly Readable
  # ------------------------------------------------------------------
  rule_box = FancyBboxPatch(
      (6.0, 20.2),
      88.0,
      44.5,
      boxstyle='round,pad=0.3,rounding_size=0.5',
      facecolor=c_subcard,
      edgecolor='#254778',
      lw=1.0,
      zorder=3,
  )
  ax.add_patch(rule_box)

  # Header Bar for Rule Section
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
      '18.2 ARJUN CAUSAL REASONING ENGINE: 3 CORE VERIFICATION RULES',
      color=c_emerald,
      fontsize=7.6,
      weight='heavy',
      va='center',
      zorder=5,
  )

  # 3 Horizontal Deduction Strips
  strip_h = 11.2
  strip_gap = 1.8
  strip_y_start = 48.0

  strip_data = [
      {
          'id': 'RULE 1: PHYSICAL ORIGIN VERIFICATION',
          'color': c_cyan,
          'triple': r'RDF Triple: ⟨Δq_Node7, :indicatesDiscontinuityAt, Span4_Flange_x58⟩',
          'desc': (
              'The system maps the high-voltage gradient spike directly to'
              ' physical structural coordinates. Because adjacent pads (Node 6'
              ' and Node 8) maintain baseline charge, broad structural'
              ' vibration is immediately ruled out.'
          ),
          'metric': 'Initial Confidence: 45%',
      },
      {
          'id': 'RULE 2: THERMAL DRIFT ELIMINATION & TRACTION COLLAPSE',
          'color': c_purple,
          'triple': r'Governing Physics: ∇D₃ = d₃₁ (∂σ_xx/∂x)  |  ∂ε₃₃ᵀ/∂x ≡ 0 (Cancels Temperature)',
          'desc': (
              'Diurnal solar heating affects all segments uniformly. The'
              ' sharp singularity at Node 7 proves the signal stems from local'
              ' stress relief (σ_xx → 0) at an incipient crack lip, not'
              ' ambient weather fluctuations.'
          ),
          'metric': 'Updated Confidence: 88%',
      },
      {
          'id': 'RULE 3: FAR-FIELD CORROBORATION & FINAL ACTION',
          'color': c_emerald,
          'triple': (
              'Validation Link: ⟨PZT2_FarFieldListener, :recordsRayShadowFrom,'
              ' PZT1_Through_Node7⟩'
          ),
          'desc': (
              'Listener PZT 2 confirms acoustic shadow attenuation along the'
              ' PZT1-Node7 propagation ray. False alarm probability drops to'
              ' near-zero; an automated maintenance repair ticket is generated'
              ' instantly.'
          ),
          'metric': 'Final Confidence: 97.4%',
      },
  ]

  for r_i, r_info in enumerate(strip_data):
    ry = strip_y_start - r_i * (strip_h + strip_gap)

    # Horizontal Strip Card
    ax.add_patch(
        FancyBboxPatch(
            (7.5, ry),
            85.0,
            strip_h,
            boxstyle='round,pad=0.2,rounding_size=0.3',
            facecolor='#081427',
            edgecolor='#204575',
            lw=0.8,
            zorder=4,
        )
    )

    # Strip Header & Badge
    ax.text(
        9.0,
        ry + strip_h - 2.2,
        r_info['id'],
        color=r_info['color'],
        fontsize=6.8,
        weight='heavy',
        zorder=5,
    )

    # Metric Badge
    ax.add_patch(
        FancyBboxPatch(
            (72.0, ry + strip_h - 3.2),
            19.0,
            2.4,
            boxstyle='round,pad=0.1,rounding_size=0.2',
            facecolor='#0c234b',
            edgecolor=r_info['color'],
            lw=0.6,
            zorder=5,
        )
    )
    ax.text(
        81.5,
        ry + strip_h - 2.0,
        r_info['metric'],
        color=c_white,
        fontsize=5.6,
        weight='black',
        ha='center',
        va='center',
        zorder=6,
    )

    # Mathematical Triple Definition
    ax.text(
        9.0,
        ry + strip_h - 4.4,
        r_info['triple'],
        color=c_gold_glow,
        fontsize=6.0,
        weight='bold',
        zorder=5,
    )

    # Detailed Explanation Text (Comfortable font size 6.0 pt)
    ax.text(
        9.0,
        ry + strip_h - 6.2,
        r_info['desc'],
        color=c_muted,
        fontsize=5.8,
        ha='left',
        va='top',
        wrap=True,
        zorder=5,
    )

  # ARJUN Access Callout Banner
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

  # Transition Badge -> Page 21
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
      'PAGE 21: THE 4-AGENT ARJUN MULTI-AGENT REASONING ARCHITECTURE CONTINUES'
      ' NEXT.',
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
      ' GARRF-MAG1-SINGBHA-2026.P20',
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
      'Page 20',
      color=c_gold_glow,
      fontsize=9.5,
      weight='black',
      ha='right',
      zorder=4,
  )

  # Save and Export High-Resolution Plate
  output_filename = 'SingBha_Magazine_Page_20_Readable_MAKG.png'
  plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
  plt.close()

  display(IPImage(filename=output_filename, width=720))
  print(
      f'Generated successfully: {output_filename} (A4 300 DPI Page 20 -'
      ' Legible & Contextually Linked)'
  )
  files.download(output_filename)


if __name__ == '__main__':
  generate_magazine_page_20_readable()
