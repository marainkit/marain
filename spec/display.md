# Display System

> **Status:** `[project decision]`. The rendering grammar for marainkit surfaces, implemented as the **Culture** theme in [`../themes/culture/`](../themes/culture/). The light document context is built. Dark mode, HUD and status escalation are in progress.

Not a theme so much as a **rendering grammar**: a declared context goes in, and tokens, layout rules and emphasis come out.

```
(type, viewing, status)  →  token set  →  render
```

---

## Context model

| Axis | Values |
|------|--------|
| **Type** | `document` · `hud` · `code` · `alert-surface` |
| **Viewing** | `daylight` · `indoor` · `low-light` · `glare-motion` |
| **Status** | `normal` · `attention` · `warn` · `critical` |

Examples:

- `document / daylight / normal`: reading a note at a desk. **The baseline, built.**
- `document / low-light / normal`: dark mode. Tokens proposed.
- `hud / low-light / critical`: a monitoring display in a dark room when something's wrong.

Context is declared with a `data-mode` attribute on `<html>`. CSS only, no JavaScript style injection.

**What may change across contexts:** contrast, colour intensity, density (spacing and size), emphasis and motion.
**What may not:** typeface family and structural hierarchy. Differences come from weight, size and spacing, never from swapping fonts.

### Adaptation rules

- **Daylight → low-light:** lower brightness, slightly raise contrast, never pure white.
- **Document → HUD:** compress spacing, raise density, sharpen edges, drop decorative spacing.

---

## Status scale

Nine levels, 0–8, in four bands. It's a display convention and has nothing to do with glyph values.

| Levels | Band | Behaviour | Token |
|--------|------|-----------|-------|
| 0–2 | Normal | neutral | `--text-*` / `--surface-*` |
| 3–5 | Attention | subtle hue shift | `--accent` (proposed) |
| 6–7 | Warning | clear signal | `--warn` |
| 8 | Critical | high contrast | `--critical` |

**Escalation is contrast plus structure, not colour alone.** Colour signals the state; contrast and density carry the weight. Bands are deliberately coarse, because each named band is a category a reader learns (see [`../research/sapir-whorf.md`](../research/sapir-whorf.md) §4.1). How invariant glyphs map onto the scale is open ([grid.md](grid.md#still-open)).

---

## Typography (locked)

| Role | Font | Why |
|------|------|-----|
| UI / content | **Atkinson Hyperlegible Next** | Letterform distinction over harmony; tested with low-vision readers |
| Code / tokens | **Intel One Mono** | Exaggerated character identity; tested with low-vision developers |

Both are open-licensed. The research behind the choice is in [`../research/reference-fonts.md`](../research/reference-fonts.md).

- Body line-height 1.68 · code 1.6 · headings 1.15 · measure 74ch max
- Legibility over personality: `Il1`, `O0` and `rn/m` must be unambiguous.
- Code, tokens and identifiers are the "truth layer". They must survive copying and transformation unambiguously, which is why they're always set in mono.

---

## Colour tokens

Warm neutrals, paper-like, never pure white or black. The light values are final; the dark values are candidates to test against HUD targets.

| Token | Light (`document / daylight`) | Dark (`document / low-light`, proposed) |
|-------|-------------------------------|------------------------------------------|
| `--surface-0` | `hsl(42 24% 95%)` page | `hsl(30 6% 11%)` |
| `--surface-1` | `hsl(42 18% 92%)` card | `hsl(30 6% 14%)` |
| `--surface-2` | `hsl(42 14% 88%)` raised | `hsl(30 5% 18%)` |
| `--surface-inset` | `hsl(42 16% 90%)` code | `hsl(30 8% 9%)` |
| `--text-0` | `hsl(30 12% 18%)` primary | `hsl(40 12% 76%)` |
| `--text-1` | `hsl(30 9% 33%)` secondary | `hsl(40 10% 60%)` |
| `--text-2` | `hsl(30 7% 48%)` muted | `hsl(40 8% 44%)` |
| `--line-0` | `hsl(38 12% 82%)` | `hsl(36 8% 20%)` |
| `--line-1` | `hsl(38 12% 72%)` | `hsl(36 8% 26%)` |
| `--line-strong` | `hsl(38 10% 58%)` | `hsl(36 8% 36%)` |
| `--focus` | `hsl(210 52% 42%)` | `hsl(210 58% 65%)` |
| `--accent` | `hsl(210 42% 40%)` | `hsl(210 50% 62%)` |
| `--warn` | `hsl(39 58% 48%)` amber | `hsl(39 62% 60%)` |
| `--critical` | `hsl(5 63% 36%)` red | `hsl(5 60% 58%)` |
| `--yes` | `hsl(126 32% 31%)` green | `hsl(126 35% 48%)` |

Syntax highlighting still uses hard-coded HSL (strings ≈ `--yes`, numbers amber, keywords `--accent`, comments `--text-2` italic). Tokenising it is on the roadmap.

---

## Rules for all display work

- Token-driven only: no hard-coded colour, spacing or type values in components.
- Context via CSS only.
- States scale, don't shout.
- Structure over decoration. The interface should disappear in use.
- **Test method:** a 60-second sustained reading test, switching fonts mid-read, judging fatigue rather than first impression.

---

## What's built

- [`style.css`](../themes/culture/style.css): the full token system plus components (buttons, badges, notices, forms, tables, breadcrumbs, code blocks, sidebar)
- [`index.html`](../themes/culture/index.html): reference page for `document / daylight / normal`, including a status-scale preview (colours not final)
- [`styleguide.html`](../themes/culture/styleguide.html): the brand and style guide, with mark, wordmark and favicon assets in `brand/` and `assets/`
- Ports: [Zed](../themes/culture/marain-zed.json) editor theme, [Ableton Live](../themes/culture/the-culture.ask) theme

## Roadmap

1. ~~Lock `document / daylight / normal`~~ ✅
2. ~~Context-switching mechanism (`data-mode`)~~ ✅
3. Finalise dark-mode tokens
4. Build `hud / low-light / normal`
5. Map the status scale onto tokens, including the `attention` band (3–5)
6. Tokenise syntax colours
7. Integrate Marain glyphs via the renderer in [rendering.md](rendering.md)

Later axes, not yet designed: reader locale/language, situation (ambient conditions, urgency), device.
