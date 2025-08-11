import streamlit as st

st.set_page_config(layout="wide")

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
      margin: 0;
      padding: 0;
      background: #fff;
      color: #1d1d1d;
      overflow-x: hidden;
    }

    /* Chart + text container */
    #scrolly__section {
      position: relative;
      max-width: 900px;
      margin: 0 auto;
      height: 100vh;
    }

    /* Fixed chart on the right */
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

    iframe {
      width: 100%;
      height: 100%;
      border: none;
      transition: opacity 0.3s ease-in-out;
    }

    /* Scrollable text content - HIDDEN SCROLLBAR */
    .scrolly__content {
      position: relative;
      width: 100%;
      max-width: 40vw;
      margin-left: 2rem;
      padding-top: 2rem;
      z-index: 2;
      overflow-y: auto;
      height: 100vh;
      
      /* Hide scrollbar for Chrome, Safari and Opera */
      scrollbar-width: none; /* Firefox */
      -ms-overflow-style: none; /* Internet Explorer 10+ */
    }

    /* Hide scrollbar for Chrome, Safari and Opera */
    .scrolly__content::-webkit-scrollbar {
      display: none;
    }

    /* Each text step block */
    .step {
      margin-bottom: 3rem;
      padding: 1rem;
      border: 2px solid #104E8B;
      background: rgba(255, 255, 255, 0.85);
      cursor: pointer;
      transition: all 0.4s ease-in-out;
      min-height: 70vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      box-sizing: border-box;
      border-radius: 6px;
      backdrop-filter: saturate(180%) blur(10px);
      opacity: 0.7;
      transform: translateY(20px);
    }

    /* Active step with smooth animation */
    .step.is-active {
      background-color: rgba(255, 255, 255, 0.95) !important;
      box-shadow: 0 8px 32px rgba(16, 78, 139, 0.2) !important;
      backdrop-filter: saturate(180%) blur(20px) !important;
      border-color: goldenrod;
      color: #3b3b3b;
      opacity: 1;
      transform: translateY(0);
      scale: 1.02;
    }

    /* Smooth scroll behavior */
    .scrolly__content {
      scroll-behavior: smooth;
    }

    /* Step titles and content styling */
    .step h3 {
      font-size: 1.5rem;
      font-weight: 600;
      margin-bottom: 1rem;
      color: #104E8B;
      transition: color 0.3s ease;
    }

    .step.is-active h3 {
      color: goldenrod;
    }

    .step p {
      font-size: 1rem;
      line-height: 1.6;
      margin-bottom: 0;
    }

    /* Navigation indicators */
    .scroll-indicator {
      position: fixed;
      left: 2rem;
      top: 50%;
      transform: translateY(-50%);
      z-index: 1000;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .indicator-dot {
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: rgba(16, 78, 139, 0.3);
      cursor: pointer;
      transition: all 0.3s ease;
    }

    .indicator-dot.active {
      background: goldenrod;
      transform: scale(1.3);
    }

    .indicator-dot:hover {
      background: rgba(16, 78, 139, 0.7);
    }

    /* Responsive styles for mobile */
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
        transform: none;
        opacity: 1;
      }
      .scroll-indicator {
        display: none;
      }
    }

    /* Header styling */
    .app-header {
      background-color: #104E8B;
      color: white;
      font-family: 'Poppins', sans-serif;
      text-align: center;
      padding: 2rem 0;
      margin: 0;
      width: 100vw;
      box-sizing: border-box;
      position: relative;
      z-index: 1000;
      box-shadow: 0 4px 8px rgba(16, 78, 139, 0.3);
    }

    .app-header h1 {
      font-weight: 700;
      font-size: 2.8rem;
      margin-bottom: 0.3rem;
      font-family: 'Lora', serif;
    }

    .app-header h2 {
      font-weight: 400;
      font-size: 1.4rem;
      margin-top: 0;
      margin-bottom: 1rem;
      font-style: italic;
    }

    .app-header hr {
      border: 0;
      height: 1px;
      background: white;
      width: 40%;
      margin: 0 auto 1.5rem auto;
      opacity: 0.7;
    }

    .app-header .intro-text {
      font-size: 1rem;
      font-style: italic;
      max-width: 600px;
      margin: 0 auto;
      line-height: 1.4;
    }

    /* Adds space between header and content */
    .wrapper {
      padding-top: 4rem;
    }

  </style>
</head>
<body>

  <header class="app-header">
    <div class="container">
      <h1>Data Scrollytelling</h1>
      <h2>Interactive analysis with Scrollama and Flourish</h2>
      <hr />
      <p class="intro-text">Discover how text and graphics interact harmoniously to tell your story.</p>
    </div>
  </header>

  <!-- Navigation indicators -->
  <div class="scroll-indicator" id="scroll-indicators">
    <div class="indicator-dot active" data-step="0"></div>
    <div class="indicator-dot" data-step="1"></div>
    <div class="indicator-dot" data-step="2"></div>
    <div class="indicator-dot" data-step="3"></div>
  </div>

  <div class="wrapper">
    <div id="scrolly__section">

      <div class="scrolly__chart">
        <iframe id="flourish-iframe" src="https://flo.uri.sh/story/872914/embed#slide-0" scrolling="no"></iframe>
      </div>

      <div class="scrolly__content" id="scroll-content">
        <div class="step is-active" data-step="0">
          <h3>Premature deaths</h3>
          <p>89% of premature deaths occurred in low- and middle-income countries. This visualization shows the global distribution and impact of air pollution on public health.</p>
        </div>
        <div class="step" data-step="1">
          <h3>Children deaths</h3>
          <p>Over 237,000 deaths of children under the age of 5 are attributed to air pollution annually. The most vulnerable populations suffer the greatest impact from environmental health hazards.</p>
        </div>
        <div class="step" data-step="2">
          <h3>Regional Impact</h3>
          <p>Exploring the regional variations in air quality and health outcomes. Notice how different areas show varying levels of pollution exposure and related health consequences.</p>
        </div>
        <div class="step" data-step="3">
          <h3>Call to Action</h3>
          <p>Understanding these patterns is crucial for developing targeted interventions and policies. The data reveals clear priorities for environmental health improvements worldwide.</p>
        </div>
      </div>

    </div>
  </div>

  <script src="https://d3js.org/d3.v5.min.js"></script>
  <script src="https://unpkg.com/scrollama"></script>

  <script>
    var scroller = scrollama();
    var currentSlide = 0;

    function handleResize() {
      var isMobile = window.matchMedia("(max-width: 768px)").matches;
      d3.selectAll('.step')
        .style('min-height', isMobile ? null : window.innerHeight * 0.7 + 'px');
      scroller.resize();
    }

    function updateChart(slideNum) {
      if (slideNum !== currentSlide) {
        var iframe = document.getElementById('flourish-iframe');
        
        // Add fade effect during transition
        iframe.style.opacity = '0.7';
        
        setTimeout(() => {
          iframe.src = 'https://flo.uri.sh/story/872914/embed#slide-' + slideNum;
          iframe.style.opacity = '1';
        }, 150);
        
        currentSlide = slideNum;
      }
    }

    function updateIndicators(activeIndex) {
      d3.selectAll('.indicator-dot')
        .classed('active', false);
      d3.select('.indicator-dot[data-step="' + activeIndex + '"]')
        .classed('active', true);
    }

    function handleStepEnter(response) {
      // Update active step with smooth transitions
      d3.selectAll('.step').classed('is-active', false);
      d3.select(response.element).classed('is-active', true);

      var slideNum = response.index;
      updateChart(slideNum);
      updateIndicators(slideNum);
    }

    function handleStepExit(response) {
      // Optional: handle when leaving a step
      // Could add additional animations here
    }

    function scrollToStep(stepIndex) {
      var targetStep = document.querySelector('.step[data-step="' + stepIndex + '"]');
      if (targetStep) {
        targetStep.scrollIntoView({
          behavior: 'smooth',
          block: 'center'
        });
      }
    }

    function init() {
      handleResize();
      
      // Setup scrollama
      scroller.setup({
        step: '.step',
        offset: 0.6, // Trigger when step is 60% visible
        debug: false,
        container: '#scroll-content'
      })
      .onStepEnter(handleStepEnter)
      .onStepExit(handleStepExit);

      // Add click handlers for navigation indicators
      d3.selectAll('.indicator-dot')
        .on('click', function() {
          var stepIndex = parseInt(d3.select(this).attr('data-step'));
          scrollToStep(stepIndex);
        });

      // Handle window resize
      window.addEventListener('resize', handleResize);

      // Optional: Add keyboard navigation
      document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowDown' && currentSlide < 3) {
          scrollToStep(currentSlide + 1);
        } else if (e.key === 'ArrowUp' && currentSlide > 0) {
          scrollToStep(currentSlide - 1);
        }
      });
    }

    // Initialize when DOM is loaded
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', init);
    } else {
      init();
    }
  </script>

</body>
</html>
"""

# Render the HTML in Streamlit
st.components.v1.html(html_code, height=1000, width=4000, scrolling=True)
