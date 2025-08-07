import streamlit as st

html_code = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Scroll-driven Flourish Story - Text over Chart</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" crossorigin="anonymous" />

  <style>
    html, body {
      margin: 0;
      padding: 0;
      font-family: 'Poppins', sans-serif;
      background: #fff;
      color: #1d1d1d;
    }

    .app-header {
      background-color: #104E8B;
      color: white;
      text-align: center;
      padding: 2rem 1rem;
      position: relative;
      z-index: 1000;
      box-shadow: 0 4px 8px rgba(16, 78, 139, 0.3);
    }

    .app-header h1 {
      font-weight: 700;
      font-size: 2.5rem;
      margin-bottom: 0.5rem;
      font-family: 'Lora', serif;
    }

    .app-header h2 {
      font-weight: 400;
      font-size: 1.3rem;
      font-style: italic;
      margin-bottom: 1rem;
    }

    .app-header .intro-text {
      font-size: 1rem;
      font-style: italic;
      max-width: 600px;
      margin: 0 auto;
      line-height: 1.4;
    }

    .wrapper {
      display: flex;
      flex-direction: row;
      position: relative;
      width: 100%;
      min-height: 100vh;
    }

    .scrolly__chart {
      position: sticky;
      top: 0;
      right: 0;
      width: 60vw;
      height: 100vh;
      z-index: 1;
      background: #fff;
    }

    iframe {
      width: 100%;
      height: 100%;
      border: none;
    }

    .scrolly__content {
      width: 40vw;
      padding: 2rem;
      z-index: 2;
    }

    .step {
      margin-bottom: 3rem;
      padding: 1rem;
      border: 2px solid #104E8B;
      background: rgba(255, 255, 255, 0.85);
      cursor: pointer;
      min-height: 70vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      border-radius: 6px;
      backdrop-filter: saturate(180%) blur(10px);
      transition: 0.3s;
    }

    .step.is-active {
      background: transparent !important;
      box-shadow: none !important;
      filter: none !important;
      backdrop-filter: none !important;
      border-color: goldenrod;
      color: #3b3b3b;
    }

    /* Responsive */
    @media (max-width: 768px) {
      .wrapper {
        flex-direction: column;
      }

      .scrolly__chart {
        width: 100vw;
        height: 50vh;
        position: relative;
      }

      .scrolly__content {
        width: 100vw;
      }

      .step {
        min-height: auto;
      }
    }
  </style>
</head>
<body>

  <header class="app-header">
    <h1>Data Scrollytelling</h1>
    <h2>Interactive analysis with Scrollama and Flourish</h2>
    <p class="intro-text">Discover how text and graphics interact harmoniously to tell your story.</p>
  </header>

  <div class="wrapper">
    <div class="scrolly__content" id="scroll-content">
      <div class="step is-active" data-step="0">
        <h3>Step 1 Title</h3>
        <p>In 2019, 99% of the world’s population was living in places where the WHO air quality guidelines were not met. Women and children bear the greatest health burden, with air pollution being one of the greatest risks to child health.</p>
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

    <div class="scrolly__chart">
      <iframe id="flourish-iframe" src="https://flo.uri.sh/story/872914/embed#slide-0" scrolling="no"></iframe>
    </div>
  </div>

  <script src="https://d3js.org/d3.v5.min.js"></script>
  <script src="https://unpkg.com/scrollama"></script>

  <script>
    var scroller = scrollama();

    function handleResize() {
      var isMobile = window.matchMedia("(max-width: 768px)").matches;
      d3.selectAll('.step')
        .style('min-height', isMobile ? null : window.innerHeight * 0.7 + 'px');
      scroller.resize();
    }

    function handleStepEnter(response) {
      d3.selectAll('.step').classed('is-active', false);
      d3.select(response.element).classed('is-active', true);

      var slideNum = response.index;
      var iframe = document.getElementById('flourish-iframe');
      iframe.src = 'https://flo.uri.sh/story/872914/embed#slide-' + slideNum;
    }

    function init() {
      handleResize();
      scroller
        .setup({
          step: '.step',
          offset: 0.7,
          debug: false
        })
        .onStepEnter(handleStepEnter);

      window.addEventListener('resize', handleResize);
    }

    init();
  </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=3000, width=2500, scrolling=True)
