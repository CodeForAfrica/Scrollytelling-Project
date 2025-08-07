import streamlit as st

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Scroll-driven Flourish Story</title>

<style>
  html, body {
    margin: 0; padding: 0;
    height: 100%;
    font-family: 'Poppins', sans-serif;
  }

  body {
    overflow-y: scroll;
    scroll-behavior: smooth;
  }

  header {
    background-color: #104E8B;
    color: white;
    padding: 2rem 1rem;
    text-align: center;
    box-shadow: 0 4px 8px rgba(16, 78, 139, 0.3);
  }
  header h1 {
    margin: 0 0 0.5rem 0;
    font-family: 'Lora', serif;
    font-weight: 700;
    font-size: 2.5rem;
  }
  header h2 {
    margin: 0 0 1rem 0;
    font-weight: 400;
    font-style: italic;
  }
  header p {
    margin: 0 auto;
    max-width: 600px;
    font-style: italic;
  }

  .container {
    display: flex;
    max-width: 1200px;
    margin: 2rem auto;
    padding: 0 1rem;
    gap: 2rem;
  }

  .text-container {
    flex: 1 1 40%;
    max-width: 480px;
  }

  .step {
    margin-bottom: 3rem;
    padding: 1.5rem;
    border: 2px solid #104E8B;
    border-radius: 6px;
    background: rgba(255 255 255 / 0.85);
    min-height: 70vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
  }

  .step.is-active {
    border-color: goldenrod;
    color: #3b3b3b;
    background: transparent !important;
  }

  .chart-container {
    flex: 1 1 60%;
    position: fixed;
    top: 0;
    right: 0;
    width: 60vw;
    height: 100vh;
    box-shadow: -5px 0 15px rgba(0,0,0,0.1);
    background: white;
  }

  iframe {
    width: 100%;
    height: 100%;
    border: none;
  }

  /* Responsive */
  @media (max-width: 768px) {
    .container {
      flex-direction: column;
      max-width: 100%;
    }
    .chart-container {
      position: relative;
      width: 100%;
      height: 50vh;
      box-shadow: none;
      margin-bottom: 2rem;
    }
    .text-container {
      max-width: 100%;
    }
  }
</style>
</head>
<body>

<header>
  <h1>Data Scrollytelling</h1>
  <h2>Interactive analysis with Scrollama and Flourish</h2>
  <p>Discover how text and graphics interact harmoniously to tell your story.</p>
</header>

<div class="container">
  <div class="text-container" id="scroll-container">
    <div class="step is-active" data-step="0">
      <h3>Step 1 Title</h3>
      <p>In 2019, 99% of the world’s population was living in places where the WHO air quality guidelines levels were not met. Women and children bear the greatest health burden, with air pollution being one of the greatest environmental risks to child health.</p>
    </div>
    <div class="step" data-step="1">
      <h3>Step 2 Title</h3>
      <p>Aliquam erat volutpat. Nullam id dolor id nibh ultricies vehicula ut id elit.</p>
    </div>
    <div class="step" data-step="2">
      <h3>Step 3 Title</h3>
      <p>Donec ullamcorper nulla non metus auctor fringilla.</p>
    </div>
    <div class="step" data-step="3">
      <h3>Step 4 Title</h3>
      <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
    </div>
  </div>

  <div class="chart-container">
    <iframe id="flourish-iframe" src="https://flo.uri.sh/story/872914/embed#slide-0" scrolling="no"></iframe>
  </div>
</div>

<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="https://unpkg.com/scrollama"></script>
<script>
  // Initialize scrollama
  var scroller = scrollama();

  function handleStepEnter(response) {
    // Remove active class from all steps
    d3.selectAll('.step').classed('is-active', false);
    // Add active class to current step
    d3.select(response.element).classed('is-active', true);

    // Change iframe src to correct slide
    var slideIndex = response.index;
    var iframe = document.getElementById('flourish-iframe');
    // Reset src to trigger reload reliably
    iframe.src = '';
    setTimeout(() => {
      iframe.src = 'https://flo.uri.sh/story/872914/embed#slide-' + slideIndex;
    }, 50);
  }

  function init() {
    scroller.setup({
      step: '.step',
      offset: 0.7,
      debug: false,
      // Use window scroll, so no container needed
      // container: '#scroll-container'  // <-- removed, use window scroll
    })
    .onStepEnter(handleStepEnter);

    window.addEventListener('resize', scroller.resize);
  }

  init();
</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=2000, scrolling=True)
