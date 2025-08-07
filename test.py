import streamlit as st

html_code = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Scroll Story with Flourish</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Lora:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Poppins', sans-serif;
      color: #1d1d1d;
      margin: 0;
      padding: 0;
    }

    .wrapper {
      padding: 96px 0;
    }

    #scrolly__section {
      display: flex;
      padding: 2rem;
    }

    .scrolly__content {
      flex: 1;
      padding-right: 2rem;
    }

    .scrolly__chart {
      flex: 1;
      position: sticky;
      top: 20px;
      height: 80vh;
    }

    .scrolly__chart iframe {
      width: 100%;
      height: 100%;
      border: none;
    }

    .step {
      margin-bottom: 50vh;
      padding: 2rem;
      border-left: 4px solid #104E8B;
      background-color: rgba(255, 255, 255, 0.6);
    }

    .step.is-active {
      background-color: #FFE97F;
    }

    h1.title {
      width: 100%;
      text-align: center;
      font-size: 3rem;
      font-weight: 700;
      margin-bottom: 4rem;
      padding: 2rem;
      background-color: #104E8B;
      color: white;
    }
  </style>
</head>
<body>
  <div class="wrapper">
    <h1 class="title">Scroll Story with Flourish</h1>

    <div class="container-fluid" id="scrolly__section">
      <div class="scrolly__content">
        <div class="step" data-step="0">
          <p>Here is some engaging introduction to the first visualization.</p>
        </div>
        <div class="step" data-step="1">
          <p>This step explains the second part of the story.</p>
        </div>
        <div class="step" data-step="2">
          <p>This step transitions to the next chart.</p>
        </div>
        <div class="step" data-step="3">
          <p>We’re reaching the final insights here.</p>
        </div>
      </div>

      <div class="scrolly__chart">
        <iframe id="flourish-iframe" src="https://flo.uri.sh/story/872914/embed#slide-0" title="Flourish Story"></iframe>
      </div>
    </div>
  </div>

  <script src="https://d3js.org/d3.v5.min.js"></script>
  <script src="https://unpkg.com/intersection-observer"></script>
  <script src="https://unpkg.com/scrollama"></script>
  <script>
    const scroller = scrollama();

    function handleResize() {
      const stepH = Math.floor(window.innerHeight * 0.75);
      d3.selectAll(".step").style("height", stepH + "px");
      scroller.resize();
    }

    function handleStepEnter(response) {
      d3.selectAll(".step").classed("is-active", (d, i) => i === response.index);
      const slide = response.index;
      const linkHead = 'https://flo.uri.sh/story/872914/embed#slide-';
      document.getElementById('flourish-iframe').src = linkHead + slide;
    }

    function init() {
      handleResize();
      scroller
        .setup({
          step: ".step",
          offset: 0.5,
          debug: false
        })
        .onStepEnter(handleStepEnter);

      window.addEventListener("resize", handleResize);
    }

    init();
  </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=2500, width = 2500, scrolling=True)
