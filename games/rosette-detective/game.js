/* Rosette Detective: original code and art (c) 2026 Joshua Israel Ventures LLC. */
(function () {
  "use strict";
  var B = window.BCW, root = document.getElementById("rd");
  if (!B || !root) return;
  var ROUNDS = 10, BEST = "bcwRosetteBest";
  /* Fact cards: each one restates facts already published on BigCatWise
     (which-big-cat-is-it.html, compare.html, the species pages and blog posts). */
  var FACT = {
    tiger: "Stripes mean tiger, the only striped cat. Every tiger's stripe pattern is unique, and its left side differs from its right, so scientists identify wild tigers from camera trap photos.",
    lion: "A plain tawny coat with no spots on adults means lion. Adult males have a mane, both sexes have a dark tuft on the tail tip, and cubs are faintly spotted.",
    cheetah: "Solid round black spots, not rosettes, mean cheetah. The black tear marks running from each eye to the mouth are unique among big cats.",
    leopard: "Small, tightly packed rosettes that are usually empty in the middle mean leopard. Wild leopards live in Africa and Asia, never in the Americas.",
    jaguar: "Large, angular rosettes with dots inside mean jaguar. It is the only big cat in the Americas, and it has a broad, heavy head and stocky body.",
    snow: "A smoky grey to cream coat with open dark rosettes means snow leopard. Its thick tail can be up to about 1 m long, and it lives in high mountains, typically at 3,000 to 5,000 m."
  };
  var CLUE = {
    tiger: "Clue: no spots at all on this coat.", lion: "Clue: look closely. Is there any pattern?", cheetah: "Clue: are these rings, or single dots?",
    leopard: "Clue: the rings are small and mostly empty.", jaguar: "Clue: peek inside the rings.", snow: "Clue: check the colour of the coat."
  };
  function rnd(seed) { return function () { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }; }

  function coat(sp, seed) {
    var r = rnd(seed), W = 320, H = 200, k = "#231a12", s = [];
    var base = { tiger: "#ef8a2b", lion: "#d3a35e", cheetah: "#eec26a", leopard: "#ecb95a", jaguar: "#e3a447", snow: "#d9d5cc" }[sp];
    s.push('<rect width="' + W + '" height="' + H + '" fill="' + base + '"/>');
    for (var f = 0; f < 70; f++) { var fx = r() * W, fy = r() * H; s.push('<path d="M' + fx.toFixed(1) + ' ' + fy.toFixed(1) + 'q3 5 1 10" stroke="rgba(255,255,255,.18)" stroke-width="1.4" fill="none"/>'); }
    if (sp === "tiger") {
      for (var x = -10; x < W + 20; x += 26 + r() * 12) {
        var w = 5 + r() * 6, y0 = r() * 30 - 10, len = 90 + r() * 110, bend = r() * 24 - 12;
        s.push('<path d="M' + x.toFixed(1) + ' ' + y0.toFixed(1) + ' q' + bend.toFixed(1) + ' ' + (len / 2).toFixed(1) + ' ' + (bend / 2).toFixed(1) + ' ' + len.toFixed(1) + '" stroke="' + k + '" stroke-width="' + w.toFixed(1) + '" fill="none" stroke-linecap="round"/>');
        if (r() > .5) s.push('<path d="M' + (x + 12).toFixed(1) + ' ' + (H - 10).toFixed(1) + ' q' + (-bend).toFixed(1) + ' -40 0 -' + (40 + r() * 50).toFixed(1) + '" stroke="' + k + '" stroke-width="' + (w * .8).toFixed(1) + '" fill="none" stroke-linecap="round"/>');
      }
    } else if (sp === "cheetah") {
      for (var i = 0; i < 95; i++) s.push('<circle cx="' + (r() * W).toFixed(1) + '" cy="' + (r() * H).toFixed(1) + '" r="' + (3.2 + r() * 2.2).toFixed(1) + '" fill="' + k + '"/>');
    } else if (sp === "lion") {
      for (var j = 0; j < 40; j++) s.push('<path d="M' + (r() * W).toFixed(1) + ' ' + (r() * H).toFixed(1) + 'q4 6 2 12" stroke="rgba(120,80,35,.25)" stroke-width="2" fill="none"/>');
    } else {
      var big = sp === "jaguar" ? 15 : sp === "snow" ? 15 : 9, step = big * 2.6;
      for (var gy = 0; gy < H + step; gy += step) for (var gx = (gy / step) % 2 ? step / 2 : 0; gx < W + step; gx += step) {
        var cx = gx + (r() - .5) * step * .4, cy = gy + (r() - .5) * step * .4, rr = big * (.8 + r() * .35), segs = 4 + Math.floor(r() * 3);
        var col = sp === "snow" ? "#4d4840" : k;
        if (sp === "jaguar" || sp === "leopard") s.push('<circle cx="' + cx.toFixed(1) + '" cy="' + cy.toFixed(1) + '" r="' + (rr * .7).toFixed(1) + '" fill="rgba(160,95,25,.28)"/>');
        for (var q = 0; q < segs; q++) {
          var a0 = q / segs * 6.283 + r() * .3, a1 = a0 + 6.283 / segs * (.55 + r() * .2);
          var x0 = cx + rr * Math.cos(a0), y0b = cy + rr * Math.sin(a0), x1 = cx + rr * Math.cos(a1), y1 = cy + rr * Math.sin(a1);
          s.push('<path d="M' + x0.toFixed(1) + ' ' + y0b.toFixed(1) + ' A' + rr.toFixed(1) + ' ' + rr.toFixed(1) + ' 0 0 1 ' + x1.toFixed(1) + ' ' + y1.toFixed(1) + '" stroke="' + col + '" stroke-width="' + (sp === "leopard" ? 3.6 : 4.4) + '" fill="none" stroke-linecap="round"/>');
        }
        if (sp === "jaguar") { var n = 1 + Math.floor(r() * 2); for (var d = 0; d < n; d++) s.push('<circle cx="' + (cx + (r() - .5) * rr * .7).toFixed(1) + '" cy="' + (cy + (r() - .5) * rr * .7).toFixed(1) + '" r="2.6" fill="' + k + '"/>'); }
      }
    }
    return '<svg viewBox="0 0 ' + W + ' ' + H + '" width="100%" role="img" aria-label="A close up of a big cat coat pattern"><title>Mystery coat pattern</title>' + s.join("") + '</svg>';
  }

  var el = function (id) { return root.querySelector("#" + id); };
  var board = el("rd-board"), coatBox = el("rd-coat"), choices = el("rd-choices"), fact = el("rd-fact"),
      status = el("rd-status"), startBtn = el("rd-start"), clueBtn = el("rd-clue"), clueTxt = el("rd-cluetext"), nextBtn = el("rd-next");
  B.initSound(el("rd-sound"));
  var deck = [], round = 0, score = 0, current = null, answered = false, clueUsed = false;
  var best = B.getBest(BEST);
  function showBest() { el("rd-best").textContent = best === null ? "none yet" : best + " points"; }
  showBest();

  B.ORDER.forEach(function (sp, i) {
    var b = document.createElement("button");
    b.type = "button"; b.className = "choice"; b.dataset.sp = sp;
    b.innerHTML = '<span class="key">' + (i + 1) + '</span> ' + B.NAMES[sp];
    b.addEventListener("click", function () { answer(sp); });
    choices.appendChild(b);
  });

  function start() {
    deck = []; while (deck.length < ROUNDS) deck = deck.concat(B.shuffle(B.ORDER.slice()));
    deck = deck.slice(0, ROUNDS); round = 0; score = 0;
    board.hidden = false; startBtn.hidden = true; next();
  }
  function next() {
    if (round >= ROUNDS) return finish();
    current = deck[round]; round++; answered = false; clueUsed = false;
    coatBox.innerHTML = coat(current, 1000 + Math.floor(Math.random() * 90000));
    fact.hidden = true; nextBtn.hidden = true; clueTxt.textContent = ""; clueBtn.disabled = false;
    [].forEach.call(choices.children, function (b) { b.disabled = false; b.classList.remove("right", "wrong"); });
    status.textContent = "Coat " + round + " of " + ROUNDS + ". Score: " + score + ".";
    choices.children[0].focus({ preventScroll: true });
  }
  function answer(sp) {
    if (answered || !current) return;
    answered = true;
    var ok = sp === current, pts = ok ? (clueUsed ? 1 : 2) : 0;
    score += pts;
    [].forEach.call(choices.children, function (b) {
      b.disabled = true;
      if (b.dataset.sp === current) b.classList.add("right"); else if (b.dataset.sp === sp) b.classList.add("wrong");
    });
    if (ok) B.good(); else B.bad();
    fact.innerHTML = '<div class="factface">' + B.face(current, 72) + '</div><div><p class="verdict">' + (ok ? "Correct! +" + pts : "Not quite. It was the " + B.NAMES[current].toLowerCase() + ".") +
      '</p><p>' + FACT[current] + '</p></div>';
    fact.hidden = false; clueBtn.disabled = true;
    status.textContent = (ok ? "Correct. " : "Wrong. The answer was " + B.NAMES[current] + ". ") + "Score: " + score + ".";
    nextBtn.textContent = round >= ROUNDS ? "See my score" : "Next coat";
    nextBtn.hidden = false; nextBtn.focus({ preventScroll: true });
  }
  function finish() {
    var max = ROUNDS * 2, msg = score + " of " + max + " points.";
    if (best === null || score > best) { best = score; B.setBest(BEST, best); msg += " New best score!"; }
    showBest();
    coatBox.innerHTML = '<div class="done">' + B.ORDER.map(function (sp) { return B.face(sp, 56); }).join("") + '<p>' + msg + '</p></div>';
    [].forEach.call(choices.children, function (b) { b.disabled = true; b.classList.remove("right", "wrong"); });
    fact.hidden = true; nextBtn.hidden = true; clueBtn.disabled = true;
    status.textContent = "Game over. " + msg;
    startBtn.textContent = "Play again"; startBtn.hidden = false; startBtn.focus({ preventScroll: true });
    current = null;
  }
  startBtn.addEventListener("click", start);
  nextBtn.addEventListener("click", next);
  clueBtn.addEventListener("click", function () { if (!current || answered) return; clueUsed = true; clueTxt.textContent = CLUE[current] + " (A right answer now scores 1 point.)"; clueBtn.disabled = true; });
  document.addEventListener("keydown", function (e) {
    if (board.hidden || e.altKey || e.ctrlKey || e.metaKey) return;
    var n = parseInt(e.key, 10);
    if (n >= 1 && n <= 6 && !answered && current) { e.preventDefault(); answer(B.ORDER[n - 1]); }
  });
})();
