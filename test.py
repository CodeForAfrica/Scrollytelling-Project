import streamlit as st

# Configuration de la page pour occuper toute la largeur
st.set_page_config(page_title="Scrollytelling", layout="wide")

# Masquer les éléments Streamlit pour une expérience fullscreen
st.markdown("""
<style>
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        max-width: 100%;
    }
    
    header[data-testid="stHeader"] {
        display: none;
    }
    
    .stApp > footer {
        display: none;
    }
    
    .stApp {
        margin-top: -80px;
    }
</style>
""", unsafe_allow_html=True)

html_code = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Scrollytelling - Graphiques Dynamiques</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <style>
    * {
      box-sizing: border-box;
    }

    body {
      font-family: 'Inter', sans-serif;
      margin: 0; 
      padding: 0;
      background: #f1f5f9;
      color: #1e293b;
      overflow-x: hidden;
      line-height: 1.6;
    }

    #scrolly__section {
      position: relative;
      width: 100%;
      min-height: 100vh;
    }

    .scrolly__chart {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 1;
      background: #ffffff;
    }

    iframe {
      width: 100%;
      height: 100%;
      border: none;
      opacity: 1;
      transition: all 0.8s ease-in-out;
    }

    .chart-info-panel {
      position: fixed;
      top: 2rem;
      right: 2rem;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(10px);
      border-radius: 16px;
      padding: 1.5rem;
      max-width: 350px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.3);
      z-index: 15;
      transform: translateY(-20px);
      opacity: 0;
      transition: all 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }

    .chart-info-panel.active {
      transform: translateY(0);
      opacity: 1;
    }

    .chart-info-title {
      font-size: 1.2rem;
      font-weight: 600;
      color: #1e293b;
      margin-bottom: 0.5rem;
    }

    .chart-info-desc {
      font-size: 0.9rem;
      color: #64748b;
      margin-bottom: 1rem;
    }

    .chart-metric {
      display: inline-block;
      background: linear-gradient(135deg, #3b82f6, #1d4ed8);
      color: white;
      padding: 0.5rem 1rem;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 500;
      margin-right: 0.5rem;
      margin-bottom: 0.5rem;
    }

    .scrolly__content {
      position: relative;
      width: 100%;
      max-width: 600px;
      margin-left: 3rem;
      padding: 10vh 0 10vh 0;
      z-index: 10;
    }

    .step {
      margin-bottom: 120vh;
      padding: 2.5rem;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(20px);
      border-radius: 20px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.4);
      transition: all 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
      transform: translateX(-50px);
      opacity: 0.6;
      min-height: 400px;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .step.is-active {
      transform: translateX(0);
      opacity: 1;
      box-shadow: 0 30px 60px rgba(59, 130, 246, 0.15);
      border-color: #3b82f6;
      background: rgba(255, 255, 255, 0.98);
    }

    .step h3 {
      font-size: 2.2rem;
      font-weight: 700;
      margin-bottom: 1rem;
      color: #1e293b;
      line-height: 1.2;
    }

    .step p {
      font-size: 1.15rem;
      color: #475569;
      margin-bottom: 1.5rem;
      line-height: 1.7;
    }

    .step-number {
      display: inline-block;
      width: 50px;
      height: 50px;
      background: linear-gradient(135deg, #3b82f6, #1d4ed8);
      color: white;
      border-radius: 50%;
      text-align: center;
      line-height: 50px;
      font-weight: 700;
      margin-bottom: 1.5rem;
      font-size: 1.3rem;
      box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }

    .step-highlight {
      background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(29, 78, 216, 0.05));
      padding: 2rem;
      border-radius: 12px;
      border-left: 5px solid #3b82f6;
      margin: 2rem 0;
      position: relative;
    }

    .step-highlight::before {
      content: "💡";
      position: absolute;
      top: -10px;
      left: 20px;
      background: white;
      padding: 5px 10px;
      border-radius: 20px;
      font-size: 1.2rem;
    }

    .step-highlight strong {
      color: #1e40af;
      font-weight: 600;
    }

    .progress-bar {
      position: fixed;
      top: 0;
      left: 0;
      width: 0%;
      height: 5px;
      background: linear-gradient(90deg, #3b82f6, #1d4ed8);
      z-index: 100;
      transition: width 0.3s ease;
      box-shadow: 0 2px 10px rgba(59, 130, 246, 0.3);
    }

    .chart-transition-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(59, 130, 246, 0.1);
      z-index: 5;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
    }

    .chart-transition-overlay.transitioning {
      opacity: 1;
    }

    /* Navigation dots */
    .nav-dots {
      position: fixed;
      right: 2rem;
      top: 50%;
      transform: translateY(-50%);
      z-index: 20;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .nav-dot {
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: rgba(59, 130, 246, 0.3);
      cursor: pointer;
      transition: all 0.3s ease;
    }

    .nav-dot.active {
      background: #3b82f6;
      transform: scale(1.3);
    }

    /* Responsive design */
    @media (max-width: 768px) {
      .scrolly__content {
        max-width: calc(100% - 2rem);
        margin-left: 1rem;
        margin-right: 1rem;
      }
      
      .step {
        padding: 2rem;
        min-height: 300px;
      }
      
      .step h3 {
        font-size: 1.8rem;
      }

      .chart-info-panel {
        top: 1rem;
        right: 1rem;
        left: 1rem;
        max-width: none;
      }

      .nav-dots {
        bottom: 2rem;
        right: 50%;
        transform: translateX(50%);
        flex-direction: row;
        top: auto;
      }
    }

    /* Animation pour les changements de graphiques */
    @keyframes chartChange {
      0% { transform: scale(1); opacity: 1; }
      50% { transform: scale(0.95); opacity: 0.7; }
      100% { transform: scale(1); opacity: 1; }
    }

    .chart-changing iframe {
      animation: chartChange 1s ease-in-out;
    }
  </style>
</head>
<body>

<div class="progress-bar" id="progress-bar"></div>

<div class="nav-dots" id="nav-dots">
  <div class="nav-dot active" data-step="0"></div>
  <div class="nav-dot" data-step="1"></div>
  <div class="nav-dot" data-step="2"></div>
  <div class="nav-dot" data-step="3"></div>
</div>

<div id="scrolly__section">
  
  <div class="scrolly__chart" id="chart-container">
    <div class="chart-transition-overlay" id="transition-overlay"></div>
    <iframe id="flourish-iframe" src="https://flo.uri.sh/visualisation/19897131/embed" scrolling="no"></iframe>
    
    <div class="chart-info-panel active" id="chart-info-0">
      <div class="chart-info-title">Vue d'ensemble des données</div>
      <div class="chart-info-desc">Introduction à notre analyse complète</div>
      <span class="chart-metric">4 Étapes</span>
      <span class="chart-metric">Données 2024</span>
    </div>

    <div class="chart-info-panel" id="chart-info-1">
      <div class="chart-info-title">Tendances de croissance</div>
      <div class="chart-info-desc">Analyse des patterns temporels</div>
      <span class="chart-metric">+25% Croissance</span>
      <span class="chart-metric">Q1-Q4 2024</span>
    </div>

    <div class="chart-info-panel" id="chart-info-2">
      <div class="chart-info-title">Analyse comparative</div>
      <div class="chart-info-desc">Comparaison par catégories</div>
      <span class="chart-metric">3 Segments</span>
      <span class="chart-metric">87% Précision</span>
    </div>

    <div class="chart-info-panel" id="chart-info-3">
      <div class="chart-info-title">Synthèse finale</div>
      <div class="chart-info-desc">Conclusions et recommandations</div>
      <span class="chart-metric">Analyse terminée</span>
      <span class="chart-metric">Prochaines étapes</span>
    </div>
  </div>

  <div class="scrolly__content" id="scroll-content">
    
    <div class="step is-active" data-step="0">
      <div class="step-number">1</div>
      <h3>Introduction à l'analyse des données</h3>
      <p>Bienvenue dans notre exploration interactive des données. Ce premier graphique présente une vue d'ensemble complète de notre dataset principal.</p>
      <div class="step-highlight">
        <strong>Points clés :</strong> Notre analyse porte sur les données collectées tout au long de l'année 2024, avec des insights particulièrement intéressants sur les tendances émergentes.
      </div>
      <p>Observez comment le graphique à droite établit le contexte général de notre étude. Chaque élément visualisé contribue à la compréhension globale des phénomènes que nous analysons.</p>
    </div>

    <div class="step" data-step="1">
      <div class="step-number">2</div>
      <h3>Découverte des tendances de croissance</h3>
      <p>En approfondissant notre analyse, des patterns de croissance remarquables émergent. Le graphique s'adapte maintenant pour mettre en évidence ces évolutions temporelles.</p>
      <div class="step-highlight">
        <strong>Résultat majeur :</strong> Nous observons une croissance constante de 25% sur l'ensemble des trimestres, avec des pics particulièrement marqués au T3 2024.
      </div>
      <p>Remarquez comment la visualisation transforme sa présentation pour souligner les trajectoires de croissance, rendant les tendances sous-jacentes immédiatement compréhensibles.</p>
    </div>

    <div class="step" data-step="2">
      <div class="step-number">3</div>
      <h3>Analyse comparative détaillée</h3>
      <p>Cette étape révèle les nuances de nos données à travers une analyse comparative. Le graphique adopte une nouvelle perspective pour illustrer les différences entre segments.</p>
      <div class="step-highlight">
        <strong>Découverte cruciale :</strong> Trois catégories principales expliquent 87% des variations observées, démontrant une concentration remarquable des effets.
      </div>
      <p>La visualisation comparative permet d'identifier les facteurs déterminants et de comprendre les mécanismes qui sous-tendent les patterns observés précédemment.</p>
    </div>

    <div class="step" data-step="3">
      <div class="step-number">4</div>
      <h3>Synthèse et perspectives d'avenir</h3>
      <p>Notre parcours analytique se conclut par une synthèse complète. Le graphique final intègre tous les éléments découverts pour offrir une vue holistique.</p>
      <div class="step-highlight">
        <strong>Conclusion stratégique :</strong> Les insights révélés ouvrent des perspectives prometteuses pour les décisions futures et orientent notre feuille de route analytique.
      </div>
      <p>Cette visualisation finale synthétise l'ensemble du parcours et démontre la puissance du storytelling interactif pour communiquer des insights complexes de manière engageante.</p>
    </div>

  </div>

</div>

<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="https://unpkg.com/scrollama"></script>

<script>
  var scroller = scrollama();
  var currentStep = 0;
  var isTransitioning = false;

  function updateProgressBar() {
    const steps = document.querySelectorAll('.step');
    const progress = Math.min((currentStep + 1) / steps.length * 100, 100);
    document.getElementById('progress-bar').style.width = progress + '%';
  }

  function updateNavDots(activeIndex) {
    document.querySelectorAll('.nav-dot').forEach((dot, index) => {
      dot.classList.toggle('active', index === activeIndex);
    });
  }

  // Différents graphiques pour chaque étape
  const chartUrls = [
    'https://flo.uri.sh/visualisation/19897131/embed',  // Graphique 1 - Vue d'ensemble
    'https://flo.uri.sh/visualisation/19897164/embed',  // Graphique 2 - Tendances temporelles
    'https://flo.uri.sh/visualisation/19897188/embed',  // Graphique 3 - Comparaisons
    'https://flo.uri.sh/visualisation/19897210/embed'   // Graphique 4 - Synthèse
  ];

  function changeChart(stepIndex) {
    if (isTransitioning) return;
    
    isTransitioning = true;
    const iframe = document.getElementById('flourish-iframe');
    const chartContainer = document.getElementById('chart-container');
    const transitionOverlay = document.getElementById('transition-overlay');
    
    // Démarrer la transition visuelle
    chartContainer.classList.add('chart-changing');
    transitionOverlay.classList.add('transitioning');
    
    // Masquer tous les panneaux d'info
    document.querySelectorAll('.chart-info-panel').forEach(panel => {
      panel.classList.remove('active');
    });
    
    // Changer la source de l'iframe avec un délai pour l'effet visuel
    setTimeout(() => {
      // Utiliser un graphique différent pour chaque étape
      const newUrl = chartUrls[stepIndex] || chartUrls[0];
      iframe.src = newUrl;
      
      console.log(`Changement vers l'étape ${stepIndex}, URL: ${newUrl}`);
      
      // Afficher le nouveau panneau d'info
      const newPanel = document.getElementById(`chart-info-${stepIndex}`);
      if (newPanel) {
        newPanel.classList.add('active');
      }
    }, 300);
    
    // Nettoyer les classes de transition
    setTimeout(() => {
      chartContainer.classList.remove('chart-changing');
      transitionOverlay.classList.remove('transitioning');
      isTransitioning = false;
    }, 1000);
  }

  function handleResize() {
    scroller.resize();
  }

  function handleStepEnter(response) {
    // Mettre à jour les classes actives
    d3.selectAll('.step').classed('is-active', false);
    d3.select(response.element).classed('is-active', true);

    const newStep = response.index;
    
    // Changer le graphique seulement si c'est une nouvelle étape
    if (newStep !== currentStep) {
      currentStep = newStep;
      changeChart(currentStep);
      updateProgressBar();
      updateNavDots(currentStep);
    }

    // Animation d'entrée pour l'étape
    response.element.style.transform = 'translateX(0) scale(1.02)';
    setTimeout(() => {
      response.element.style.transform = 'translateX(0) scale(1)';
    }, 200);
  }

  function handleStepExit(response) {
    // Animation de sortie subtile
    response.element.style.transform = 'translateX(-20px) scale(0.98)';
  }

  function init() {
    handleResize();
    
    scroller.setup({
      step: '.step',
      offset: 0.5,
      debug: false,
      container: '#scroll-content'
    })
    .onStepEnter(handleStepEnter)
    .onStepExit(handleStepExit);

    window.addEventListener('resize', handleResize);
    
    // Initialiser les premiers éléments
    updateProgressBar();
    updateNavDots(0);
    
    // Gestionnaire de clic pour les points de navigation
    document.querySelectorAll('.nav-dot').forEach((dot, index) => {
      dot.addEventListener('click', () => {
        const targetStep = document.querySelector(`[data-step="${index}"]`);
        if (targetStep) {
          targetStep.scrollIntoView({ 
            behavior: 'smooth', 
            block: 'center' 
          });
        }
      });
    });
  }

  // Initialisation au chargement de la page
  document.addEventListener('DOMContentLoaded', function() {
    init();
    
    // Petite animation d'entrée
    setTimeout(() => {
      document.querySelector('.step.is-active').style.animation = 'none';
    }, 1000);
  });

  // Gestion du redimensionnement pour maintenir la responsivité
  let resizeTimeout;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(handleResize, 100);
  });
</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=2500, width = 3000, scrolling=True)
