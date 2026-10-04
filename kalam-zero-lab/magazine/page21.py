import io
import urllib.request
from google.colab import files
from IPython.display import Image as IPImage, display
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def generate_magazine_page_21_arjun_multi_agent():
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

  # Section 19 Header Block
  ax.text(
      6.5,
      118.8,
      'SECTION 19 • ARJUN MULTI-AGENT AUTONOMOUS REASONING ARCHITECTURE',
      color=c_gold_glow,
      fontsize=9.4,
      weight='heavy',
      ha='left',
      zorder=4,
  )
  ax.text(
      6.5,
      114.6,
      'The 4-Agent Consensus Engine: From Micro-Spike to Structural Action',
      color=c_white,
      fontsize=13.6,
      weight='black',
      ha='left',
      zorder=4,
  )
  ax.text(
      6.5,
      111.4,
      'Deconstructing the collaborative multi-agent loop that parses EMCD Node 7'
      ' signals, queries the MAKG, validates physics, and issues maintenance'
      ' directives.',
      color=c_muted,
      fontsize=8.4,
      weight='medium',
      ha='left',
      zorder=4,
  )

  # ------------------------------------------------------------------
  # CARD 1: THE 4-AGENT ORCHESTRATION MATRIX (y = 66.5 to 110.0)
  # 2x2 Grid of Agents with Large, Clear, Readable Fonts
  # ------------------------------------------------------------------
  card1_box = FancyBboxPatch(
      (6.0, 66.5),
      88.0,
      43.5,
      boxstyle='round,pad=0.3,rounding_size=0.5',
      facecolor=c_subcard,
      edgecolor='#254778',
      lw=1.0,
      zorder=3,
  )
  ax.add_patch(card1_box)

  # Card 1 Title Bar
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
      '19.1 THE 4-AGENT DEDUCTION LOOP: COLLABORATIVE CONSENSUS PIPELINE',
      color=c_gold_glow,
      fontsize=7.6,
      weight='heavy',
      va='center',
      zorder=5,
  )

  # 2x2 Grid of Agents
  grid_w = 41.5
  grid_h = 17.5
  gap_x = 3.0
  gap_y = 1.6

  agents = [
      {
          'pos': (7.5, 87.0),
          'id': 'AGENT 1: PERCEPTION AGENT',
          'role': 'Signal Ingestion & Virtual Ground Filter',
          'color': c_cyan,
          'pts': [
              '• Monitors nodal TIA outputs; detects +380% spike at Node 7.',
              '• Verifies virtual ground (0V) integrity to reject cable capacitance.',
              '• Passes validated gradient vector ∇D₃ to Knowledge Agent.',
          ],
      },
      {
          'pos': (51.0, 87.0),
          'id': 'AGENT 2: GRAPH TRIPLES AGENT',
          'role': 'Asset BIM & Digital Twin Graph Traversal',
          'color': c_gold_glow,
          'pts': [
              '• Maps Node 7 to Span 4, Deck Flange, at coordinate x = 58.0 m.',
              '• Identifies spatial proximity to Anchorage G3 prestressed rebar.',
              '• Dispatches structural geometry context to Physics Arbiter.',
          ],
      },
      {
          'pos': (7.5, 68.0),
          'id': 'AGENT 3: PHYSICS ARBITER AGENT',
          'role': 'Constitutive Tensor & Boundary Enforcement',
          'color': c_purple,
          'pts': [
              '• Confirms stress singularity condition: traction σ_xx → 0 at crack mouth.',
              '• Validates thermal immunity proof: ∂ε₃₃ᵀ/∂x ≡ 0 cancels diurnal drift.',
              '• Cross-examines listener PZT 2 for >18 dB ray shadow attenuation.',
          ],
      },
      {
          'pos': (51.0, 68.0),
          'id': 'AGENT 4: ACTION & DIRECTIVE AGENT',
          'role': 'Confidence Scoring & Automated Work Order',
          'color': c_emerald,
          'pts': [
              '• Reaches multi-agent consensus with 97.4% diagnostic confidence.',
              '• Rules out sensor fault, thermal noise, and ground loop anomalies.',
              '• Generates mm-accurate maintenance ticket and alerts highway engineers.',
          ],
      },
  ]

  for ag in agents:
    gx, gy = ag['pos']
    ax.add_patch(
        FancyBboxPatch(
            (gx, gy),
            grid_w,
            grid_h,
            boxstyle='round,pad=0.2,rounding_size=0.3',
            facecolor='#081427',
            edgecolor=ag['color'],
            lw=0.9,
            zorder=4,
        )
    )

    # Agent Title
    ax.text(
        gx + 1.5,
        gy + grid_h - 2.2,
        ag['id'],
        color=ag['color'],
        fontsize=6.6,
        weight='heavy',
        zorder=5,
    )
    # Role Subtitle
    ax.text(
        gx + 1.5,
        gy + grid_h - 4.0,
        ag['role'],
        color=c_white,
        fontsize=5.6,
        weight='bold',
        zorder=5,
    )

    # Bullet points with generous spacing
    by = gy + grid_h - 6.6
    for pt in ag['pts']:
      ax.text(
          gx + 1.5,
          by,
          pt,
          color='#cbd5e1',
          fontsize=5.4,
          weight='medium',
          zorder=5,
      )
      by -= 3.2

  # Center Interaction Arrows (Agent 1 -> 2 -> 3 -> 4)
  ax.annotate(
      '',
      xy=(50.5, 95.8),
      xytext=(49.5, 95.8),
      arrowprops=dict(arrowstyle='->', color=c_gold_glow, lw=1.2),
      zorder=6,
  )
  ax.annotate(
      '',
      xy=(71.7, 86.5),
      xytext=(71.7, 85.8),
      arrowprops=dict(arrowstyle='->', color=c_purple, lw=1.2),
      zorder=6,
  )
  ax.annotate(
      '',
      xy=(49.5, 76.8),
      xytext=(50.5, 76.8),
      arrowprops=dict(arrowstyle='->', color=c_emerald, lw=1.2),
      zorder=6,
  )

  # ------------------------------------------------------------------
  # CARD 2: THE CONSENSUS PROTOCOL & ELIMINATION ENGINE (y = 20.2 to 64.5)
  # Explaining how agents reject false positives
  # ------------------------------------------------------------------
  card2_box = FancyBboxPatch(
      (6.0, 20.2),
      88.0,
      44.5,
      boxstyle='round,pad=0.3,rounding_size=0.5',
      facecolor=c_subcard,
      edgecolor='#254778',
      lw=1.0,
      zorder=3,
  )
  ax.add_patch(card2_box)

  # Card 2 Header Bar
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
      '19.2 AUTONOMOUS CONSENSUS & FALSE POSITIVE ELIMINATION PROTOCOL',
      color=c_emerald,
      fontsize=7.6,
      weight='heavy',
      va='center',
      zorder=5,
  )

  # 3 Wide Horizontal Consensus Stages
  st_h = 11.2
  st_gap = 1.8
  st_y_start = 48.0

  protocols = [
      {
          'title': 'STAGE A • PERCEPTION & NOISE ELIMINATION',
          'color': c_cyan,
          'formula': 'Check: Virtual Ground V_sum == 0V  &  Adjacent Nodes Δq_{N6}, Δq_{N8} ≈ Baseline',
          'desc': (
              'Perception Agent cross-checks adjacent sensor channels. If an isolated spike'
              ' occurs without ground loop continuity, it is discarded as electromagnetic noise.'
              ' Verified real signals advance to the Knowledge Graph.'
          ),
          'status': 'Noise Rejected: 100%',
      },
      {
          'title': 'STAGE B • GRAPH-PHYSICS CONSENSUS REASONING',
          'color': c_purple,
          'formula': 'Check: d₃₁ (∂σ_xx/∂x) ≫ Threshold  &  ∂ε₃₃ᵀ/∂x ≡ 0 (Thermal Neutrality)',
          'desc': (
              'Physics Arbiter interrogates the Graph. If the spike coincides with a stress'
              ' concentration zone and passes the thermal invariance test, ambient temperature shifts'
              ' are permanently ruled out as the root cause.'
          ),
          'status': 'Thermal Drift: 0.00%',
      },
      {
          'title': 'STAGE C • MULTI-PATH CORROBORATION & ACTION DIRECTIVE',
          'color': c_emerald,
          'formula': 'Consensus: PZT 2 Ray Shadow > 18 dB  ==>  Issue Work Order [FATIGUE-CRACK-SP4]',
          'desc': (
              'Final verification requires far-field corroboration from listener PZT 2. Once the'
              ' transmission drop across Node 7 is verified, Action Agent confirms true flaw'
              ' presence with 97.4% confidence and schedules repairs.'
          ),
          'status': 'Confidence: 97.4%',
      },
  ]

  for p_i, p_info in enumerate(protocols):
    py = st_y_start - p_i * (st_h + st_gap)

    # Stage Box
    ax.add_patch(
        FancyBboxPatch(
            (7.5, py),
            85.0,
            st_h,
            boxstyle='round,pad=0.2,rounding_size=0.3',
            facecolor='#081427',
            edgecolor='#204575',
            lw=0.8,
            zorder=4,
        )
    )

    # Title & Badge
    ax.text(
        9.0,
        py + st_h - 2.2,
        p_info['title'],
        color=p_info['color'],
        fontsize=6.8,
        weight='heavy',
        zorder=5,
    )
    ax.add_patch(
        FancyBboxPatch(
            (72.0, py + st_h - 3.2),
            19.0,
            2.4,
            boxstyle='round,pad=0.1,rounding_size=0.2',
            facecolor='#0c234b',
            edgecolor=p_info['color'],
            lw=0.6,
            zorder=5,
        )
    )
    ax.text(
        81.5,
        py + st_h - 2.0,
        p_info['status'],
        color=c_white,
        fontsize=5.6,
        weight='black',
        ha='center',
        va='center',
        zorder=6,
    )

    # Mathematical Formula
    ax.text(
        9.0,
        py + st_h - 4.4,
        p_info['formula'],
        color=c_gold_glow,
        fontsize=6.0,
        weight='bold',
        zorder=5,
    )

    # Detailed Description Text
    ax.text(
        9.0,
        py + st_h - 6.2,
        p_info['desc'],
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

  # Transition Badge -> Page 22
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
      'PAGE 22: REAL-WORLD FIELD DEPLOYMENTS & EMPIRICAL VALIDATION DATA'
      ' CONTINUES NEXT.',
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
      ' GARRF-MAG1-SINGBHA-2026.P21',
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
      'Page 21',
      color=c_gold_glow,
      fontsize=9.5,
      weight='black',
      ha='right',
      zorder=4,
  )

  # Save and Export High-Resolution Plate
  output_filename = 'SingBha_Magazine_Page_21_ARJUN_Multi_Agent.png'
  plt.savefig(output_filename, dpi=300, facecolor=c_abyss)
  plt.close()

  display(IPImage(filename=output_filename, width=720))
  print(
      f'Generated successfully: {output_filename} (A4 300 DPI Page 21 - ARJUN'
      ' Multi-Agent Architecture)'
  )
  files.download(output_filename)


if __name__ == '__main__':
  generate_magazine_page_21_arjun_multi_agent()
