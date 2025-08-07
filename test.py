import streamlit as st

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Scroll-driven Flourish Story</title>
<style>
  body {
    margin: 0; padding: 0;
    font-family: 'Poppins', sans-serif;
    overflow-x: hidden;
  }
  .header {
    position: fixed;
    top: 0; left: 0;
    width: 100%;
    background: #104E8B;
    color: white;
    padding: 1rem 0;
    text-align: center;
    z-index: 10;
  }
  #container {
    display: flex;
    max-width: 900px;
    margin: 100px auto 50px; /* leave space for header fixed */
  }
  .content {
    width: 40vw;
    padding-right: 2rem;
  }
  .step {
    border: 2px solid #104E8B;
    border-radius: 6px;
    padding: 1rem;
    margin-bottom: 2rem;
    min-height: 70vh;
    background: rgba(255 255 255 / 0.85);
    cursor: pointer;
    transition: all 0.3s;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .step.is-active {
    border-color: goldenrod;
    background: transparent;
    color: #3b3b3b;
  }
  .chart {
    position: fixed;
    right: 0;
    top: 0;
    width: 55vw;
    height: 100vh;
    box-shadow: -5px 0 15px rgba(0,0,0,0.1);
    background: white;
    z-index: 5;
  }
  iframe {
    width: 100%;
    height: 100%;
    border: none;
  }
  @media (max-width: 768px) {
    #container {
      flex-direction: column;
      margin: 150px 1rem 50px;
    }
    .content {
      width: 100%;
      padding: 0;
    }
    .chart {
      position: relative;
      width: 100%;
      height: 300px;
      box-shadow: none;
      margin-bottom: 2rem;
    }
    .step {
      min-height: auto;
    }
  }
</style>
</head>
<body>

<header class="header">
  <h1>Data Scrollytelling</h1>
  <h3>Interactive analysis with Scrollama and Flourish</h3>
</header>

<div id="container">
  <div class="content" id="scrolly-content">
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
  <div class="chart">
    <iframe id="flourish-iframe" src="https://flo.uri.sh/story/872914/embed#slide-0" scrolling="no"></iframe>
  </div>
</div>

<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="https://unpkg.com/scrollama"></script>
<script>
  var scroller = scrollama();

  function handleStepEnter(response) {
    // Set active class on current step
    document.querySelectorAll('.step').forEach(s => s.classList.remove('is-active'));
    response.element.classList.add('is-active');

    // Change Flourish slide
    var slideNum = response.index;
    var iframe = document.getElementById('flourish-iframe');
    iframe.src = 'https://flo.uri.sh/story/872914/embed#slide-' + slideNum;
  }

  function init() {
    scroller.setup({
      step: '.step',
      offset: 0.7,
      debug: false
    })
    .onStepEnter(handleStepEnter);

    window.addEventListener('resize', scroller.resize);
  }

  init();
</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=1200, width=1000, scrolling=True)
