"""Games hub and three original browser games. Game code lives in games/*.js (hand written, not generated)."""
from build import add, BASE_URL, PUBLISHER, SITE

GL = "Games are original works &copy; 2026 Joshua Israel Ventures LLC."
GC = [("Games", "games/index.html")]

def game_ld(name, path, desc, genre, teaches):
    return [{"@context": "https://schema.org", "@type": "VideoGame", "name": name, "url": BASE_URL + path, "description": desc,
             "genre": genre, "gamePlatform": "Web browser", "applicationCategory": "Game", "operatingSystem": "Any",
             "playMode": "SinglePlayer", "inLanguage": "en", "isAccessibleForFree": True, "typicalAgeRange": "7-",
             "educationalUse": "Practice", "teaches": teaches, "author": PUBLISHER, "publisher": PUBLISHER,
             "copyrightHolder": PUBLISHER, "copyrightYear": 2026, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}]

def bar(prefix):
    return ('<div class="gamebar"><span>Best score on this device: <b id="%s-best">none yet</b></span>'
            '<button type="button" id="%s-sound" aria-pressed="false">Sound: off</button></div>') % (prefix, prefix)

PRIV = ('<p class="note">No sign up, no ads, no trackers and no personal data. Your best score is saved only in this browser '
        '(local storage) and never sent anywhere. See our <a href="{rel}privacy.html">privacy policy</a>.</p>')

CHEETAH_SVG = ('<svg viewBox="0 0 120 60" width="100%" aria-hidden="true"><path d="M8 30q-8-10 2-16" stroke="#e0a83c" stroke-width="5" fill="none" stroke-linecap="round"/>'
               '<ellipse cx="50" cy="32" rx="34" ry="13" fill="#f2c766"/><path d="M28 40l-10 16M40 42l-4 16M64 42l6 16M74 38l14 16" stroke="#e0a83c" stroke-width="6" stroke-linecap="round"/>'
               '<circle cx="90" cy="24" r="13" fill="#f2c766"/><path d="M82 13l2-8 6 6M96 12l4-7 2 9" fill="#e0a83c"/><circle cx="94" cy="22" r="2.4" fill="#231a12"/>'
               '<path d="M94 25q-1 6 3 9" stroke="#231a12" stroke-width="2" fill="none"/><circle cx="102" cy="28" r="2" fill="#231a12"/>'
               '<g fill="#231a12"><circle cx="34" cy="28" r="2.2"/><circle cx="44" cy="34" r="2.2"/><circle cx="54" cy="26" r="2.2"/><circle cx="62" cy="35" r="2.2"/><circle cx="70" cy="27" r="2.2"/><circle cx="26" cy="36" r="2"/></g></svg>')
PREY_SVG = ('<svg viewBox="0 0 80 60" width="100%" aria-hidden="true"><ellipse cx="36" cy="30" rx="22" ry="10" fill="#c98a4b"/><ellipse cx="36" cy="34" rx="18" ry="5" fill="#fff3df"/>'
            '<path d="M22 36l-6 18M30 38l-2 16M44 38l2 16M52 34l8 18" stroke="#9c6533" stroke-width="3.5" stroke-linecap="round"/>'
            '<path d="M56 24l8-10" stroke="#c98a4b" stroke-width="7" stroke-linecap="round"/><ellipse cx="68" cy="12" rx="8" ry="5" fill="#c98a4b"/>'
            '<path d="M66 8q-2-8 2-8M70 8q2-8 6-6" stroke="#3a2614" stroke-width="2" fill="none"/><circle cx="71" cy="11" r="1.5" fill="#231a12"/><path d="M14 28l-6-4" stroke="#3a2614" stroke-width="3" stroke-linecap="round"/></svg>')

# ---------------------------------------------------------------- HUB
add("games/index.html", "Big Cat Games for Kids: Free, Fun and Fact Based | BigCatWise",
    "Free big cat games that teach real facts: identify big cats by their coats, sprint like a cheetah and round up big cats by habitat. No sign up, no ads.",
    "Big cat games", kind="page", headline="Games",
    lead="Three free, original browser games that turn real big cat facts into play. They work with touch and keyboard, need no sign up, show no ads and collect no data. Every game ends with a fact card drawn from our sourced articles.",
    body='''<div class="grid">
<a class="tile hot" href="rosette-detective/"><h3>Rosette Detective</h3><p>Spots, stripes or rosettes? Name the big cat from a close up of its coat. Ten coats per game.</p></a>
<a class="tile hot" href="cheetah-burst/"><h3>Cheetah Burst</h3><p>Tap to sprint, turn when the prey swerves, and catch it before your energy runs out and before 300 m.</p></a>
<a class="tile hot" href="range-roundup/"><h3>Range Roundup</h3><p>Which big cats live wild in Africa, the Pantanal or the high Himalaya? Round them up by region and habitat.</p></a>
</div>
<section class="card"><h2>What the games teach</h2><ul>
<li><b>Rosette Detective:</b> how to tell all six big cats apart by their markings, from our <a href="{rel}which-big-cat-is-it.html">big cat ID guide</a>.</li>
<li><b>Cheetah Burst:</b> real cheetah speed research: 93 km/h top speed in wild cheetahs, short chases and why agility matters, from <a href="{rel}blog/how-fast-is-a-cheetah.html">how fast is a cheetah?</a></li>
<li><b>Range Roundup:</b> where each big cat lives today, from <a href="{rel}habitats.html">big cat habitats</a>.</li></ul></section>
<section class="card"><h2>For parents and teachers</h2><p>The games are short (two to five minutes), work on phones, tablets and computers, and have sound off by default with a mute toggle. Motion is reduced automatically if your device asks for reduced motion. Nothing is collected: best scores stay in the browser on your own device.</p>
<p>Want to use them in class? Each game page lists the facts it covers and links to the full article, so students can check every answer.</p></section>
<p class="gameline">''' + GL + '''</p>''' + PRIV,
    related=[("Which big cat is it? ID guide", "which-big-cat-is-it.html"), ("How fast is a cheetah?", "blog/how-fast-is-a-cheetah.html"), ("Big cat habitats", "habitats.html"), ("Compare big cats", "compare.html")],
    extra_ld=[{"@context": "https://schema.org", "@type": "ItemList", "name": "BigCatWise games", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": BASE_URL + "games/" + s + "/", "name": n} for i, (s, n) in enumerate(
            [("rosette-detective", "Rosette Detective"), ("cheetah-burst", "Cheetah Burst"), ("range-roundup", "Range Roundup")])]}],
    priority="0.8")

# ---------------------------------------------------------------- ROSETTE DETECTIVE
add("games/rosette-detective/index.html", "Rosette Detective: Guess the Big Cat by Its Coat | BigCatWise Games",
    "Free big cat ID game: look at a close up of a coat and decide if it is a lion, tiger, leopard, jaguar, cheetah or snow leopard. Learn a real fact every round.",
    "Rosette Detective: guess the big cat by its coat", kind="page", headline="Rosette Detective", crumbs=GC,
    lead="Spots, stripes, rosettes or plain fur? Each round shows a close up of a big cat's coat, drawn fresh by the game. Pick the species, then read a fact card that explains the giveaway.",
    body='''<div class="gamebox" id="rd">''' + bar("rd") + '''
<button type="button" class="btn" id="rd-start">Start the case</button>
<div id="rd-board" hidden>
<div class="coat" id="rd-coat"></div>
<div class="choices" id="rd-choices" role="group" aria-label="Which big cat has this coat?"></div>
<p><button type="button" class="btn alt" id="rd-clue">Need a clue?</button> <span id="rd-cluetext"></span></p>
<div class="factcard" id="rd-fact" hidden aria-live="polite"></div>
<button type="button" class="btn" id="rd-next" hidden>Next coat</button>
</div>
<p class="sr" id="rd-status" aria-live="polite"></p></div>
<section class="card"><h2>How to play</h2><ul><li>Tap a species, or press keys 1 to 6.</li><li>A right answer scores 2 points, or 1 point if you used a clue.</li><li>Ten coats per game. Your best score is kept on this device only.</li></ul></section>
<section class="card"><h2>Facts this game teaches</h2><ul>
<li>Stripes mean tiger, the only striped cat, and each tiger's stripes are unique.</li>
<li>A plain tawny adult coat means lion.</li>
<li>Solid round spots, not rosettes, mean cheetah.</li>
<li>Small rosettes that are usually empty mean leopard; larger rosettes with dots inside mean jaguar.</li>
<li>A smoky grey coat with open rosettes means snow leopard.</li></ul>
<p>Every fact comes from our <a href="{rel}which-big-cat-is-it.html">big cat ID guide</a> and <a href="{rel}blog/leopard-vs-jaguar-vs-cheetah.html">leopard vs jaguar vs cheetah</a>, which are sourced to the IUCN SSC Cat Specialist Group and leading zoos. The coats in the game are simplified drawings, not photos, so real animals vary more.</p></section>
<p class="gameline">''' + GL + '''</p>''' + PRIV + '''
<script src="{rel}games/shared.js" defer></script><script src="{rel}games/rosette-detective/game.js" defer></script>''',
    related=[("All games", "games/index.html"), ("Which big cat is it?", "which-big-cat-is-it.html"), ("Why do tigers have stripes?", "blog/why-do-tigers-have-stripes.html")],
    extra_ld=game_ld("Rosette Detective", "games/rosette-detective/", "Identify big cats from close ups of their coat patterns.", "Educational quiz",
                     "Identifying lions, tigers, leopards, jaguars, cheetahs and snow leopards by coat pattern"), priority="0.7")

# ---------------------------------------------------------------- CHEETAH BURST
add("games/cheetah-burst/index.html", "Cheetah Burst: Free Cheetah Speed Tapping Game | BigCatWise Games",
    "Tap to sprint like a cheetah, turn when the prey swerves and catch it before you run out of energy. A free speed game based on real wild cheetah research.",
    "Cheetah Burst: sprint, turn, catch", kind="page", headline="Cheetah Burst", crumbs=GC,
    lead="Wild cheetahs have been measured at 93 km/h, but they win hunts with bursts of speed, hard braking and sharp turns, and their chases are short. Tap to build speed, turn when the prey swerves, and catch it before your energy or the 300 m run out.",
    body='''<div class="gamebox" id="cb">''' + bar("cb") + '''
<div class="track" id="cb-stage"><div class="ground" id="cb-ground"></div>
<div class="runner" id="cb-cat">''' + CHEETAH_SVG + '''</div><div class="prey" id="cb-prey">''' + PREY_SVG + '''</div>
<div class="swerve" id="cb-swerve" hidden>Swerve! Turn!</div></div>
<div class="meters"><div>Speed: <span id="cb-speed">0 km/h</span></div><div>Distance: <span id="cb-dist">0 m of 300 m</span></div></div>
<div class="energy" aria-hidden="true"><span id="cb-energy"></span></div>
<p id="cb-msg">Press Start, then tap Sprint as fast as you can.</p>
<button type="button" class="btn" id="cb-start">Start the chase</button>
<div class="bigbtns"><button type="button" class="btn" id="cb-run" disabled>Sprint!</button><button type="button" class="btn alt" id="cb-turn" disabled>Turn</button></div>
<div class="factcard" id="cb-fact" hidden></div>
<p class="sr" id="cb-live" aria-live="polite"></p></div>
<section class="card"><h2>How to play</h2><ul><li>Tap <b>Sprint!</b> (or press Space or the right arrow) again and again to speed up. The top speed is capped at 93 km/h, the fastest run measured in wild cheetahs.</li>
<li>When "Swerve! Turn!" appears, tap <b>Turn</b> (or press the up arrow or T) quickly, or you overshoot and lose speed.</li>
<li>Running fast drains your energy bar. Catch the prey before it runs out, and before 300 m.</li></ul></section>
<section class="card"><h2>Facts this game teaches</h2><ul>
<li>The fastest speed measured in wild hunting cheetahs is 25.9 m/s, about 93 km/h, from GPS collars in Botswana (Wilson et al., 2013, <i>Nature</i>).</li>
<li>The average top speed of a run in that study was much lower, 14.9 m/s or about 54 km/h.</li>
<li>Successful hunts involved hard braking and sharp turns, so agility matters as much as top speed.</li>
<li>Chases seldom cover more than about 300 m (IUCN SSC Cat Specialist Group).</li>
<li>Cheetahs do not stop because they overheat (Hetem et al., 2013, <i>Biology Letters</i>).</li></ul>
<p>Read the full story in <a href="{rel}blog/how-fast-is-a-cheetah.html">how fast is a cheetah?</a> The energy bar, prey speed and swerve timing are game rules, not measurements.</p></section>
<p class="gameline">''' + GL + '''</p>''' + PRIV + '''
<script src="{rel}games/shared.js" defer></script><script src="{rel}games/cheetah-burst/game.js" defer></script>''',
    related=[("All games", "games/index.html"), ("How fast is a cheetah?", "blog/how-fast-is-a-cheetah.html"), ("Cheetah facts", "cheetah.html")],
    extra_ld=game_ld("Cheetah Burst", "games/cheetah-burst/", "Tap to sprint like a cheetah, turn with swerving prey and catch it within 300 m.", "Educational action",
                     "Cheetah top speed, short chase distances and the role of agility in hunting"), priority="0.7")

# ---------------------------------------------------------------- RANGE ROUNDUP
add("games/range-roundup/index.html", "Range Roundup: Big Cat Habitat Sorting Game | BigCatWise Games",
    "Free big cat habitat game: round up which lions, tigers, leopards, jaguars, cheetahs and snow leopards live wild in each region and habitat. Real facts every card.",
    "Range Roundup: which big cats live here?", kind="page", headline="Range Roundup", crumbs=GC,
    lead="Each card names a region or habitat. Round up every big cat that lives there in the wild, then check your answer and learn where each species really lives today.",
    body='''<div class="gamebox" id="rr">''' + bar("rr") + '''
<button type="button" class="btn" id="rr-start">Start the round up</button>
<div id="rr-board" hidden>
<div class="region"><div id="rr-icon"></div><h2 id="rr-title">Region</h2></div>
<p class="pen" id="rr-pen"></p>
<div class="tray" id="rr-tray" role="group" aria-label="Big cats to round up"></div>
<button type="button" class="btn" id="rr-check">Check</button> <button type="button" class="btn" id="rr-next" hidden>Next card</button>
<div class="factcard" id="rr-fact" hidden aria-live="polite"></div>
</div>
<p class="sr" id="rr-status" aria-live="polite"></p></div>
<section class="card"><h2>How to play</h2><ul><li>Tap each big cat that lives wild in the region or habitat shown (or press keys 1 to 6). Tap again to remove it.</li>
<li>Press Check. You score a point for each right cat, lose one for each wrong cat, and get 2 bonus points for a perfect round up.</li>
<li>Eight cards per game, including one trick card.</li></ul></section>
<section class="card"><h2>Facts this game teaches</h2><ul>
<li>Africa has lions, leopards and cheetahs; the Americas have only the jaguar.</li>
<li>Asiatic lions live wild only in and around Gir forest in India, and wild Asiatic cheetahs only in Iran.</li>
<li>Snow leopards typically live at 3,000 to 5,000 m in the mountains of Central and South Asia.</li>
<li>Jaguars use the Pantanal wetlands; tigers live in the Sundarbans mangroves.</li>
<li>Europe and Australia have no wild big cats today.</li></ul>
<p>All answers follow our <a href="{rel}habitats.html">big cat habitats</a> guide and <a href="{rel}which-big-cat-is-it.html#by-region">big cats by region</a>, sourced to the IUCN SSC Cat Specialist Group.</p></section>
<p class="gameline">''' + GL + '''</p>''' + PRIV + '''
<script src="{rel}games/shared.js" defer></script><script src="{rel}games/range-roundup/game.js" defer></script>''',
    related=[("All games", "games/index.html"), ("Big cat habitats", "habitats.html"), ("Which big cat is it?", "which-big-cat-is-it.html")],
    extra_ld=game_ld("Range Roundup", "games/range-roundup/", "Sort the six big cats into the regions and habitats where they live wild.", "Educational sorting",
                     "Where lions, tigers, leopards, jaguars, cheetahs and snow leopards live in the wild"), priority="0.7")
