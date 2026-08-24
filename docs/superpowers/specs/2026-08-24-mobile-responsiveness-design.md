# Design Spec: Mobile Responsiveness & Phone Layout Optimization

## Goal
Optimize `index.html` (English) and `pt/index.html` (Portuguese) so they display cleanly on mobile devices (smartphones/phones), ensuring responsive controls, table scrollability, Perso-Arabic text wrapping, and touch-friendly targets.

---

## 1. Responsive Layout & Breakpoints

- **Breakpoint**: `@media (max-width: 680px)` for mobile devices.

### Body & Container
- Body padding: `1rem 0.75rem`.
- `h1`: Scales down to `1.6rem`.
- `h2`: Scales down to `1.3rem`.

### Sticky Control Bar
- `.controls`: Stack elements vertically on small screens (`flex-direction: column; align-items: stretch; gap: 0.8rem;`).
- `.btn-big-toggle`: `width: 100%; justify-content: center; text-align: center; padding: 0.75rem 1rem; min-height: 44px;`.
- Language switcher: Centered with touch targets (`min-height: 44px`).

### Table Responsiveness
- Enclose tables in responsive scroll wrappers (`.table-wrapper { overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 1rem 0; }`).
- Or set `table { display: block; overflow-x: auto; -webkit-overflow-scrolling: touch; }` for direct mobile fallback.

### Perso-Arabic Script Display on Mobile
- `.perso-arabic`, `.ar`:
  - `font-size: 1.5rem;` (down from `2.2rem` in cards).
  - `line-height: 2.2;`.
  - `overflow-wrap: break-word; word-break: break-word;`.
  - `padding: 0.8rem 1rem;`.

### Cards & Spacing
- `.card`: `padding: 1rem;`.
- `.english`, `.portuguese`: `font-size: 1rem;`.
- `.ipa`: `font-size: 0.85rem;`.

---

## 2. Verification & Testing

- Validate layout on narrow screens (360px, 390px, 414px, 768px).
- Verify zero horizontal page scrolling.
- Verify `python3 build.py` succeeds.
