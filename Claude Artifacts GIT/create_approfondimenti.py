import os

# Directory di lavoro
base_dir = r"C:\Users\Alle\Desktop\MEMEX\99_Archivio\Claude Artifacts GIT"

# Template base HTML
template_base = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Approfondimento: {title} - Entropia del Debito</title>
    
    <!-- Chart.js for visualizations -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    
    <!-- Math.js for calculations -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/11.11.0/math.min.js"></script>
    
    <style>
        :root {{
            --primary-dark: #0a0e27;
            --primary-light: #1a1f3a;
            --accent-blue: #00d4ff;
            --accent-purple: #8b5cf6;
            --accent-red: #ef4444;
            --accent-green: #10b981;
            --accent-yellow: #f59e0b;
            --text-primary: #e2e8f0;
            --text-secondary: #94a3b8;
            --border-color: #334155;
            --glow-blue: 0 0 30px rgba(0, 212, 255, 0.5);
            --glow-purple: 0 0 30px rgba(139, 92, 246, 0.5);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0a0e27 100%);
            color: var(--text-primary);
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }}

        /* Animated background particles */
        #particles-bg {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            opacity: 0.3;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            position: relative;
            z-index: 1;
        }}

        /* Header */
        .header {{
            text-align: center;
            padding: 40px 0;
            margin-bottom: 40px;
            position: relative;
            overflow: hidden;
        }}

        .header::before {{
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(139, 92, 246, 0.1) 0%, transparent 70%);
            animation: pulse 4s ease-in-out infinite;
        }}

        @keyframes pulse {{
            0%, 100% {{ opacity: 0.3; transform: translate(-50%, -50%) scale(1); }}
            50% {{ opacity: 0.6; transform: translate(-50%, -50%) scale(1.1); }}
        }}

        h1 {{
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(45deg, var(--accent-blue), var(--accent-purple));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
            position: relative;
            z-index: 1;
            text-shadow: 0 0 40px rgba(139, 92, 246, 0.4);
        }}

        .subtitle {{
            font-size: 1.2rem;
            color: var(--text-secondary);
            position: relative;
            z-index: 1;
        }}

        /* Navigation */
        .nav-buttons {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin: 30px 0;
            flex-wrap: wrap;
        }}

        .nav-button {{
            background: linear-gradient(135deg, var(--accent-purple), var(--accent-blue));
            border: none;
            border-radius: 12px;
            padding: 12px 30px;
            color: white;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(139, 92, 246, 0.3);
            text-decoration: none;
            display: inline-block;
        }}

        .nav-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(139, 92, 246, 0.5);
        }}

        .nav-button.primary {{
            background: linear-gradient(135deg, var(--accent-green), var(--accent-blue));
            font-size: 1.1rem;
            padding: 15px 40px;
        }}

        /* Cards */
        .card {{
            background: rgba(26, 31, 58, 0.8);
            border: 1px solid var(--border-color);
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 25px;
            backdrop-filter: blur(10px);
            position: relative;
            overflow: hidden;
        }}

        .card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple));
            animation: shimmer 3s ease-in-out infinite;
        }}

        @keyframes shimmer {{
            0%, 100% {{ transform: translateX(-100%); }}
            50% {{ transform: translateX(100%); }}
        }}

        .card h2 {{
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: var(--accent-blue);
        }}

        .card h3 {{
            font-size: 1.3rem;
            margin: 25px 0 15px 0;
            color: var(--accent-purple);
        }}

        /* Alert boxes */
        .alert {{
            background: rgba(239, 68, 68, 0.1);
            border: 1px solid var(--accent-red);
            border-radius: 10px;
            padding: 15px;
            margin: 20px 0;
            display: flex;
            align-items: center;
            gap: 15px;
        }}

        .alert-icon {{
            font-size: 1.5rem;
            color: var(--accent-red);
        }}

        .info-box {{
            background: rgba(0, 212, 255, 0.1);
            border: 1px solid var(--accent-blue);
            border-radius: 10px;
            padding: 15px;
            margin: 20px 0;
        }}

        /* Responsive */
        @media (max-width: 768px) {{
            h1 {{ font-size: 2rem; }}
            .nav-buttons {{ flex-direction: column; }}
            .nav-button {{ width: 100%; }}
        }}
    </style>
</head>
<body>
    <!-- Animated particles background -->
    <canvas id="particles-bg"></canvas>

    <div class="container">
        <!-- Header -->
        <div class="header">
            <h1>{icon} APPROFONDIMENTO: {header}</h1>
            <p class="subtitle">{subtitle}</p>
        </div>

        <!-- Navigation -->
        <div class="nav-buttons">
            <a href="entropia-debito-dashboard.html" class="nav-button primary">
                ← Torna alla Dashboard
            </a>
            {prev_button}
            {next_button}
        </div>

        <!-- Content -->
        {content}

        <!-- Bottom Navigation -->
        <div class="nav-buttons" style="margin-top: 50px;">
            <a href="entropia-debito-dashboard.html" class="nav-button">
                ← Dashboard Principale
            </a>
            {bottom_next_button}
        </div>
    </div>

    <script>
        // Initialize particles background
        function initParticles() {{
            const canvas = document.getElementById('particles-bg');
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;

            const particles = [];
            const particleCount = 100;

            class Particle {{
                constructor() {{
                    this.x = Math.random() * canvas.width;
                    this.y = Math.random() * canvas.height;
                    this.vx = (Math.random() - 0.5) * 0.5;
                    this.vy = (Math.random() - 0.5) * 0.5;
                    this.radius = Math.random() * 2;
                    this.opacity = Math.random() * 0.5 + 0.2;
                }}

                update() {{
                    this.x += this.vx;
                    this.y += this.vy;

                    if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
                    if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
                }}

                draw() {{
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                    ctx.fillStyle = `rgba(139, 92, 246, ${{this.opacity}})`;
                    ctx.fill();
                }}
            }}

            for (let i = 0; i < particleCount; i++) {{
                particles.push(new Particle());
            }}

            function animate() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                particles.forEach(particle => {{
                    particle.update();
                    particle.draw();
                }});
                requestAnimationFrame(animate);
            }}

            animate();
        }}

        // Initialize on load
        window.addEventListener('load', initParticles);

        // Handle window resize
        window.addEventListener('resize', () => {{
            const canvas = document.getElementById('particles-bg');
            if (canvas) {{
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            }}
        }});
    </script>
</body>
</html>"""

# Configurazione per ogni sezione
sections = [
    {
        'filename': 'entropia-approfondimento-termodinamica.html',
        'title': 'Termodinamica',
        'icon': '🔬',
        'header': 'TERMODINAMICA',
        'subtitle': 'Le Leggi della Termodinamica Applicate all\'Economia',
        'prev': 'entropia-approfondimento-overview.html',
        'next': 'entropia-approfondimento-simulazione.html',
        'content_file': 'content_termodinamica.txt'
    },
    {
        'filename': 'entropia-approfondimento-simulazione.html',
        'title': 'Simulazione',
        'icon': '🔮',
        'header': 'SIMULAZIONE',
        'subtitle': 'Modellare il Futuro Entropico',
        'prev': 'entropia-approfondimento-termodinamica.html',
        'next': 'entropia-approfondimento-metriche.html',
        'content_file': 'content_simulazione.txt'
    },
    {
        'filename': 'entropia-approfondimento-metriche.html',
        'title': 'Metriche Live',
        'icon': '📡',
        'header': 'METRICHE LIVE',
        'subtitle': 'Leggere i Segni Vitali del Sistema',
        'prev': 'entropia-approfondimento-simulazione.html',
        'next': 'entropia-approfondimento-collasso.html',
        'content_file': 'content_metriche.txt'
    },
    {
        'filename': 'entropia-approfondimento-collasso.html',
        'title': 'Curve di Collasso',
        'icon': '💀',
        'header': 'CURVE DI COLLASSO',
        'subtitle': 'Anatomia del Collasso: Comprendere l\'Inevitabile',
        'prev': 'entropia-approfondimento-metriche.html',
        'next': 'entropia-approfondimento-strategie.html',
        'content_file': 'content_collasso.txt'
    },
    {
        'filename': 'entropia-approfondimento-strategie.html',
        'title': 'Strategie',
        'icon': '🎯',
        'header': 'STRATEGIE',
        'subtitle': 'Navigare l\'Entropia: Strategie per un Mondo in Debito',
        'prev': 'entropia-approfondimento-collasso.html',
        'next': 'entropia-approfondimento-storia.html',
        'content_file': 'content_strategie.txt'
    },
    {
        'filename': 'entropia-approfondimento-storia.html',
        'title': 'Casi Storici',
        'icon': '📚',
        'header': 'CASI STORICI',
        'subtitle': 'Lezioni dalla Storia: L\'Entropia Attraverso i Millenni',
        'prev': 'entropia-approfondimento-strategie.html',
        'next': 'entropia-approfondimento-filosofia.html',
        'content_file': 'content_storia.txt'
    },
    {
        'filename': 'entropia-approfondimento-filosofia.html',
        'title': 'Filosofia',
        'icon': '🧠',
        'header': 'FILOSOFIA',
        'subtitle': 'La Dimensione Filosofica: Significato nell\'Era dell\'Entropia',
        'prev': 'entropia-approfondimento-storia.html',
        'next': None,
        'content_file': 'content_filosofia.txt'
    }
]

# Genera i file
for section in sections:
    # Crea pulsanti di navigazione
    prev_button = f'<a href="{section["prev"]}" class="nav-button">← Precedente</a>' if section['prev'] else ''
    next_button = f'<a href="{section["next"]}" class="nav-button">Prossimo →</a>' if section['next'] else ''
    bottom_next_button = f'<a href="{section["next"]}" class="nav-button primary">Prossimo Approfondimento →</a>' if section['next'] else '<a href="entropia-debito-dashboard.html" class="nav-button primary">Torna all\'Inizio →</a>'
    
    # Riempi il template
    html_content = template_base.format(
        title=section['title'],
        icon=section['icon'],
        header=section['header'],
        subtitle=section['subtitle'],
        prev_button=prev_button,
        next_button=next_button,
        content='<div class="card"><h2>Contenuto in arrivo...</h2><p>Il contenuto completo di questa sezione sarà aggiunto a breve.</p></div>',
        bottom_next_button=bottom_next_button
    )
    
    # Salva il file
    filepath = os.path.join(base_dir, section['filename'])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Creato: {section['filename']}")

print("\nTutti i file sono stati creati con successo!")