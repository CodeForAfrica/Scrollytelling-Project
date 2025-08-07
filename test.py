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
  <title>Scroll-driven Flourish Story - Text over Chart</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" crossorigin="anonymous" />

  <style>
    body {
      font-family: 'Poppins', sans-serif;
      margin: 0; padding: 0;
      background: #fff;
      color: #1d1d1d;
      overflow-x: hidden;
    }

    #scrolly__section {
      position: relative;
      max-width: 900px;
      margin: 0 auto;
      height: 100vh;
    }

    .scrolly__chart {
      position: fixed;
      top: 0;
      right: 0;
      width: 60vw;
      height: 100vh;
      z-index: 1;
      background: #fff;
      box-shadow: -5px 0 15px rgba(0,0,0,0.1);
    }

    iframe {
      width: 100%;
      height: 100%;
      border: none;
      transition: opacity 0.5s ease-in-out;
    }

    /* Indicateur de changement de graphique */
    .chart-loading {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background: rgba(16, 78, 139, 0.9);
      color: white;
      padding: 1rem 2rem;
      border-radius: 25px;
      font-weight: 600;
      z-index: 10;
      opacity: 0;
      transition: opacity 0.3s ease;
    }

    .chart-loading.show {
      opacity: 1;
    }

    .scrolly__content {
      position: relative;
      width: 100%;
      max-width: 40vw;
      margin-left: 2rem;
      padding-top: 2rem;
      z-index: 2;
      overflow-y: auto;
      height: 100vh;
    }

    .step {
      margin-bottom: 3rem;
      padding: 1rem;
      border: 2px solid #104E8B;
      background: rgba(255 255 255 / 0.85);
      cursor: pointer;
      transition: background-color 0.3s, color 0.3s, transform 0.3s;
      min-height: 70vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      box-sizing: border-box;
      border-radius: 6px;
      backdrop-filter: saturate(180%) blur(10px);
    }

    .step.is-active {
      background-color: goldenrod;
      color: #3b3b3b;
      border-color: goldenrod;
      transform: scale(1.02);
    }

    /* Scrollbar styling for content */
    .scrolly__content::-webkit-scrollbar {
      width: 8px;
    }
    .scrolly__content::-webkit-scrollbar-thumb {
      background-color: rgba(16,78,139,0.5);
      border-radius: 4px;
    }
    .scrolly__content::-webkit-scrollbar-track {
      background: transparent;
    }

    /* Responsive */
    @media (max-width: 768px) {
      .scrolly__chart {
        position: relative;
        width: 100vw;
        height: 50vh;
        box-shadow: none;
      }
      .scrolly__content {
        max-width: 100vw;
        margin-left: 0;
        height: auto;
        overflow-y: visible;
        padding: 1rem;
      }
      .step {
        min-height: auto;
      }
    }

    /* Animation pour indiquer le changement de graphique */
    @keyframes chartPulse {
      0% { transform: scale(1); }
      50% { transform: scale(0.98); }
      100% { transform: scale(1); }
    }

    .chart-changing {
      animation: chartPulse 0.6s ease-in-out;
    }
  </style>
</head>
<body>

<div id="scrolly__section">

  <div class="scrolly__chart">
    <div class="chart-loading" id="chart-loading">Chargement du graphique...</div>
    <iframe id="flourish-iframe" src="https://flo.uri.sh/visualisation/19897131/embed" scrolling="no"></iframe>
  </div>

  <div class="scrolly__content" id="scroll-content">
    <div class="step is-active" data-step="0">
      <h3>Vue d'ensemble des données</h3>
      <p>Bienvenue dans notre exploration des données. Ce premier graphique présente une vue d'ensemble complète de notre analyse, établissant le contexte pour notre histoire basée sur les données.</p>
    </div>
    <div class="step" data-step="1">
      <h3>Tendances temporelles</h3>
      <p>Observez maintenant l'évolution temporelle des données. Ce graphique révèle les patterns et tendances qui se sont développés au fil du temps, montrant les dynamiques importantes de notre étude.</p>
    </div>
    <div class="step" data-step="2">
      <h3>Analyse comparative</h3>
      <p>Cette visualisation compare différents segments de nos données. Elle met en évidence les contrastes et similitudes entre les catégories, révélant des insights cruciaux pour notre compréhension globale.</p>
    </div>
    <div class="step" data-step="3">
      <h3>Synthèse et conclusions</h3>
      <p>Notre parcours se termine par une synthèse complète. Ce graphique final intègre tous les éléments précédents pour offrir une vision holistique des conclusions de notre analyse des données.</p>
    </div>
  </div>

</div>

<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="https://unpkg.com/scrollama"></script>

<script>
  var scroller = scrollama();
  var currentStep = -1; // Initialiser à -1 pour forcer le premier changement

  // Différents graphiques pour chaque étape
  const chartUrls = [
    'https://flo.uri.sh/visualisation/19897131/embed',  // Graphique 1 - Vue d'ensemble
    'https://flo.uri.sh/visualisation/19897164/embed',  // Graphique 2 - Tendances temporelles
    'https://flo.uri.sh/visualisation/19897188/embed',  // Graphique 3 - Comparaisons
    'https://flo.uri.sh/visualisation/19897210/embed'   // Graphique 4 - Synthèse
  ];

  function handleResize() {
    // on mobile, let steps have auto height
    var isMobile = window.matchMedia("(max-width: 768px)").matches;
    d3.selectAll('.step')
      .style('min-height', isMobile ? null : window.innerHeight * 0.7 + 'px');
    scroller.resize();
  }

  function changeChart(slideNum) {
    const iframe = document.getElementById('flourish-iframe');
    const chartContainer = document.querySelector('.scrolly__chart');
    const loadingIndicator = document.getElementById('chart-loading');
    
    // Afficher l'indicateur de chargement
    loadingIndicator.classList.add('show');
    
    // Animation sur le conteneur
    chartContainer.classList.add('chart-changing');
    
    // Changer l'URL du graphique
    const newUrl = chartUrls[slideNum] || chartUrls[0];
    
    setTimeout(() => {
      iframe.src = newUrl;
      console.log(`Changement vers l'étape ${slideNum}, URL: ${newUrl}`);
    }, 300);
    
    // Masquer l'indicateur après le chargement
    setTimeout(() => {
      loadingIndicator.classList.remove('show');
      chartContainer.classList.remove('chart-changing');
    }, 1500);
  }

  function handleStepEnter(response) {
    d3.selectAll('.step').classed('is-active', false);
    d3.select(response.element).classed('is-active', true);

    var slideNum = response.index;
    
    // Changer le graphique seulement si c'est une nouvelle étape
    if (slideNum !== currentStep) {
      currentStep = slideNum;
      changeChart(slideNum);
    }
  }

  function init() {
    handleResize();
    scroller.setup({
      step: '.step',
      offset: 0.7,
      debug: false,
      container: '#scroll-content'  // important: limit scrollama to the scroll container
    })
    .onStepEnter(handleStepEnter);

    window.addEventListener('resize', handleResize);
  }

  init();
</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=2500, width=3000, scrolling=True)
