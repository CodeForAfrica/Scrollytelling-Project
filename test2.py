import streamlit as st

st.set_page_config(layout="wide")

import streamlit as st

import streamlit as st

html_code = """
<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Scrollytelling - Texte sur Graphique</title>
<style>
  html, body {
    margin: 0;
    padding: 0;
    font-family: Poppins, Arial, sans-serif;
    background: #000;
    color: #fff;
    overflow-x: hidden;
  }

  /* Container that holds everything */
  .scrolly-container {
    position: relative;
    width: 100%;
    height: 100%;
  }

  /* Fixed chart background */
  .visuals {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    z-index: 1;
    background: black;
  }
  .visuals iframe {
    width: 100%;
    height: 100%;
    border: none;
    display: block;
  }

  /* Scrolling text overlay */
  .scrolling-text {
    position: relative;
    z-index: 2;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .step {
    min-height: 100vh;
    max-width: 700px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 2rem;
    box-sizing: border-box;
    background: rgba(0,0,0,0.55); /* semi-transparent overlay */
    backdrop-filter: blur(4px);
    border-radius: 10px;
    margin-bottom: 2rem;
    transition: background 0.3s;
  }

  .step.is-active {
    background: rgba(0,0,0,0.75);
    border: 2px solid gold;
  }

  .step h3 {
    font-size: 2rem;
    margin-bottom: 1rem;
    text-align: center;
  }
  .step p {
    font-size: 1.2rem;
    line-height: 1.6;
    text-align: center;
  }
</style>
</head>
<body>

<div class="scrolly-container">
  <!-- Background chart -->
  <div class="visuals">
    <iframe id="flourish-iframe" src="https://flo.uri.sh/visualisation/24728120/embed" scrolling="no"></iframe>
  </div>

  <!-- Overlay scrolling text -->
  <div class="scrolling-text">
    <div class="step" data-src="https://flo.uri.sh/visualisation/24728120/embed">
      <h3>Exposure pollution</h3>
      <p>Exposure to PM2 varies across the continent.</p>
    </div>
    <div class="step" data-src="https://flo.uri.sh/visualisation/24838022/embed">
      <h3>Household pollution</h3>
      <p>Indoor air pollution death rates are high in the West, Central and East.</p>
    </div>
    <div class="step" data-src="https://flo.uri.sh/visualisation/24838425/embed">
      <h3>Ambient pollution</h3>
      <p>Northern and Southern Africa record the highest outdoor air pollution death rates.</p>
    </div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
  const steps = document.querySelectorAll('.step');
  const iframe = document.getElementById('flourish-iframe');

  function setStepHeights() {
    const vh = window.innerHeight;
    steps.forEach(step => step.style.minHeight = vh + 'px');
  }
  setStepHeights();
  window.addEventListener('resize', setStepHeights);

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        steps.forEach(s => s.classList.remove('is-active'));
        entry.target.classList.add('is-active');
        const newSrc = entry.target.dataset.src;
        if (iframe.src !== newSrc) {
          iframe.src = newSrc;
        }
      }
    });
  }, { threshold: 0.5 });

  steps.forEach(step => observer.observe(step));
});
</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=1200, scrolling=True)
