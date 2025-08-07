import streamlit as st

html_code = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Scroll-driven Flourish Story</title>
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
      max-width: 1000px;
      margin: 0 auto;
      height: 100vh;
      display: flex;
    }

    .scrolly__content {
      width: 40vw;
      height: 100vh;
      overflow-y: auto;
      z-index: 2;
      padding: 2rem;
    }

    .step {
      margin-bottom: 2rem;
      padding: 1rem;
      border: 2px solid #104E8B;
      transition: background-color 0.3s, color 0.3s;
      min-height: 70vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      background: rgba(255, 255, 255, 0.8);
      border-radius: 5px;
    }

    .step.is-active {
      background-color: transparent;
      border-color: goldenrod;
    }

    .scrolly__chart {
      position: fixed;
      right: 0;
      top: 0;
      width: 60vw;
      height: 100vh;
      z-index: 1;
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
      #scrolly__section {
        flex-direction: column;
        height: auto;
      }

      .scrolly__content {
        width: 100vw;
        height: auto;
        padding: 1rem;
        overflow-y: visible;
      }

      .scrolly__chart {
        position: relative;
        width: 100vw;
        height: 50vh;
      }
    }
  </style>
</head>
<body>

<div id="scrolly__section">
  <div class="scrolly__content" id="scroll-content">
    <div class="step is-active" data-step="0">
      <h3>Step 1 Title</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur at suscipit sapien.</p>
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
    const stepHeight = window.innerHeight * 0.7;
    d3.selectAll('.step').style('min-height', stepHeight + 'px');
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
        offset: 0.6,
        debug: false,
        container: '#scroll-content'
      })
      .onStepEnter(handleStepEnter);

    window.addEventListener('resize', handleResize);
  }

  init();
</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=1000, scrolling=True)
