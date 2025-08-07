import streamlit as st

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Scrollytelling with Scrollama & Flourish</title>
<style>
  body {
    margin: 0; padding: 0;
    font-family: 'Poppins', sans-serif;
    overflow-x: hidden;
    background: #fff;
  }
  #container {
    display: flex;
    max-width: 900px;
    margin: 1rem auto;
    height: 90vh;
  }
  /* Texte à gauche avec scroll indépendant */
  #scroll-content {
    flex: 0 0 40vw;
    overflow-y: auto;
    padding: 1rem 2rem;
    box-sizing: border-box;
    border-right: 2px solid #104E8B;
    position: relative;
    z-index: 10; /* texte au-dessus */
  }
  .step {
    margin-bottom: 2rem;
    padding: 1rem;
    min-height: 70vh;
    background: rgba(255 255 255 / 0.85);
    border: 2px solid #104E8B;
    border-radius: 6px;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    justify-content: center;
    transition: background-color 0.3s, color 0.3s, border-color 0.3s;
  }
  .step.is-active {
    border-color: goldenrod;
    background: transparent;
    color: #3b3b3b;
  }
  /* Graphique à droite, fixe */
  #chart-container {
    position: fixed;
    right: 0;
    top: 0;
    width: 55vw;
    height: 100vh;
    box-shadow: -5px 0 15px rgba(0,0,0,0.1);
    background: white;
    z-index: 5; /* en dessous du texte */
  }
  #flourish-iframe {
    width: 100%;
    height: 100%;
    border: none;
  }
  /* Responsive */
  @media (max-width: 768px) {
    #container {
      flex-direction: column;
      height: auto;
    }
    #scroll-content {
      flex: none;
      width: 100vw;
      height: 50vh;
      border-right: none;
      border-bottom: 2px solid #104E8B;
    }
    #chart-container {
      position: relative;
      width: 100vw;
      height: 50vh;
      box-shadow: none;
    }
    .step {
      min-height: auto;
    }
  }
</style>
</head>
<body>

<div id="container">
  <div id="scroll-content">
    <div class="step is-active" data-step="0">
      <h2>Step 1 Title</h2>
      <p>In 2019, 99% of the world’s population was living in places where the WHO air quality guidelines levels were not met. Women and children bear the greatest health burden.</p>
    </div>
    <div class="step" data-step="1">
      <h2>Step 2 Title</h2>
      <p>Aliquam erat volutpat. Nullam id dolor id nibh ultricies vehicula ut id elit.</p>
    </div>
    <div class="step" data-step="2">
      <h2>Step 3 Title</h2>
      <p>Donec ullamcorper nulla non metus auctor fringilla.</p>
    </div>
    <div class="step" data-step="3">
      <h2>Step 4 Title</h2>
      <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
    </div>
  </div>

  <div id="chart-container">
    <iframe id="flourish-iframe" src="https://flo.uri.sh/story/872914/embed#slide-0" scrolling="no"></iframe>
  </div>
</div>

<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="https://unpkg.com/scrollama"></script>
<script>
  var scroller = scrollama();

  function handleStepEnter(response) {
    // Enlever la classe active sur tous
    document.querySelectorAll('.step').forEach(step => step.classList.remove('is-active'));
    // Ajouter la classe active à celui qui entre
    response.element.classList.add('is-active');

    // Changer la slide Flourish selon l’étape
    var slideNum = response.index;
    var iframe = document.getElementById('flourish-iframe');
    iframe.src = 'https://flo.uri.sh/story/872914/embed#slide-' + slideNum;
  }

  function init() {
    scroller.setup({
      step: '.step',
      offset: 0.7,
      container: '#scroll-content', // Très important, on dit à Scrollama d’écouter ce div scrollable
      debug: false,
    })
    .onStepEnter(handleStepEnter);

    window.addEventListener('resize', scroller.resize);
  }

  init();
</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=900, width=1000, scrolling=False)
