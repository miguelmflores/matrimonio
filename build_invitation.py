import base64
import os

print("Reading and encoding PNG and MP3 media files...")

b64_digi01 = base64.b64encode(open('Digi01.png', 'rb').read()).decode('ascii')
b64_digi02 = base64.b64encode(open('Digi02.png', 'rb').read()).decode('ascii')
b64_digi03 = base64.b64encode(open('Digi03.png', 'rb').read()).decode('ascii')
b64_digi04 = base64.b64encode(open('Digi04.png', 'rb').read()).decode('ascii')

audio_path = 'Turning_Page_112k.mp3' if os.path.exists('Turning_Page_112k.mp3') else 'Turning Page - Sleeping At Last Violin.mp3'
b64_audio = base64.b64encode(open(audio_path, 'rb').read()).decode('ascii')

print(f"Loaded Digi01: {len(b64_digi01)} chars, Digi02: {len(b64_digi02)} chars, Digi03: {len(b64_digi03)} chars, Digi04: {len(b64_digi04)} chars")
print(f"Loaded Audio: {len(b64_audio)} chars from {audio_path}")

html_content = f"""<!DOCTYPE html>
<html lang="es" class="locked-scroll">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>Miguel y Macarena — 30 de enero de 2027</title>
  <meta name="description" content="Nos complace invitarles a la unión de nuestras vidas en matrimonio. Sábado 30 de enero de 2027, Talca.">
  <!-- Metadatos Open Graph para WhatsApp y redes sociales -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://miguelmflores.github.io/matrimonio/">
  <meta property="og:title" content="Miguel &amp; Macarena — Matrimonio 💍">
  <meta property="og:description" content="Nos complace invitarles a celebrar la unión de nuestras vidas en matrimonio. Sábado 30 de enero de 2027, Talca.">
  <meta property="og:image" content="https://miguelmflores.github.io/matrimonio/Digi01.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">

  <!-- Tipografía: Fuentes clásicas serif y sans-serif con soporte offline total -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,500&family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">

  <style>
    /* ==========================================================================
       VARIABLES Y SISTEMA DE DISEÑO ELEGANTE Y CÁLIDO
       ========================================================================== */
    :root {{
      --bg-page: #FAF8F5;
      --bg-cream-soft: #F4F1EA;
      --bg-cream-card: #FCFAF7;
      --bg-card-white: #ffffff;
      
      --olive-primary: #8B9A6B;
      --olive-dark: #4F5A3C;
      --olive-deep: #2F3724;
      --olive-light: #A3B18A;
      --olive-subtle: #EDF2E8;
      --olive-pastel: #D8E0CF;
      
      --gold-accent: #BFA06B;
      --gold-light: #F6F1E7;
      
      --text-dark: #2B2F26;
      --text-body: #4E5346;
      --text-muted: #747A6B;
      
      --font-serif: 'Cormorant Garamond', 'Playfair Display', Georgia, 'Times New Roman', serif;
      --font-sans: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      
      --shadow-card: 0 14px 34px rgba(0, 0, 0, 0.08), 0 3px 10px rgba(0, 0, 0, 0.04);
      --shadow-hover: 0 18px 44px rgba(0, 0, 0, 0.12), 0 4px 14px rgba(0, 0, 0, 0.06);
      --shadow-button: 0 8px 24px rgba(139, 154, 107, 0.35);
      
      --radius-sm: 8px;
      --radius-md: 16px;
      --radius-lg: 24px;
      --radius-full: 9999px;
      
      --transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    /* RESET & BASE */
    *, *::before, *::after {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      -webkit-tap-highlight-color: transparent;
    }}

    html {{
      scroll-behavior: smooth;
      font-size: 16px;
      background-color: var(--bg-page);
      color: var(--text-dark);
      overflow-x: hidden;
    }}

    /* BLOQUEO DE SCROLL INICIAL HASTA QUE SE ABRA EL SOBRE */
    html.locked-scroll,
    body.locked-scroll {{
      overflow: hidden !important;
      height: 100vh !important;
      height: 100dvh !important;
      touch-action: pan-x;
    }}

    body {{
      font-family: var(--font-sans);
      line-height: 1.6;
      background-color: var(--bg-page);
      overflow-x: hidden;
      width: 100%;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      margin: 0;
      padding: 0;
    }}

    /* CONTENEDOR PRINCIPAL MOBILE-FIRST */
    .app-container {{
      width: 100%;
      max-width: 520px;
      margin: 0 auto;
      position: relative;
      background-color: var(--bg-page);
      box-shadow: 0 0 60px rgba(0, 0, 0, 0.04);
    }}

    /* ==========================================================================
       ESTRUCTURA DE ESCENAS
       ========================================================================== */
    .scene {{
      position: relative;
      width: 100%;
      min-height: 100vh;
      min-height: 100dvh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      padding: 2.2rem 1.2rem 1.8rem 1.2rem;
      scroll-margin-top: 0px;
      box-sizing: border-box;
    }}

    /* ==========================================================================
       ESCENA 1: PANTALLA DE APERTURA (HERO)
       ========================================================================== */
    .hero-scene {{
      background: radial-gradient(circle at 50% 30%, #FFFFFF 0%, var(--bg-page) 80%);
      text-align: center;
    }}

    .hero-header {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.25rem;
      margin-bottom: 0.6rem;
      z-index: 2;
      animation: fadeInDown 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}

    .hero-title {{
      font-family: var(--font-serif);
      font-size: 2.65rem;
      font-weight: 500;
      letter-spacing: 0.02em;
      color: var(--olive-deep);
      line-height: 1.15;
    }}

    .hero-date {{
      font-family: var(--font-serif);
      font-size: 1.15rem;
      letter-spacing: 0.22em;
      color: var(--olive-dark);
      text-transform: uppercase;
      font-weight: 500;
    }}

    /* ESCENARIO DEL SOBRE CON HALO LATENTE (+30% TAMAÑO, RESPONSIVO EN ALTURA) */
    .envelope-stage {{
      position: relative;
      width: 100%;
      max-width: min(455px, calc((100dvh - 185px) * 0.6956));
      aspect-ratio: 1113 / 1600;
      margin: 0.2rem auto;
      cursor: pointer;
      transition: transform 0.35s ease, filter 0.35s ease;
      filter: drop-shadow(0 16px 36px rgba(0, 0, 0, 0.12));
    }}

    /* HALO LATENTE PULSANTE ALREDEDOR DEL SOBRE HASTA EL PRIMER CLIC */
    .envelope-stage.pulsing-halo {{
      animation: envelopeHaloGlow 2.6s ease-in-out infinite;
    }}

    @keyframes envelopeHaloGlow {{
      0%, 100% {{
        filter: drop-shadow(0 16px 36px rgba(0, 0, 0, 0.12))
                drop-shadow(0 0 10px rgba(139, 154, 107, 0.35));
        transform: scale(1);
      }}
      50% {{
        filter: drop-shadow(0 20px 48px rgba(139, 154, 107, 0.55))
                drop-shadow(0 0 22px rgba(139, 154, 107, 0.7))
                drop-shadow(0 0 38px rgba(191, 160, 107, 0.3));
        transform: scale(1.018);
      }}
    }}

    .envelope-stage:active {{
      transform: scale(0.99);
    }}

    /* Capa 1: Digi03.png (Sobre abierto con orquídea - Centrado simétrico exacto) */
    .envelope-img-base {{
      position: absolute;
      top: 0;
      left: -1.62%;
      width: 100%;
      height: 100%;
      object-fit: contain;
      display: block;
      z-index: 1;
      pointer-events: none;
    }}

    /* Capa 2: Digi04.png (Sobre con invitaciones reveladas - Pura transición sin traslación) */
    .envelope-img-revealed {{
      position: absolute;
      top: 0;
      left: -1.62%;
      width: 100%;
      height: 100%;
      object-fit: contain;
      display: block;
      z-index: 2;
      opacity: 0;
      transition: opacity 1.35s cubic-bezier(0.16, 1, 0.3, 1);
      pointer-events: none;
    }}

    .envelope-img-revealed.revealed {{
      opacity: 1;
    }}

    /* CONTENEDOR 100% CENTRADO HORIZONTAL PARA EL MENSAJE SUGERENTE */
    .start-prompt-wrap {{
      position: absolute;
      bottom: 22px;
      left: 0;
      right: 0;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      pointer-events: none;
      z-index: 10;
    }}

    /* MENSAJE SUGERENTE LATENTE PARA INICIAR */
    .start-prompt {{
      pointer-events: auto;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      color: var(--olive-deep);
      padding: 0.65rem 1.45rem;
      border-radius: var(--radius-full);
      font-family: var(--font-serif);
      font-size: 1.08rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      box-shadow: 0 8px 26px rgba(79, 90, 60, 0.28);
      border: 1.5px solid var(--olive-light);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.55rem;
      animation: promptFloat 2.4s ease-in-out infinite;
      cursor: pointer;
      white-space: nowrap;
      transition: opacity 0.5s ease, transform 0.5s ease, visibility 0.5s ease;
      user-select: none;
      -webkit-user-select: none;
      margin: 0 auto;
    }}

    .start-prompt-icon {{
      font-size: 1.15rem;
      line-height: 1;
      display: inline-flex;
      align-items: center;
      justify-content: center;
    }}

    .start-prompt-text {{
      line-height: 1.2;
      display: inline-block;
    }}

    .start-prompt-wrap.hidden,
    .start-prompt.hidden {{
      opacity: 0;
      visibility: hidden;
      transform: scale(0.9);
      pointer-events: none;
    }}

    @keyframes promptFloat {{
      0%, 100% {{
        transform: translateY(0);
      }}
      50% {{
        transform: translateY(-5px);
      }}
    }}

    /* BOTÓN REUTILIZABLE: 'DESLIZA HACIA ABAJO' EN CADA ESCENA */
    .scroll-indicator-btn {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.35rem;
      margin-top: 1rem;
      cursor: pointer;
      color: var(--olive-dark);
      z-index: 10;
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      padding: 0.65rem 1.4rem;
      border-radius: var(--radius-full);
      border: 1px solid rgba(139, 154, 107, 0.25);
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.05);
      transition: var(--transition);
      user-select: none;
      -webkit-user-select: none;
    }}

    .scroll-indicator-btn:hover {{
      background: #ffffff;
      color: var(--olive-deep);
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
      border-color: var(--olive-primary);
    }}

    .scroll-indicator-btn:active {{
      transform: scale(0.97);
    }}

    /* EL BOTÓN DE HERO APARECE SÓLO DESPUÉS DEL PRIMER CLIC */
    .scroll-indicator-btn.hero-scroll-btn {{
      opacity: 0;
      visibility: hidden;
      transform: translateY(12px);
      transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1),
                  transform 0.8s cubic-bezier(0.16, 1, 0.3, 1),
                  visibility 0.8s ease;
      pointer-events: none;
    }}

    .scroll-indicator-btn.hero-scroll-btn.visible {{
      opacity: 1;
      visibility: visible;
      transform: translateY(0);
      pointer-events: auto;
    }}

    .scroll-text {{
      font-family: var(--font-serif);
      font-size: 0.95rem;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      font-weight: 600;
      color: var(--olive-deep);
    }}

    .scroll-chevron {{
      animation: bounceGentle 2.2s infinite ease-in-out;
      color: var(--olive-primary);
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    /* ==========================================================================
       ESCENA 2: TARJETA DIGI01 (INVITACIÓN PRINCIPAL EN ARCO)
       ========================================================================== */
    .digi01-scene {{
      background: var(--bg-page);
      justify-content: center;
      gap: 1.5rem;
      padding-top: 2rem;
      padding-bottom: 2rem;
    }}

    /* FRASE DE BIENVENIDA */
    .welcome-quote-card {{
      background: rgba(255, 255, 255, 0.88);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border-radius: var(--radius-md);
      padding: 1.6rem 1.6rem;
      text-align: center;
      border: 1px solid rgba(139, 154, 107, 0.2);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.04);
      width: 100%;
      max-width: 472px;
      position: relative;
    }}

    .welcome-quote-card::before {{
      content: "“";
      font-family: var(--font-serif);
      font-size: 3.5rem;
      color: var(--olive-light);
      position: absolute;
      top: -12px;
      left: 50%;
      transform: translateX(-50%);
      line-height: 1;
      opacity: 0.5;
    }}

    .welcome-quote-text {{
      font-family: var(--font-serif);
      font-size: 1.25rem;
      font-style: italic;
      color: var(--olive-deep);
      line-height: 1.55;
      margin-top: 0.4rem;
    }}

    /* CONTENEDOR DE TARJETAS (+15% TAMAÑO: max-width 472px) */
    .card-presentation-box {{
      position: relative;
      width: 100%;
      max-width: 472px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    .card-transparent-wrapper {{
      position: relative;
      width: 100%;
      display: block;
      cursor: pointer;
      filter: drop-shadow(0 16px 36px rgba(0, 0, 0, 0.11));
      transition: transform 0.35s ease, filter 0.35s ease;
    }}

    .card-transparent-wrapper:hover {{
      transform: translateY(-4px);
      filter: drop-shadow(0 22px 42px rgba(0, 0, 0, 0.15));
    }}

    .card-png-image {{
      width: 100%;
      height: auto;
      display: block;
      vertical-align: middle;
    }}

    /* BOTÓN DISCRETO DE LUPA EN LA ESQUINA SUPERIOR IZQUIERDA */
    .card-zoom-badge {{
      position: absolute;
      top: 16px;
      left: 16px;
      width: 38px;
      height: 38px;
      background: rgba(255, 255, 255, 0.92);
      border: 1px solid rgba(139, 154, 107, 0.3);
      color: var(--olive-dark);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      z-index: 10;
      transition: var(--transition);
      backdrop-filter: blur(4px);
    }}

    .card-zoom-badge:hover {{
      background: var(--olive-primary);
      color: #ffffff;
      transform: scale(1.1);
      box-shadow: 0 6px 16px rgba(139, 154, 107, 0.35);
    }}

    /* ==========================================================================
       ESCENA 3: TARJETA DIGI02 (DETALLES Y ACOMPAÑAMIENTO ELEGANTE)
       ========================================================================== */
    .digi02-scene {{
      background: var(--bg-page);
      justify-content: center;
      gap: 1.4rem;
      padding-top: 2rem;
      padding-bottom: 2rem;
    }}

    /* ENCABEZADO DECORATIVO PARA QUE DIGI02 NO QUEDE ABANDONADA */
    .digi02-header {{
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.3rem;
      width: 100%;
      max-width: 472px;
    }}

    .digi02-tag {{
      font-family: var(--font-serif);
      font-size: 0.9rem;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--olive-primary);
      font-weight: 600;
    }}

    .digi02-title {{
      font-family: var(--font-serif);
      font-size: 2.1rem;
      color: var(--olive-deep);
      font-weight: 500;
    }}

    .digi02-ornament {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
      color: var(--olive-light);
      font-size: 0.85rem;
    }}

    .digi02-ornament::before,
    .digi02-ornament::after {{
      content: "";
      display: inline-block;
      width: 32px;
      height: 1px;
      background: var(--olive-pastel);
    }}

    /* FRANJA DE DETALLES CLAVE QUE ACOMPAÑA A DIGI02 */
    .digi02-key-pills {{
      display: flex;
      align-items: center;
      justify-content: center;
      flex-wrap: wrap;
      gap: 0.6rem;
      width: 100%;
      max-width: 472px;
      margin-top: 0.2rem;
    }}

    .key-pill {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: rgba(255, 255, 255, 0.85);
      border: 1px solid var(--olive-subtle);
      color: var(--olive-dark);
      padding: 0.4rem 0.85rem;
      border-radius: var(--radius-full);
      font-size: 0.82rem;
      font-weight: 500;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
    }}

    /* ZONA TÁCTIL INTERACTIVA PARA EL QR EN DIGI02.PNG (CUADRADO EXACTO) */
    .qr-hotspot {{
      position: absolute;
      /* Coordenadas ajustadas con precisión milimétrica para envolver únicamente el cuadrado del QR */
      top: 75.6%;
      left: 42.4%;
      width: 15.7%;
      height: 12.5%;
      border-radius: 6px;
      cursor: pointer;
      z-index: 10;
      border: 2px dashed rgba(139, 154, 107, 0.7);
      animation: pulseHighlight 2.4s infinite;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .qr-hotspot:hover {{
      border-color: var(--olive-dark);
      background-color: rgba(139, 154, 107, 0.2);
    }}

    /* TOOLTIP / BURBUJA ELEGANTE SITUADA DEBAJO DEL QR SIN TAPAR EL TEXTO */
    .qr-tooltip-bubble {{
      position: absolute;
      top: 89.2%;
      left: 50%;
      transform: translateX(-50%);
      background: #ffffff;
      color: var(--olive-deep);
      font-size: 0.75rem;
      font-weight: 600;
      line-height: 1.35;
      padding: 0.45rem 0.85rem;
      border-radius: var(--radius-md);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.16);
      border: 1.2px solid var(--olive-pastel);
      display: flex;
      align-items: center;
      gap: 0.45rem;
      z-index: 15;
      cursor: pointer;
      width: 86%;
      max-width: 320px;
      text-align: center;
      justify-content: center;
      animation: floatTooltip 3s ease-in-out infinite;
      transition: var(--transition);
    }}

    .qr-tooltip-bubble:hover {{
      background-color: var(--olive-subtle);
      transform: translateX(-50%) scale(1.02);
    }}

    .qr-tooltip-bubble::after {{
      content: "";
      position: absolute;
      bottom: 100%;
      left: 50%;
      transform: translateX(-50%);
      border-width: 6px;
      border-style: solid;
      border-color: transparent transparent #ffffff transparent;
    }}

    .qr-tooltip-icon {{
      flex-shrink: 0;
      width: 20px;
      height: 20px;
      background: var(--olive-subtle);
      color: var(--olive-dark);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    /* ==========================================================================
       ESCENA 4: INFORMACIÓN PRÁCTICA, ITINERARIO Y CUENTA REGRESIVA
       ========================================================================== */
    .details-section {{
      background-color: var(--bg-page);
      padding: 2.5rem 1.2rem 3.5rem 1.2rem;
      display: flex;
      flex-direction: column;
      gap: 2.8rem;
      align-items: center;
      width: 100%;
      scroll-margin-top: 10px;
    }}

    .section-title-wrap {{
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.35rem;
    }}

    .section-subtitle {{
      font-family: var(--font-serif);
      font-size: 0.95rem;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      color: var(--olive-dark);
      font-weight: 500;
    }}

    .section-main-title {{
      font-family: var(--font-serif);
      font-size: 2.25rem;
      color: var(--olive-deep);
      font-weight: 500;
    }}

    .section-divider-ornament {{
      width: 60px;
      height: 2px;
      background: var(--olive-light);
      margin-top: 0.3rem;
      position: relative;
    }}

    .section-divider-ornament::after {{
      content: "✦";
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background: var(--bg-page);
      padding: 0 6px;
      color: var(--olive-primary);
      font-size: 0.85rem;
    }}

    /* CUENTA REGRESIVA DESTACADA */
    .countdown-card {{
      background: #ffffff;
      border-radius: var(--radius-lg);
      padding: 2.2rem 1.4rem;
      width: 100%;
      max-width: 460px;
      text-align: center;
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.06);
      border: 1px solid rgba(139, 154, 107, 0.25);
      position: relative;
      overflow: hidden;
    }}

    .countdown-card::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: linear-gradient(90deg, var(--olive-pastel), var(--olive-primary), var(--olive-dark));
    }}

    .countdown-heading {{
      font-family: var(--font-serif);
      font-size: 1.55rem;
      color: var(--olive-deep);
      font-weight: 600;
      margin-bottom: 0.2rem;
    }}

    .countdown-subheading {{
      font-size: 0.88rem;
      color: var(--text-muted);
      margin-bottom: 1.8rem;
    }}

    .countdown-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 0.65rem;
    }}

    .countdown-item {{
      background: var(--bg-cream-soft);
      border: 1px solid var(--olive-subtle);
      border-radius: var(--radius-md);
      padding: 0.95rem 0.2rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
    }}

    .countdown-number {{
      font-family: var(--font-serif);
      font-size: 2.25rem;
      font-weight: 700;
      color: var(--olive-dark);
      line-height: 1;
    }}

    .countdown-label {{
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--text-muted);
      margin-top: 0.4rem;
      font-weight: 600;
    }}

    /* TARJETAS DE CEREMONIA Y RECEPCIÓN */
    .event-cards-container {{
      width: 100%;
      max-width: 460px;
      display: flex;
      flex-direction: column;
      gap: 1.8rem;
    }}

    .info-card {{
      background: #ffffff;
      border-radius: var(--radius-lg);
      padding: 2.2rem 1.6rem;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
      border: 1px solid rgba(139, 154, 107, 0.2);
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
    }}

    .info-card-icon {{
      width: 54px;
      height: 54px;
      background: var(--olive-subtle);
      color: var(--olive-dark);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 1.1rem;
    }}

    .info-card-tag {{
      font-family: var(--font-serif);
      font-size: 0.85rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--olive-primary);
      font-weight: 600;
      margin-bottom: 0.35rem;
    }}

    .info-card-title {{
      font-family: var(--font-serif);
      font-size: 1.65rem;
      color: var(--olive-deep);
      font-weight: 600;
      line-height: 1.25;
      margin-bottom: 0.5rem;
    }}

    .info-card-time {{
      font-family: var(--font-serif);
      font-size: 1.35rem;
      color: var(--olive-dark);
      font-weight: 600;
      background: var(--bg-cream-soft);
      padding: 0.35rem 1.1rem;
      border-radius: var(--radius-full);
      margin-bottom: 0.9rem;
      display: inline-block;
    }}

    .info-card-place {{
      font-weight: 600;
      font-size: 1.02rem;
      color: var(--text-dark);
      margin-bottom: 0.3rem;
    }}

    .info-card-address {{
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.45;
      margin-bottom: 1.5rem;
      max-width: 320px;
    }}

    /* BOTONES DE CÓMO LLEGAR */
    .btn-maps {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.55rem;
      background: transparent;
      color: var(--olive-dark);
      border: 1.5px solid var(--olive-primary);
      padding: 0.75rem 1.6rem;
      border-radius: var(--radius-full);
      font-size: 0.9rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      text-decoration: none;
      cursor: pointer;
      transition: var(--transition);
      width: 100%;
      max-width: 260px;
    }}

    .btn-maps:hover {{
      background: var(--olive-primary);
      color: #ffffff;
      box-shadow: 0 6px 18px rgba(139, 154, 107, 0.3);
      transform: translateY(-2px);
    }}

    /* TARJETA DE DRESSCODE & NOTAS */
    .notes-card {{
      background: #ffffff;
      border-radius: var(--radius-lg);
      padding: 2rem 1.6rem;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
      border: 1px solid rgba(139, 154, 107, 0.2);
      width: 100%;
      max-width: 460px;
      text-align: center;
      display: flex;
      flex-direction: column;
      gap: 1.6rem;
    }}

    .note-block {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.35rem;
    }}

    .note-block-divider {{
      width: 40px;
      height: 1px;
      background: var(--olive-pastel);
      margin: 0 auto;
    }}

    .note-title {{
      font-family: var(--font-serif);
      font-size: 1.35rem;
      color: var(--olive-deep);
      font-weight: 600;
    }}

    .note-value {{
      font-weight: 600;
      color: var(--olive-dark);
      font-size: 1.05rem;
    }}

    .note-detail {{
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.45;
    }}

    .note-detail.accent {{
      color: #9E5B5B;
      font-weight: 500;
    }}

    /* BOTÓN PRINCIPAL DE CONFIRMACIÓN (WHATSAPP) */
    .rsvp-container {{
      width: 100%;
      max-width: 460px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.9rem;
      margin-top: 0.5rem;
    }}

    .btn-rsvp {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.75rem;
      background: linear-gradient(135deg, var(--olive-primary) 0%, var(--olive-dark) 100%);
      color: #ffffff;
      border: none;
      padding: 1.15rem 2rem;
      border-radius: var(--radius-full);
      font-size: 1.08rem;
      font-family: var(--font-serif);
      letter-spacing: 0.05em;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      box-shadow: var(--shadow-button);
      transition: var(--transition);
      width: 100%;
      text-align: center;
    }}

    .btn-rsvp:hover {{
      transform: translateY(-3px) scale(1.01);
      box-shadow: 0 10px 28px rgba(79, 90, 60, 0.4);
      background: linear-gradient(135deg, #7D8C5F 0%, #3F4830 100%);
    }}

    .btn-rsvp:active {{
      transform: scale(0.98);
    }}

    .btn-rsvp.expired-btn {{
      background: linear-gradient(135deg, #A8B1A2 0%, #7E8777 100%);
      opacity: 0.72;
      cursor: not-allowed;
      box-shadow: none;
      transform: none;
    }}

    .rsvp-caption {{
      font-size: 0.82rem;
      color: var(--text-muted);
      text-align: center;
    }}

    /* TARJETA DE PLAZO DE CONFIRMACIÓN (CONTADOR & MENSAJE VENCIDO) */
    .rsvp-deadline-card {{
      width: 100%;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border: 1px solid var(--olive-pastel);
      border-radius: var(--radius-lg);
      padding: 1.25rem 1.35rem;
      box-shadow: 0 10px 28px rgba(79, 90, 60, 0.08);
      margin-top: 0.4rem;
      box-sizing: border-box;
      transition: all 0.4s ease;
    }}

    .rsvp-deadline-header {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.65rem;
      margin-bottom: 0.95rem;
      text-align: center;
    }}

    .rsvp-deadline-icon {{
      font-size: 1.35rem;
      line-height: 1;
    }}

    .rsvp-deadline-title {{
      font-family: var(--font-serif);
      font-size: 1.15rem;
      font-weight: 600;
      color: var(--olive-deep);
      margin: 0;
      letter-spacing: 0.02em;
    }}

    .rsvp-deadline-sub {{
      font-family: var(--font-sans);
      font-size: 0.8rem;
      color: var(--olive-dark);
      margin: 0.15rem 0 0 0;
      font-weight: 500;
    }}

    .rsvp-countdown-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 0.45rem;
    }}

    .rsvp-countdown-box {{
      background: var(--olive-subtle);
      border: 1px solid rgba(139, 154, 107, 0.32);
      border-radius: var(--radius-md);
      padding: 0.65rem 0.25rem;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }}

    .rsvp-countdown-num {{
      font-family: var(--font-serif);
      font-size: 1.45rem;
      font-weight: 700;
      color: var(--olive-deep);
      line-height: 1.1;
    }}

    .rsvp-countdown-lbl {{
      font-family: var(--font-sans);
      font-size: 0.65rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--olive-dark);
      font-weight: 600;
      margin-top: 0.2rem;
    }}

    /* ESTADO VENCIDO DE CONFIRMACIÓN */
    .rsvp-deadline-expired {{
      text-align: center;
      padding: 0.5rem 0.2rem;
    }}

    .rsvp-expired-icon {{
      font-size: 1.9rem;
      margin-bottom: 0.45rem;
      line-height: 1;
    }}

    .rsvp-expired-title {{
      font-family: var(--font-serif);
      font-size: 1.3rem;
      font-weight: 600;
      color: var(--olive-deep);
      margin: 0 0 0.55rem 0;
    }}

    .rsvp-expired-msg {{
      font-family: var(--font-sans);
      font-size: 0.9rem;
      line-height: 1.6;
      color: var(--text-body);
      margin: 0;
    }}

    /* FRASE DE CIERRE */
    .closing-section {{
      width: 100%;
      max-width: 460px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1.2rem;
      margin-top: 1rem;
    }}

    .closing-card {{
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(8px);
      border-radius: var(--radius-lg);
      padding: 2.2rem 1.8rem;
      border: 1px solid rgba(139, 154, 107, 0.25);
      width: 100%;
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.04);
      position: relative;
    }}

    .closing-phrase {{
      font-family: var(--font-serif);
      font-size: 1.35rem;
      font-style: italic;
      color: var(--olive-deep);
      line-height: 1.55;
    }}

    .closing-signature {{
      font-family: var(--font-serif);
      font-size: 1.45rem;
      font-weight: 500;
      color: var(--olive-dark);
      margin-top: 1rem;
      letter-spacing: 0.05em;
    }}

    /* ENLACE DISCRETO DE RECOMENDACIONES DE ALOJAMIENTO */
    .accommodation-link-wrap {{
      margin-top: 0.5rem;
      padding-bottom: 2rem;
    }}

    .link-accommodation {{
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      color: var(--olive-dark);
      font-size: 0.88rem;
      text-decoration: underline;
      text-underline-offset: 4px;
      cursor: pointer;
      font-weight: 500;
      opacity: 0.88;
      transition: var(--transition);
      background: none;
      border: none;
      font-family: inherit;
    }}

    .link-accommodation:hover {{
      opacity: 1;
      color: var(--olive-deep);
    }}

    /* ==========================================================================
       MODAL DE ALOJAMIENTO Y TIPS DE VIAJE A TALCA
       ========================================================================== */
    .modal-backdrop {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(20, 24, 17, 0.65);
      backdrop-filter: blur(6px);
      -webkit-backdrop-filter: blur(6px);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.2rem;
      z-index: 1000;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.3s ease, visibility 0.3s ease;
    }}

    .modal-backdrop.active {{
      opacity: 1;
      visibility: visible;
    }}

    .modal-box {{
      background: #ffffff;
      border-radius: var(--radius-lg);
      width: 100%;
      max-width: 480px;
      max-height: 88vh;
      overflow-y: auto;
      padding: 2rem 1.5rem;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.25);
      position: relative;
      transform: translateY(20px) scale(0.96);
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      border: 1px solid var(--olive-subtle);
    }}

    .modal-backdrop.active .modal-box {{
      transform: translateY(0) scale(1);
    }}

    .modal-close-btn {{
      position: absolute;
      top: 1.2rem;
      right: 1.2rem;
      background: var(--bg-cream-soft);
      border: none;
      color: var(--text-dark);
      width: 34px;
      height: 34px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1.1rem;
      transition: var(--transition);
    }}

    .modal-close-btn:hover {{
      background: var(--olive-pastel);
      color: var(--olive-deep);
    }}

    .modal-header {{
      text-align: center;
      margin-bottom: 1.8rem;
      padding-right: 1.5rem;
      padding-left: 1.5rem;
    }}

    .modal-title {{
      font-family: var(--font-serif);
      font-size: 1.7rem;
      color: var(--olive-deep);
      font-weight: 600;
    }}

    .modal-subtitle {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: 0.2rem;
    }}

    .hotels-list {{
      display: flex;
      flex-direction: column;
      gap: 1.1rem;
    }}

    .hotel-item {{
      background: var(--bg-page);
      border: 1px solid var(--olive-subtle);
      border-radius: var(--radius-md);
      padding: 1.1rem;
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
      transition: transform 0.2s ease;
    }}

    .hotel-item:hover {{
      border-color: var(--olive-light);
    }}

    .hotel-number {{
      font-family: var(--font-serif);
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--olive-primary);
      text-transform: uppercase;
      letter-spacing: 0.1em;
    }}

    .hotel-name {{
      font-family: var(--font-serif);
      font-size: 1.25rem;
      font-weight: 600;
      color: var(--olive-deep);
      line-height: 1.2;
    }}

    .hotel-location {{
      font-size: 0.85rem;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }}

    .btn-hotel-map {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: #ffffff;
      color: var(--olive-dark);
      border: 1px solid var(--olive-light);
      padding: 0.5rem 0.9rem;
      border-radius: var(--radius-full);
      font-size: 0.82rem;
      font-weight: 600;
      text-decoration: none;
      align-self: flex-start;
      margin-top: 0.2rem;
      transition: var(--transition);
    }}

    .btn-hotel-map:hover {{
      background: var(--olive-primary);
      color: #ffffff;
    }}

    /* SECCIÓN DE TIPS DE VIAJE A TALCA */
    .travel-tips-container {{
      margin-top: 1.8rem;
      padding-top: 1.6rem;
      border-top: 1px dashed var(--olive-pastel);
    }}

    .travel-tips-title {{
      font-family: var(--font-serif);
      font-size: 1.35rem;
      color: var(--olive-deep);
      font-weight: 600;
      margin-bottom: 0.9rem;
      display: flex;
      align-items: center;
      gap: 0.45rem;
    }}

    .travel-tips-grid {{
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }}

    .travel-tip-card {{
      background: var(--bg-cream-soft);
      border: 1px solid rgba(139, 154, 107, 0.25);
      border-radius: var(--radius-md);
      padding: 0.9rem 1rem;
      font-size: 0.84rem;
      line-height: 1.45;
    }}

    .travel-tip-header {{
      display: flex;
      align-items: center;
      gap: 0.4rem;
      font-weight: 600;
      color: var(--olive-dark);
      margin-bottom: 0.25rem;
      font-size: 0.88rem;
    }}

    .travel-tip-desc {{
      color: var(--text-body);
    }}

    .travel-recommendation-box {{
      margin-top: 1rem;
      background: #FFF9EE;
      border: 1px solid #EADBBA;
      border-radius: var(--radius-md);
      padding: 0.85rem 1rem;
      font-size: 0.82rem;
      color: #7A5C28;
      line-height: 1.45;
    }}

    /* ==========================================================================
       MODAL LIGHTBOX PANTALLA COMPLETA
       ========================================================================== */
    .lightbox-modal {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(15, 18, 14, 0.96);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      z-index: 2000;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.3s ease, visibility 0.3s ease;
      touch-action: pinch-zoom;
    }}

    .lightbox-modal.active {{
      opacity: 1;
      visibility: visible;
    }}

    .lightbox-toolbar {{
      position: absolute;
      top: 1rem;
      right: 1rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      z-index: 2010;
    }}

    .lightbox-btn {{
      background: rgba(255, 255, 255, 0.18);
      border: 1px solid rgba(255, 255, 255, 0.3);
      color: #ffffff;
      width: 42px;
      height: 42px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1.2rem;
      transition: var(--transition);
      backdrop-filter: blur(4px);
    }}

    .lightbox-btn:hover {{
      background: rgba(255, 255, 255, 0.35);
      transform: scale(1.08);
    }}

    .lightbox-content {{
      max-width: 92vw;
      max-height: 88vh;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: zoom-in;
    }}

    .lightbox-content.zoomed {{
      transform: scale(1.6);
      cursor: zoom-out;
    }}

    .lightbox-img {{
      max-width: 100%;
      max-height: 88vh;
      object-fit: contain;
      border-radius: var(--radius-sm);
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
      user-select: none;
      -webkit-user-select: none;
    }}

    .lightbox-hint {{
      position: absolute;
      bottom: 1.2rem;
      left: 50%;
      transform: translateX(-50%);
      color: rgba(255, 255, 255, 0.7);
      font-size: 0.8rem;
      background: rgba(0, 0, 0, 0.4);
      padding: 0.35rem 0.85rem;
      border-radius: var(--radius-full);
      pointer-events: none;
    }}

    /* ==========================================================================
       ANIMACIONES CSS
       ========================================================================== */
    @keyframes fadeInDown {{
      from {{
        opacity: 0;
        transform: translateY(-16px);
      }}
      to {{
        opacity: 1;
        transform: translateY(0);
      }}
    }}

    @keyframes fadeInUp {{
      from {{
        opacity: 0;
        transform: translateY(16px);
      }}
      to {{
        opacity: 1;
        transform: translateY(0);
      }}
    }}

    @keyframes bounceGentle {{
      0%, 20%, 50%, 80%, 100% {{
        transform: translateY(0);
      }}
      40% {{
        transform: translateY(5px);
      }}
      60% {{
        transform: translateY(2px);
      }}
    }}

    @keyframes pulseHighlight {{
      0%, 100% {{
        box-shadow: 0 0 0 0 rgba(139, 154, 107, 0.5);
      }}
      50% {{
        box-shadow: 0 0 0 8px rgba(139, 154, 107, 0);
      }}
    }}

    @keyframes floatTooltip {{
      0%, 100% {{
        transform: translate(-50%, 0);
      }}
      50% {{
        transform: translate(-50%, -4px);
      }}
    }}

    /* MEDIA QUERIES RESPONSIVAS */
    @media (max-width: 380px) {{
      .hero-title {{
        font-size: 2.2rem;
      }}
      .countdown-number {{
        font-size: 1.85rem;
      }}
      .info-card-title {{
        font-size: 1.45rem;
      }}
      .qr-tooltip-bubble {{
        font-size: 0.72rem;
        padding: 0.4rem 0.75rem;
      }}
    }}

    @media (min-width: 521px) {{
      body {{
        background: #ECE8E1;
      }}
      .app-container {{
        margin: 20px auto;
        border-radius: var(--radius-lg);
        overflow: hidden;
      }}
    }}
  </style>
</head>
<body class="locked-scroll">

  <!-- ELEMENTO DE AUDIO EMBEBIDO Y OCULTO (SIN CONTROLES VISIBLES) -->
  <audio id="bgMusic" loop preload="auto" playsinline>
    <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mp3">
  </audio>

  <div class="app-container">

    <!-- ======================================================================
         ESCENA 1: PANTALLA DE APERTURA (HERO & TRANSICIÓN DEL SOBRE)
         ====================================================================== -->
    <section class="scene hero-scene" id="scene-hero">
      
      <!-- Nombres y Fecha elegantes en la parte superior -->
      <div class="hero-header">
        <h1 class="hero-title">Miguel y Macarena</h1>
        <p class="hero-date">30 de enero de 2027</p>
      </div>

      <!-- Sobre interactivo con halo latente (+30% TAMAÑO) -->
      <div class="envelope-stage pulsing-halo" id="envelopeStage" onclick="startExperience(event)" title="Haz clic para iniciar">
        <!-- Imagen Base: Digi03.png (Sobre abierto con orquídea blanca vacía) -->
        <img class="envelope-img-base" src="data:image/png;base64,{b64_digi03}" alt="Sobre de matrimonio con orquídea">
        <!-- Imagen Revelada: Digi04.png (Sobre con las 2 invitaciones delante) -->
        <img class="envelope-img-revealed" id="envelopeRevealed" src="data:image/png;base64,{b64_digi04}" alt="Invitación Miguel y Macarena">
        
        <!-- Mensaje sugerente latente perfectamente centrado en su contenedor -->
        <div class="start-prompt-wrap" id="startPromptWrap">
          <div class="start-prompt" id="startPrompt" onclick="startExperience(event)">
            <span class="start-prompt-icon">💌</span>
            <span class="start-prompt-text">Haz clic para iniciar</span>
          </div>
        </div>
      </div>

      <!-- Botón de desplazamiento guiado hacia Digi01 (Aparece tras el clic inicial) -->
      <div class="scroll-indicator-btn hero-scroll-btn" id="heroScrollBtn" onclick="goToScene('scene-digi01')">
        <span class="scroll-text">Desliza hacia abajo</span>
        <div class="scroll-chevron">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="6 9 12 15 18 9"></polyline>
          </svg>
        </div>
      </div>

    </section>

    <!-- ======================================================================
         ESCENA 2: INVITACIÓN PRINCIPAL (DIGI01 EN ARCO)
         ====================================================================== -->
    <section class="scene digi01-scene" id="scene-digi01">

      <!-- Frase de bienvenida tomada de Digi01 -->
      <div class="welcome-quote-card">
        <p class="welcome-quote-text">
          “Hay momentos que se vuelven inolvidables cuando se comparten. Por eso, este día queremos vivirlo con ustedes.”
        </p>
      </div>

      <!-- Tarjeta Digi01 (+15% tamaño) con ícono de lupa en esquina superior izquierda -->
      <div class="card-presentation-box">
        <div class="card-transparent-wrapper" onclick="openLightbox('digi01')" title="Toca para ver en pantalla completa">
          
          <!-- Ícono de lupa en esquina superior izquierda -->
          <button class="card-zoom-badge" onclick="openLightbox('digi01', event)" title="Ver en pantalla completa">
            <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="7"></circle>
              <line x1="21" y1="21" x2="16" y2="16"></line>
              <line x1="11" y1="8" x2="11" y2="14"></line>
              <line x1="8" y1="11" x2="14" y2="11"></line>
            </svg>
          </button>

          <img class="card-png-image" id="imgDigi01" src="data:image/png;base64,{b64_digi01}" alt="Invitación Principal Miguel y Macarena">
        </div>
      </div>

      <!-- Botón 'Desliza hacia abajo' que guía hacia Digi02 -->
      <div class="scroll-indicator-btn" onclick="goToScene('scene-digi02')">
        <span class="scroll-text">Desliza hacia abajo</span>
        <div class="scroll-chevron">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="6 9 12 15 18 9"></polyline>
          </svg>
        </div>
      </div>

    </section>

    <!-- ======================================================================
         ESCENA 3: TARJETA DE DETALLES (DIGI02 CON ELEMENTOS DE ACOMPAÑAMIENTO)
         ====================================================================== -->
    <section class="scene digi02-scene" id="scene-digi02">

      <!-- Encabezado decorativo que acompaña y da contexto a Digi02 -->
      <div class="digi02-header">
        <span class="digi02-tag">Detalles de la Boda</span>
        <h2 class="digi02-title">Información Importante</h2>
        <div class="digi02-ornament">✦</div>
      </div>

      <!-- Tarjeta Digi02 (+15% tamaño) con QR interactivo y lupa -->
      <div class="card-presentation-box">
        <div class="card-transparent-wrapper" id="frameDigi02" onclick="handleCardClick(event)" title="Toca para ampliar la tarjeta">
          
          <!-- Ícono de lupa en esquina superior izquierda -->
          <button class="card-zoom-badge" onclick="openLightbox('digi02', event)" title="Ver en pantalla completa">
            <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="7"></circle>
              <line x1="21" y1="21" x2="16" y2="16"></line>
              <line x1="11" y1="8" x2="11" y2="14"></line>
              <line x1="8" y1="11" x2="14" y2="11"></line>
            </svg>
          </button>

          <img class="card-png-image" id="imgDigi02" src="data:image/png;base64,{b64_digi02}" alt="Detalles de la Boda">
          
          <!-- Zona táctil interactiva: CUADRADO EXACTO que envuelve únicamente el QR -->
          <div class="qr-hotspot" onclick="openPenaOlaveMap(event)" title="Abrir ubicación de Peña &amp; Olave en Google Maps">
          </div>

          <!-- Burbuja flotante situada elegantemente debajo del QR sin tapar el texto -->
          <div class="qr-tooltip-bubble" onclick="openPenaOlaveMap(event)">
            <div class="qr-tooltip-icon">
              <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                <circle cx="12" cy="10" r="3"></circle>
              </svg>
            </div>
            <span>Presiona el QR para guardar el centro de eventos en tu mapa</span>
          </div>
        </div>
      </div>

      <!-- Píldoras de resumen que enmarcan y realzan a Digi02 -->
      <div class="digi02-key-pills">
        <span class="key-pill">👗 Cocktail Formal</span>
        <span class="key-pill">✉️ Buzón de Sobres</span>
        <span class="key-pill">🍸 Recepción Adultos</span>
      </div>

      <!-- Botón de desplazamiento guiado hacia la sección práctica -->
      <div class="scroll-indicator-btn" onclick="goToScene('scene-details')">
        <span class="scroll-text">Desliza hacia abajo</span>
        <div class="scroll-chevron">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="6 9 12 15 18 9"></polyline>
          </svg>
        </div>
      </div>

    </section>

    <!-- ======================================================================
         ESCENA 4: INFORMACIÓN PRÁCTICA, ITINERARIO, CUENTA REGRESIVA Y CIERRE
         ====================================================================== -->
    <section class="details-section" id="scene-details">

      <div class="section-title-wrap">
        <span class="section-subtitle">Acompáñanos</span>
        <h2 class="section-main-title">Información del Gran Día</h2>
        <div class="section-divider-ornament"></div>
      </div>

      <!-- CUENTA REGRESIVA DESTACADA -->
      <div class="countdown-card">
        <h3 class="countdown-heading">Esperando este gran momento</h3>
        <p class="countdown-subheading">Sábado 30 de enero de 2027 &bull; 16:30 hrs</p>
        
        <div class="countdown-grid">
          <div class="countdown-item">
            <span class="countdown-number" id="cdDays">000</span>
            <span class="countdown-label">Días</span>
          </div>
          <div class="countdown-item">
            <span class="countdown-number" id="cdHours">00</span>
            <span class="countdown-label">Horas</span>
          </div>
          <div class="countdown-item">
            <span class="countdown-number" id="cdMinutes">00</span>
            <span class="countdown-label">Minutos</span>
          </div>
          <div class="countdown-item">
            <span class="countdown-number" id="cdSeconds">00</span>
            <span class="countdown-label">Segundos</span>
          </div>
        </div>
      </div>

      <!-- TARJETAS DE ITINERARIO (CEREMONIA Y RECEPCIÓN) -->
      <div class="event-cards-container">
        
        <!-- CEREMONIA RELIGIOSA (ENLACE DIRECTO GOOGLE MAPS) -->
        <div class="info-card">
          <div class="info-card-icon">
            <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.8">
              <path d="M18 20V10l-6-5-6 5v10"></path>
              <path d="M12 2v3"></path>
              <path d="M10 3.5h4"></path>
              <rect x="10" y="14" width="4" height="6"></rect>
            </svg>
          </div>
          <span class="info-card-tag">Unión Sagrada</span>
          <h3 class="info-card-title">Ceremonia Religiosa</h3>
          <span class="info-card-time">16:30 hrs</span>
          <p class="info-card-place">Iglesia Evangélica Pentecostal Talca Sur Oriente</p>
          <p class="info-card-address">27 Oriente con 10 Sur #2830, Talca Sur Oriente</p>
          <a class="btn-maps" href="https://maps.app.goo.gl/xPJMxEn1eLPBu2zZ8" target="_blank" rel="noopener noreferrer">
            <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"></polygon>
              <line x1="9" y1="3" x2="9" y2="18"></line>
              <line x1="15" y1="6" x2="15" y2="21"></line>
            </svg>
            Cómo llegar
          </a>
        </div>

        <!-- RECEPCIÓN (ENLACE DIRECTO GOOGLE MAPS) -->
        <div class="info-card">
          <div class="info-card-icon">
            <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.8">
              <path d="M8 22h8"></path>
              <path d="M12 15v7"></path>
              <path d="M12 15a5 5 0 0 0 5-5c0-4-3-8-5-8s-5 4-5 8a5 5 0 0 0 5 5z"></path>
            </svg>
          </div>
          <span class="info-card-tag">Celebración</span>
          <h3 class="info-card-title">Recepción</h3>
          <span class="info-card-time">18:00 hrs</span>
          <p class="info-card-place">Peña &amp; Olave</p>
          <p class="info-card-address">Sector Aldea Campesina, Ciudad de Talca</p>
          <a class="btn-maps" href="https://maps.app.goo.gl/wLWdGoWVMG6QNN3y6" target="_blank" rel="noopener noreferrer">
            <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"></polygon>
              <line x1="9" y1="3" x2="9" y2="18"></line>
              <line x1="15" y1="6" x2="15" y2="21"></line>
            </svg>
            Cómo llegar
          </a>
        </div>

      </div>

      <!-- NOTAS ADICIONALES (DRESSCODE, REGALOS, RECEPCIÓN ADULTOS) -->
      <div class="notes-card">
        
        <!-- Dresscode -->
        <div class="note-block">
          <h4 class="note-title">Código de Vestimenta</h4>
          <p class="note-value">Cocktail Formal</p>
          <p class="note-detail accent">Damas: por favor evitar colores negro y blanco.</p>
        </div>

        <div class="note-block-divider"></div>

        <!-- Regalos -->
        <div class="note-block">
          <h4 class="note-title">Regalos</h4>
          <p class="note-detail">
            Su presencia será el mayor regalo. Si aún así desean hacernos un obsequio, agradeceríamos que fuera mediante sobres anónimos. Dispondremos de un buzón para el efecto el día de la boda.
          </p>
        </div>

        <div class="note-block-divider"></div>

        <!-- Solo Adultos -->
        <div class="note-block">
          <h4 class="note-title">Recepción</h4>
          <p class="note-detail">
            Queremos que disfruten de este día con total libertad. Por ello, hemos preparado una recepción sólo para adultos. Agradecemos de corazón su comprensión.
          </p>
        </div>

      </div>

      <!-- BOTÓN DE CONFIRMACIÓN POR WHATSAPP Y CONTADOR DE PLAZO -->
      <div class="rsvp-container">
        <a class="btn-rsvp" id="btnRsvp" href="https://wa.me/56964304680?text=Hola!%20Confirmar%C3%A9%20con%20mucho%20gusto%20mi%20asistencia%20a%20la%20boda%20de%20Miguel%20y%20Macarena%20el%2030%20de%20enero%20de%202027." target="_blank" rel="noopener noreferrer">
          <!-- Icono WhatsApp SVG -->
          <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor">
            <path d="M12.031 2C6.511 2 2.031 6.48 2.031 12c0 1.96.57 3.79 1.55 5.34L2 22l4.81-1.54A9.97 9.97 0 0 0 12.03 22c5.52 0 10-4.48 10-10s-4.48-10-10-10zm5.82 14.24c-.24.69-1.21 1.29-1.95 1.45-.5.11-1.15.19-3.32-.71-2.77-1.15-4.57-3.95-4.71-4.14-.14-.19-1.12-1.49-1.12-2.85 0-1.35.71-2.02.96-2.29.25-.27.55-.34.73-.34.18 0 .37 0 .53.01.17.01.4.06.61.57.24.58.82 2.01.89 2.16.07.15.12.33.02.53-.1.2-.15.32-.3.49-.15.18-.31.39-.45.53-.15.14-.3.3-.13.6.17.29.77 1.27 1.66 2.06 1.14 1.02 2.1 1.34 2.4 1.48.29.15.47.13.64-.08.18-.2.76-.89.96-1.19.2-.3.41-.25.68-.15.28.1 1.76.83 2.06.98.3.15.5.23.57.35.08.13.08.74-.16 1.43z"/>
          </svg>
          <span id="btnRsvpText">Confirmaré con mucho gusto</span>
        </a>
        <p class="rsvp-caption" id="rsvpCaption">Toca el botón para enviar tu confirmación vía WhatsApp</p>

        <!-- CONTADOR DE PLAZO PARA CONFIRMAR ASISTENCIA (HASTA EL 15 DE NOVIEMBRE DE 2026) -->
        <div class="rsvp-deadline-card" id="rsvpDeadlineContainer">
          <!-- Estado Activo: Cuenta regresiva -->
          <div class="rsvp-deadline-active" id="rsvpCountdownActive">
            <div class="rsvp-deadline-header">
              <span class="rsvp-deadline-icon">⏳</span>
              <div class="rsvp-deadline-titles">
                <h4 class="rsvp-deadline-title">Plazo para confirmar asistencia</h4>
                <p class="rsvp-deadline-sub">Último día: Domingo 15 de noviembre de 2026</p>
              </div>
            </div>
            <div class="rsvp-countdown-grid">
              <div class="rsvp-countdown-box">
                <span class="rsvp-countdown-num" id="rsvpDays">00</span>
                <span class="rsvp-countdown-lbl">Días</span>
              </div>
              <div class="rsvp-countdown-box">
                <span class="rsvp-countdown-num" id="rsbpHours">00</span>
                <span class="rsvp-countdown-lbl">Horas</span>
              </div>
              <div class="rsvp-countdown-box">
                <span class="rsvp-countdown-num" id="rsvpMinutes">00</span>
                <span class="rsvp-countdown-lbl">Min</span>
              </div>
              <div class="rsvp-countdown-box">
                <span class="rsvp-countdown-num" id="rsvpSeconds">00</span>
                <span class="rsvp-countdown-lbl">Seg</span>
              </div>
            </div>
          </div>

          <!-- Estado Vencido: Mensaje afectuoso a partir del 16 de noviembre de 2026 a las 00:00 hrs -->
          <div class="rsvp-deadline-expired" id="rsvpCountdownExpired" style="display: none;">
            <div class="rsvp-expired-icon">🕊️</div>
            <h4 class="rsvp-expired-title">Plazo de confirmación finalizado</h4>
            <p class="rsvp-expired-msg">
              El plazo para confirmar asistencia ha vencido (15 de noviembre de 2026). Nos hubiera encantado contar con su presencia en nuestro gran día. ¡Agradecemos de corazón su cariño y comprensión!
            </p>
          </div>
        </div>
      </div>

      <!-- FRASE DE CIERRE -->
      <div class="closing-section">
        <div class="closing-card">
          <p class="closing-phrase">
            “Este día, damos vuelta la página y comenzamos un nuevo capítulo. Queremos escribirlo junto a ustedes.”
          </p>
          <p class="closing-signature">Miguel y Macarena</p>
        </div>

        <!-- ENLACE DISCRETO DE RECOMENDACIONES DE ALOJAMIENTO -->
        <div class="accommodation-link-wrap">
          <button class="link-accommodation" onclick="openAccommodationModal()">
            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M2 4v16M2 8h18a2 2 0 0 1 2 2v10M2 17h20M6 8v9"></path>
            </svg>
            Recomendaciones de alojamiento cerca del centro
          </button>
        </div>
      </div>

    </section>

  </div>

  <!-- ==========================================================================
       MODAL DE RECOMENDACIONES DE ALOJAMIENTO Y TIPS DE VIAJE A TALCA
       ========================================================================== -->
  <div class="modal-backdrop" id="accommodationModal" onclick="handleModalBackdropClick(event)">
    <div class="modal-box" role="dialog" aria-modal="true" aria-labelledby="modalTitle">
      <button class="modal-close-btn" onclick="closeAccommodationModal()" aria-label="Cerrar modal">&times;</button>
      
      <div class="modal-header">
        <h3 class="modal-title" id="modalTitle">Alojamiento en Talca</h3>
        <p class="modal-subtitle">Recomendaciones seleccionadas y tips de viaje para su llegada</p>
      </div>

      <div class="hotels-list">
        
        <!-- Hotel 1 -->
        <div class="hotel-item">
          <span class="hotel-number">Opción 1</span>
          <h4 class="hotel-name">Hotel Marcos Gamero</h4>
          <p class="hotel-location">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
              <circle cx="12" cy="10" r="3"></circle>
            </svg>
            Muy cerca de Plaza de Armas (1 Oriente #1070)
          </p>
          <a class="btn-hotel-map" href="https://www.google.com/maps/search/?api=1&query=Hotel+Marcos+Gamero+Talca" target="_blank" rel="noopener noreferrer">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"></polygon>
            </svg>
            Ver en Google Maps
          </a>
        </div>

        <!-- Hotel 2 -->
        <div class="hotel-item">
          <span class="hotel-number">Opción 2</span>
          <h4 class="hotel-name">Hotel Diego de Almagro Talca</h4>
          <p class="hotel-location">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
              <circle cx="12" cy="10" r="3"></circle>
            </svg>
            Sobre la Alameda (Av. 4 Norte #1011)
          </p>
          <a class="btn-hotel-map" href="https://www.google.com/maps/search/?api=1&query=Hotel+Diego+de+Almagro+Talca" target="_blank" rel="noopener noreferrer">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"></polygon>
            </svg>
            Ver en Google Maps
          </a>
        </div>

        <!-- Hotel 3 -->
        <div class="hotel-item">
          <span class="hotel-number">Opción 3</span>
          <h4 class="hotel-name">Ecohotel Talca</h4>
          <p class="hotel-location">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
              <circle cx="12" cy="10" r="3"></circle>
            </svg>
            Cerca de Plaza de Armas (5 Oriente #1059)
          </p>
          <a class="btn-hotel-map" href="https://www.google.com/maps/search/?api=1&query=Ecohotel+Talca" target="_blank" rel="noopener noreferrer">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"></polygon>
            </svg>
            Ver en Google Maps
          </a>
        </div>

      </div>

      <!-- SECCIÓN ENRIQUECIDA CON TIPS DE VIAJE A TALCA -->
      <div class="travel-tips-container">
        <h4 class="travel-tips-title">
          <span>🚗</span> Tips de Viaje para llegar a Talca
        </h4>
        <div class="travel-tips-grid">
          
          <div class="travel-tip-card">
            <div class="travel-tip-header">
              <span>🚆</span> En Tren (EFE Trenes de Chile)
            </div>
            <p class="travel-tip-desc">
              Desde Estación Central (Santiago) hasta Estación Talca en el servicio rápido / expreso. Tiempo estimado: <strong>~2 hrs 40 min a 2 hrs 50 min</strong>. Es una de las alternativas más cómodas, puntuales y con vista panorámica campestre.
            </p>
          </div>

          <div class="travel-tip-card">
            <div class="travel-tip-header">
              <span>🚗</span> En Auto Particular
            </div>
            <p class="travel-tip-desc">
              Vía Ruta 5 Sur directa (~255 km desde Santiago). Tiempo estimado: <strong>~2 hrs 45 min a 3 horas</strong> dependiendo del flujo. Considerar los 3 peajes troncales habituales (Angostura, Quinta y Río Claro).
            </p>
          </div>

          <div class="travel-tip-card">
            <div class="travel-tip-header">
              <span>🚌</span> En Bus Interurbano
            </div>
            <p class="travel-tip-desc">
              Salidas regulares cada 15 a 30 minutos desde los terminales Sur y Alameda en Santiago (Buses Talca París &amp; Londres, Pullman Bus, Cóndor). Tiempo estimado: <strong>~3 hrs a 3 hrs 30 min</strong>.
            </p>
          </div>

          <div class="travel-tip-card">
            <div class="travel-tip-header">
              <span>✈️</span> Llegada desde otras Regiones (Vía Aérea)
            </div>
            <p class="travel-tip-desc">
              Para familiares y amigos que viajan desde el norte o extremo sur: vuelo hacia Aeropuerto de Santiago (SCL) + conexión terrestre directa hacia Talca (en tren, transfer, bus o vehículo de alquiler).
            </p>
          </div>

        </div>

        <div class="travel-recommendation-box">
          <strong>💡 Recomendación importante:</strong> Enero es temporada alta de vacaciones de verano en la Región del Maule. Sugerimos realizar reservas de alojamiento y pasajes con anticipación para asegurar disponibilidad y tarifas preferenciales.
        </div>
      </div>

    </div>
  </div>

  <!-- ==========================================================================
       MODAL LIGHTBOX PANTALLA COMPLETA PARA DIGI01 Y DIGI02
       ========================================================================== -->
  <div class="lightbox-modal" id="lightboxModal" onclick="handleLightboxBackdropClick(event)">
    <div class="lightbox-toolbar">
      <!-- Botón Zoom +/- -->
      <button class="lightbox-btn" id="btnZoomToggle" onclick="toggleLightboxZoom(event)" title="Alternar zoom">
        <svg id="iconZoomIn" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          <line x1="11" y1="8" x2="11" y2="14"></line>
          <line x1="8" y1="11" x2="14" y2="11"></line>
        </svg>
        <svg id="iconZoomOut" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" style="display:none;">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          <line x1="8" y1="11" x2="14" y2="11"></line>
        </svg>
      </button>

      <!-- Botón Cerrar -->
      <button class="lightbox-btn" onclick="closeLightbox()" title="Cerrar vista">&times;</button>
    </div>

    <div class="lightbox-content" id="lightboxContent" onclick="toggleLightboxZoom(event)">
      <img class="lightbox-img" id="lightboxImg" src="" alt="Invitación ampliada">
    </div>

    <div class="lightbox-hint">Toca la imagen para alternar zoom</div>
  </div>

  <!-- ==========================================================================
       JAVASCRIPT AUTOCONTENIDO (LÓGICA DE EXPERIENCIA, MÚSICA Y NAVEGACIÓN)
       ========================================================================== -->
  <script>
    // -------------------------------------------------------------------------
    // 1. CONTROL DE AUDIO (VOLUMEN CONFORTABLE AL 45% = 0.45)
    // -------------------------------------------------------------------------
    const bgMusic = document.getElementById('bgMusic');
    const TARGET_VOLUME = 0.45; // Máximo 45% de volumen para evitar sobresaltos
    let musicStarted = false;

    function playAudioWithComfortVolume() {{
      if (musicStarted || !bgMusic) return;

      bgMusic.volume = 0;
      const playPromise = bgMusic.play();
      if (playPromise !== undefined) {{
        playPromise.then(() => {{
          musicStarted = true;
          
          // Suave incremento de volumen en 1.0 segundo hasta el 45% (0.45)
          let currentVol = 0;
          const fadeInterval = setInterval(() => {{
            currentVol += 0.03;
            if (currentVol >= TARGET_VOLUME) {{
              currentVol = TARGET_VOLUME;
              clearInterval(fadeInterval);
            }}
            bgMusic.volume = currentVol;
          }}, 50);

        }}).catch(() => {{
          // Política de reproducción automática
        }});
      }}
    }}

    // -------------------------------------------------------------------------
    // 2. BLOQUEO / DESBLOQUEO DE SCROLL Y EXPERIENCIA INICIAL
    // -------------------------------------------------------------------------
    let isExperienceStarted = false;
    let isScrollLocked = true;

    function preventScrollWhenLocked(e) {{
      if (isScrollLocked) {{
        e.preventDefault();
      }}
    }}

    // Evitar que el usuario baje antes del primer clic
    window.addEventListener('touchmove', preventScrollWhenLocked, {{ passive: false }});
    window.addEventListener('wheel', preventScrollWhenLocked, {{ passive: false }});

    const envelopeStage = document.getElementById('envelopeStage');
    const envelopeRevealed = document.getElementById('envelopeRevealed');
    const startPrompt = document.getElementById('startPrompt');
    const startPromptWrap = document.getElementById('startPromptWrap');
    const heroScrollBtn = document.getElementById('heroScrollBtn');

    // -------------------------------------------------------------------------
    // PANTALLA COMPLETA INMERSIVA (MÓVIL Y ESCRITORIO)
    // -------------------------------------------------------------------------
    function requestAppFullscreen() {{
      try {{
        const docEl = document.documentElement;
        const requestFs = docEl.requestFullscreen ||
                          docEl.webkitRequestFullscreen ||
                          docEl.webkitRequestFullScreen ||
                          docEl.mozRequestFullScreen ||
                          docEl.msRequestFullscreen;
        if (requestFs) {{
          const promise = requestFs.call(docEl);
          if (promise && typeof promise.catch === 'function') {{
            promise.catch(function() {{
              // Silencioso si el navegador o usuario no lo autoriza
            }});
          }}
        }}
      }} catch (err) {{
        // Silencioso para garantizar compatibilidad total
      }}
    }}

    // Intentar activar pantalla completa al cargar la página (si el entorno/browser lo permite)
    window.addEventListener('DOMContentLoaded', () => {{
      requestAppFullscreen();
    }});
    window.addEventListener('load', () => {{
      requestAppFullscreen();
    }});

    // Activar pantalla completa al interactuar por primera vez en cualquier parte
    window.addEventListener('click', function tryFsOnce() {{
      requestAppFullscreen();
    }}, {{ passive: true }});
    window.addEventListener('touchstart', function tryFsTouchOnce() {{
      requestAppFullscreen();
    }}, {{ passive: true }});

    function startExperience(event) {{
      if (event) event.stopPropagation();
      if (isExperienceStarted) return;
      isExperienceStarted = true;

      // 0. Activar Pantalla Completa inmersiva
      requestAppFullscreen();

      // 1. Iniciar música al 45% de volumen
      playAudioWithComfortVolume();

      // 2. Quitar halo y ocultar mensaje sugerente
      if (envelopeStage) {{
        envelopeStage.classList.remove('pulsing-halo');
      }}
      if (startPrompt) {{
        startPrompt.classList.add('hidden');
      }}
      if (startPromptWrap) {{
        startPromptWrap.classList.add('hidden');
      }}

      // 3. Ejecutar transición suave pura hacia Digi04 (sin movimiento ni escala)
      if (envelopeRevealed) {{
        envelopeRevealed.classList.add('revealed');
      }}

      // 4. Desbloquear scroll del documento
      isScrollLocked = false;
      window.removeEventListener('touchmove', preventScrollWhenLocked);
      window.removeEventListener('wheel', preventScrollWhenLocked);
      document.documentElement.classList.remove('locked-scroll');
      document.body.classList.remove('locked-scroll');

      // 5. Mostrar botón 'Desliza hacia abajo' tras un breve instante
      setTimeout(() => {{
        if (heroScrollBtn) {{
          heroScrollBtn.classList.add('visible');
        }}
      }}, 500);
    }}

    // -------------------------------------------------------------------------
    // 3. NAVEGACIÓN GUIADA ESCENA POR ESCENA ('DESLIZA HACIA ABAJO')
    // -------------------------------------------------------------------------
    function goToScene(targetId) {{
      playAudioWithComfortVolume();
      const targetElement = document.getElementById(targetId);
      if (targetElement) {{
        targetElement.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
      }}
    }}

    // -------------------------------------------------------------------------
    // 4. CUENTA REGRESIVA HASTA EL 30 DE ENERO DE 2027 A LAS 16:30 HRS (CHILE)
    // -------------------------------------------------------------------------
    // En enero, Chile se encuentra en horario de verano (UTC-3).
    const targetDate = new Date("2027-01-30T16:30:00-03:00").getTime();

    const elDays = document.getElementById('cdDays');
    const elHours = document.getElementById('cdHours');
    const elMinutes = document.getElementById('cdMinutes');
    const elSeconds = document.getElementById('cdSeconds');

    function updateCountdown() {{
      const now = new Date().getTime();
      const difference = targetDate - now;

      if (difference <= 0) {{
        elDays.textContent = "00";
        elHours.textContent = "00";
        elMinutes.textContent = "00";
        elSeconds.textContent = "00";
        return;
      }}

      const days = Math.floor(difference / (1000 * 60 * 60 * 24));
      const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((difference % (1000 * 60)) / 1000);

      elDays.textContent = days.toString().padStart(2, '0');
      elHours.textContent = hours.toString().padStart(2, '0');
      elMinutes.textContent = minutes.toString().padStart(2, '0');
      elSeconds.textContent = seconds.toString().padStart(2, '0');
    }}

    updateCountdown();
    setInterval(updateCountdown, 1000);

    // -------------------------------------------------------------------------
    // 5. CUENTA REGRESIVA DE CONFIRMACIÓN (HASTA EL 15 DE NOVIEMBRE DE 2026 23:59:59)
    // -------------------------------------------------------------------------
    // Último día para confirmar: Domingo 15 de noviembre de 2026.
    // A las 00:00 hrs del lunes 16 de noviembre de 2026 (UTC-3 Chile), el plazo vence.
    const rsvpDeadline = new Date("2026-11-16T00:00:00-03:00").getTime();

    const rsvpActiveEl = document.getElementById('rsvpCountdownActive');
    const rsvpExpiredEl = document.getElementById('rsvpCountdownExpired');
    const btnRsvp = document.getElementById('btnRsvp');
    const btnRsvpText = document.getElementById('btnRsvpText');
    const rsvpCaption = document.getElementById('rsvpCaption');

    const elRsvpDays = document.getElementById('rsvpDays');
    const elRsbpHours = document.getElementById('rsbpHours');
    const elRsvpMinutes = document.getElementById('rsvpMinutes');
    const elRsvpSeconds = document.getElementById('rsvpSeconds');

    function updateRsvpCountdown() {{
      const now = new Date().getTime();
      let difference = rsvpDeadline - now;

      // Soporte para pruebas inmediatas agregando ?test_expired=true en la URL
      if (window.location.search.includes('test_expired=true')) {{
        difference = -1;
      }}

      if (difference <= 0) {{
        // PLAZO VENCIDO (Desde el 16 de noviembre 00:00 hrs)
        if (rsvpActiveEl) rsvpActiveEl.style.display = 'none';
        if (rsvpExpiredEl) rsvpExpiredEl.style.display = 'block';
        if (btnRsvp) {{
          btnRsvp.classList.add('expired-btn');
          btnRsvp.removeAttribute('href');
          btnRsvp.style.pointerEvents = 'none';
        }}
        if (btnRsvpText) {{
          btnRsvpText.textContent = "Plazo de confirmación finalizado";
        }}
        if (rsvpCaption) {{
          rsvpCaption.textContent = "El periodo para confirmar asistencia ha concluido";
        }}
        return;
      }}

      // PLAZO ACTIVO
      if (rsvpActiveEl) rsvpActiveEl.style.display = 'block';
      if (rsvpExpiredEl) rsvpExpiredEl.style.display = 'none';

      const days = Math.floor(difference / (1000 * 60 * 60 * 24));
      const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((difference % (1000 * 60)) / 1000);

      if (elRsvpDays) elRsvpDays.textContent = days.toString().padStart(2, '0');
      if (elRsbpHours) elRsbpHours.textContent = hours.toString().padStart(2, '0');
      if (elRsvpMinutes) elRsvpMinutes.textContent = minutes.toString().padStart(2, '0');
      if (elRsvpSeconds) elRsvpSeconds.textContent = seconds.toString().padStart(2, '0');
    }}

    updateRsvpCountdown();
    setInterval(updateRsvpCountdown, 1000);

    // -------------------------------------------------------------------------
    // 5. INTERACCIÓN DEL QR EN DIGI02 (ENLACE DIRECTO A PEÑA & OLAVE)
    // -------------------------------------------------------------------------
    function openPenaOlaveMap(event) {{
      if (event) event.stopPropagation();
      playAudioWithComfortVolume();
      const mapsUrl = "https://maps.app.goo.gl/wLWdGoWVMG6QNN3y6";
      window.open(mapsUrl, '_blank', 'noopener,noreferrer');
    }}

    function handleCardClick(event) {{
      // Si el clic no fue dentro del tooltip ni el hotspot ni la lupa, abrir lightbox
      if (!event.target.closest('.qr-hotspot') && !event.target.closest('.qr-tooltip-bubble') && !event.target.closest('.card-zoom-badge')) {{
        openLightbox('digi02');
      }}
    }}

    // -------------------------------------------------------------------------
    // 6. MODAL DE ALOJAMIENTO Y TIPS
    // -------------------------------------------------------------------------
    const accommodationModal = document.getElementById('accommodationModal');

    function openAccommodationModal() {{
      playAudioWithComfortVolume();
      if (accommodationModal) {{
        accommodationModal.classList.add('active');
        document.body.style.overflow = 'hidden';
      }}
    }}

    function closeAccommodationModal() {{
      if (accommodationModal) {{
        accommodationModal.classList.remove('active');
        document.body.style.overflow = '';
      }}
    }}

    function handleModalBackdropClick(event) {{
      if (event.target === accommodationModal) {{
        closeAccommodationModal();
      }}
    }}

    // -------------------------------------------------------------------------
    // 7. LIGHTBOX PANTALLA COMPLETA PARA DIGI01 Y DIGI02
    // -------------------------------------------------------------------------
    const lightboxModal = document.getElementById('lightboxModal');
    const lightboxImg = document.getElementById('lightboxImg');
    const lightboxContent = document.getElementById('lightboxContent');
    const iconZoomIn = document.getElementById('iconZoomIn');
    const iconZoomOut = document.getElementById('iconZoomOut');
    let isZoomed = false;

    const imagesData = {{
      'digi01': 'data:image/png;base64,{b64_digi01}',
      'digi02': 'data:image/png;base64,{b64_digi02}'
    }};

    function openLightbox(cardId, event) {{
      if (event) event.stopPropagation();
      playAudioWithComfortVolume();
      if (!lightboxModal || !lightboxImg) return;
      
      const imgSrc = imagesData[cardId];
      if (imgSrc) {{
        lightboxImg.src = imgSrc;
        lightboxModal.classList.add('active');
        document.body.style.overflow = 'hidden';
        resetLightboxZoom();
      }}
    }}

    function closeLightbox() {{
      if (lightboxModal) {{
        lightboxModal.classList.remove('active');
        document.body.style.overflow = '';
        resetLightboxZoom();
      }}
    }}

    function resetLightboxZoom() {{
      isZoomed = false;
      if (lightboxContent) lightboxContent.classList.remove('zoomed');
      if (iconZoomIn) iconZoomIn.style.display = 'block';
      if (iconZoomOut) iconZoomOut.style.display = 'none';
    }}

    function toggleLightboxZoom(event) {{
      if (event) event.stopPropagation();
      isZoomed = !isZoomed;
      if (lightboxContent) {{
        if (isZoomed) {{
          lightboxContent.classList.add('zoomed');
          if (iconZoomIn) iconZoomIn.style.display = 'none';
          if (iconZoomOut) iconZoomOut.style.display = 'block';
        }} else {{
          lightboxContent.classList.remove('zoomed');
          if (iconZoomIn) iconZoomIn.style.display = 'block';
          if (iconZoomOut) iconZoomOut.style.display = 'none';
        }}
      }}
    }}

    function handleLightboxBackdropClick(event) {{
      if (event.target === lightboxModal) {{
        closeLightbox();
      }}
    }}

    // Cerrar modales con tecla Escape
    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        closeAccommodationModal();
        closeLightbox();
      }}
    }});
  </script>
</body>
</html>
"""

output_paths = [
    "index.html",
    "invitacion-miguel-macarena.html",
    "Invitación Matrimonio - Miguel y Macarena.html"
]
for p in output_paths:
    with open(p, "w", encoding="utf-8") as f:
        f.write(html_content)
    file_size = os.path.getsize(p)
    print(f"File '{p}' written successfully! Size: {file_size} bytes ({file_size/1024/1024:.2f} MB)")
