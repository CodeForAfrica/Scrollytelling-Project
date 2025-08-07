import streamlit as st

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Scroll Story</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: 'Poppins', sans-serif;
    }
    .container {
      display: flex;
      max-width: 1200px;
      margin: 0 auto;
      padding: 2rem;
    }
    .text {
      flex: 1;
      padding-right: 2rem;
    }
    .step {
      margin-bottom: 80vh;
      padding: 2rem;
      border-left: 4px solid #104E8B;
      background-color: rgba(255, 255, 255, 0.8);
    }
    .step.is-active {
      background-color: #FFE97F;
    }
    .chart {
      flex: 1;
      position: sticky;
      top: 20px;
      height: 80vh;
    }
    .chart iframe {
      width: 100%;
      height: 100%;
      border: none;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="text">
      <div class="step" data-step="0">
        <p>Introduction to the visualization.</p>
      </div>
      <div class="step" data-step="1">
        <p>This step adds more context.</p>
      </div>
      <div class="step" data-step="2">
        <p>More insights here.</p>
      </div>
      <div class="step" data-step="3">
        <p>Final conclusions are shown now.</p>
      </div>
    </div>
    <div class="chart">
      <iframe id="flourish" src="https://flo.uri.sh/story/872914/embed#slide-0" title="Flourish Story"></iframe>
    </div>
  </div>

  <!-- Scrollama & D3 -->
  <script src="https://d3js.org/d3.v5.min.js"></script>
  <script src="https://unpkg.com/scrollama"></script>

  <script>
    const scroller = scrollama();

    function handleResize() {
      const stepHeight = Math.floor(window.innerHeight * 0.75);
      d3.selectAll(".step").style("height", stepHeight + "px");
      scroller.resize();
    }

    function handleStepEnter(response) {
      d3.selectAll(".step").classed("is-active", function (d, i) {
        return i === response.index;
      });

      const iframe = document.getElementById("flourish");
      iframe.src = "https://flo.uri.sh/story/872914/embed#slide-" + response.index;
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

    window.onload = init;
  </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=3000, scrolling=True)
