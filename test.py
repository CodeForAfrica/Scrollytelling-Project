import streamlit as st

html_code = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Data story with flourish</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" crossorigin="anonymous" />
  <link href="https://fonts.googleapis.com/css2?family=Poppins&family=Lora&display=swap" rel="stylesheet" />

  <style>
    body {
      font-family: 'Poppins', sans-serif;
      color: #1d1d1d;
    }
    .wrapper {
      padding: 96px 0;
    }
    .font-secondary {
      font-family: 'Lora', serif !important;
    }
    .text-h1 { font-size: 36px; line-height: 52px; }
    .text-h2 { font-size: 32px; line-height: 36px; font-weight: 500; }
    .text-body-1 { font-size: 20px; font-weight: 400; line-height: 32px; }
    .text-body-2 { font-size: 16px; font-weight: 400; line-height: 28px; }
    .blockquote {
      font-size: 32px; font-weight: 700; line-height: 36px;
      text-transform: uppercase; text-align: center;
    }
    .text-caption {
      font-size: 14px; line-height: 22px;
    }
    a {
      color: #104E8B !important;
      border-bottom: 2px solid #104E8B;
      text-decoration: none;
      word-break: break-word;
    }
    #scrolly__section {
      display: flex;
      padding: 1rem;
    }
    #scrolly__section > * {
      flex: 1;
    }
    .scrolly__content {
      padding: 0 1rem;
      width: 100%;
    }
    .scrolly__chart {
      position: sticky;
      top: 0;
      width: 100%;
      margin: 0;
      transform: translate3d(0,0,0);
      z-index: 0;
    }
    .scrolly__chart iframe {
      width: 100%;
      height: 500px;
      border: none;
    }
    .step {
      margin: 0 auto 2rem auto;
      border: 2px solid #104E8B;
      padding: 1rem;
      cursor: pointer;
    }
    .step.is-active {
      background-color: goldenrod;
      color: #3b3b3b;
    }
  </style>
</head>

<body>
  <div class="wrapper">
    <div class="container py-5">
      <h3 class="text-h2 font-secondary mb-3">Scrollama + Flourish embed demo</h3>
      <div class="container-fluid" id="root">
        <div class="row justify-content-center" id="scrolly__section">
          <div class="col-4 scrolly__content">
            <div class="step" data-step="1"><p>Step 1 content</p></div>
            <div class="step" data-step="2"><p>Step 2 content</p></div>
            <div class="step" data-step="3"><p>Step 3 content</p></div>
            <div class="step" data-step="4"><p>Step 4 content</p></div>
          </div>

          <div class="col-6 scrolly__chart">
            <iframe id="chart-frame" scrolling="no" src="https://flo.uri.sh/story/872914/embed#slide-0"></iframe>
          </div>
        </div>
      </div>
    </div>

  <script src="https://d3js.org/d3.v5.min.js"></script>
  <script src="https://unpkg.com/scrollama"></script>

  <script>
    const scrollySection = d3.select("#scrolly__section");
    const steps = scrollySection.selectAll(".step");
    const iframe = document.getElementById("chart-frame");
    const scroller = scrollama();

    function handleStepEnter(response) {
      // Highlight active step
      steps.classed("is-active", (d, i) => i === response.index);

      // Change iframe src based on step index (for demo purposes)
      const stepNum = response.index + 1;
      iframe.src = `https://flo.uri.sh/story/872914/embed#slide-${stepNum - 1}`;
    }

    function handleResize() {
      // Update step height to 75% of viewport height
      const stepHeight = Math.floor(window.innerHeight * 0.75);
      steps.style("height", stepHeight + "px");
    }

    function init() {
      handleResize();

      scroller
        .setup({
          container: "#root",
          graphic: ".scrolly__chart",
          text: ".scrolly__content",
          step: ".step",
          offset: 0.5,
          debug: false,
        })
        .onStepEnter(handleStepEnter);

      window.addEventListener("resize", handleResize);
    }

    init();
  </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=900, scrolling=True)
