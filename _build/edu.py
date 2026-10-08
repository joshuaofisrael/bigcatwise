"""Teachers hub, printables, lesson pages, research roundup and photo credits (8 Oct 2026)."""
from build import add, BASE_URL, PUBLISHER
from sources import CSG, WILSON, DURANT, KLEMUK, WEISS, FENNELL, PACKER1990, PACKER1991, HEINSOHN1995
from photos import PHOTOS_LIST, credit_line, have

TC = [("Teachers", "teachers/index.html")]
NGSS = "https://www.nextgenscience.org/pe/"
PE = {
 "1-LS1-2": ("Read texts and use media to determine patterns in behavior of parents and offspring that help offspring survive.", NGSS + "1-ls1-2-molecules-organisms-structures-and-processes"),
 "2-LS4-1": ("Make observations of plants and animals to compare the diversity of life in different habitats.", NGSS + "2-ls4-1-biological-evolution-unity-and-diversity"),
 "3-LS2-1": ("Construct an argument that some animals form groups that help members survive.", NGSS + "3-ls2-1-ecosystems-interactions-energy-and-dynamics"),
 "3-LS4-2": ("Use evidence to construct an explanation for how the variations in characteristics among individuals of the same species may provide advantages in surviving, finding mates, and reproducing.", NGSS + "3-ls4-2-biological-evolution-unity-and-diversity"),
 "4-LS1-1": ("Construct an argument that plants and animals have internal and external structures that function to support survival, growth, behavior, and reproduction.", NGSS + "4-ls1-1-molecules-organisms-structures-and-processes"),
 "MS-LS1-4": ("Use argument based on empirical evidence and scientific reasoning to support an explanation for how characteristic animal behaviors and specialized plant structures affect the probability of successful reproduction of animals and plants respectively.", NGSS + "ms-ls1-4-molecules-organisms-structures-and-processes"),
 "HS-LS2-7": ("Design, evaluate, and refine a solution for reducing the impacts of human activities on the environment and biodiversity.", NGSS + "hs-ls2-7-ecosystems-interactions-energy-and-dynamics"),
 "HS-LS2-8": ("Evaluate evidence for the role of group behavior on individual and species' chances to survive and reproduce.", NGSS + "hs-ls2-8-ecosystems-interactions-energy-and-dynamics"),
}
def pe(code):
    return '<a href="%s" rel="noopener">NGSS %s</a>' % (PE[code][1], code)
def align(codes):
    return [{"@type": "AlignmentObject", "alignmentType": "teaches", "educationalFramework": "Next Generation Science Standards",
             "targetName": c, "targetDescription": PE[c][0], "targetUrl": PE[c][1]} for c in codes]
def lr(name, path, desc, levels, rtype, codes=(), teaches=None):
    d = {"@context": "https://schema.org", "@type": "LearningResource", "name": name, "url": BASE_URL + path.replace("index.html", ""),
         "description": desc, "educationalLevel": levels, "learningResourceType": rtype, "inLanguage": "en", "isAccessibleForFree": True,
         "audience": {"@type": "EducationalAudience", "educationalRole": "teacher"}, "publisher": PUBLISHER, "author": PUBLISHER,
         "copyrightHolder": PUBLISHER, "copyrightYear": 2026, "license": BASE_URL + "terms.html"}
    if codes:
        d["educationalAlignment"] = align(codes)
    if teaches:
        d["teaches"] = teaches
    return [d]
KIDSAFE = ('<p class="note">Free for classroom use. No sign up, no ads and no data collected from students. '
           'Print with your browser (Ctrl+P or Cmd+P); the site menu and buttons are hidden automatically when printing.</p>')
PRINT = '<p><button type="button" class="btn printbtn" onclick="window.print()">Print this page</button></p>'

# ---------------------------------------------------------------- HUB
add("teachers/index.html", "Big Cat Lesson Plans, Worksheets & Printables for Teachers | BigCatWise",
    "Free big cat teaching resources: printable fact sheets, worksheets with answer keys, vocabulary, NGSS aligned lesson ideas for K-12 and fact based classroom games.",
    "Big cats in the classroom: free resources for teachers", kind="page", headline="Teachers",
    lead="Free, printable and sourced big cat resources for K to 12 classrooms: one page fact sheets for all six species, worksheets with answer keys, a vocabulary list, short lesson ideas by grade band and three classroom games. Everything is original, ad free and needs no sign up.",
    body='''<div class="grid">
<a class="tile hot" href="big-cat-fact-sheets.html"><h3>Fact sheets</h3><p>Six one page printable fact sheets: lion, tiger, leopard, jaguar, cheetah and snow leopard.</p></a>
<a class="tile hot" href="big-cat-worksheets.html"><h3>Worksheets</h3><p>Four printable worksheets for grades 2 to 12, from riddles to reading real research.</p></a>
<a class="tile hot" href="answer-keys.html"><h3>Answer keys</h3><p>Answers for every worksheet, with page links so students can check the evidence.</p></a>
<a class="tile hot" href="big-cat-vocabulary.html"><h3>Vocabulary list</h3><p>Twenty four kid friendly big cat science words with definitions.</p></a>
<a class="tile" href="big-cat-adaptations-lesson-plan.html"><h3>Adaptations lesson plan</h3><p>A 45 minute grades 3 to 5 lesson on big cat body structures and camouflage.</p></a>
<a class="tile" href="cheetah-worksheet-3rd-grade.html"><h3>Cheetah worksheet, grade 3</h3><p>A reading passage, questions and speed math, with an answer key.</p></a>
<a class="tile" href="lion-pride-lesson-plan.html"><h3>Lion pride lesson plan</h3><p>Why do some animals live in groups? A grade 3 lesson with a high school extension.</p></a>
<a class="tile" href="../research/"><h3>For students and researchers</h3><p>The peer reviewed papers behind our articles, with DOIs.</p></a>
</div>
<section class="card" id="lesson-ideas"><h2>Lesson ideas by grade band</h2>
<p>Standards are listed only where the activity genuinely addresses the performance expectation. Codes link to the official wording on nextgenscience.org.</p>
<h3>Grades K to 2</h3><ul>
<li><b>How big cat parents keep cubs safe.</b> Read the cub sections of the <a href="../lion.html">lion</a> and <a href="../cheetah.html">cheetah</a> pages aloud, then sort picture cards into "what the cub does" and "what the mother does". Lion mothers keep cubs together in a group and defend them; cheetah mothers raise cubs alone. Fits ''' + pe("1-LS1-2") + '''.</li>
<li><b>Different places, different animals.</b> Use the <a href="../habitats.html">habitats guide</a> to compare savanna, rainforest and high mountains, and list the animals students can spot in each photo. Fits ''' + pe("2-LS4-1") + '''.</li></ul>
<h3>Grades 3 to 5</h3><ul>
<li><b>Why do lions live in groups?</b> Students argue from evidence that a pride helps lions survive. Full plan: <a href="lion-pride-lesson-plan.html">lion pride lesson plan</a>. Fits ''' + pe("3-LS2-1") + '''.</li>
<li><b>Built for the job.</b> Match body structures (cheetah claws, snow leopard tail, tiger stripes) to what they do. Full plan: <a href="big-cat-adaptations-lesson-plan.html">big cat adaptations lesson plan</a>. Fits ''' + pe("4-LS1-1") + ''' and ''' + pe("3-LS4-2") + '''.</li></ul>
<h3>Grades 6 to 8</h3><ul>
<li><b>Behavior and breeding success.</b> Students read <a href="../blog/why-do-lions-live-in-prides.html">why do lions live in prides?</a> and write an argument explaining how lionesses pooling cubs in a cr&egrave;che and defending them against infanticidal males raises the odds that cubs survive. Fits ''' + pe("MS-LS1-4") + '''.</li>
<li><b>Counting what you cannot see.</b> Use <a href="../blog/how-many-big-cats-are-left.html">how many big cats are left?</a> to discuss why estimates come as ranges and what "mature individuals" means.</li></ul>
<h3>Grades 9 to 12</h3><ul>
<li><b>Evaluate the evidence on group living.</b> Students compare the hunting hypothesis with the cub defence and territory evidence from Packer, Scheel and Pusey (1990) and Heinsohn and Packer (1995), then judge which explanation the data support. See worksheet 4 on the <a href="big-cat-worksheets.html#w4">worksheets page</a>. Fits ''' + pe("HS-LS2-8") + '''.</li>
<li><b>Design a coexistence plan.</b> Using the snow leopard and conservation pages, teams design and critique ways to reduce livestock losses and retaliatory killing (for example predator proof corrals and livestock insurance, which our <a href="../snow-leopard.html#status">snow leopard page</a> describes). Fits ''' + pe("HS-LS2-7") + '''.</li></ul></section>
<section class="card" id="games"><h2>Games as classroom activities</h2><ul>
<li><a href="../games/rosette-detective/">Rosette Detective</a>: a 5 minute warm up on identifying big cats by coat pattern. Ask students to explain each answer using the fact card.</li>
<li><a href="../games/cheetah-burst/">Cheetah Burst</a>: a quick brain break. Afterwards, ask why a real cheetah cannot keep sprinting (see the fact cards and the cheetah speed article).</li>
<li><a href="../games/range-roundup/">Range Roundup</a>: an exit ticket on habitats and continents. The trick card (Europe and Australia) is a good discussion starter.</li></ul>
<p>The games need no accounts and save nothing except an optional best score in the browser.</p></section>
<section class="card"><h2>About these resources</h2><p>All worksheets, fact sheets and games are original works of Joshua Israel Ventures LLC. Facts come from the IUCN SSC Cat Specialist Group, leading zoos and peer reviewed research, listed on each article and on our <a href="../research/">research page</a>. Photos are public domain (CC0) or Creative Commons licensed, credited under each photo and on our <a href="../credits/">photo credits</a> page. Spotted an error? Email <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a>.</p></section>''' + KIDSAFE,
    related=[("Big cat fact sheets", "teachers/big-cat-fact-sheets.html"), ("Big cat worksheets", "teachers/big-cat-worksheets.html"), ("Games", "games/index.html"), ("Glossary", "glossary.html")],
    extra_ld=lr("BigCatWise resources for teachers", "teachers/index.html", "Free big cat fact sheets, worksheets, answer keys, vocabulary and NGSS aligned lesson ideas.",
                ["Kindergarten", "Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Middle school", "High school"], ["Lesson plan", "Worksheet", "Fact sheet"],
                ["1-LS1-2", "2-LS4-1", "3-LS2-1", "3-LS4-2", "4-LS1-1", "MS-LS1-4", "HS-LS2-7", "HS-LS2-8"]), priority="0.8")

# ---------------------------------------------------------------- FACT SHEETS
SHEETS = [
 ("lion", "Lion", "Panthera leo", "110 to 272 kg", "137 to 250 cm, plus a 60 to 100 cm tail", "About 12 to 18 years", "Sub-Saharan Africa; Gir landscape, Gujarat, India", "Vulnerable",
  ["The only truly social big cat: prides are built around related lionesses.", "Adult males have a mane; both sexes have a dark tail tuft.", "A roar can carry over several kilometres.", "About 22,000 to 25,000 adult and subadult lions in Africa (2025) and about 670 in India (2020)."]),
 ("tiger", "Tiger", "Panthera tigris", "75 to 325 kg", "150 to 230 cm, plus a 90 to 110 cm tail", "About 12 to 15 years", "10 countries in South, Southeast and East Asia and the Russian Far East", "Endangered",
  ["The largest cat and the only striped cat.", "Every tiger's stripes are unique, and its left and right sides differ.", "Tigers have a white spot on the back of each ear.", "About 3,726 to 5,578 wild tigers, not counting cubs."]),
 ("leopard", "Leopard", "Panthera pardus", "17 to 90 kg", "91 to 191 cm, plus a 51 to 101 cm tail", "About 13 to 21 years", "Sub-Saharan Africa and scattered parts of Asia", "Vulnerable",
  ["The most widespread big cat.", "Small rosettes, usually empty in the middle.", "Often stores its kills up in trees.", "Black panthers in Africa and Asia are melanistic leopards."]),
 ("jaguar", "Jaguar", "Panthera onca", "36 to 148 kg", "110 to 170 cm, plus a 44 to 80 cm tail", "Up to about 26 years recorded", "Mexico to northern Argentina", "Near Threatened",
  ["The only big cat in the Americas.", "Large rosettes, usually with dots inside.", "Kills prey with a skull piercing bite and swims readily.", "About 57,000 to 64,000 jaguars in Amazonia alone."]),
 ("cheetah", "Cheetah", "Acinonyx jubatus", "23 to 65 kg", "113 to 140 cm, plus a 60 to 84 cm tail", "Up to about 14 years in the wild", "Mainly southern and eastern Africa; Sahara; Iran", "Vulnerable",
  ["The fastest land animal: wild cheetahs have been measured at about 93 km/h.", "Solid round spots and black tear marks from eye to mouth.", "Semi retractable claws grip like running spikes.", "It cannot roar; it purrs and chirps."]),
 ("snow-leopard", "Snow leopard", "Panthera uncia", "30 to 50 kg", "90 to 120 cm, plus an 80 to 100 cm tail", "About 10 to 20 years", "Mountains of 12 countries in Central and South Asia", "Vulnerable",
  ["Lives typically at 3,000 to 5,000 m.", "Smoky grey coat with open rosettes and a very long, thick tail.", "It cannot roar.", "About 7,446 to 7,996 snow leopards, including 2,710 to 3,386 mature adults."]),
]
fs = []
for slug, name, sci, wt, ln, life, rng, status, facts in SHEETS:
    fs.append('<section class="card sheet" id="%s" style="break-after:page"><h2>%s fact sheet</h2><p class="sci"><i>%s</i></p>'
              '<div class="tablewrap"><table><tbody><tr><th scope="row">Weight</th><td>%s</td></tr><tr><th scope="row">Head and body length</th><td>%s</td></tr>'
              '<tr><th scope="row">Lifespan</th><td>%s</td></tr><tr><th scope="row">Where it lives</th><td>%s</td></tr><tr><th scope="row">IUCN Red List</th><td>%s</td></tr></tbody></table></div>'
              '<h3>Four amazing facts</h3><ol>%s</ol><p>Draw it! <span class="lines" style="display:block"></span><span class="lines" style="display:block"></span></p>'
              '<p class="note">Source: IUCN SSC Cat Specialist Group, summarised on <a href="../%s.html">BigCatWise %s facts</a>. bigcatwise.com</p></section>'
              % (slug, name, sci, wt, ln, life, rng, status, "".join("<li>%s</li>" % f for f in facts), slug, name.lower()))
add("teachers/big-cat-fact-sheets.html", "Printable Big Cat Fact Sheets for Kids (Free) | BigCatWise",
    "Six free printable big cat fact sheets for the classroom: lion, tiger, leopard, jaguar, cheetah and snow leopard, each with sourced facts and a drawing space.",
    "Printable big cat fact sheets", kind="page", headline="Fact sheets", crumbs=TC,
    lead="One printable page per species with size, lifespan, range, conservation status and four sourced facts. Each sheet prints on its own page.",
    body=PRINT + '<p class="jump">Jump to: ' + " | ".join('<a href="#%s">%s</a>' % (s[0], s[1]) for s in SHEETS) + '</p>' + "".join(fs) + KIDSAFE,
    related=[("Worksheets", "teachers/big-cat-worksheets.html"), ("Compare big cats", "compare.html"), ("Teachers hub", "teachers/index.html")],
    sources=[CSG["lion"], CSG["tiger"], CSG["leopard"], CSG["jaguar"], CSG["cheetah"], CSG["snow"], WILSON],
    extra_ld=lr("Printable big cat fact sheets", "teachers/big-cat-fact-sheets.html", "Six one page printable fact sheets on the big cats.",
                ["Grade 2", "Grade 3", "Grade 4", "Grade 5", "Middle school"], ["Fact sheet", "Printable"]), priority="0.7")

# ---------------------------------------------------------------- WORKSHEETS
W1 = [("I have stripes, and no two of us have the same pattern. I live in Asia.", ""), ("I am the only big cat in the Americas. My big rosettes have dots inside.", ""),
      ("I live in high mountains and have a very long, thick tail. I cannot roar.", ""), ("I am the fastest land animal. I have black tear marks on my face.", ""),
      ("I live in a group called a pride.", ""), ("I often carry my food up a tree. My small rosettes are usually empty.", "")]
add("teachers/big-cat-worksheets.html", "Free Big Cat Worksheets (Printable, Grades 2 to 12) | BigCatWise",
    "Four free printable big cat worksheets: which big cat am I riddles, a habitat match, cheetah speed math and a lion research reading for older students.",
    "Printable big cat worksheets", kind="page", headline="Worksheets", crumbs=TC,
    lead="Four printable worksheets that use real, sourced facts. Answers are on the separate answer key page, so you can print the questions on their own.",
    body=PRINT + '''<p class="jump">Jump to: <a href="#w1">1. Which big cat am I? (grades 2 to 4)</a> | <a href="#w2">2. Habitat match (grades 2 to 5)</a> | <a href="#w3">3. Cheetah speed math (grades 4 to 6)</a> | <a href="#w4">4. Reading the research (grades 9 to 12)</a></p>
<section class="card sheet" id="w1" style="break-after:page"><h2>Worksheet 1: Which big cat am I?</h2><p>Name: <span class="lines" style="display:inline-block;width:60%"></span></p>
<p>Read each clue. Write lion, tiger, leopard, jaguar, cheetah or snow leopard.</p><ol>''' + "".join('<li>%s<span class="lines" style="display:block"></span></li>' % q for q, _ in W1) + '''</ol>
<p class="note">Check your answers with the <a href="../which-big-cat-is-it.html">big cat ID guide</a>.</p></section>
<section class="card sheet" id="w2" style="break-after:page"><h2>Worksheet 2: Big cat habitat match</h2><p>Name: <span class="lines" style="display:inline-block;width:60%"></span></p>
<p>Draw a line from each big cat to a place where it lives in the wild.</p>
<div class="tablewrap"><table><thead><tr><th>Big cat</th><th>Place</th></tr></thead><tbody>
<tr><td>Snow leopard</td><td>A. Amazon rainforest and the Pantanal wetlands of South America</td></tr>
<tr><td>Jaguar</td><td>B. Sundarbans mangroves of India and Bangladesh</td></tr>
<tr><td>Cheetah</td><td>C. Gir forest in western India (a small population of this cat)</td></tr>
<tr><td>Tiger</td><td>D. Rocky mountain slopes at 3,000 to 5,000 m in Central Asia</td></tr>
<tr><td>Asiatic lion</td><td>E. Open grassland of eastern and southern Africa</td></tr></tbody></table></div>
<p><b>Bonus:</b> Which continent has no wild big cats today: Africa, Asia or Australia? <span class="lines" style="display:inline-block;width:30%"></span></p></section>
<section class="card sheet" id="w3" style="break-after:page"><h2>Worksheet 3: Cheetah speed math</h2><p>Name: <span class="lines" style="display:inline-block;width:60%"></span></p>
<p>Scientists in Botswana put GPS collars on wild cheetahs. The fastest run they measured was 25.9 metres per second, about 93 kilometres per hour. The average top speed of a run was 14.9 metres per second, about 54 km/h. Cheetah chases seldom go further than about 300 m.</p><ol>
<li>Round 25.9 m/s to the nearest whole number. <span class="lines" style="display:block"></span></li>
<li>How much faster is 93 km/h than 54 km/h? <span class="lines" style="display:block"></span></li>
<li>A cheetah runs at 25 m/s. How many metres does it cover in 4 seconds? <span class="lines" style="display:block"></span></li>
<li>At 25 m/s, how many seconds would a 300 m chase take? <span class="lines" style="display:block"></span></li>
<li>A cheetah's stride can be about 7 m long. About how many strides is a 70 m dash? <span class="lines" style="display:block"></span></li>
<li>Most hunts are run well below top speed. From the article, give one reason why. <span class="lines" style="display:block"></span><span class="lines" style="display:block"></span></li></ol>
<p class="note">Source: Wilson et al. (2013), <i>Nature</i>, summarised in <a href="../blog/how-fast-is-a-cheetah.html">how fast is a cheetah?</a></p></section>
<section class="card sheet" id="w4"><h2>Worksheet 4: Reading the research on lion prides (grades 9 to 12)</h2><p>Name: <span class="lines" style="display:inline-block;width:60%"></span></p>
<p>Read <a href="../blog/why-do-lions-live-in-prides.html">why do lions live in prides?</a> and, if you can, the abstracts of the three papers it cites. Then answer.</p><ol>
<li>State the "hunting hypothesis" for why lions live in groups in one sentence. <span class="lines" style="display:block"></span></li>
<li>Packer, Scheel and Pusey (1990) found two group sizes gave the best foraging success when prey was scarce. What were they, and why does that weaken the hunting hypothesis? <span class="lines" style="display:block"></span><span class="lines" style="display:block"></span></li>
<li>Give two other benefits of group living supported by the evidence. <span class="lines" style="display:block"></span><span class="lines" style="display:block"></span></li>
<li>Heinsohn and Packer (1995) used playback experiments. What is a playback experiment and what did it reveal about cooperation? <span class="lines" style="display:block"></span><span class="lines" style="display:block"></span></li>
<li>How does the 1991 DNA study help explain why female lions cooperate? <span class="lines" style="display:block"></span><span class="lines" style="display:block"></span></li>
<li>Claim, evidence, reasoning: write a short paragraph on the main reason lions live in prides. <span class="lines" style="display:block"></span><span class="lines" style="display:block"></span><span class="lines" style="display:block"></span></li></ol>
<p class="note">Aligned to <a href="''' + PE["HS-LS2-8"][1] + '''" rel="noopener">NGSS HS-LS2-8</a>.</p></section>''' + '<p>Answers: <a href="answer-keys.html">worksheet answer keys</a>.</p>' + KIDSAFE,
    related=[("Answer keys", "teachers/answer-keys.html"), ("Fact sheets", "teachers/big-cat-fact-sheets.html"), ("Teachers hub", "teachers/index.html")],
    extra_ld=lr("Printable big cat worksheets", "teachers/big-cat-worksheets.html", "Four printable big cat worksheets for grades 2 to 12.",
                ["Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "High school"], ["Worksheet", "Printable"], ["HS-LS2-8"]), priority="0.7")

# ---------------------------------------------------------------- ANSWER KEYS
add("teachers/answer-keys.html", "Big Cat Worksheet Answer Keys | BigCatWise",
    "Answer keys for the free BigCatWise big cat worksheets: which big cat am I, habitat match, cheetah speed math and the lion pride research reading.",
    "Answer keys for the big cat worksheets", kind="page", headline="Answer keys", crumbs=TC,
    lead="Answers for every BigCatWise worksheet, with links to the page that holds the evidence so students can check for themselves.",
    body=PRINT + '''<section class="card sheet"><h2>Worksheet 1: Which big cat am I?</h2><ol><li>Tiger</li><li>Jaguar</li><li>Snow leopard</li><li>Cheetah</li><li>Lion</li><li>Leopard</li></ol><p class="note">Evidence: <a href="../which-big-cat-is-it.html">big cat ID guide</a>.</p></section>
<section class="card sheet"><h2>Worksheet 2: Habitat match</h2><ul><li>Snow leopard: D</li><li>Jaguar: A</li><li>Cheetah: E</li><li>Tiger: B</li><li>Asiatic lion: C</li></ul><p>Bonus: Australia (Europe and Antarctica have no wild big cats today either).</p><p class="note">Evidence: <a href="../habitats.html">big cat habitats</a>.</p></section>
<section class="card sheet"><h2>Worksheet 3: Cheetah speed math</h2><ol><li>26 m/s</li><li>39 km/h faster (93 minus 54)</li><li>100 m (25 x 4)</li><li>12 seconds (300 divided by 25)</li><li>About 10 strides (70 divided by 7)</li>
<li>Any one of: the cheetahs in the study mostly hunted impala in fairly thick vegetation, so braking and sharp turns mattered more than straight line speed; sprinting takes extreme energy and muscle effort, so chases are short.</li></ol><p class="note">Evidence: <a href="../blog/how-fast-is-a-cheetah.html">how fast is a cheetah?</a></p></section>
<section class="card sheet"><h2>Worksheet 4: Reading the research on lion prides</h2><ol>
<li>Lions live in groups because hunting together lets each lion catch more food.</li>
<li>One female alone, or a group of five or six. If small groups did worse than lone females, food alone cannot explain why females in small prides still forage together, which radio collar data showed they did.</li>
<li>Any two: groups of mothers defend cubs against infanticidal males; larger groups win territorial contests against smaller neighbouring prides; helping close relatives also passes on shared genes.</li>
<li>Researchers played recordings of roars from unfamiliar lions to simulate intruders. Some females consistently led the approach while others lagged behind, and leaders did not punish laggards, showing cooperation is not simply based on reciprocity.</li>
<li>DNA fingerprinting showed female pride companions are always closely related, so cooperating helps relatives (kin), which can favour cooperation.</li>
<li>Answers vary. A strong answer claims that cub defence and territory explain prides better than hunting, cites the 1990 foraging and creche data, and reasons that group members gain survival and breeding benefits.</li></ol>
<p class="note">Evidence: <a href="../blog/why-do-lions-live-in-prides.html">why do lions live in prides?</a></p></section>
<section class="card sheet"><h2>Cheetah worksheet for grade 3</h2><p>The answers are printed at the bottom of the <a href="cheetah-worksheet-3rd-grade.html#key">grade 3 cheetah worksheet</a>.</p></section>''' + KIDSAFE,
    related=[("Worksheets", "teachers/big-cat-worksheets.html"), ("Teachers hub", "teachers/index.html")],
    extra_ld=lr("Big cat worksheet answer keys", "teachers/answer-keys.html", "Answer keys for the BigCatWise worksheets.", ["Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "High school"], ["Answer key"]),
    priority="0.5")

# ---------------------------------------------------------------- VOCABULARY
VOC = [("Adaptation", "A body part or behavior that helps an animal survive where it lives, like a cheetah's long tail for balance."),
 ("Apex predator", "A predator at the top of its food chain with no natural predators as a healthy adult."),
 ("Camera trap", "A camera that takes a photo when an animal moves past. Scientists use them to identify individual tigers by their stripes."),
 ("Camouflage", "Colours or patterns that help an animal blend into its surroundings, like a tiger's stripes in tall grass."),
 ("Coalition", "A group of male lions or cheetahs, often brothers, that live and defend territory together."),
 ("Conservation", "Protecting wild animals and the places they live."),
 ("Cr&egrave;che", "A nursery group where several lion mothers keep their cubs together and protect them."),
 ("Crepuscular", "Most active at dawn and dusk."),
 ("Cub", "A young big cat."),
 ("Endangered", "An IUCN Red List category for species at very high risk of extinction in the wild. The tiger is Endangered."),
 ("Habitat", "The natural home of an animal, such as savanna, rainforest or high mountains."),
 ("Home range", "The whole area an animal uses for its normal activities."),
 ("IUCN Red List", "The global list that rates how close species are to extinction."),
 ("Melanism", "A natural variation that makes fur very dark. Black panthers are melanistic leopards or jaguars."),
 ("Panthera", "The group (genus) of big cats that includes the lion, tiger, leopard, jaguar and snow leopard."),
 ("Predator", "An animal that hunts and eats other animals."),
 ("Prey", "An animal that is hunted and eaten by another animal."),
 ("Pride", "A lion family group of related females, their cubs and one or more adult males."),
 ("Rosette", "A rose shaped cluster of dark spots, found on leopards, jaguars and snow leopards."),
 ("Semi retractable claws", "Claws that cannot be fully pulled in, like a cheetah's, which grip the ground when running."),
 ("Solitary", "Living alone. Most big cats, except lions, are solitary as adults."),
 ("Territory", "An area an animal defends against others of its kind."),
 ("Vulnerable", "An IUCN Red List category for species at high risk of extinction in the wild. Lions, leopards, cheetahs and snow leopards are Vulnerable."),
 ("Wildlife corridor", "A strip of habitat that links populations so animals can move between them.")]
add("teachers/big-cat-vocabulary.html", "Big Cat Vocabulary List for Kids (Printable) | BigCatWise",
    "A printable big cat vocabulary list for the classroom: 24 science words like adaptation, camouflage, pride, rosette and predator, with kid friendly definitions.",
    "Big cat vocabulary list", kind="page", headline="Vocabulary", crumbs=TC,
    lead="Twenty four big cat science words with short, kid friendly definitions. Print it as a word wall or a study sheet. For more detail, see our full <a href=\"../glossary.html\">big cat glossary</a>.",
    body=PRINT + '<section class="card sheet"><h2>Word list</h2><dl>' + "".join("<dt>%s</dt><dd>%s</dd>" % v for v in VOC) + '</dl></section>'
         '<section class="card sheet"><h2>Quick check</h2><p>Fill in the word: A lion family group is called a <span class="lines" style="display:inline-block;width:25%"></span>. '
         'A rose shaped cluster of spots is a <span class="lines" style="display:inline-block;width:25%"></span>. An animal that is hunted is called <span class="lines" style="display:inline-block;width:25%"></span>.</p>'
         '<p class="note">Answers: pride, rosette, prey.</p></section>' + KIDSAFE,
    related=[("Glossary", "glossary.html"), ("Worksheets", "teachers/big-cat-worksheets.html"), ("Teachers hub", "teachers/index.html")],
    extra_ld=lr("Big cat vocabulary list", "teachers/big-cat-vocabulary.html", "Twenty four big cat science words with kid friendly definitions.",
                ["Grade 2", "Grade 3", "Grade 4", "Grade 5", "Middle school"], ["Vocabulary list", "Printable"]), priority="0.6")

# ---------------------------------------------------------------- LESSON: ADAPTATIONS (target: big cat adaptations lesson plan)
add("teachers/big-cat-adaptations-lesson-plan.html", "Big Cat Adaptations Lesson Plan (Grades 3 to 5, Free) | BigCatWise",
    "A free 45 minute big cat adaptations lesson plan for grades 3 to 5: structure and function cards, a camouflage investigation, exit ticket and NGSS 4-LS1-1 alignment.",
    "Big cat adaptations lesson plan (grades 3 to 5)", kind="page", headline="Big cat adaptations lesson plan", crumbs=TC,
    lead="In this 45 minute lesson, students match real big cat body structures to the jobs they do, test why stripes and spots work as camouflage, and write an evidence based claim. Everything you need is free and printable, and every fact links to a sourced BigCatWise page.",
    body='''<section class="card"><h2>At a glance</h2><div class="tablewrap"><table><tbody>
<tr><th scope="row">Grades</th><td>3 to 5</td></tr><tr><th scope="row">Time</th><td>45 minutes</td></tr>
<tr><th scope="row">Standards</th><td>''' + pe("4-LS1-1") + ''': ''' + PE["4-LS1-1"][0] + '''<br>''' + pe("3-LS4-2") + ''' (camouflage extension): ''' + PE["3-LS4-2"][0] + '''</td></tr>
<tr><th scope="row">Materials</th><td>Printed <a href="big-cat-fact-sheets.html">fact sheets</a>, the structure cards below, scissors, a sheet of striped or patterned paper and a sheet of plain paper per group</td></tr>
<tr><th scope="row">Students will</th><td>Name at least three big cat structures and explain how each one helps the cat survive; explain why a pattern can hide a large animal.</td></tr></tbody></table></div></section>
<section class="card"><h2>1. Hook (5 minutes)</h2><p>Play one round of <a href="../games/rosette-detective/">Rosette Detective</a> on the board. Ask: "Why would a big cat need spots or stripes at all?" Collect ideas without judging them.</p></section>
<section class="card"><h2>2. Structure and function cards (15 minutes)</h2><p>Print and cut out the cards. Groups match each structure to its job, then check against the answers in the right column (fold it under before printing if you want a challenge).</p>
<div class="tablewrap"><table><thead><tr><th>Structure</th><th>What it does</th><th>Evidence page</th></tr></thead><tbody>
<tr><td>Cheetah's semi retractable claws</td><td>Stay partly out and grip the ground like running spikes when it speeds up and turns</td><td><a href="../blog/how-fast-is-a-cheetah.html">How fast is a cheetah?</a></td></tr>
<tr><td>Cheetah's long tail</td><td>Helps it balance and steer in sharp turns</td><td><a href="../blog/how-fast-is-a-cheetah.html">How fast is a cheetah?</a></td></tr>
<tr><td>Cheetah's flexible spine</td><td>Bends and stretches with each bound, making strides up to about 7 m long</td><td><a href="../blog/how-fast-is-a-cheetah.html">How fast is a cheetah?</a></td></tr>
<tr><td>Snow leopard's very long, thick tail</td><td>Up to about 1 m long; helps it balance on steep rock and wraps around its body for warmth when it rests</td><td><a href="../snow-leopard.html">Snow leopard facts</a></td></tr>
<tr><td>Snow leopard's broad, furry paws</td><td>Help it move on snow and rocky ground</td><td><a href="../which-big-cat-is-it.html">ID guide</a></td></tr>
<tr><td>Tiger's stripes</td><td>Break up its outline in tall grass and forest shadows so prey notices it later</td><td><a href="../blog/why-do-tigers-have-stripes.html">Why do tigers have stripes?</a></td></tr>
<tr><td>Lion's, tiger's, leopard's and jaguar's vocal folds</td><td>Their shape helps these cats make a deep, loud roar; a lion's roar can carry over several kilometres</td><td><a href="../blog/which-big-cats-can-roar.html">Which big cats can roar?</a></td></tr>
<tr><td>Jaguar's broad head and strong jaw</td><td>Power a bite strong enough to pierce a skull</td><td><a href="../jaguar.html">Jaguar facts</a></td></tr>
</tbody></table></div>
<p class="note">Teacher tip: one structure can do more than one job. Ask students to find another example (the snow leopard's tail helps with balance and warmth).</p></section>
<section class="card"><h2>3. Camouflage investigation (15 minutes)</h2><ol>
<li>Each group cuts two simple cat shapes the same size: one from plain paper and one from striped or patterned paper.</li>
<li>Tape both onto a "grass" background made of vertical stripes (draw them, or use a patterned sheet).</li>
<li>From across the room, a partner counts how many seconds it takes to spot each shape. Repeat with three spotters.</li>
<li>Groups record the times in a table and decide which shape was harder to find.</li></ol>
<p>Discuss: tigers are orange, so why do they still hide well? Share the finding from Fennell and colleagues (2019): deer and most mammals cannot reliably tell orange from green, so to them a tiger's colour blends in. Students can read more in <a href="../blog/why-do-tigers-have-stripes.html">why do tigers have stripes?</a></p></section>
<section class="card"><h2>4. Exit ticket (10 minutes)</h2><p>Students answer: "Pick one big cat. Name one external structure and one behavior, and explain how each helps it survive. Use one fact from a BigCatWise page as evidence." For a quick check, they can play <a href="../games/range-roundup/">Range Roundup</a> once and write down one surprise.</p></section>
<section class="card"><h2>Differentiation and extension</h2><ul>
<li><b>Support:</b> give students the structure cards with the "what it does" column already matched and ask them to draw each structure.</li>
<li><b>Challenge:</b> students compare the cheetah and the lion: which structures suit a sprinter and which suit a group hunter? See the <a href="../compare.html">comparison table</a>.</li>
<li><b>Home link:</b> students teach a family member three big cat adaptations using the printable fact sheet.</li></ul></section>''' + KIDSAFE,
    related=[("Big cat fact sheets", "teachers/big-cat-fact-sheets.html"), ("Why do tigers have stripes?", "blog/why-do-tigers-have-stripes.html"), ("How fast is a cheetah?", "blog/how-fast-is-a-cheetah.html"), ("Teachers hub", "teachers/index.html")],
    sources=[WILSON, FENNELL, KLEMUK, CSG["snow"], CSG["jaguar"]],
    extra_ld=lr("Big cat adaptations lesson plan", "teachers/big-cat-adaptations-lesson-plan.html", "A 45 minute grades 3 to 5 lesson on big cat structures, functions and camouflage.",
                ["Grade 3", "Grade 4", "Grade 5"], ["Lesson plan"], ["4-LS1-1", "3-LS4-2"], "How big cat body structures and coat patterns help them survive"), priority="0.7")

# ---------------------------------------------------------------- CHEETAH WORKSHEET (target: cheetah worksheet for 3rd grade)
add("teachers/cheetah-worksheet-3rd-grade.html", "Cheetah Worksheet for 3rd Grade (Free Printable) | BigCatWise",
    "A free printable cheetah worksheet for 3rd grade: a short reading passage about the fastest land animal, comprehension questions, speed math and an answer key.",
    "Cheetah worksheet for 3rd grade", kind="page", headline="Cheetah worksheet for 3rd grade", crumbs=TC,
    lead="A one page reading passage written for third graders, followed by comprehension questions, a little speed math and a draw and label task. The answer key is at the bottom, so print only the first section for students.",
    body=PRINT + '''<section class="card sheet" style="break-after:page"><h2>Reading: The fastest runner on land</h2><p>Name: <span class="lines" style="display:inline-block;width:60%"></span></p>
<p>The cheetah is the fastest land animal. Scientists put special collars on wild cheetahs in Botswana, in Africa. The fastest cheetah ran about 93 kilometres per hour. That is as fast as a car on a highway!</p>
<p>A cheetah has a slim body and long legs. Its back can bend and stretch like a spring, so each jump forward is very long. Its claws stay partly out, like the spikes on running shoes, so it can grip the ground. Its long tail helps it balance when it turns quickly.</p>
<p>Cheetahs cannot run fast for long. Most chases are shorter than about 300 metres. After a chase, a cheetah must rest and catch its breath before it eats. Lions and hyenas sometimes steal its food while it rests.</p>
<p>You can tell a cheetah by its solid round black spots and the black lines that run from its eyes to its mouth, like tear marks. Cheetahs cannot roar. They purr and make chirping sounds, like a bird.</p>
<h3>Questions</h3><ol>
<li>What is the fastest land animal? <span class="lines" style="display:block"></span></li>
<li>How fast did the fastest wild cheetah run? <span class="lines" style="display:block"></span></li>
<li>How do a cheetah's claws help it run? <span class="lines" style="display:block"></span></li>
<li>What does the cheetah's long tail help it do? <span class="lines" style="display:block"></span></li>
<li>Why do you think a cheetah has to rest after a chase? <span class="lines" style="display:block"></span></li>
<li>Name two ways to tell a cheetah from other big cats. <span class="lines" style="display:block"></span></li>
<li><b>Math:</b> A chase is 300 metres long. A cheetah has already run 180 metres. How many metres are left? <span class="lines" style="display:block"></span></li>
<li><b>Math:</b> If a cheetah runs 25 metres every second, how far does it go in 3 seconds? <span class="lines" style="display:block"></span></li></ol>
<h3>Draw and label</h3><p>Draw a cheetah. Label its <b>spots</b>, <b>tear marks</b>, <b>claws</b> and <b>tail</b>.</p><div style="height:9em;border:2px dashed #b88a4a;border-radius:16px"></div></section>
<section class="card" id="teacher-notes"><h2>Teacher notes</h2><ul>
<li>Reading level: written for grade 3 with short sentences; key words are spots, claws, balance and chase.</li>
<li>Standards fit: question 3, 4 and the labelling task address how external structures support survival and behavior (''' + pe("4-LS1-1") + '''; often taught in grade 4, so use it here as an early introduction).</li>
<li>All facts come from <a href="../blog/how-fast-is-a-cheetah.html">how fast is a cheetah?</a> and our <a href="../cheetah.html">cheetah facts</a> page, based on Wilson et al. (2013) in <i>Nature</i> and the IUCN SSC Cat Specialist Group.</li>
<li>Follow up with the <a href="../games/cheetah-burst/">Cheetah Burst</a> game: students experience why speed alone is not enough.</li></ul></section>
<section class="card sheet" id="key"><h2>Answer key</h2><ol><li>The cheetah.</li><li>About 93 kilometres per hour.</li><li>They stay partly out and grip the ground, like spikes on running shoes.</li><li>Balance when it turns quickly.</li>
<li>Running so fast takes a huge amount of energy, so it gets tired and must catch its breath (accept similar answers).</li><li>Any two: solid round black spots; black tear marks from eyes to mouth; slim body with long legs; it purrs and chirps instead of roaring.</li>
<li>120 metres.</li><li>75 metres.</li></ol></section>''' + KIDSAFE,
    related=[("Cheetah facts", "cheetah.html"), ("How fast is a cheetah?", "blog/how-fast-is-a-cheetah.html"), ("Cheetah Burst game", "games/cheetah-burst/index.html"), ("Teachers hub", "teachers/index.html")],
    sources=[WILSON, CSG["cheetah"]],
    extra_ld=lr("Cheetah worksheet for 3rd grade", "teachers/cheetah-worksheet-3rd-grade.html", "A printable cheetah reading passage, questions and speed math for grade 3, with answer key.",
                ["Grade 3"], ["Worksheet", "Reading passage", "Answer key"], ["4-LS1-1"], "Cheetah speed and the structures that make it fast"), priority="0.7")

# ---------------------------------------------------------------- LESSON: LION PRIDES (target: animals that live in groups lesson plan)
add("teachers/lion-pride-lesson-plan.html", "Why Do Animals Live in Groups? Lion Pride Lesson Plan (Grade 3) | BigCatWise",
    "A free grade 3 lesson plan on why some animals live in groups, using real lion pride research. Includes argument writing, a sorting activity and a high school extension.",
    "Lion pride lesson plan: why do some animals live in groups?", kind="page", headline="Lion pride lesson plan", crumbs=TC,
    lead="Lions are the only big cats that live in groups. This 40 minute lesson uses real field research to help third graders build an argument that living in a group helps lions survive, with a ready made extension for high school biology.",
    body='''<section class="card"><h2>At a glance</h2><div class="tablewrap"><table><tbody>
<tr><th scope="row">Grade</th><td>3 (extension for grades 9 to 12)</td></tr><tr><th scope="row">Time</th><td>40 minutes</td></tr>
<tr><th scope="row">Standards</th><td>''' + pe("3-LS2-1") + ''': ''' + PE["3-LS2-1"][0] + '''<br>Extension: ''' + pe("HS-LS2-8") + ''': ''' + PE["HS-LS2-8"][0] + '''</td></tr>
<tr><th scope="row">Materials</th><td>The <a href="big-cat-fact-sheets.html#lion">lion fact sheet</a>, the sorting cards below, chart paper</td></tr></tbody></table></div></section>
<section class="card"><h2>1. Wonder (5 minutes)</h2><p>Show the lion pride photo from <a href="../blog/why-do-lions-live-in-prides.html">why do lions live in prides?</a> Ask: "Tigers, leopards and jaguars mostly live alone. Why might lions live together?" Record guesses on chart paper.</p></section>
<section class="card"><h2>2. Read the evidence (10 minutes)</h2><p>Read these kid friendly evidence cards aloud. Each one is based on research reported in our article.</p><ol>
<li>Lion mothers keep their cubs together in a nursery group called a cr&egrave;che. Groups of mothers can protect cubs from dangerous male lions.</li>
<li>Prides of lions defend their home area from other prides. Bigger groups usually win against smaller groups.</li>
<li>The lionesses in a pride are always close relatives: they are family.</li>
<li>Scientists expected group hunting to give every lion more food, but when food was scarce a lion hunting alone often did about as well as a big group.</li></ol></section>
<section class="card"><h2>3. Sort it (10 minutes)</h2><p>In pairs, students sort the cards into "helps lions survive in a group" and "does not explain why lions live in groups". Card 4 is the surprise: it shows food is not the main reason. Discuss how scientists changed their minds when the data did not fit the first idea.</p></section>
<section class="card"><h2>4. Argue (15 minutes)</h2><p>Students write a claim with two pieces of evidence: "Living in a pride helps lions survive because ___ and ___." Sentence starters: "One piece of evidence is...", "This shows that...".</p>
<p>Share a few aloud. Then compare with other animals students know that live in groups, such as herds, flocks or schools of fish.</p></section>
<section class="card"><h2>High school extension</h2><p>Older students read the abstracts of Packer, Scheel and Pusey (1990) in <i>The American Naturalist</i>, Heinsohn and Packer (1995) in <i>Science</i> and Packer and colleagues (1991) in <i>Nature</i> (links in the sources below and on our <a href="../research/">research page</a>), then complete <a href="big-cat-worksheets.html#w4">worksheet 4</a>. Ask them to separate correlation from cause: what would they need to measure to show that group size causes better cub survival?</p></section>''' + KIDSAFE,
    related=[("Why do lions live in prides?", "blog/why-do-lions-live-in-prides.html"), ("Lion facts", "lion.html"), ("Worksheets", "teachers/big-cat-worksheets.html"), ("Teachers hub", "teachers/index.html")],
    sources=[PACKER1990, HEINSOHN1995, PACKER1991, CSG["lion"]],
    extra_ld=lr("Lion pride lesson plan: why do some animals live in groups?", "teachers/lion-pride-lesson-plan.html", "A grade 3 lesson on animal groups using lion pride research, with a high school extension.",
                ["Grade 3", "High school"], ["Lesson plan"], ["3-LS2-1", "HS-LS2-8"], "Why some animals form groups that help members survive"), priority="0.7")

# ---------------------------------------------------------------- RESEARCH
PAPERS = [
 ("Vocal anatomy and roaring", [
  ("Weissengruber, G. E., Forstenpointner, G., Peters, G., K&uuml;bber-Heiss, A., and Fitch, W. T. (2002). Hyoid apparatus and pharynx in the lion (<i>Panthera leo</i>), jaguar (<i>Panthera onca</i>), tiger (<i>Panthera tigris</i>), cheetah (<i>Acinonyx jubatus</i>) and domestic cat (<i>Felis silvestris f. catus</i>). <i>Journal of Anatomy</i>, 201(3), 195-209.", "10.1046/j.1469-7580.2002.00088.x", "blog/which-big-cats-can-roar.html", "Which big cats can roar?"),
  ("Klemuk, S. A., Riede, T., Walsh, E. J., and Titze, I. R. (2011). Adapted to roar: functional morphology of tiger and lion vocal folds. <i>PLoS ONE</i>, 6(11), e27029.", "10.1371/journal.pone.0027029", "blog/which-big-cats-can-roar.html", "Which big cats can roar?")]),
 ("Cheetah locomotion and physiology", [
  ("Wilson, A. M., Lowe, J. C., Roskilly, K., Hudson, P. E., Golabek, K. A., and McNutt, J. W. (2013). Locomotion dynamics of hunting in wild cheetahs. <i>Nature</i>, 498(7453), 185-189.", "10.1038/nature12295", "blog/how-fast-is-a-cheetah.html", "How fast is a cheetah?"),
  ("Hetem, R. S., Mitchell, D., de Witt, B. A., Fick, L. G., Meyer, L. C. R., Maloney, S. K., and Fuller, A. (2013). Cheetah do not abandon hunts because they overheat. <i>Biology Letters</i>, 9(5), 20130472.", "10.1098/rsbl.2013.0472", "blog/how-fast-is-a-cheetah.html", "How fast is a cheetah?")]),
 ("Coat colour and camouflage", [
  ("Fennell, J. G., Talas, L., Baddeley, R. J., Cuthill, I. C., and Scott-Samuel, N. E. (2019). Optimizing colour for camouflage and visibility using deep learning: the effects of the environment and the observer's visual system. <i>Journal of the Royal Society Interface</i>, 16(154), 20190183.", "10.1098/rsif.2019.0183", "blog/why-do-tigers-have-stripes.html", "Why do tigers have stripes?")]),
 ("Lion social behavior", [
  ("Packer, C., Scheel, D., and Pusey, A. E. (1990). Why lions form groups: food is not enough. <i>The American Naturalist</i>, 136(1), 1-19.", "10.1086/285079", "blog/why-do-lions-live-in-prides.html", "Why do lions live in prides?"),
  ("Packer, C., Gilbert, D. A., Pusey, A. E., and O'Brien, S. J. (1991). A molecular genetic analysis of kinship and cooperation in African lions. <i>Nature</i>, 351, 562-565.", "10.1038/351562a0", "blog/why-do-lions-live-in-prides.html", "Why do lions live in prides?"),
  ("Heinsohn, R., and Packer, C. (1995). Complex cooperative strategies in group-territorial African lions. <i>Science</i>, 269(5228), 1260-1262.", "10.1126/science.7652573", "blog/why-do-lions-live-in-prides.html", "Why do lions live in prides?")]),
 ("Population status and conservation", [
  ("Durant, S. M., Mitchell, N., Groom, R., et al. (2017). The global decline of cheetah <i>Acinonyx jubatus</i> and what it means for conservation. <i>Proceedings of the National Academy of Sciences</i>, 114(3), 528-533.", "10.1073/pnas.1611122114", "blog/how-many-big-cats-are-left.html", "How many big cats are left?")]),
]
rb = []
n = 0
for topic, items in PAPERS:
    rb.append('<section class="card"><h2>%s</h2><ul>' % topic)
    for ref, doi, page, label in items:
        n += 1
        rb.append('<li>%s <a href="https://doi.org/%s" rel="noopener">doi:%s</a><br><span class="note">Used in: <a href="../%s">%s</a></span></li>' % (ref, doi, doi, page, label))
    rb.append('</ul></section>')
add("research/index.html", "Big Cat Research Papers: Sources for Students & Researchers | BigCatWise",
    "The peer reviewed big cat research behind BigCatWise: papers on roaring, cheetah speed, tiger camouflage, lion prides and cheetah decline, each with a verified DOI.",
    "For students and researchers: the papers behind BigCatWise", kind="page", headline="Research",
    lead="Every BigCatWise fact article cites its sources. This page gathers the peer reviewed papers we rely on in one place, grouped by topic, with full references and DOIs that we have checked against Crossref. It is a good starting point for a school report or a literature search.",
    body='''<section class="card"><h2>How to use this list</h2><ul>
<li>Click a DOI to open the paper's official page. Many abstracts are free to read; full text may need a library login.</li>
<li>Each entry links to the BigCatWise article that explains the findings in plain English.</li>
<li>For species facts such as weights and population estimates, our main source is the IUCN SSC Cat Specialist Group species pages, linked from each species page.</li></ul></section>''' + "".join(rb) + '''
<section class="card"><h2>Reference organisations</h2><ul>
<li><a href="https://www.catsg.org/" rel="noopener">IUCN SSC Cat Specialist Group</a>: species accounts and status summaries for all wild cats.</li>
<li><a href="https://www.iucnredlist.org/" rel="noopener">IUCN Red List of Threatened Species</a>: official conservation assessments.</li></ul>
<p class="note">References are formatted in APA style. DOIs verified on Crossref on 8 October 2026. If you find a broken link or an error, email <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a>.</p></section>''',
    related=[("Teachers hub", "teachers/index.html"), ("Blog", "blog/index.html"), ("Glossary", "glossary.html")],
    extra_ld=[{"@context": "https://schema.org", "@type": "ItemList", "name": "Peer reviewed papers cited on BigCatWise", "numberOfItems": n,
               "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": {"@type": "ScholarlyArticle", "sameAs": "https://doi.org/" + d,
                                    "identifier": {"@type": "PropertyValue", "propertyID": "DOI", "value": d}, "name": __import__("re").sub("<[^>]+>", "", r).split(". ", 1)[0]}}
                                   for i, (r, d, _, _) in enumerate([x for _, it in PAPERS for x in it])]}],
    priority="0.7")

# ---------------------------------------------------------------- CREDITS
rows = "".join((('<tr><td><a href="../img/%s-960.webp">%s</a></td>' if have(p["slug"]) else '<tr><td><!-- %s -->%s (being added)</td>') + '<td><a href="%s" rel="noopener">%s</a></td><td>%s</td><td><a href="%s" rel="license noopener">%s</a></td><td><a href="../%s">%s</a></td></tr>')
               % (p["slug"], p["slug"], p["page"], p["title"], p["author"], p["licurl"], p["lic"], p["used_on"].replace("index.html", ""), p["used_on"].replace("index.html", "") or "home page")
               for p in PHOTOS_LIST)
add("credits/index.html", "Photo Credits and Licences | BigCatWise",
    "Credits and licences for every photo on BigCatWise: source file, photographer, licence and where each image is used. All photos are CC0 or Creative Commons licensed.",
    "Photo credits and licences", kind="page", headline="Photo credits",
    lead="BigCatWise uses only photos that are free to reuse: public domain (CC0) or Creative Commons Attribution ShareAlike, all from Wikimedia Commons. We checked the licence on each file's own page before use and credit the photographer under every photo and here.",
    body='''<section class="card"><h2>Photos</h2><div class="tablewrap"><table><thead><tr><th>File on BigCatWise</th><th>Source file page</th><th>Author</th><th>Licence</th><th>Used on</th></tr></thead><tbody>''' + rows + '''</tbody></table></div>
<p class="note">Our copies are resized, cropped to a 3:2 frame and converted to WebP; no other changes were made. Photos licensed CC BY-SA remain under that licence, so you may reuse our resized copies under the same licence with credit to the photographer. Licences checked 8 October 2026.</p></section>
<section class="card"><h2>Illustrations, games and fonts</h2><p>The logo, icons, paw doodles, game art and diagrams are original works drawn in code by BigCatWise. Games are original works &copy; 2026 Joshua Israel Ventures LLC; see the <a href="../games/CREDITS.md">games credits file</a>. Fonts: Fredoka and Nunito from Google Fonts, under the SIL Open Font License 1.1.</p>
<p>Think a photo is credited wrongly? Email <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a> and we will fix or remove it promptly.</p></section>''',
    related=[("About", "about.html"), ("Terms of use", "terms.html"), ("Games", "games/index.html")], priority="0.3")

# Cite box and visible "Last reviewed" date on the printable, lesson and research pages
from build import PAGES  # noqa: E402
for _p in PAGES:
    if _p.path.startswith(("teachers/big-cat-", "teachers/answer-keys", "teachers/cheetah-", "teachers/lion-", "research/")):
        _p.cite = True
        _p.reviewed = "2026-10-08"
