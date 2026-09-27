---
name: Warm Clinical Mastery
colors:
  surface: '#fff8f5'
  surface-dim: '#e7d7cf'
  surface-bright: '#fff8f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fff1ea'
  surface-container: '#fbebe2'
  surface-container-high: '#f5e5dc'
  surface-container-highest: '#efdfd7'
  on-surface: '#221a15'
  on-surface-variant: '#584143'
  inverse-surface: '#382f29'
  inverse-on-surface: '#feeee5'
  outline: '#8c7073'
  outline-variant: '#e0bec1'
  surface-tint: '#b2244a'
  primary: '#af2148'
  on-primary: '#ffffff'
  primary-container: '#d13c5f'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb2bc'
  secondary: '#006c49'
  on-secondary: '#ffffff'
  secondary-container: '#6cf8bb'
  on-secondary-container: '#00714d'
  tertiary: '#825100'
  on-tertiary: '#ffffff'
  tertiary-container: '#a36700'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffd9dd'
  primary-fixed-dim: '#ffb2bc'
  on-primary-fixed: '#400012'
  on-primary-fixed-variant: '#910134'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffddb8'
  tertiary-fixed-dim: '#ffb95f'
  on-tertiary-fixed: '#2a1700'
  on-tertiary-fixed-variant: '#653e00'
  background: '#fff8f5'
  on-background: '#221a15'
  surface-variant: '#efdfd7'
typography:
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 3rem
    fontWeight: '800'
    lineHeight: 3.5rem
    letterSpacing: -0.03em
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 2.25rem
    fontWeight: '700'
    lineHeight: 2.75rem
    letterSpacing: -0.025em
  headline-xl-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.75rem
    fontWeight: '700'
    lineHeight: 2.25rem
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.5rem
    fontWeight: '700'
    lineHeight: 2rem
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.25rem
    fontWeight: '600'
    lineHeight: 1.75rem
    letterSpacing: -0.015em
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: 1.75rem
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: 1.5rem
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.875rem
    fontWeight: '500'
    lineHeight: 1.25rem
  label-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.875rem
    fontWeight: '700'
    lineHeight: 1.25rem
    letterSpacing: 0.02em
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.75rem
    fontWeight: '700'
    lineHeight: 1rem
    letterSpacing: 0.04em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.6875rem
    fontWeight: '600'
    lineHeight: 0.875rem
    letterSpacing: 0.05em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 2rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

The design system is engineered for ambitious students tackling demanding healthcare certifications. It balances the calm structure of an evidence-based clinical curriculum with the warmth, encouraging momentum, and visual delight of premium wellness and learning platforms.

### Personality & Tone
- **Empathetic & Steady:** Medical and anatomical study is high-stress. The UI counters cognitive overload with gentle warm hues, generous negative space, and uncluttered layouts.
- **Vibrant & Motivating:** Milestones, streak celebrations, and correct answers provide crisp, energetic feedback without juvenile gimmicks or distraction.
- **Clinically Precise:** Typography hierarchy, dense anatomical diagrams, and flashcard recall tools retain razor-sharp clarity and professional gravitas.

### Design Aesthetic
The aesthetic pairs warm minimalism with tactile, pill-soft geometry and diffused ambient illumination. It rejects sterile hospital grays and stark clinical whites in favor of linen creams, comforting rose undertones, and confident raspberry accents that guide the eye directly to high-priority study actions.

## Colors

The palette establishes an organic, supportive environment that mitigates eye fatigue over prolonged study sessions.

### Application Roles
- **Canvas Base:** Soft warm cream (`#FAF8F5`) for the overarching backdrop; surface containers step upward to `#FFFFFF` for focus panels and study cards, with secondary grouped wells in warm porcelain (`#F6F3EE`).
- **Primary (`#E1496B`):** Confident raspberry coral. Reserved for focal interaction points: primary CTA buttons ("Start Exam", "Flip Card"), active tab indicators, and critical navigational highlights.
- **Secondary (`#10B981`):** Fresh botanical mint. Dedicated to positive reinforcement: mastered anatomical decks, streak validation, accuracy score rings, and successful answers.
- **Tertiary (`#F59E0B`):** Warm burnished gold. Deployed specifically for daily streaks, XP counters, and high-value exam milestones.
- **Neutral (`#4A403A`):** Deep warm espresso charcoal rather than pure black. Preserves soft contrast while exceeding WCAG AAA legibility across body text and clinical definitions.
- **Muted Accents & Dividers:** Subtle rose mist (`#FCECEF`) for subtle chip backgrounds and warm oat (`#EAE3DB`) for low-contrast structural borders.

## Typography

Plus Jakarta Sans is utilized across all typography roles to ensure consistent geometric warmth, modern clarity, and excellent legibility across Latin-dense medical terminology (e.g., *Musculus sternocleidomastoideus*).

### Rules & Hierarchy
- **Letter Spacing:** Headlines utilize slightly negative tracking (`-0.02em` to `-0.03em`) for a confident, unified appearance, while small uppercase badges and tags apply positive tracking (`+0.02em` to `+0.05em`) for immediate scannability.
- **Numerals & Metrics:** Large metrics (streak days, retention percentages) always utilize bold weights (`700` or `800`) paired with `label-md` descriptive subtitles placed directly beneath.
- **Long-Form Learning:** Flashcard backs and diagnostic study cases should be constrained to a max-width of `65ch` using `body-md` or `body-lg` to prevent reader fatigue.

## Layout & Spacing

The layout is built for fluid responsiveness with specialized optimization for tablet landscape orientation—the primary workstation setup for healthcare students utilizing dual pen-and-touch interfaces.

### Tablet Landscape & Desktop Grid
- **Main Shell:** Employs an asymmetrical 12-column layout. 
  - Columns 1–3: Persistent navigation rail and quick-stats sidebar (retention pace, active streak counter).
  - Columns 4–9: Primary active study stream (interactive cards, practice test interface, lecture summary).
  - Columns 10–12: Contextual examination breakdown (upcoming deadlines, muscular/skeletal focus areas, daily review queue).
- **Gutters & Margin:** `2rem` outer canvas padding; `1.5rem` internal grid gutters.

### Mobile Reflow
- Shifts into a unified single-column flow with a persistent bottom pill navigation bar.
- Secondary stats collapse into horizontal swipe carousels.
- Outer canvas margins adapt to `1rem`.

## Elevation & Depth

Visual hierarchy uses a hybrid of tonal layering and warm ambient diffusion, steering clear of stark, dark drop-shadows.

### Elevation Tiers
- **Tier 0 (Background Canvas):** Base color `#FAF8F5`. No shadow.
- **Tier 1 (Resting Cards & Containers):** Pure surface white (`#FFFFFF`) with a `1px` structural outline in `#EAE3DB` paired with a gentle ambient drop: `0px 4px 20px -2px rgba(74, 64, 58, 0.04)`.
- **Tier 2 (Interactive Hover & Active Study Blocks):** Slight upward physical lift: `0px 8px 28px -4px rgba(225, 73, 107, 0.08)`. The tinted coral shadow provides responsive warmth.
- **Tier 3 (Floating Action Bars, Dialogs, Modals):** Crisp floating elements resting above a warm blur backdrop (`backdrop-filter: blur(12px) rgba(250, 248, 245, 0.8)`), supported by `0px 16px 40px -8px rgba(74, 64, 58, 0.12)`.

## Shapes

The interface embraces a friendly, pill-forward design system (Level 3 roundedness) that feels welcoming and approachable, removing clinical rigidity without sacrificing spatial efficiency.

### Shape Geometry Rules
- **Interactive Controls:** All standalone buttons, search pills, chip selectors, and badge tags maintain fully rounded stadium/pill profiles (`rounded-full` or `9999px`).
- **Cards & Functional Modules:** Main modular cards feature large, smooth corner radii (`rounded-2xl` to `rounded-3xl` / `1.5rem` to `2rem`), softening the screen perimeter.
- **Progress Trackers & Rings:** Linear progress bars feature pill ends. Ring meters implement rounded stroke ends to convey an organic, encouraging progression rate.

## Components

### Buttons
- **Primary Action:** Solid raspberry fill (`#E1496B`) with white text, pill-shaped (`9999px` border-radius), minimum touch target of `48px`. On hover, subtle `scale(1.02)` with coral ambient glow.
- **Secondary / Ghost:** Soft rose tint (`#FCECEF`) with `#E1496B` text. Borders remain invisible or `1px` solid `#F7D6DE`.
- **Tertiary Utility:** Warm transparent background with `#4A403A` text, accenting to `#E1496B` upon press.

### Cards & Flashcard Containers
- Built on `#FFFFFF` with `rounded-3xl` curvature and a persistent hairline boundary of `#EAE3DB`.
- **Active Anatomy Question Card:** Inset padding of `space-xl` (`2.5rem`) on tablet/desktop, with questions anchored at `headline-lg` and sub-metadata styled in `label-md`.

### Badges, Streaks & Stat Chips
- **Streak Tracker:** Pill-shaped badge featuring a tertiary gold background (`#FEF3C7`), tertiary gold text (`#B45309`), and an integrated flame or checkmark icon.
- **Medical Category Tags:** Soft-toned pills (e.g., `#EEF2FF` for *Neurology*, `#ECFDF5` for *Orthopedics*) with high-contrast text in `label-sm`.

### Progress Rings & Visual Trackers
- Circular progress indicators use a `12px` stroke with soft rounded caps.
- Background track set to `#F6F3EE`; filled track utilizes secondary mint (`#10B981`) or raspberry (`#E1496B`) depending on current mastery level.

### Form Inputs & Multiple Choice Selectors
- Text fields utilize `#FFFFFF` or `#F6F3EE` fills with an outline of `#EAE3DB`. Focus state shifts outline to `2px solid #E1496B` accompanied by a soft glow ring.
- **Multiple Choice Options:** Full-width pill-shaped rows. Unselected state rests on clean white with warm gray borders. Selected state shifts to `#FCECEF` background with `#E1496B` border and checkmark; verified correct answers resolve to `#ECFDF5` with `#10B981` border.