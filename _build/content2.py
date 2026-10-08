from build import add, BASE_URL, PAGES, TODAY, CF_BEACON_TOKEN
from sources import CSG, SDZ, PAN, WWF, NZP, IUCN, WILSON, DURANT, KLEMUK, WEISS, FENNELL, SLT
from content import jump

ALLCSG = [CSG[k] for k in ("lion", "tiger", "leopard", "jaguar", "cheetah", "snow")]
SP = [("Lion", "lion.html"), ("Tiger", "tiger.html"), ("Leopard", "leopard.html"), ("Jaguar", "jaguar.html"),
      ("Cheetah", "cheetah.html"), ("Snow leopard", "snow-leopard.html")]

# ------------------------------------------------------------------ COMPARE (unique asset)
ROWS = [
 ("lion", "Lion", "<i>Panthera leo</i>", "110 to 272 kg", "137 to 250 cm", "Sub-Saharan Africa; Gir, India", "Savanna, grassland, open woodland", "Prides; male coalitions", "Yes", "Vulnerable", "About 22,000 to 25,000 adults and subadults in Africa (2025) plus about 670 in India (2020)"),
 ("tiger", "Tiger", "<i>Panthera tigris</i>", "75 to 325 kg", "150 to 230 cm", "South, Southeast and East Asia; Russian Far East", "Forests, mangroves, grassland", "Solitary", "Yes", "Endangered", "3,726 to 5,578 excluding cubs"),
 ("leopard", "Leopard", "<i>Panthera pardus</i>", "17 to 90 kg", "91 to 191 cm", "Sub-Saharan Africa; scattered across Asia", "Almost any habitat with cover", "Solitary", "Yes", "Vulnerable", "No reliable global estimate"),
 ("jaguar", "Jaguar", "<i>Panthera onca</i>", "36 to 148 kg", "110 to 170 cm", "Mexico to northern Argentina", "Rainforest, wetlands, dry forest", "Solitary", "Yes", "Near Threatened", "57,000 to 64,000 in Amazonia (about 89% of the total)"),
 ("cheetah", "Cheetah", "<i>Acinonyx jubatus</i>", "23 to 65 kg", "113 to 140 cm", "Southern and eastern Africa; Sahara; Iran", "Savanna, grassland, dry woodland, desert", "Females solitary; male coalitions", "No", "Vulnerable", "About 6,500 mature individuals"),
 ("snow-leopard", "Snow leopard", "<i>Panthera uncia</i>", "30 to 50 kg", "90 to 120 cm", "Mountains of Central and South Asia", "Alpine and subalpine mountains", "Solitary", "No", "Vulnerable", "7,446 to 7,996 (2,710 to 3,386 mature)"),
]
table = ('<div class="tablewrap"><table><thead><tr><th>Species</th><th>Weight</th><th>Head and body</th><th>Range</th><th>Main habitats</th>'
         '<th>Social life</th><th>Roars?</th><th>IUCN status</th><th>Population estimate</th></tr></thead><tbody>' +
         "".join('<tr id="row-%s"><td><a href="%s.html">%s</a><br><span class="sci">%s</span></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % ((r[0],) + tuple(r))
                 for r in ROWS) + '</tbody></table></div>')
add("compare.html", "Big Cat Comparison Table: Size, Range, Status & Population | BigCatWise",
    "Compare lions, tigers, leopards, jaguars, cheetahs and snow leopards side by side: weight, length, range, habitat, social life, roaring, IUCN status and numbers.",
    "Big cat comparison: size, range, status and population",
    lead="The tiger is the largest big cat, the lion is the only social one, the leopard has the widest range, the jaguar is the only big cat in the Americas, the cheetah is the fastest, and the snow leopard lives highest. The table below compares all six on size, range, habitat, social life, voice, IUCN Red List status and the latest population estimates.",
    headline="Big cat comparison table",
    body=jump([("table", "Comparison table"), ("biggest", "Biggest"), ("which-roar", "Which roar"), ("tell-apart", "Spotted cats"), ("status", "Status ranking"), ("definition", "What is a big cat")]) +
    '<section class="card" id="table"><h2>Big cat comparison table</h2><p>Weights and lengths are the full ranges listed by the IUCN SSC Cat Specialist Group for each species, covering both sexes and all populations. Tap a species name for its full profile.</p>' + table +
    '<p class="note">Population figures come from the most recent IUCN Cat Specialist Group summaries cited on each species page. They are estimates with wide uncertainty, and the counting methods differ between species, so compare them with care.</p></section>' +
    '''<section class="card" id="biggest"><h2>Which big cat is the biggest?</h2>
<p>The tiger is the largest, at up to about 325 kg. The lion is second, and the largest male lions overlap with smaller tigers. The jaguar is third and the largest cat in the Americas. Leopards, snow leopards and cheetahs are much lighter, though a big male leopard can outweigh a cheetah. The cheetah is built light for speed rather than power.</p></section>
<section class="card" id="which-roar"><h2>Which big cats roar?</h2>
<p>Lions, tigers, leopards and jaguars can roar. Snow leopards cannot, despite being in the same genus, and cheetahs cannot either; cheetahs purr and chirp instead. Details in <a href="blog/which-big-cats-can-roar.html">which big cats can roar</a>.</p></section>
<section class="card" id="tell-apart"><h2>How to tell the spotted cats apart</h2>
<ul><li><b>Cheetah:</b> solid round spots, black tear marks from eye to mouth, slim build, small head, long legs.</li>
<li><b>Leopard:</b> rosettes usually without a central spot, medium build; Africa and Asia only.</li>
<li><b>Jaguar:</b> larger rosettes usually with spots inside, stocky build, big head, shorter tail; Americas only.</li>
<li><b>Snow leopard:</b> smoky grey coat, very long thick tail, high mountains of Asia.</li></ul>
<p>Full guides: <a href="which-big-cat-is-it.html">which big cat is it? ID guide</a> and <a href="blog/leopard-vs-jaguar-vs-cheetah.html">leopard vs jaguar vs cheetah</a>.</p></section>
<section class="card" id="status"><h2>Which big cat is most endangered?</h2>
<p>On the IUCN Red List the tiger is the only one of the six listed as Endangered at species level. Lion, leopard, cheetah and snow leopard are Vulnerable, and the jaguar is Near Threatened. Species level labels hide serious local crises, though: the Asiatic cheetah in Iran and the Indochinese leopard are Critically Endangered, and the northern lion subspecies is Endangered. See <a href="conservation.html">big cat conservation</a> and <a href="blog/how-many-big-cats-are-left.html">how many big cats are left</a>.</p></section>
<section class="card" id="definition"><h2>What counts as a big cat?</h2>
<p>Strictly, "big cats" means the five members of the genus <i>Panthera</i>: lion, tiger, leopard, jaguar and snow leopard. In everyday use the cheetah is usually included, and sometimes the puma (cougar) and clouded leopards too. This site covers the five <i>Panthera</i> species plus the cheetah.</p></section>''',
    related=SP + [("Big cat FAQ", "faq.html")], sources=ALLCSG + [DURANT, IUCN], priority="1.0")

# ------------------------------------------------------------------ BEHAVIOR
add("behavior.html", "Big Cat Behavior: Hunting, Social Life, Roaring & Territory | BigCatWise",
    "How big cats behave: who lives in groups and who lives alone, how each species hunts, how they communicate by roaring and scent marking, and how cubs grow up.",
    "Big cat behavior: hunting, social life and communication",
    lead="Most big cats are solitary, territorial hunters that rely on stealth and ambush. The lion is the exception, living in prides, and the cheetah is the odd one out as a daytime sprinter. All of them communicate over long distances with scent marks and calls, and mothers raise cubs alone for a year or two.",
    headline="Big cat behavior",
    body=jump([("social", "Social life"), ("hunting", "Hunting styles"), ("communication", "Communication"), ("territory", "Territories"), ("cubs", "Cubs"), ("activity", "Activity")]) +
    '''<section class="card" id="social"><h2>Do big cats live in groups?</h2>
<p>Only lions live in stable social groups. A pride is built around related females, with an average of four to six adult lionesses in Africa, plus their cubs and one or more resident males. Male lions and male cheetahs often form coalitions, frequently of brothers, which helps them win and hold territory. Tigers, leopards, jaguars and snow leopards are solitary as adults; males and females meet mainly to mate, and mothers raise cubs on their own.</p></section>
<section class="card" id="hunting"><h2>How do big cats hunt?</h2>
<div class="tablewrap"><table><thead><tr><th>Species</th><th>Main hunting style</th><th>Typical prey</th></tr></thead><tbody>
<tr><td><a href="lion.html">Lion</a></td><td>Group stalking and ambush; also scavenging</td><td>Wildebeest, zebra, buffalo, antelope</td></tr>
<tr><td><a href="tiger.html">Tiger</a></td><td>Solitary stalk and ambush, then drags kill to cover</td><td>Deer such as chital and sambar, gaur, wild pig</td></tr>
<tr><td><a href="leopard.html">Leopard</a></td><td>Close stalk and short rush; often caches kills in trees</td><td>Very broad, from hyraxes to eland</td></tr>
<tr><td><a href="jaguar.html">Jaguar</a></td><td>Ambush, often near water; skull piercing bite</td><td>Peccaries, capybaras, caiman, turtles, fish</td></tr>
<tr><td><a href="cheetah.html">Cheetah</a></td><td>Stalk then high speed chase over a short distance, by day</td><td>Gazelles, impala, springbok</td></tr>
<tr><td><a href="snow-leopard.html">Snow leopard</a></td><td>Stalk from above and chase down steep slopes</td><td>Wild sheep and goats such as bharal and ibex</td></tr>
</tbody></table></div>
<p>Ambush hunting means most attempts fail, so big cats need large areas with plenty of prey. A tiger, for example, is estimated to need around 50 to 60 large prey animals a year. That is why loss of prey to hunting by people is a serious threat on its own.</p></section>
<section class="card" id="communication"><h2>How do big cats communicate?</h2>
<p><b>Roars and calls.</b> Lions, tigers, leopards and jaguars can roar; a lion's roar carries over several kilometres and helps pride members find each other and warn rivals off. Leopards make a repeated rasping call often likened to sawing wood. Snow leopards and cheetahs cannot roar. Cheetahs purr and chirp. See <a href="blog/which-big-cats-can-roar.html">which big cats can roar</a>.</p>
<p><b>Scent.</b> Big cats spray urine on trees and rocks, leave droppings in prominent places and scrape the ground with their hind feet. These marks tell neighbours who lives there, and whether a female is ready to breed. You may see a cat curl its lip while sniffing a mark; this is the flehmen response, which draws scent towards an organ in the roof of the mouth.</p>
<p><b>Visual signals.</b> Lions' manes, ear markings on tigers (white spots on the backs of the ears) and tail postures all carry information at close range.</p></section>
<section class="card" id="territory"><h2>How big are big cat territories?</h2>
<p>Territory size tracks prey. Figures from the IUCN Cat Specialist Group show the range:</p>
<ul><li><b>Tiger:</b> females 10 to 39 km&sup2; in prey rich Chitwan, Nepal, but 100 to 400 km&sup2; in the Russian Far East, where one male used 1,379 km&sup2;.</li>
<li><b>Lion:</b> pride territories of 50 to 200 km&sup2; where prey is dense, up to 500 to 5,000 km&sup2; where it is scarce.</li>
<li><b>Leopard:</b> roughly 30 to 78 km&sup2; for males and 15 to 38 km&sup2; for females in African protected areas, but over 2,000 km&sup2; in the Kalahari.</li>
<li><b>Cheetah:</b> territorial males hold small territories averaging about 30 km&sup2;, while non territorial cheetahs can roam over thousands of square kilometres.</li></ul></section>
<section class="card" id="cubs"><h2>How do big cats raise their cubs?</h2>
<p>Cubs are born blind and helpless after a pregnancy of roughly three to three and a half months (about 103 days in tigers, 90 to 105 days in leopards). Litters are usually one to four or five cubs, and cheetahs can have up to six. Mothers hide young cubs and move them between dens. Cubs learn to hunt by watching and practising for many months; young tigers become independent at about 18 to 28 months. Cub mortality is high: in Chitwan about a third of tiger cubs die in their first year, with infanticide by males a leading cause.</p></section>
<section class="card" id="activity"><h2>Are big cats nocturnal?</h2>
<p>Most big cats are most active from dusk to dawn, and they rest for much of the day. Activity shifts with heat, prey and people: leopards in undisturbed Gabonese rainforest were found to be largely active by day, while cats near people tend to become more nocturnal. The cheetah is the clear exception, hunting mainly in daylight, which helps it avoid lions and hyenas.</p></section>''',
    related=SP + [("Where big cats live", "habitats.html"), ("Big cat glossary", "glossary.html")],
    sources=ALLCSG + [WILSON, SDZ["lion"]], priority="0.8")

# ------------------------------------------------------------------ HABITATS
add("habitats.html", "Where Do Big Cats Live? Habitats & Range by Species | BigCatWise",
    "Where lions, tigers, leopards, jaguars, cheetahs and snow leopards live: continents, habitats from rainforest to 5,000 m mountains, and which species share ranges.",
    "Where do big cats live? Habitats and range by species",
    lead="Big cats live in Africa, Asia and the Americas. Africa has lions, leopards and cheetahs; Asia has tigers, leopards, snow leopards, a few lions in India and a handful of cheetahs in Iran; the Americas have only the jaguar. Their habitats run from savanna and desert to rainforest, mangroves and mountains above 5,000 m.",
    headline="Big cat habitats",
    body=jump([("continents", "By continent"), ("types", "By habitat"), ("elevation", "Elevation"), ("shared", "Shared ranges"), ("shrinking", "Shrinking ranges")]) +
    '''<section class="card" id="continents"><h2>Which big cats live on each continent?</h2>
<div class="tablewrap"><table><thead><tr><th>Region</th><th>Big cats</th></tr></thead><tbody>
<tr><td>Africa</td><td><a href="lion.html">Lion</a>, <a href="leopard.html">leopard</a>, <a href="cheetah.html">cheetah</a></td></tr>
<tr><td>South Asia</td><td><a href="tiger.html">Tiger</a>, leopard, <a href="snow-leopard.html">snow leopard</a>, Asiatic lion (Gir, India only)</td></tr>
<tr><td>Southeast and East Asia</td><td>Tiger, leopard (fragmented), snow leopard (China, Mongolia)</td></tr>
<tr><td>Central Asia and the Middle East</td><td>Snow leopard, leopard (rare), Asiatic cheetah (Iran only)</td></tr>
<tr><td>Russian Far East</td><td>Amur tiger, Amur leopard</td></tr>
<tr><td>The Americas</td><td><a href="jaguar.html">Jaguar</a></td></tr>
<tr><td>Europe, Australia, Antarctica</td><td>No wild big cats today</td></tr>
</tbody></table></div></section>
<section class="card" id="types"><h2>What habitats do big cats use?</h2>
<p><b>Savanna and grassland.</b> The classic home of lions and cheetahs in eastern and southern Africa, shared with leopards wherever there is cover such as riverine trees and rocky outcrops.</p>
<p><b>Tropical forest.</b> Jaguars in the Amazon, leopards in Central African rainforest and tigers in South and Southeast Asian forests.</p>
<p><b>Wetlands and mangroves.</b> Jaguars thrive in the seasonally flooded Pantanal and along Amazon rivers; tigers live in the Sundarbans mangroves of India and Bangladesh.</p>
<p><b>Temperate forest.</b> Amur tigers and Amur leopards live in snowy mixed forests of the Russian Far East and northeastern China.</p>
<p><b>Desert and semi desert.</b> Cheetahs survive at very low densities in the Sahara, and leopards persist in arid mountains of Arabia and southwest Asia.</p>
<p><b>High mountains.</b> Snow leopards live on rugged slopes, cliffs and alpine meadows, typically at 3,000 to 5,000 m.</p></section>
<section class="card" id="elevation"><h2>How high do big cats live?</h2>
<ul><li>Snow leopards typically 3,000 to 5,000 m, occasionally above 5,500 m in the Himalayas, but as low as 600 to 2,500 m at the northern edge of their range.</li>
<li>Leopards have been recorded up to 5,200 m in the Himalayas and 4,600 m on Mount Kenya.</li>
<li>Lions have been recorded up to 4,240 m in Ethiopia's Bale Mountains.</li>
<li>Cheetahs have been recorded up to 4,000 m on Mount Kenya.</li>
<li>Jaguars are mostly below 1,000 m, but have been reported up to 3,800 m.</li></ul></section>
<section class="card" id="shared"><h2>Where do big cats share territory?</h2>
<p>In much of eastern and southern Africa, lions, leopards and cheetahs live side by side. Lions are dominant: they steal kills and kill cubs of the other two, so leopards cache food in trees and cheetahs hunt by day and often do best where lions are scarce, including on farmland. In parts of India and Nepal, tigers and leopards share forests, with leopards tending to use edges and areas near villages. In the Himalayas, leopards and snow leopards can meet where forests give way to open alpine slopes.</p></section>
<section class="card" id="shrinking"><h2>How much of their range have big cats lost?</h2>
<p>All six species occupy only part of their former ranges. Less than 7 percent of the tiger's original range remains; lions held about 6 percent of their historical range in 2025; and cheetahs are confined to around 9 percent of theirs. Leopard range shrank by 11 percent between 2016 and 2023 alone. Read <a href="conservation.html">big cat conservation</a> for the causes.</p></section>''',
    related=SP + [("Which big cat is it? ID guide", "which-big-cat-is-it.html"), ("Big cat behavior", "behavior.html"), ("Compare big cats", "compare.html")],
    sources=ALLCSG + [DURANT], priority="0.8")

# ------------------------------------------------------------------ CONSERVATION
add("conservation.html", "Big Cat Conservation: Status, Threats & What Helps | BigCatWise",
    "Big cat conservation explained: IUCN Red List status for all six species, latest population estimates, the main threats, and the measures that actually help.",
    "Big cat conservation: status, threats and what helps",
    lead="All six big cats covered here are declining or depend on ongoing protection. On the IUCN Red List the tiger is Endangered; the lion, leopard, cheetah and snow leopard are Vulnerable; and the jaguar is Near Threatened. The main threats are loss of habitat and prey, killing in conflicts over livestock, and poaching for the illegal wildlife trade.",
    headline="Big cat conservation",
    body=jump([("status", "Status table"), ("threats", "Threats"), ("helps", "What helps"), ("cites", "Trade protection"), ("you", "How you can help")]) +
    '''<section class="card" id="status"><h2>Conservation status of each big cat</h2>
<div class="tablewrap"><table><thead><tr><th>Species</th><th>IUCN Red List</th><th>Population estimate</th><th>Trend notes</th></tr></thead><tbody>
<tr><td><a href="tiger.html">Tiger</a></td><td>Endangered</td><td>3,726 to 5,578 excluding cubs</td><td>Range down by more than half over three generations; Green Status Critically Depleted (2025)</td></tr>
<tr><td><a href="lion.html">Lion</a></td><td>Vulnerable</td><td>About 22,000 to 25,000 in Africa (2025); about 670 in India (2020)</td><td>Stable or rising in southern Africa; steep losses in West and Central Africa</td></tr>
<tr><td><a href="leopard.html">Leopard</a></td><td>Vulnerable</td><td>No reliable global estimate</td><td>Range fell 11% from 2016 to 2023; collapse in Southeast Asia</td></tr>
<tr><td><a href="cheetah.html">Cheetah</a></td><td>Vulnerable</td><td>About 6,500 mature individuals</td><td>Most assessed subpopulations declining; Asiatic cheetah under 50 mature adults</td></tr>
<tr><td><a href="snow-leopard.html">Snow leopard</a></td><td>Vulnerable</td><td>7,446 to 7,996 (2,710 to 3,386 mature)</td><td>Further decline of about 10% projected</td></tr>
<tr><td><a href="jaguar.html">Jaguar</a></td><td>Near Threatened</td><td>57,000 to 64,000 in Amazonia (about 89% of the total)</td><td>Most of 34 subpopulations Endangered or Critically Endangered</td></tr>
</tbody></table></div>
<p class="note">Figures are taken from IUCN SSC Cat Specialist Group summaries; see each species page for detail. A new global jaguar assessment is expected around 2027.</p></section>
<section class="card" id="threats"><h2>What are the biggest threats to big cats?</h2>
<ol><li><b>Habitat loss and fragmentation.</b> Farms, plantations, roads and settlements break habitat into islands too small for viable populations, and cut the corridors cats use to move between them.</li>
<li><b>Prey depletion.</b> Snaring and hunting for bushmeat, and competition with livestock, empty landscapes of the animals big cats eat, even inside protected areas.</li>
<li><b>Conflict with people.</b> When cats kill livestock, or occasionally people, they are often shot, trapped or poisoned in retaliation. This is a leading threat to lions, jaguars, snow leopards and cheetahs.</li>
<li><b>Poaching and illegal trade.</b> Tiger skins and bones are in demand, and as tigers have become scarce, trade has shifted to lion, leopard and jaguar parts. Cheetah cubs are taken for the illegal pet trade, particularly in the Horn of Africa.</li>
<li><b>Small, isolated populations.</b> Groups such as the Asiatic lions in Gir or the Amur leopards face inbreeding and the risk that one disease outbreak or disaster could wipe them out.</li></ol></section>
<section class="card" id="helps"><h2>What actually helps big cats?</h2>
<ul><li><b>Well managed protected areas</b> with enough rangers and funding. India's Project Tiger, launched in 1973, created a network of tiger reserves, and the IUCN's Green Status work finds tigers would be far worse off without such efforts.</li>
<li><b>Wildlife corridors</b> that connect populations so animals can disperse and breed between them.</li>
<li><b>Reducing conflict</b> with predator proof livestock enclosures (corrals and bomas), herding and guarding, livestock insurance and compensation schemes, and vaccination programmes that keep herds healthier.</li>
<li><b>Restoring prey</b> by tackling snaring and overhunting.</li>
<li><b>Anti poaching and anti trafficking work</b> along trade routes, plus reducing consumer demand.</li>
<li><b>Community based conservation</b> so that people who live alongside big cats benefit from them, for example through tourism income or jobs.</li>
<li><b>Reintroductions and translocations</b> where habitat is ready, such as plans to return tigers to Kazakhstan and Cambodia and India's cheetah project at Kuno National Park.</li></ul></section>
<section class="card" id="cites"><h2>Is trade in big cats illegal?</h2>
<p>International commercial trade in tigers, leopards, jaguars, cheetahs and snow leopards is banned under Appendix I of CITES, the Convention on International Trade in Endangered Species. Asiatic lions are on Appendix I; African lions are on Appendix II, which allows strictly regulated trade. Many range countries also ban hunting and domestic trade, though enforcement varies.</p></section>
<section class="card" id="you"><h2>How can you help big cats?</h2>
<ul><li>Support established conservation organisations that publish their results.</li>
<li>Never buy products made from wild cats, including skins, teeth, claws, bone wine or "medicines".</li>
<li>Avoid attractions that offer cub petting, walking with lions or photos with big cats; conservation groups warn these can feed the captive breeding and parts trade.</li>
<li>If you travel to see big cats, choose operators that keep their distance, follow park rules and support local communities.</li>
<li>Share accurate information. Correcting myths, like the idea that tigers live in Africa, helps people care about the real animals.</li></ul></section>''',
    related=SP + [("How many big cats are left?", "blog/how-many-big-cats-are-left.html"), ("Compare big cats", "compare.html")],
    sources=ALLCSG + [DURANT, WWF["tiger"], PAN["lion"], IUCN], priority="0.9")

# ------------------------------------------------------------------ FAQ
FAQ = [
 ("What animals count as big cats?", "Strictly, the five species of the genus Panthera: lion, tiger, leopard, jaguar and snow leopard. In everyday use the cheetah is usually included too, and sometimes the puma and clouded leopards."),
 ("What is the biggest big cat?", "The tiger, at up to about 325 kg. The lion is second and the jaguar third."),
 ("What is the smallest big cat?", "Of the six covered here, the cheetah and snow leopard are the lightest, and small female leopards can weigh as little as about 17 kg."),
 ("Which big cat is the fastest?", "The cheetah. A study of wild cheetahs measured a top speed of 25.9 m/s, about 93 km/h, and the IUCN Cat Specialist Group gives up to about 103 km/h."),
 ("Can all big cats roar?", "No. Lions, tigers, leopards and jaguars can roar. Snow leopards and cheetahs cannot."),
 ("What is a black panther?", "A leopard or jaguar with melanism, a genetic variation that makes the fur very dark. It is not a separate species, and the rosettes are still faintly visible."),
 ("Are white tigers a separate species?", "No. White tigers are a rare colour variant of the tiger. The IUCN Cat Specialist Group notes that the last documented white tiger in the wild was shot in India in 1958."),
 ("Do lions live in the jungle?", "No. Lions live mainly in savanna, grassland and open woodland. King of the jungle is just a nickname."),
 ("Are there tigers in Africa?", "No. Wild tigers live only in Asia. Africa's big cats are the lion, leopard and cheetah."),
 ("Which big cat lives in the Americas?", "The jaguar, from Mexico to northern Argentina. The puma also lives there but is not usually counted as a big cat."),
 ("Which big cat is the most endangered?", "At species level, the tiger, which is listed as Endangered. Some populations of other species are worse off, such as the Critically Endangered Asiatic cheetah in Iran."),
 ("Is the snow leopard a leopard?", "No. It is a separate species, Panthera uncia. Genetic studies suggest its closest living relative is the tiger."),
 ("Can big cats purr?", "Cheetahs purr. Whether the roaring cats truly purr is debated, and they generally do not purr continuously the way domestic cats do."),
 ("How long do big cats live?", "In the wild most live about 10 to 15 years, with ranges for each species listed on its profile page. Lifespans in zoos are often longer."),
 ("Are big cats dangerous to people?", "They can be. Attacks on people do happen but are uncommon, and most big cats avoid people. Conflicts are more often about livestock. Follow local guidance in big cat areas and never approach a wild cat."),
]
add("faq.html", "Big Cat FAQ: Myths, Records & Quick Answers | BigCatWise",
    "Quick, sourced answers to common big cat questions: which cats count as big cats, the biggest and fastest, black panthers, white tigers, roaring and more.",
    "Big cat FAQ: quick answers and common myths",
    lead="Short answers to the questions people ask most about lions, tigers, leopards, jaguars, cheetahs and snow leopards, including the common myths. Each answer links to a fuller explanation elsewhere on the site.",
    kind="article", headline="Big cat FAQ",
    body='<section class="card"><h2>Myths vs facts</h2><ul><li class="myth">Myth: lions are the king of the jungle.</li><li class="fact">Fact: lions live in savanna and open woodland, not rainforest. <a href="lion.html#range">Lion range</a></li><li class="myth">Myth: black panthers are their own species.</li><li class="fact">Fact: they are melanistic leopards or jaguars. <a href="leopard.html#black">Black panthers</a></li><li class="myth">Myth: tigers live in Africa.</li><li class="fact">Fact: wild tigers live only in Asia. <a href="tiger.html#range">Tiger range</a></li><li class="myth">Myth: every big cat roars.</li><li class="fact">Fact: snow leopards and cheetahs cannot roar. <a href="blog/which-big-cats-can-roar.html">Which cats roar</a></li></ul></section>',
    faq=FAQ, related=SP + [("Which big cat is it? ID guide", "which-big-cat-is-it.html"), ("Compare big cats", "compare.html"), ("Big cat glossary", "glossary.html")],
    sources=ALLCSG + [WILSON, KLEMUK], priority="0.8")

# ------------------------------------------------------------------ GLOSSARY
GL = [("Apex predator", "A predator at the top of its food chain with no natural predators as a healthy adult."),
 ("Bharal", "Also called blue sheep; a wild mountain sheep that is a key prey of snow leopards."),
 ("Camera trap", "A remote camera triggered by movement. Because tiger stripes and leopard rosettes are unique, camera trap photos can identify individuals for population counts."),
 ("Capture recapture", "A survey method that estimates population size from how often known individuals are detected again, widely used with camera traps."),
 ("CITES", "The Convention on International Trade in Endangered Species. Appendix I bans international commercial trade; Appendix II allows regulated trade."),
 ("Coalition", "A group of male lions or cheetahs, often brothers, that live and defend territory together."),
 ("Crepuscular", "Most active at dawn and dusk."),
 ("Felid", "Any member of the cat family, Felidae."),
 ("Flehmen response", "A lip curling grimace that draws scent towards the vomeronasal (Jacobson's) organ in the roof of the mouth."),
 ("Green Status of Species", "An IUCN assessment that measures how far a species is from full recovery and how much conservation has helped. The tiger was rated Critically Depleted in 2025."),
 ("Home range", "The whole area an animal uses in its normal activities. Compare territory."),
 ("Human wildlife conflict", "Situations where wildlife and people come into conflict, for example big cats killing livestock and people killing cats in retaliation."),
 ("IUCN Red List", "The global list of species' extinction risk. Categories include Least Concern, Near Threatened, Vulnerable, Endangered, Critically Endangered, Extinct in the Wild and Extinct."),
 ("Mature individuals", "Adults capable of breeding. Red List population figures often count only these, so they are lower than total counts."),
 ("Melanism", "A genetic variation causing very dark fur. Melanistic leopards and jaguars are called black panthers."),
 ("Panthera", "The genus of roaring cats: lion, tiger, leopard, jaguar and snow leopard."),
 ("Pride", "A lion social group of related females, their cubs and one or more resident males."),
 ("Prey base", "The wild animals available for a predator to eat in an area."),
 ("Rosette", "A rose shaped cluster of dark spots, typical of leopards, jaguars and snow leopards."),
 ("Scrape", "A mark made by scraping the ground with the hind feet, often with urine or scent, to signal presence."),
 ("Semi retractable claws", "Claws that cannot be fully pulled in, as in the cheetah, giving extra grip when running."),
 ("Stalk and ambush", "Hunting by creeping close under cover and then attacking with a short rush."),
 ("Subspecies", "A distinct population within a species, often geographically separate. Tiger and leopard subspecies are under active scientific review."),
 ("Territory", "The part of a home range that an animal actively defends against others of its kind."),
 ("Ungulate", "A hoofed mammal, such as deer, antelope, wild pig or buffalo. Ungulates are the main prey of most big cats."),
 ("Wildlife corridor", "A strip of habitat that links populations so animals can move and breed between them.")]
add("glossary.html", "Big Cat Glossary: Terms Explained Simply | BigCatWise",
    "Plain English definitions of big cat terms: pride, coalition, rosette, melanism, flehmen response, IUCN Red List categories, CITES appendices and more.",
    "Big cat glossary",
    lead="Definitions of the terms you will meet when reading about big cats, from pride and rosette to IUCN Red List categories and CITES appendices.",
    kind="page", headline="Big cat glossary",
    body='<section class="card"><dl>' + "".join('<dt id="%s">%s</dt><dd>%s</dd>' % (t.lower().replace(" ", "-"), t, d) for t, d in GL) + '</dl></section>',
    related=SP + [("Big cat FAQ", "faq.html")], sources=[IUCN] + ALLCSG[:2], priority="0.6")

import blog  # noqa  registers blog posts
import content3  # noqa  ID guide
from blog import POSTS

# ------------------------------------------------------------------ HOME
tiles = "".join('<a class="tile" href="%s"><h3>%s</h3><p>%s</p></a>' % t for t in [
 ("lion.html", "Lion", "The only social big cat"), ("tiger.html", "Tiger", "The largest cat on Earth"),
 ("leopard.html", "Leopard", "The most widespread big cat"), ("jaguar.html", "Jaguar", "Big cat of the Americas"),
 ("cheetah.html", "Cheetah", "The fastest land animal"), ("snow-leopard.html", "Snow leopard", "Ghost of the mountains"),
 ("which-big-cat-is-it.html", "Which big cat is it?", "ID guide and big cats by region"), ("compare.html", "Compare all six", "Size, range, status, numbers"), ("behavior.html", "Behavior", "Hunting, prides, roaring"),
 ("habitats.html", "Habitats", "Where each species lives"), ("conservation.html", "Conservation", "Threats and what helps"),
 ("faq.html", "FAQ and myths", "Quick answers"), ("glossary.html", "Glossary", "Terms explained"), ("blog/index.html", "Blog", "Answers to big cat questions")])
posts = "".join('<li><a href="blog/%s">%s</a></li>' % (p.path.split("/")[1], p.headline or p.h1) for p in POSTS)
add("index.html", "BigCatWise: Big Cat Facts on Lions, Tigers, Leopards & More",
    "BigCatWise is a free, sourced guide to big cats: lions, tigers, leopards, jaguars, cheetahs and snow leopards. Species facts, behavior, habitats and conservation.",
    "Big cat facts: lions, tigers, leopards, jaguars, cheetahs and snow leopards", kind="home",
    body='''<section class="hero"><p class="lead">BigCatWise is a free, plain English guide to the world's big cats. It covers what each species looks like, how it hunts and lives, where it is found and how it is faring in the wild, with sources from the IUCN Cat Specialist Group, leading zoos, conservation groups and peer reviewed research.</p>
<a class="btn" href="compare.html">Compare all six big cats</a> <a class="btn alt" href="which-big-cat-is-it.html">Which big cat is it?</a></section>
<div class="grid">''' + tiles + '''</div>
<section class="card"><h2>Big cats at a glance</h2><ul>
<li>The <a href="tiger.html">tiger</a> is the largest cat, at up to about 325 kg, and every tiger's stripes are unique.</li>
<li>The <a href="lion.html">lion</a> is the only big cat that lives in groups, called prides.</li>
<li>The <a href="leopard.html">leopard</a> has the widest range, across Africa and Asia.</li>
<li>The <a href="jaguar.html">jaguar</a> is the only big cat in the Americas and kills prey with a skull piercing bite.</li>
<li>The <a href="cheetah.html">cheetah</a> is the fastest land animal; wild cheetahs have been measured at 93 km/h.</li>
<li>The <a href="snow-leopard.html">snow leopard</a> lives at 3,000 to 5,000 m and cannot roar.</li>
<li>All six are listed on the IUCN Red List as Near Threatened or worse. See <a href="conservation.html">conservation</a>.</li></ul></section>
<section class="card"><h2>Latest from the blog</h2><ul>''' + posts + '''</ul></section>''',
    priority="1.0")

# ------------------------------------------------------------------ TRUST PAGES
add("about.html", "About BigCatWise: Who We Are & How We Write | BigCatWise",
    "About BigCatWise: an independent big cat education site operated by Joshua Israel Ventures LLC. How we research, source and update our content.",
    "About BigCatWise", kind="page", headline="About",
    lead="BigCatWise is a brand of Joshua Israel Ventures LLC: an independent educational website about the world's big cats.",
    body='''<section class="card"><h2>What we cover</h2><p>We explain the biology, behavior, habitats and conservation of six species: the lion, tiger, leopard, jaguar, cheetah and snow leopard. Our aim is clear, accurate, answer first pages that are useful to students, teachers, travellers and anyone curious about big cats.</p></section>
<section class="card"><h2>How we write and source</h2><p>All text and illustrations on this site are original. Facts and figures are drawn from reputable sources, principally the IUCN SSC Cat Specialist Group and IUCN Red List, Smithsonian's National Zoo and Conservation Biology Institute, San Diego Zoo Wildlife Alliance, WWF, Panthera, the Snow Leopard Trust and peer reviewed research. Each page lists its sources and shows when it was last updated. We do not claim field expertise we do not have, and we do not invent statistics.</p>
<p>Wild population estimates change as new surveys are published. If you spot something out of date or wrong, please <a href="contact.html">tell us</a> and we will check and correct it.</p></section>
<section class="card"><h2>Who runs BigCatWise</h2><p>BigCatWise is a brand of Joshua Israel Ventures LLC. The site is owned and operated by Joshua Israel Ventures LLC. The site carries no advertising or affiliate links at present; if that changes, we will say so clearly on the affected pages and in our <a href="privacy.html">privacy policy</a>.</p></section>''',
    related=[("Contact", "contact.html"), ("Terms of use", "terms.html"), ("Privacy", "privacy.html"), ("Disclaimer", "disclaimer.html"), ("Compare big cats", "compare.html")], priority="0.4")

add("contact.html", "Contact BigCatWise | BigCatWise",
    "Contact the BigCatWise team with questions, corrections or suggestions about our big cat guides. Email us or use the contact form.",
    "Contact BigCatWise", kind="page", headline="Contact",
    lead='Questions, corrections or ideas for a new guide? Email <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a> or use the form below.',
    body='''<section class="card"><h2>Send us a message</h2>
<form class="contact" action="https://formsubmit.co/joshuaofisrael@gmail.com" method="POST">
<input type="hidden" name="_subject" value="BigCatWise contact"><input type="hidden" name="_template" value="table">
<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
<input type="hidden" name="_captcha" value="false">
<label for="name">Name</label><input id="name" type="text" name="name" required>
<label for="email">Email</label><input id="email" type="email" name="email" required>
<label for="message">Message</label><textarea id="message" name="message" rows="6" required></textarea>
<button class="btn" type="submit">Send message</button></form>
<p class="note">Messages are delivered by FormSubmit, a free form service, to our inbox. We use your details only to reply. See our <a href="privacy.html">privacy policy</a>.</p></section>''',
    related=[("About", "about.html"), ("Big cat FAQ", "faq.html")], priority="0.3")

analytics = ("We use Cloudflare Web Analytics to count page views. It is cookieless and does not collect personal data or track you across sites."
             if CF_BEACON_TOKEN else
             "We do not currently run any analytics script. We plan to add Cloudflare Web Analytics, which is cookieless and does not collect personal data or track you across sites, and will update this page when we do.")
add("privacy.html", "Privacy Policy | BigCatWise",
    "BigCatWise privacy policy: Joshua Israel Ventures LLC is the data controller. What we collect, how contact messages are handled, analytics and your choices.",
    "Privacy policy", kind="page", headline="Privacy",
    lead="BigCatWise is a brand of Joshua Israel Ventures LLC. Joshua Israel Ventures LLC is the data controller for personal information collected through this website. We collect as little information as possible, and this page explains what we collect and why.",
    body='''<section class="card"><h2>Who we are</h2><p>This website, bigcatwise.com, is owned and operated by Joshua Israel Ventures LLC ("we", "us"). You can contact us about privacy at <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a>.</p></section>
<section class="card"><h2>What we collect</h2><ul>
<li><b>Contact form messages.</b> If you use our contact form, your name, email address and message are processed by FormSubmit (formsubmit.co), a third party form service, and delivered to our inbox.</li>
<li><b>Emails you send us.</b> If you email us directly, we receive your email address and whatever you include in the message.</li>
<li><b>Analytics.</b> ''' + analytics + '''</li></ul>
<p>We use contact details only to reply to you and to handle your request. We do not sell, rent or share them for marketing.</p></section>
<section class="card"><h2>Hosting and fonts</h2><p>The site is hosted on GitHub Pages. Like any web host, GitHub may log technical data such as IP addresses for security and operations; see GitHub's privacy statement. Headings use the free Fredoka font served by Google Fonts, so your browser requests the font from Google's servers, which receive your IP address as part of that request. We use no other Google services on this site.</p></section>
<section class="card"><h2>Cookies, ads and affiliates</h2><p>We do not set cookies. There is no Google AdSense or other advertising code and there are no affiliate links or affiliate cookies on this site. If that changes, we will update this policy and our <a href="disclaimer.html">disclaimer</a> before it goes live.</p></section>
<section class="card"><h2>Retention and your choices</h2><p>We keep contact messages only as long as needed to respond and keep a reasonable record of the conversation. You can ask us to access, correct or delete the personal information you sent us by emailing <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a>.</p></section>
<section class="card"><h2>Children</h2><p>The site is general educational content and is not directed at collecting information from children. Please do not send us personal information about a child.</p></section>
<section class="card"><h2>Changes</h2><p>We will post any changes to this policy on this page. Last updated 8 October 2026.</p></section>''',
    related=[("Terms of use", "terms.html"), ("Disclaimer", "disclaimer.html"), ("About", "about.html"), ("Contact", "contact.html")], priority="0.2")

add("terms.html", "Terms of Use | BigCatWise",
    "BigCatWise terms of use: your agreement with Joshua Israel Ventures LLC, general information only, no warranties, limitation of liability, Michigan law.",
    "Terms of use", kind="page", headline="Terms of use",
    lead="These terms govern your use of bigcatwise.com. By using the site you agree to them. If you do not agree, please do not use the site.",
    body='''<section class="card"><h2>Who you are agreeing with</h2><p>BigCatWise is a brand owned by Joshua Israel Ventures LLC. BigCatWise is a brand name, not a separate company or a registered assumed name. When you use this website, your agreement is with Joshua Israel Ventures LLC ("we", "us").</p></section>
<section class="card"><h2>General information only</h2><p>All content on BigCatWise is general educational information about big cats. It is not professional advice of any kind, including veterinary advice, wildlife handling or animal management advice, travel or travel safety advice, or legal advice. Never approach, feed or handle wild or captive big cats. For safety, travel or animal welfare decisions, follow official guidance and qualified professionals. Facts and population figures are summaries of published sources and may change as new research appears.</p></section>
<section class="card"><h2>No warranties</h2><p>The site and all content are provided "as is" and "as available", without warranties of any kind, express or implied, including warranties of accuracy, completeness, fitness for a particular purpose and non infringement. We do not warrant that the site will be uninterrupted or error free.</p></section>
<section class="card"><h2>Limitation of liability</h2><p>To the fullest extent permitted by law, Joshua Israel Ventures LLC and its members, managers and contributors will not be liable for any direct, indirect, incidental, consequential, special or punitive damages, or any loss of data, profits or goodwill, arising from or related to your use of, or inability to use, the site or its content, even if advised of the possibility of such damages. Where liability cannot be excluded, it is limited to the maximum extent the law allows.</p></section>
<section class="card"><h2>Intellectual property</h2><p>The BigCatWise name and logo, and all original text and illustrations on this site, are owned by Joshua Israel Ventures LLC. You may share links and short quotations with attribution. Please do not copy or republish substantial parts of the site without written permission.</p></section>
<section class="card"><h2>External links</h2><p>We link to outside sources such as zoos, conservation organisations and scientific journals. We are not responsible for their content or policies.</p></section>
<section class="card"><h2>Governing law</h2><p>These terms are governed by the laws of the State of Michigan, United States, without regard to its conflict of law rules.</p></section>
<section class="card"><h2>Changes and contact</h2><p>We may update these terms by posting a new version on this page. Questions: <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a>. Last updated 8 October 2026.</p></section>''',
    related=[("Privacy", "privacy.html"), ("Disclaimer", "disclaimer.html"), ("About", "about.html"), ("Contact", "contact.html")], priority="0.2")

add("disclaimer.html", "Disclaimer & Affiliate Disclosure | BigCatWise",
    "BigCatWise disclaimer: accuracy of our big cat information, no professional relationship, and our advertising and affiliate disclosure.",
    "Disclaimer and affiliate disclosure", kind="page", headline="Disclaimer",
    lead="BigCatWise is a brand of Joshua Israel Ventures LLC. Please read this disclaimer together with our terms of use.",
    body='''<section class="card"><h2>Accuracy</h2><p>We research every page carefully and cite reputable sources such as the IUCN SSC Cat Specialist Group, the IUCN Red List, leading zoos, conservation organisations and peer reviewed studies. Even so, wild animal populations, conservation status and scientific understanding change, and errors can happen. We make no guarantee that any information is complete, current or error free. If you spot a mistake, please <a href="contact.html">tell us</a>.</p></section>
<section class="card"><h2>No professional relationship</h2><p>Using this site, or contacting us, does not create any professional, advisory or client relationship. Our content is general information, not veterinary, wildlife handling, travel safety or legal advice. Always follow official guidance and qualified professionals, and never approach wild or captive big cats.</p></section>
<section class="card" id="affiliate"><h2>Advertising and affiliate disclosure</h2><p>There are currently no paid placements, sponsored posts, advertisements or affiliate links on BigCatWise, and we receive no compensation for mentioning any organisation, product or service. Links to zoos, conservation groups and research are provided purely as sources.</p><p>If we add advertising or affiliate links in future, we will disclose them clearly and conspicuously on the pages where they appear, in line with the US Federal Trade Commission's guidance on endorsements, and we will update this page and our <a href="privacy.html">privacy policy</a>.</p></section>
<section class="card"><h2>Contact</h2><p>Questions about this disclaimer: <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a>. Last updated 8 October 2026.</p></section>''',
    related=[("Terms of use", "terms.html"), ("Privacy", "privacy.html"), ("About", "about.html"), ("Contact", "contact.html")], priority="0.2")

add("404.html", "Page Not Found | BigCatWise", "This page could not be found.", "This page has wandered off",
    kind="page", noindex=True, sitemap=False,
    body='<p>We could not find that page. Try the <a href="{rel}index.html">home page</a>, the <a href="{rel}compare.html">big cat comparison table</a> or the <a href="{rel}faq.html">big cat FAQ</a>.</p>')

def llms(base):
    L = ["# BigCatWise", "",
         "> BigCatWise is a free, original educational website about big cats: the lion, tiger, leopard, jaguar, cheetah and snow leopard. It explains each species' appearance, behavior, habitat and range, and conservation status, with population estimates and facts sourced from the IUCN SSC Cat Specialist Group, the IUCN Red List, leading zoos, conservation organisations and peer reviewed research. Operated by Joshua Israel Ventures LLC.",
         "", "Content is general education. Population figures are estimates that change as new surveys are published.", "", "## Species guides"]
    def item(path):
        for p in PAGES:
            if p.path == path:
                u = base if path == "index.html" else base + (path[:-10] if path.endswith("index.html") else path)
                return "- [%s](%s): %s" % (p.headline or p.h1, u, p.description)
    for s in ["lion.html", "tiger.html", "leopard.html", "jaguar.html", "cheetah.html", "snow-leopard.html"]:
        L.append(item(s))
    L += ["", "## Topic guides"] + [item(s) for s in ["behavior.html", "habitats.html", "conservation.html", "faq.html", "glossary.html"]]
    L += ["", "## Tools", item("which-big-cat-is-it.html"), "- [Big cats by region](%swhich-big-cat-is-it.html#by-region): deep links #africa, #asia, #south-asia, #southeast-asia, #east-asia, #central-asia, #middle-east, #americas (also #north-america, #central-america, #south-america), #elsewhere (also #europe, #australia)" % base, item("compare.html"),
          "- [Comparison table rows](%scompare.html#table): deep links such as #row-tiger and #row-cheetah" % base]
    L += ["", "## Blog"] + [item(p.path) for p in POSTS]
    L += ["", "## Optional", item("about.html"), item("contact.html"), item("terms.html"), item("privacy.html"), item("disclaimer.html"), ""]
    return "\n".join(L)
