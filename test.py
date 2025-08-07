import streamlit as st

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Scroll-driven Flourish Story</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" />

  <style>
    body {
      font-family: 'Poppins', sans-serif;
      margin: 0;
      padding: 0;
      background: #fff;
      color: #1d1d1d;
      overflow: hidden;
    }

    .app-header {
      background-color: #104E8B;
      color: white;
      text-align: center;
      padding: 2rem 0;
      margin: 0;
      width: 100vw;
      box-shadow: 0 4px 8px rgba(16, 78, 139, 0.3);
    }

    .app-header h1 {
      font-weight: 700;
      font-size: 2.8rem;
      margin: 0;
    }

    .wrapper {
      display: flex;
      height: calc(100vh - 160px); /* Adjusted height for header */
      overflow: hidden;
    }

    .scrolly__chart {
      position: sticky;
      top: 0;
      width: 60vw;
      height: 100%;
      z-index: 1;
    }

    iframe {
      width: 100%;
      height: 100%;
      border: none;
    }

    .scrolly__content {
      width: 40vw;
      height: 100%;
      overflow-y: scroll;
      padding: 2rem;
      background: transparent;
      z-index: 2;
    }

    .step {
      margin-bottom: 3rem;
      padding: 1rem;
      border: 2px solid #104E8B;
      background: transparent;
      cursor: pointer;
      transition: background-color 0.3s, color 0.3s;
      min-height: 70vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      border-radius: 6px;
      color: #000;
    }

    .step.is-active {
      border-color: goldenrod;
      color: #000;
    }

    @media (max-width: 768px) {
      .wrapper {
        flex-direction: column;
        height: auto;
      }
      .scrolly__chart {
        width: 100vw;
        height: 50vh;
        position: relative;
      }
      .scrolly__content {
        width: 100vw;
        height: auto;
        overflow-y: visible;
      }
    }
  </style>
</head>
<body>

  <header class="app-header">
    <h1>Data Scrollytelling</h1>
  </header>

  <div class="wrapper">
    <div class="scrolly__content">
      <div class="step is-active" data-step="0">
        <h3>Step 1 Title</h3>
        <p>In 2019, 99% of the world’s population was living in places where the WHO air quality guidelines levels were not met. Women and children bear the greatest health burden, with air pollution being one of the greatest risks to child health.</p>
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
        .onStepEnter(handleStepEnter)
        .container(document.querySelector('.scrolly__content'));

      window.addEventListener('resize', handleResize);
    }

    init();
  </script>
</body>
</html>
"""

# In Streamlit:
st.components.v1.html(html_code, height=1000, scrolling=True)
