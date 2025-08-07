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

    .flourish-container {
      width: 100%;
      height: 100%;
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
      background: rgba(255, 255, 255, 0.6);
      cursor: pointer;
      transition: background-color 0.3s, color 0.3s;
      min-height: 70vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      border-radius: 6px;
      backdrop-filter: saturate(180%) blur(10px);
    }

    .step.is-active {
      background-color: goldenrod;
      color: #3b3b3b;
      border-color: goldenrod;
    }

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
  </style>
</head>
<body>

<div id="scrolly__section">

  <div class="scrolly__chart">
    <div class="flourish-container" id="flourish-container">
      <iframe id="flourish-iframe" src="https://flo.uri.sh/story/872914/embed#slide-0" frameborder="0" allowfullscreen scrolling="no"></iframe>
    </div>
  </div>

  <div class="scrolly__content" id="scroll-content">
    <div class="step is-active" data-step="0">
      <h3>Step 1 Title</h3>
      <p>Introduction to the first visualization. Text scrolls on top of the Flourish chart.</p>
    </div>
    <div class="step" data-step="1">
      <h3>Step 2 Title</h3>
      <p>This step displays a new chart or another slide.</p>
    </div>
    <div class="step" data-step="2">
      <h3>Step 3 Title</h3>
      <p>Contextual insight continues here.</p>
    </div>
    <div class="step" data-step="3">
      <h3>Step 4 Title</h3>
      <p>Final summary with another visual.</p>
    </div>
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
    var flourishContainer = document.getElementById('flourish-container');
    var newIframe = document.createElement('iframe');
    newIframe.src = 'https://flo.uri.sh/story/872914/embed#slide-' + slideNum;
    newIframe.setAttribute('frameborder', '0');
    newIframe.setAttribute('allowfullscreen', '');
    newIframe.setAttribute('scrolling', 'no');
    newIframe.style.width = '100%';
    newIframe.style.height = '100%';

    flourishContainer.innerHTML = '';
    flourishContainer.appendChild(newIframe);
  }

  function init() {
    handleResize();
    scroller.setup({
      step: '.step',
      offset: 0.7,
      debug: false,
      container: '#scroll-content'
    }).onStepEnter(handleStepEnter);

    window.addEventListener('resize', handleResize);
  }

  init();
</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=2500, width=1400, scrolling=True)
