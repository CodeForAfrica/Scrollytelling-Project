import streamlit as st

st.set_page_config(layout="wide")

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

  /* Fullscreen fixed chart */
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

  /* Overlay scrolling text */
  .scrolling-text {
    position: relative;
    z-index: 2;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 10vh;
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
    text-align: center;
    color: white;
    transition: transform 0.3s, opacity 0.3s;
    opacity: 0.6;
  }

  .step.is-active {
    transform: scale(1.05);
    opacity: 1;
  }

  .step h3 {
    font-size: 2.2rem;
    margin-bottom: 1rem;
  }
  .step p {
    font-size: 1.3rem;
    line-height: 1.6;
  }
</style>
</head>
<body>

<div class="visuals">
    <iframe id="flourish-iframe" src="https://flo.uri.sh/visualisation/24728120/embed" scrolling="no"></iframe>
</div>

<div class="scrolling-text">
  <div class="step" data-slide="0">
    <h3>Exposure pollution</h3>
    <p>Exposure to PM2 varies across the continent.</p>
  </div>
  <div class="step" data-slide="1">
    <h3>Household pollution</h3>
    <p>Indoor air pollution death rates are high in the West, Central and East.</p>
  </div>
  <div class="step" data-slide="2">
    <h3>Ambient pollution</h3>
    <p>Northern and Southern Africa record the highest outdoor air pollution death rates.</p>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
  const steps = document.querySelectorAll('.step');
  const iframe = document.getElementById('flourish-iframe');
  const baseUrl = "https://flo.uri.sh/story/872914/embed#slide-";

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
        const slideNum = entry.target.dataset.slide;
        iframe.contentWindow.postMessage({ message: "update", slide: slideNum }, "*");
        iframe.src = baseUrl + slideNum;
      }
    });
  }, { threshold: 0.6 });

  steps.forEach(step => observer.observe(step));
});
</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=1200, scrolling=True)
