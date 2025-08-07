import streamlit as st

html_code = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link href="https://fonts.googleapis.com/css2?family=Lora&family=Poppins:wght@400;700&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Poppins', sans-serif; margin: 0; padding: 0; overflow-x: hidden; }
    .container { position: relative; }

    .chart {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 1;
    }

    .chart iframe {
      width: 100%;
      height: 100%;
      border: none;
    }

    .text {
      position: relative;
      z-index: 2;
      width: 100%;
      max-width: 600px;
      margin: 0 auto;
      padding-top: 3rem;
    }

    .step {
      margin: 4rem 0;
      padding: 2rem;
      background: rgba(255, 255, 255, 0.9);
      border-radius: 8px;
      border: 2px solid #104E8B;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
      transition: background 0.3s;
      min-height: 80vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .step.is-active {
      background: transparent;
      border-color: goldenrod;
    }

    @media (max-width: 768px) {
      .text {
        padding: 1rem;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="chart">
      <iframe id="viz" src="https://flo.uri.sh/story/872914/embed"></iframe>
    </div>
    <div class="text" id="step-container">
      <div class="step is-active"> <h3>Step 1</h3><p>Intro text that explains the story.</p></div>
      <div class="step"> <h3>Step 2</h3><p>More data insight here.</p></div>
      <div class="step"> <h3>Step 3</h3><p>Additional explanation continues.</p></div>
      <div class="step"> <h3>Step 4</h3><p>Final conclusion or takeaway.</p></div>
    </div>
  </div>

  <script src="https://d3js.org/d3.v5.min.js"></script>
  <script src="https://unpkg.com/scrollama"></script>
  <script>
    var scroller = scrollama();
    scroller.setup({
      step: '.step',
      offset: 0.6
    }).onStepEnter(function(response) {
      d3.selectAll('.step').classed('is-active', false);
      d3.select(response.element).classed('is-active', true);

      var iframe = document.getElementById('viz');
      // Send message to Flourish iframe to change slide
      iframe.contentWindow.postMessage(
        JSON.stringify({ messageType: 'changeSlide', slide: response.index }),
        '*'
      );
    });
    window.addEventListener('resize', scroller.resize);
  </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=2500, scrolling=True)
