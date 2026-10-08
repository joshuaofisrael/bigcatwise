/* Range Roundup: original code and art (c) 2026 Joshua Israel Ventures LLC. */
(function () {
  "use strict";
  var B = window.BCW, root = document.getElementById("rr");
  if (!B || !root) return;
  var BEST = "bcwRangeRoundupBest";
  /* Every answer and fact restates habitats.html and which-big-cat-is-it.html on BigCatWise
     (IUCN SSC Cat Specialist Group sourced). Wild populations only. */
  var CARDS = [
    { id: "africa", name: "Africa", icon: "sun", ans: ["lion", "leopard", "cheetah"],
      fact: "Africa has three big cats: the lion, leopard and cheetah. In much of eastern and southern Africa all three live side by side." },
    { id: "americas", name: "The Americas", icon: "river", ans: ["jaguar"],
      fact: "The jaguar is the only big cat in the Americas, living from Mexico to northern Argentina. A wild spotted big cat in the Americas is a jaguar." },
    { id: "south-asia", name: "South Asia (India, Nepal and neighbours)", icon: "forest", ans: ["tiger", "leopard", "snow", "lion"],
      fact: "South Asia has tigers, leopards, snow leopards in the mountains, and Asiatic lions, which live wild only in and around Gir forest in western India." },
    { id: "russian-far-east", name: "Russian Far East", icon: "snowtree", ans: ["tiger", "leopard"],
      fact: "Amur tigers and Amur leopards live in the snowy mixed forests of the Russian Far East and northeastern China." },
    { id: "central-asia", name: "Central Asia and the Middle East", icon: "mountain", ans: ["snow", "leopard", "cheetah"],
      fact: "Snow leopards live in the mountains here, leopards are rare, and the last wild Asiatic cheetahs survive only in Iran." },
    { id: "savanna", name: "Savanna and grassland of eastern and southern Africa", icon: "grass", ans: ["lion", "cheetah", "leopard"],
      fact: "Savanna is the classic home of lions and cheetahs, shared with leopards wherever there is cover such as riverside trees and rocky outcrops." },
    { id: "rainforest", name: "Tropical rainforest", icon: "forest", ans: ["jaguar", "leopard", "tiger"],
      fact: "Jaguars live in the Amazon, leopards in Central African rainforest, and tigers in the forests of South and Southeast Asia." },
    { id: "wetland", name: "Pantanal wetlands and Sundarbans mangroves", icon: "river", ans: ["jaguar", "tiger"],
      fact: "Jaguars thrive in the seasonally flooded Pantanal and along Amazon rivers, and tigers live in the Sundarbans mangroves of India and Bangladesh." },
    { id: "mountains", name: "High mountain slopes of Central and South Asia, 3,000 to 5,000 m", icon: "mountain", ans: ["snow"], ok: ["leopard"],
      fact: "Snow leopards typically live at 3,000 to 5,000 m on rugged slopes, cliffs and alpine meadows. Leopards have been recorded as high as 5,200 m in the Himalayas, so picking the leopard here does not cost you points." },
    { id: "desert", name: "The Sahara and the dry mountains of Arabia", icon: "sun", ans: ["cheetah", "leopard"],
      fact: "Cheetahs survive at very low densities in the Sahara, and leopards persist in the arid mountains of Arabia and southwest Asia." },
    { id: "europe", name: "Europe and Australia (wild cats only)", icon: "question", ans: [],
      fact: "Trick card! Europe, Australia and Antarctica have no wild big cats today. Nothing to round up here." }
  ];
  var ICON = {
    sun: '<circle cx="40" cy="30" r="14" fill="#ffd23f"/><path d="M8 62q32-16 64 0z" fill="#e8b45a"/>',
    river: '<path d="M8 60q20-20 34-6t30-8" stroke="#2fa7d8" stroke-width="7" fill="none" stroke-linecap="round"/><circle cx="20" cy="22" r="10" fill="#4caf50"/><circle cx="56" cy="20" r="12" fill="#3d9a40"/>',
    forest: '<path d="M14 62l12-34 12 34zM34 62l14-42 14 42z" fill="#2f9e44"/><rect x="24" y="58" width="4" height="6" fill="#7a4a1d"/><rect x="46" y="58" width="4" height="6" fill="#7a4a1d"/>',
    snowtree: '<path d="M20 62l14-40 14 40z" fill="#2f8f5b"/><path d="M27 42l7-20 7 20z" fill="#fff"/><circle cx="60" cy="20" r="3" fill="#cfe9ff"/><circle cx="12" cy="28" r="3" fill="#cfe9ff"/>',
    mountain: '<path d="M4 62l24-40 14 20 10-14 24 34z" fill="#8a8f9c"/><path d="M28 22l7 12-7-3-7 3zM52 28l5 7-5-2-5 2z" fill="#fff"/>',
    grass: '<path d="M6 62q6-22 8 0M18 62q4-26 10 0M34 62q2-20 8 0M48 62q6-24 8 0M62 62q4-18 8 0" stroke="#c79a2e" stroke-width="4" fill="none"/><circle cx="58" cy="18" r="9" fill="#ffd23f"/>',
    question: '<circle cx="40" cy="36" r="24" fill="#b9c6ff"/><text x="40" y="47" text-anchor="middle" font-size="32" font-family="Fredoka,sans-serif" fill="#2a2050">?</text>'
  };
  var el = function (id) { return root.querySelector("#" + id); };
  var board = el("rr-board"), title = el("rr-title"), icon = el("rr-icon"), pen = el("rr-pen"), tray = el("rr-tray"),
      checkBtn = el("rr-check"), nextBtn = el("rr-next"), startBtn = el("rr-start"), fact = el("rr-fact"), status = el("rr-status");
  B.initSound(el("rr-sound"));
  var best = B.getBest(BEST);
  function showBest() { el("rr-best").textContent = best === null ? "none yet" : best + " points"; }
  showBest();
  var deck = [], idx = 0, score = 0, maxScore = 0, card = null, picked = {}, checked = false;

  B.ORDER.forEach(function (sp) {
    var b = document.createElement("button");
    b.type = "button"; b.className = "cattoken"; b.dataset.sp = sp; b.setAttribute("aria-pressed", "false");
    b.innerHTML = B.face(sp, 52) + '<span>' + B.NAMES[sp] + '</span>';
    b.addEventListener("click", function () { toggle(sp, b); });
    tray.appendChild(b);
  });
  function toggle(sp, b) {
    if (checked || !card) return;
    picked[sp] = !picked[sp];
    b.setAttribute("aria-pressed", picked[sp] ? "true" : "false");
    b.classList.toggle("in", !!picked[sp]);
    B.beep(picked[sp] ? 600 : 420, 60);
    var n = Object.keys(picked).filter(function (k) { return picked[k]; });
    pen.textContent = n.length ? "In the round up: " + n.map(function (k) { return B.NAMES[k]; }).join(", ") : "Tap the big cats that live here wild. Tap again to remove. None? Just press Check.";
  }
  function start() {
    var trick = CARDS.filter(function (c) { return c.id === "europe"; });
    deck = B.shuffle(CARDS.filter(function (c) { return c.id !== "europe"; })).slice(0, 7).concat(trick);
    deck = B.shuffle(deck); idx = 0; score = 0; maxScore = 0;
    board.hidden = false; startBtn.hidden = true; show();
  }
  function show() {
    if (idx >= deck.length) return finish();
    card = deck[idx]; idx++; picked = {}; checked = false;
    title.textContent = card.name;
    icon.innerHTML = '<svg viewBox="0 0 80 66" width="96" height="80" aria-hidden="true">' + ICON[card.icon] + '</svg>';
    [].forEach.call(tray.children, function (b) { b.disabled = false; b.classList.remove("in", "right", "wrong", "missed"); b.setAttribute("aria-pressed", "false"); });
    pen.textContent = "Tap the big cats that live here wild. Tap again to remove. None? Just press Check.";
    fact.hidden = true; nextBtn.hidden = true; checkBtn.hidden = false; checkBtn.disabled = false;
    status.textContent = "Card " + idx + " of " + deck.length + ": " + card.name + ". Score: " + score + ".";
  }
  function check() {
    if (checked || !card) return;
    checked = true;
    var right = 0, wrong = 0, missed = 0;
    [].forEach.call(tray.children, function (b) {
      var sp = b.dataset.sp, should = card.ans.indexOf(sp) >= 0, did = !!picked[sp];
      b.disabled = true;
      if (did && should) { right++; b.classList.add("right"); }
      else if (did && !should && (card.ok || []).indexOf(sp) >= 0) { b.classList.add("right"); }
      else if (did && !should) { wrong++; b.classList.add("wrong"); }
      else if (!did && should) { missed++; b.classList.add("missed"); }
    });
    var perfect = wrong === 0 && missed === 0, pts = Math.max(0, right - wrong) + (perfect ? 2 : 0);
    score += pts; maxScore += card.ans.length + 2;
    if (perfect) B.good(); else B.bad();
    var names = card.ans.length ? card.ans.map(function (k) { return B.NAMES[k]; }).join(", ") : "none";
    fact.innerHTML = '<p class="verdict">' + (perfect ? "Perfect round up! +" + pts : "+" + pts + ". The answer: " + names + ".") + '</p><p>' + card.fact + '</p>';
    fact.hidden = false; checkBtn.hidden = true;
    nextBtn.textContent = idx >= deck.length ? "See my score" : "Next card"; nextBtn.hidden = false; nextBtn.focus({ preventScroll: true });
    status.textContent = (perfect ? "Perfect. " : "Answer: " + names + ". ") + "Score: " + score + ".";
  }
  function finish() {
    var m = score + " of " + maxScore + " points.";
    if (best === null || score > best) { best = score; B.setBest(BEST, best); m += " New best score!"; }
    showBest(); card = null;
    title.textContent = "Round up complete!"; icon.innerHTML = ""; pen.textContent = m;
    [].forEach.call(tray.children, function (b) { b.disabled = true; b.classList.remove("in", "right", "wrong", "missed"); });
    fact.hidden = true; nextBtn.hidden = true; checkBtn.hidden = true;
    status.textContent = "Game over. " + m;
    startBtn.textContent = "Play again"; startBtn.hidden = false; startBtn.focus({ preventScroll: true });
  }
  startBtn.addEventListener("click", start);
  checkBtn.addEventListener("click", check);
  nextBtn.addEventListener("click", show);
  document.addEventListener("keydown", function (e) {
    if (board.hidden || !card || checked || e.altKey || e.ctrlKey || e.metaKey) return;
    var n = parseInt(e.key, 10);
    if (n >= 1 && n <= 6) { e.preventDefault(); toggle(B.ORDER[n - 1], tray.children[n - 1]); }
  });
})();
