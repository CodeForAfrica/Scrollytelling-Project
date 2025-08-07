import streamlit as st

html_code = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Data story with flourish - Text on chart</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" crossorigin="anonymous">
  <link href="https://fonts.googleapis.com/css2?family=Poppins&family=Lora&display=swap" rel="stylesheet" />
  <style>
    body {
      font-family: 'Poppins', sans-serif;
      margin: 0; padding: 0;
      background: #fff;
      overflow-x: hidden;
    }

    #scrolly__section {
      position: relative;
      height: 90vh;
      max-width: 1200px;
      margin: auto;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .scrolly__chart {
      position: relative;
      width: 100%;
      height: 100%;
      z-index: 1;
    }

    .scrolly__chart iframe {
      width: 100%;
      height: 100%;
      border: none;
    }

    /* Texte défilant par dessus le graphique */
    .scrolly__content {
      position: fixed; /* fixe au viewport */
      top: 10vh;
      left: 50%;
      width: 45vw;
      height: 80vh;
      overflow-y: auto;
      padding: 2rem;
      background: rgba(255 255 255 / 0.85);
      box-shadow: 0 0 15px rgba(0,0,0,0.15);
      border-radius: 10px;
      z-index: 10;
      font-family: 'Lora', serif;
    }

    .step {
      margin-bottom: 2rem;
      border: 2px solid #104E8B;
      padding: 1rem 1.5rem;
      border-radius: 6px;
      background: white;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    .step.is-active {
      background-color: goldenrod;
      color: #3b3b3b;
      border-color: goldenrod;
    }

    .step p {
      margin: 0.5rem 0;
      font-size: 1rem;
      line-height: 1.5;
      text-align: left;
    }

    /* Responsive */
    @media (max-width: 768px) {
      .scrolly__content {
        position: relative;
        width: 90vw;
        height: auto;
        max-height: 50vh;
        top: auto;
        left: auto;
        padding: 1rem;
        margin: 1rem auto;
      }
      #scrolly__section {
        flex-direction: column;
        height: auto;
      }
    }
  </style>
</head>
<body>

  <div id="scrolly__section">
    <div class="scrolly__chart">
      <iframe scrolling="no" src="https://flo.uri.sh/story/872914/embed#slide-0"></iframe>
    </div>

    <div class="scrolly__content">
      <div class="step is-active" data-step="0">
        <p><strong>Lorem ipsum dolor sit amet</strong></p>
        <p>Consectetur adipisicing elit. Accusantium debitis modi labore unde commodi, dolorem ut enim, necessitatibus odit facere et pariatur minus! Aliquam rem earum tempore accusamus corporis similique.</p>
      </div>
      <div class="step" data-step="1">
        <p><strong>Step 2 Title</strong></p>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium debitis modi labore unde commodi, dolorem ut enim, necessitatibus odit facere et pariatur minus!</p>
      </div>
      <div class="step" data-step="2">
        <p><strong>Step 3 Title</strong></p>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis aut, cum reprehenderit obcaecati minima eius aperiam dolorem laboriosam ullam facere.</p>
      </div>
      <div class="step" data-step="3">
        <p><strong>Step 4 Title</strong></p>
        <p>Maecenas sed diam eget risus varius blandit sit amet non magna. Donec ullamcorper nulla non metus auctor fringilla.</p>
      </div>
    </div>
  </div>

  <script src="https://unpkg.com/d3@5.9.1/dist/d3.min.js"></script>
  <script src="https://unpkg.com/scrollama"></script>

  <script>
    const scroller = scrollama();

    function handleStepEnter(response) {
      // Gestion des classes active sur texte
      document.querySelectorAll('.step').forEach((el) => el.classList.remove('is-active'));
      response.element.classList.add('is-active');

      // Changement de slide Flourish
      const slideNum = response.index;
      const iframe = document.querySelector('.scrolly__chart iframe');
      iframe.src = `https://flo.uri.sh/story/872914/embed#slide-${slideNum}`;
    }

    function init() {
      scroller.setup({
        step: '.step',
        offset: 0.7,
        container: '.scrolly__content',  // scroll dans ce container texte
        debug: false,
      }).onStepEnter(handleStepEnter);

      window.addEventListener('resize', scroller.resize);
    }

    init();
  </script>

</body>
</html>
"""

st.components.v1.html(html_code, height=900, width=1000, scrolling=False)
