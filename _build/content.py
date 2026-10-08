from build import add, BASE_URL
from sources import CSG, SDZ, PAN, WWF, NZP, IUCN, WILSON, DURANT, KLEMUK, WEISS, FENNELL, SLT

SPECIES_REL = [("Which big cat is it? ID guide", "which-big-cat-is-it.html"), ("Big cat comparison table", "compare.html"), ("Big cat behavior", "behavior.html"),
               ("Where big cats live", "habitats.html"), ("Big cat conservation", "conservation.html")]

def facts(rows):
    return ('<section class="card facts"><h2>Quick facts</h2><div class="tablewrap"><table><tbody>' +
            "".join('<tr><th scope="row">%s</th><td>%s</td></tr>' % r for r in rows) +
            '</tbody></table></div><p class="note">Size and lifespan ranges are those listed by the IUCN SSC Cat Specialist Group and cover both sexes and all populations.</p></section>')

def jump(items):
    return '<p class="jump">Jump to: ' + " | ".join('<a href="#%s">%s</a>' % (i, t) for i, t in items) + '</p>'

# ------------------------------------------------------------------ LION
add("lion.html", "Lion Facts: Prides, Hunting, Habitat & Status | BigCatWise",
    "Lion facts in plain English: how prides work, who does the hunting, where wild lions live today, how many are left and why the species is Vulnerable.",
    "Lion facts: prides, hunting, habitat and conservation status",
    lead="The lion (<i>Panthera leo</i>) is the only truly social big cat. Wild lions live in prides built around related females, mainly in sub-Saharan Africa, with one small population in and around Gir forest in western India. The species is listed as Vulnerable on the IUCN Red List, and the IUCN Cat Specialist Group estimated roughly 22,000 to 25,000 adult and subadult lions in Africa in 2025.",
    crumbs=[("Species", "compare.html")], headline="Lion facts",
    body=jump([("facts", "Quick facts"), ("appearance", "Appearance"), ("pride", "Pride life"), ("hunting", "Hunting"),
               ("roar", "Roaring"), ("range", "Where lions live"), ("status", "Status")]) +
    '<div id="facts">' + facts([("Scientific name", "<i>Panthera leo</i>"), ("Weight", "110 to 272 kg (males are much heavier than females)"),
                ("Head and body length", "137 to 250 cm, plus a 60 to 100 cm tail"), ("Lifespan", "About 12 to 18 years"),
                ("Litter size", "1 to 4 cubs"), ("Range", "Sub-Saharan Africa; Gir landscape, Gujarat, India"),
                ("IUCN Red List", "Vulnerable (northern subspecies <i>P. l. leo</i>: Endangered)")]) + '</div>' +
    '''<section class="card" id="appearance"><h2>What does a lion look like?</h2>
<p>Lions have a plain tawny coat, a long tail ending in a dark tuft and, in adult males, a mane around the head and neck. The mane makes males look larger and is the most obvious difference between the sexes; no other wild cat shows such a striking visual difference between males and females. Cubs are born with faint spots that usually fade as they grow.</p>
<p>Size varies by region and sex. Adult males are clearly bigger and heavier than lionesses, and large male lions can match or exceed smaller tigers, although the tiger is the largest cat species overall. See the <a href="compare.html">big cat comparison table</a> for side by side sizes.</p></section>
<section class="card" id="pride"><h2>How does a lion pride work?</h2>
<p>A pride is a group of related adult females, their cubs and one or more adult males. The IUCN Cat Specialist Group gives an average of four to six adult lionesses per pride in Africa, with prides ranging from 1 to 21 females. Lionesses usually stay in the pride where they were born, while young males leave and try to win a pride of their own later.</p>
<p>Males often team up in coalitions, frequently brothers or other males that grew up together. A coalition that takes over a pride may kill young cubs fathered by the previous males, which brings the females back into breeding condition sooner. Competition is intense, and a single male rarely holds a pride for long except where lions are scarce.</p>
<p>Pride territories vary hugely with prey. Where prey is plentiful, lions can live at 10 to 40 per 100 km&sup2; with territories of 50 to 200 km&sup2;; in dry, prey poor areas, home ranges can grow to thousands of square kilometres.</p></section>
<section class="card" id="hunting"><h2>Do male lions hunt?</h2>
<p>Yes. Lionesses do much of the cooperative hunting, often stalking and surrounding prey as a group, but males hunt too, especially larger and more dangerous animals such as buffalo, and they hunt alone when they are not with a pride. Lions are also frequent scavengers and will take carcasses from other predators, which makes them especially vulnerable to poisoned carcasses.</p>
<p>Typical prey includes wildebeest, zebra, buffalo, antelope and warthog, depending on what is common locally. Lions spend a large part of each day resting and are most active from dusk to dawn.</p></section>
<section class="card" id="roar"><h2>Why do lions roar?</h2>
<p>A lion's roar advertises territory and helps pride members locate each other. It can carry over several kilometres. Lions, tigers, leopards and jaguars can roar thanks to the structure of their larynx and vocal folds; the snow leopard and cheetah cannot. Our post <a href="blog/which-big-cats-can-roar.html">which big cats can roar</a> explains the anatomy.</p></section>
<section class="card" id="range"><h2>Where do lions live?</h2>
<p>Lions live mainly in savanna, grassland, open woodland and scrub, not in dense rainforest, so the phrase "king of the jungle" is misleading. They have been recorded as high as 4,240 m in Ethiopia's Bale Mountains. In 2025 their known range was estimated at about 6 percent of their historical range.</p>
<p>The IUCN recognises two subspecies. <i>Panthera leo melanochaita</i> lives in southern and eastern Africa. <i>Panthera leo leo</i> covers West and Central Africa and the Asiatic lions of India, which survive as a single population centred on Gir Forest National Park and Wildlife Sanctuary in Gujarat. That population grew from a tiny remnant in the late 1800s to about 670 adult and subadult lions in 2020, and lions now range across a wider area known as the Greater Gir Landscape.</p>
<p>Lions have disappeared from many African countries, including all of North Africa, and in West Africa they survive only in small, isolated populations.</p></section>
<section class="card" id="status"><h2>How many lions are left and why are they declining?</h2>
<p>Estimates for Africa compiled by the IUCN Cat Specialist Group fell from about 33,000 lions in 2006 to about 25,000 in 2018, and the 2025 estimate was roughly 22,000 to 25,000 adults and subadults. Populations in southern Africa, many in fenced reserves, are stable or increasing, while the steepest losses are in West and Central Africa.</p>
<p>The main threats are conflict with people over livestock, loss of habitat and of the wild prey lions depend on (often through snaring and the bushmeat trade), and a growing illegal trade in lion bones and other parts. The Asiatic population is protected but vulnerable because all of it sits in one landscape, so a single disease outbreak could hit the whole population. Read more on our <a href="conservation.html">big cat conservation</a> page.</p></section>''',
    faq=[("Where do lions live besides Africa?", "The only wild lions outside Africa live in and around Gir forest in Gujarat, western India. They belong to the northern subspecies <i>Panthera leo leo</i>."),
         ("How many lions are left in the wild?", "The IUCN Cat Specialist Group estimated roughly 22,000 to 25,000 adult and subadult lions in Africa in 2025, plus about 670 adult and subadult Asiatic lions counted in India in 2020."),
         ("Do lions really live in the jungle?", "No. Lions prefer savanna, grassland and open woodland. The nickname king of the jungle is a figure of speech, not a description of their habitat.")],
    related=[("Tiger facts", "tiger.html"), ("Leopard facts", "leopard.html"), ("Cheetah facts", "cheetah.html")] + SPECIES_REL,
    sources=[CSG["lion"], NZP["lion"], SDZ["lion"], PAN["lion"], IUCN], priority="0.9")

# ------------------------------------------------------------------ TIGER
add("tiger.html", "Tiger Facts: Size, Stripes, Range & How Many Are Left | BigCatWise",
    "Tiger facts: the largest cat, why stripes are unique, where wild tigers survive, what they hunt and the latest IUCN population estimate.",
    "Tiger facts: size, stripes, range and conservation status",
    lead="The tiger (<i>Panthera tigris</i>) is the largest living cat, weighing 75 to 325 kg depending on population and sex. It is a solitary, mostly forest dwelling ambush hunter found only in Asia, in ten countries from India to the Russian Far East. Listed as Endangered, it numbered an estimated 3,726 to 5,578 wild individuals (excluding cubs) in the latest IUCN assessment.",
    crumbs=[("Species", "compare.html")], headline="Tiger facts",
    body=jump([("facts", "Quick facts"), ("stripes", "Stripes"), ("subspecies", "Subspecies"), ("life", "Daily life"),
               ("hunting", "Hunting"), ("range", "Range"), ("status", "Status")]) +
    '<div id="facts">' + facts([("Scientific name", "<i>Panthera tigris</i>"), ("Weight", "75 to 325 kg"),
                ("Head and body length", "150 to 230 cm, plus a 90 to 110 cm tail"), ("Lifespan", "About 12 to 15 years"),
                ("Litter size", "1 to 5 cubs, after a gestation of about 103 days"), ("Range", "10 countries in South, Southeast and East Asia and the Russian Far East"),
                ("IUCN Red List", "Endangered")]) + '</div>' +
    '''<section class="card" id="stripes"><h2>Are every tiger's stripes different?</h2>
<p>Yes. Tigers are the only cats with stripes, and each tiger's pattern is unique, varying in the number, width and shape of stripes. Researchers use this to identify individual tigers in camera trap photos, which is the basis of many population surveys. Stripes break up the tiger's outline among grass, reeds and forest shadows. Our post <a href="blog/why-do-tigers-have-stripes.html">why do tigers have stripes</a> covers the science, including why an orange coat still works as camouflage.</p>
<p>White tigers are not a separate species or subspecies. They are a rare colour variant; according to the IUCN Cat Specialist Group, the last documented white tiger in the wild was shot in Bihar, India, in 1958.</p></section>
<section class="card" id="subspecies"><h2>How many tiger subspecies are there?</h2>
<p>Traditionally six living subspecies were recognised: Amur (Russian Far East and northeastern China), South China (likely extinct in the wild), Northern Indochinese, Malayan, Sumatran and Bengal tigers. Three more, the Bali, Javan and Caspian tigers, are extinct.</p>
<p>Recent genetic studies propose just two subspecies: a mainland Asian form and a Sunda Islands form (Sumatra, and formerly Java and Bali). The IUCN Cat Specialist Group notes that tiger taxonomy is still under review, so you will see both systems used.</p></section>
<section class="card" id="life"><h2>Do tigers live alone?</h2>
<p>Adult tigers are solitary. Females hold territories where they raise cubs; males range more widely, and a male's territory often overlaps those of one to three females. Home range size depends on prey: in Nepal's Chitwan National Park female ranges average about 10 to 39 km&sup2;, while in the Russian Far East female ranges can reach 100 to 400 km&sup2; and one male's range was measured at 1,379 km&sup2;.</p>
<p>Cubs become independent at about 18 to 28 months. Tigers are strong swimmers and are at home in wet habitats such as the mangrove forests of the Sundarbans.</p></section>
<section class="card" id="hunting"><h2>What do tigers eat?</h2>
<p>Tigers mainly hunt large hoofed mammals such as chital, sambar, gaur and wild pig, usually by stalking close and ambushing. After a kill a tiger often drags the carcass into cover and returns to feed over several days. The IUCN Cat Specialist Group estimates that a tiger needs around 50 to 60 large prey animals a year, which is why prey depletion is as dangerous to tigers as direct poaching.</p></section>
<section class="card" id="range"><h2>Where do tigers live?</h2>
<p>Wild tigers survive with confirmed breeding in Bangladesh, Bhutan, China, India, Indonesia, Malaysia, Myanmar, Nepal, Russia and Thailand. They use tropical and temperate forests, mangroves and grasslands, from steamy lowlands to snowy forests in the Russian Far East, as long as there is cover, water and enough prey. Less than 7 percent of the tiger's original range remains, and tigers have vanished from countries including Singapore, Iran, Vietnam, Lao PDR and Cambodia. There are no wild tigers in Africa.</p></section>
<section class="card" id="status"><h2>How many tigers are left in the wild?</h2>
<p>The latest IUCN assessment estimated 3,726 to 5,578 tigers (excluding cubs), with about 3,140 mature individuals. That compares with an estimated 100,000 at the start of the twentieth century. India holds a large share of the world's wild tigers.</p>
<p>In 2025 the first IUCN Green Status assessment for the tiger rated it Critically Depleted, while also finding that conservation work such as India's Project Tiger (launched in 1973) has prevented even greater losses. Poaching for skins and body parts, loss and fragmentation of forests, prey depletion and conflict with people remain the main threats. See <a href="conservation.html">big cat conservation</a> for how these threats are being tackled.</p></section>''',
    faq=[("Is the tiger the biggest cat?", "Yes. The tiger is the largest living cat species, at 75 to 325 kg, though size varies by population and big male lions can outweigh smaller tigers."),
         ("Are there tigers in Africa?", "No. Wild tigers live only in Asia. Lions, leopards and cheetahs are Africa's big cats."),
         ("How many wild tigers are there?", "The latest IUCN assessment estimated 3,726 to 5,578 wild tigers excluding cubs, with about 3,140 mature individuals.")],
    related=[("Lion facts", "lion.html"), ("Leopard facts", "leopard.html"), ("Snow leopard facts", "snow-leopard.html"),
             ("Why do tigers have stripes?", "blog/why-do-tigers-have-stripes.html")] + SPECIES_REL,
    sources=[CSG["tiger"], WWF["tiger"], NZP["tiger"], SDZ["tiger"], PAN["tiger"], IUCN], priority="0.9")

# ------------------------------------------------------------------ LEOPARD
add("leopard.html", "Leopard Facts: Range, Rosettes, Hunting & Black Panthers | BigCatWise",
    "Leopard facts: the most widespread big cat, how leopards hunt and cache prey in trees, what a black panther is, and why the leopard is Vulnerable.",
    "Leopard facts: range, rosettes, hunting and black panthers",
    lead="The leopard (<i>Panthera pardus</i>) is the most widespread and adaptable big cat, found across much of sub-Saharan Africa and parts of Asia from the Middle East to the Russian Far East. It is a solitary stalker that often hauls kills into trees, and a melanistic (black) leopard is what many people call a black panther. The leopard is listed as Vulnerable on the IUCN Red List.",
    crumbs=[("Species", "compare.html")], headline="Leopard facts",
    body=jump([("facts", "Quick facts"), ("look", "Appearance"), ("black", "Black panthers"), ("hunting", "Hunting"),
               ("range", "Range"), ("status", "Status")]) +
    '<div id="facts">' + facts([("Scientific name", "<i>Panthera pardus</i>"), ("Weight", "17 to 90 kg"),
                ("Head and body length", "91 to 191 cm, plus a 51 to 101 cm tail"), ("Lifespan", "About 13 to 21 years"),
                ("Litter size", "1 to 4 cubs, after a gestation of 90 to 105 days"), ("Range", "Sub-Saharan Africa and scattered parts of Asia"),
                ("IUCN Red List", "Vulnerable")]) + '</div>' +
    '''<section class="card" id="look"><h2>How do you recognise a leopard?</h2>
<p>Leopards have a pale yellow to golden coat covered in rosettes: rings or broken circles of dark spots. Unlike a jaguar's rosettes, a leopard's usually have no spot in the middle. Leopards are also lighter and longer bodied than jaguars, and they are bigger and stockier than cheetahs, which have solid round spots. Size and colour vary a lot across the leopard's huge range. Our <a href="blog/leopard-vs-jaguar-vs-cheetah.html">leopard vs jaguar vs cheetah guide</a> shows how to tell them apart.</p></section>
<section class="card" id="black"><h2>What is a black panther?</h2>
<p>"Black panther" is not a species. It is a common name for a leopard or jaguar with melanism, a genetic variation that produces very dark fur. Look closely in good light and the rosettes are still visible. In Asia and Africa a black panther is a leopard; in the Americas it is a jaguar.</p></section>
<section class="card" id="hunting"><h2>How do leopards hunt?</h2>
<p>Leopards stalk to very close range, then attack with a short burst of speed and a powerful swipe of the front paw. They eat an exceptionally wide range of prey, from rock hyraxes of about 4 kg up to eland, and in some areas domestic animals. Leopards are famous for carrying kills up into trees, which keeps the meat away from lions and hyenas.</p>
<p>In savannas and woodlands leopards are mainly active between sunset and sunrise, but studies in undisturbed rainforest in Gabon found them largely active by day. Adults are solitary; in African protected areas male home ranges are roughly 30 to 78 km&sup2; and female ranges 15 to 38 km&sup2;, but ranges in the Kalahari have exceeded 2,000 km&sup2;.</p></section>
<section class="card" id="range"><h2>Where do leopards live?</h2>
<p>The leopard has the largest range of any big cat. It occurs across most of sub-Saharan Africa and, in fragmented pockets, in the Arabian Peninsula, Turkey, southwest Asia and the Caucasus, the Himalayas, South Asia, Indochina, Peninsular Malaysia, Java, China and the Russian Far East. It lives in rainforest, savanna, mountains and semi desert, and has been recorded up to 5,200 m in the Himalayas. Given cover and prey, and freedom from persecution, leopards can persist surprisingly close to people.</p></section>
<section class="card" id="status"><h2>Why is the leopard Vulnerable?</h2>
<p>Despite their adaptability, leopards have vanished from large parts of their historic range. The IUCN Cat Specialist Group recorded an 11 percent reduction in leopard range between 2016 and 2023. In Southeast Asia leopards are gone or functionally gone from most of their range, surviving mainly in Thailand, Myanmar, Malaysia and Java, and populations in North Africa and Arabia are tiny or lost. The Amur leopard survives as a single population in the Russian Far East and neighbouring northeast China after intensive conservation work.</p>
<p>Threats include habitat loss, prey depletion, retaliatory killing over livestock, illegal trade in skins and parts, and poorly managed trophy hunting. Several leopard subspecies are assessed separately and some, such as the Indochinese leopard, are Critically Endangered.</p></section>''',
    faq=[("Is a black panther a separate species?", "No. A black panther is a leopard or jaguar with melanism, a genetic variation causing dark fur. The rosettes are still faintly visible."),
         ("Why do leopards drag prey into trees?", "Hoisting a kill into a tree keeps it away from lions, hyenas and other competitors so the leopard can feed over several days."),
         ("Where do leopards live?", "Leopards live across most of sub-Saharan Africa and in scattered parts of Asia, from the Middle East and Caucasus to India, Southeast Asia, China and the Russian Far East.")],
    related=[("Jaguar facts", "jaguar.html"), ("Cheetah facts", "cheetah.html"), ("Snow leopard facts", "snow-leopard.html"),
             ("Leopard vs jaguar vs cheetah", "blog/leopard-vs-jaguar-vs-cheetah.html")] + SPECIES_REL,
    sources=[CSG["leopard"], SDZ["leopard"], PAN["leopard"], WWF["amur"], IUCN], priority="0.9")

# ------------------------------------------------------------------ JAGUAR
add("jaguar.html", "Jaguar Facts: Bite, Swimming, Range & Status | BigCatWise",
    "Jaguar facts: the largest cat in the Americas, its skull piercing bite, love of water, rosettes with central spots, range and Near Threatened status.",
    "Jaguar facts: bite, swimming, range and conservation status",
    lead="The jaguar (<i>Panthera onca</i>) is the largest cat in the Americas and the only big cat that regularly kills prey by biting through the skull. It ranges from Mexico to northern Argentina, is a strong swimmer that hunts caiman and fish, and is listed as Near Threatened on the IUCN Red List, with most jaguars living in the Amazon.",
    crumbs=[("Species", "compare.html")], headline="Jaguar facts",
    body=jump([("facts", "Quick facts"), ("look", "Appearance"), ("bite", "Bite and hunting"), ("water", "Water"),
               ("range", "Range"), ("status", "Status")]) +
    '<div id="facts">' + facts([("Scientific name", "<i>Panthera onca</i>"), ("Weight", "36 to 148 kg"),
                ("Head and body length", "110 to 170 cm, plus a relatively short 44 to 80 cm tail"), ("Lifespan", "Up to about 26 years recorded"),
                ("Litter size", "1 to 4 cubs"), ("Range", "Mexico to northern Argentina"),
                ("IUCN Red List", "Near Threatened (new assessment expected around 2027)")]) + '</div>' +
    '''<section class="card" id="look"><h2>How is a jaguar different from a leopard?</h2>
<p>Jaguars are stockier and more muscular than leopards, with a massive head, broad chest and a relatively short tail. Their rosettes are larger and usually have one or more dark spots inside, while leopard rosettes are usually empty. Geography is the easiest clue: wild jaguars live only in the Americas and wild leopards only in Africa and Asia. Melanistic jaguars are one of the two animals called "black panthers". Size varies by region, and jaguars in more open habitats tend to be larger.</p></section>
<section class="card" id="bite"><h2>How does a jaguar kill its prey?</h2>
<p>The IUCN Cat Specialist Group describes the jaguar as the only big cat that regularly kills prey by piercing the skull with its canines. Its big head and robust teeth may be an adaptation for cracking armoured reptiles such as tortoises and river turtles. Jaguars also break the necks of large prey and kill small prey with a blow to the head.</p>
<p>Jaguars are opportunistic generalists: more than 85 prey species have been recorded in their diet, including peccaries, armadillos, capybaras, caiman, deer, turtles and fish. Where cattle ranching overlaps jaguar habitat, cattle can form a large part of the diet, which drives conflict with ranchers.</p></section>
<section class="card" id="water"><h2>Do jaguars like water?</h2>
<p>Yes. Jaguars are excellent swimmers, cross wide rivers and readily catch fish, capybaras and caiman in water. They are most often found in wet lowland habitats such as rainforest, swamps and seasonally flooded wetlands like the Pantanal, generally below 1,000 m, though they have been reported as high as 3,800 m.</p></section>
<section class="card" id="range"><h2>Where do jaguars live?</h2>
<p>Jaguars range from Mexico through Central America to northern Argentina, with occasional individuals recorded in the southwestern United States. The Amazon is the stronghold: the IUCN Cat Specialist Group estimates 57,000 to 64,000 jaguars there, about 89 percent of the total.</p></section>
<section class="card" id="status"><h2>Are jaguars endangered?</h2>
<p>Globally the jaguar is Near Threatened, but the picture is uneven. Of 34 identified jaguar subpopulations, only the Amazonian one is assessed as Least Concern; the others are Endangered or Critically Endangered. In Brazil's Atlantic Forest only about 200 adults (plus or minus 80) are thought to remain. Habitat loss and fragmentation, depletion of prey, killing by ranchers over livestock and illegal trade in jaguar parts are the main threats. Panthera, which is co leading the next IUCN jaguar assessment, expects it around 2027.</p></section>''',
    faq=[("Is a jaguar bigger than a leopard?", "Generally yes. Jaguars are stockier and heavier, at 36 to 148 kg against 17 to 90 kg for leopards, although sizes overlap and vary by region."),
         ("Do jaguars live in Africa?", "No. Wild jaguars live only in the Americas, from Mexico to northern Argentina. The spotted big cat of Africa is the leopard."),
         ("Can jaguars swim?", "Yes. Jaguars are excellent swimmers and hunt fish, capybaras and caiman in rivers and wetlands.")],
    related=[("Leopard facts", "leopard.html"), ("Cheetah facts", "cheetah.html"), ("Leopard vs jaguar vs cheetah", "blog/leopard-vs-jaguar-vs-cheetah.html")] + SPECIES_REL,
    sources=[CSG["jaguar"], WWF["jaguar"], SDZ["jaguar"], PAN["jaguar"], IUCN], priority="0.9")

# ------------------------------------------------------------------ CHEETAH
add("cheetah.html", "Cheetah Facts: Speed, Hunting, Range & Status | BigCatWise",
    "Cheetah facts: how fast cheetahs really run, why they cannot roar, how they hunt by day, where they live and why only about 6,500 mature adults remain.",
    "Cheetah facts: speed, hunting, range and conservation status",
    lead="The cheetah (<i>Acinonyx jubatus</i>) is the fastest land animal, a slender daytime hunter of open country that sprints in short bursts after gazelles and impala. It is not a roaring cat and sits outside the genus <i>Panthera</i>. Listed as Vulnerable, it numbers roughly 6,500 mature individuals, mostly in southern and eastern Africa, plus a critically endangered remnant in Iran.",
    crumbs=[("Species", "compare.html")], headline="Cheetah facts",
    body=jump([("facts", "Quick facts"), ("speed", "Speed"), ("body", "Built for speed"), ("hunting", "Hunting"),
               ("social", "Social life"), ("range", "Range"), ("status", "Status")]) +
    '<div id="facts">' + facts([("Scientific name", "<i>Acinonyx jubatus</i>"), ("Weight", "23 to 65 kg"),
                ("Head and body length", "113 to 140 cm, plus a 60 to 84 cm tail"), ("Lifespan", "Up to about 14 years in the wild"),
                ("Litter size", "1 to 6 cubs"), ("Range", "Mainly southern and eastern Africa; Sahara; Iran"),
                ("IUCN Red List", "Vulnerable (Asiatic cheetah: Critically Endangered)")]) + '</div>' +
    '''<section class="card" id="speed"><h2>How fast is a cheetah?</h2>
<p>The IUCN Cat Specialist Group gives speeds of up to about 103 km/h during a chase. The best measured wild data come from a 2013 study in Botswana that fitted five cheetahs with GPS and motion sensor collars: the fastest of 367 runs reached 25.9 m/s (93 km/h, 58 mph), but most hunts used only moderate speeds, and acceleration, braking and sharp turns mattered as much as top speed. Chases seldom cover more than about 300 m. Our post <a href="blog/how-fast-is-a-cheetah.html">how fast is a cheetah</a> goes into the details.</p></section>
<section class="card" id="body"><h2>What makes a cheetah so fast?</h2>
<ul><li>Long legs, big thigh muscles and a very flexible spine allow strides of up to about 7 m.</li>
<li>Semi retractable claws grip the ground like running spikes.</li>
<li>A long tail, about half the head and body length, helps with balance in turns.</li>
<li>Enlarged lungs, heart and nasal passages help it recover after a sprint.</li></ul>
<p>Cheetahs also have black "tear marks" running from the inner eye to the mouth, and solid round spots rather than rosettes.</p></section>
<section class="card" id="hunting"><h2>How do cheetahs hunt?</h2>
<p>Cheetahs usually stalk first, then sprint over a short distance and trip or knock the prey off balance before a suffocating bite to the throat. They prefer prey of about 10 to 56 kg: Thomson's gazelle on East African plains, impala in woodland, springbok and young kudu in southern Africa. Cheetahs hunt mainly by day, which helps them avoid lions and hyenas, but those larger predators still steal kills and kill cubs. Cheetahs are not obligate drinkers and can get much of their moisture from prey.</p></section>
<section class="card" id="social"><h2>Do cheetahs live alone?</h2>
<p>Adult females are solitary and non territorial, raising cubs alone. Males may live alone or in small coalitions, often brothers, and some hold small territories averaging around 30 km&sup2; that contain prey, water and access to females. Cheetahs cannot roar; they purr and make high pitched chirping calls.</p></section>
<section class="card" id="range"><h2>Where do cheetahs live?</h2>
<p>Cheetahs live in savanna, grassland, dry woodland and desert. Strongholds are in Namibia and Botswana and in Kenya and Tanzania, with very sparse populations in the Sahara. Remarkably, about two thirds of cheetahs live outside protected areas, often on farmland, partly because lions and hyenas are scarcer there. In Asia, the Asiatic cheetah survives only in Iran, where fewer than 50 mature individuals are thought to remain. In 2022 India began bringing cheetahs from southern Africa to Kuno National Park in an effort to restore the species there.</p></section>
<section class="card" id="status"><h2>How many cheetahs are left?</h2>
<p>A major 2017 study led by Sarah Durant estimated about 7,100 adult and adolescent cheetahs (around 6,500 mature individuals) in 33 subpopulations, occupying about 9 percent of the species' historical range. Only two subpopulations exceed 1,000 mature individuals, and most of those whose trend could be assessed are declining. Threats include habitat loss and fragmentation, conflict with livestock and game farmers, prey depletion, road deaths and the illegal trade in live cubs and skins. Cheetahs also have very low genetic diversity, the legacy of ancient population bottlenecks.</p></section>''',
    faq=[("Is a cheetah a big cat?", "In the strict sense no: big cats are the roaring cats of the genus Panthera, and the cheetah belongs to its own genus, Acinonyx. In everyday use the cheetah is usually included as a big cat, as it is on this site."),
         ("Can cheetahs roar?", "No. Cheetahs purr and make chirping and other calls, but they cannot roar."),
         ("What is the top speed of a cheetah?", "The fastest run measured in a study of wild cheetahs was 25.9 m/s, about 93 km/h or 58 mph. The IUCN Cat Specialist Group gives up to about 103 km/h.")],
    related=[("Leopard facts", "leopard.html"), ("Lion facts", "lion.html"), ("How fast is a cheetah?", "blog/how-fast-is-a-cheetah.html")] + SPECIES_REL,
    sources=[CSG["cheetah"], DURANT, WILSON, NZP["cheetah"], WWF["cheetah"], SDZ["cheetah"], PAN["cheetah"]], priority="0.9")

# ------------------------------------------------------------------ SNOW LEOPARD
add("snow-leopard.html", "Snow Leopard Facts: Adaptations, Range, Diet & Status | BigCatWise",
    "Snow leopard facts: how this mountain cat survives at 3,000 to 5,000 m, why it cannot roar, what it eats, where it lives and how many remain.",
    "Snow leopard facts: adaptations, range, diet and status",
    lead="The snow leopard (<i>Panthera uncia</i>) is a big cat of the high mountains of Central and South Asia, usually living between 3,000 and 5,000 m. It has thick smoky grey fur, huge paws and an exceptionally long tail, and unlike its relatives it cannot roar. It is listed as Vulnerable, with the latest estimate at about 7,400 to 8,000 individuals.",
    crumbs=[("Species", "compare.html")], headline="Snow leopard facts",
    body=jump([("facts", "Quick facts"), ("adapt", "Adaptations"), ("voice", "Voice"), ("diet", "Diet"),
               ("range", "Range"), ("status", "Status")]) +
    '<div id="facts">' + facts([("Scientific name", "<i>Panthera uncia</i>"), ("Weight", "30 to 50 kg"),
                ("Head and body length", "90 to 120 cm, plus an 80 to 100 cm tail"), ("Lifespan", "About 10 to 20 years"),
                ("Litter size", "1 to 5 cubs"), ("Range", "Mountains of 12 countries in Central and South Asia"),
                ("IUCN Red List", "Vulnerable")]) + '</div>' +
    '''<section class="card" id="adapt"><h2>How are snow leopards adapted to the cold?</h2>
<ul><li><b>Long, thick tail:</b> up to about 1 m, or 75 to 90 percent of head and body length. It helps with balance on steep rock and is wrapped around the body for warmth when resting.</li>
<li><b>Enlarged nasal cavity:</b> helps warm cold, thin air.</li>
<li><b>Short forelimbs and strong chest muscles:</b> suited to climbing and leaping on steep slopes.</li>
<li><b>Dense fur and broad, furry paws:</b> insulation, and grip on snow and scree.</li></ul>
<p>The coat is pale grey to cream with dark rosettes and spots, superb camouflage against rock. Snow leopards often stalk from above and chase prey down steep slopes.</p></section>
<section class="card" id="voice"><h2>Can snow leopards roar?</h2>
<p>No. Although the snow leopard belongs to the genus <i>Panthera</i> with the roaring cats, its vocal folds lack the fibro elastic tissue needed for a deep roar. It yowls, especially in the breeding season, and makes other calls. See <a href="blog/which-big-cats-can-roar.html">which big cats can roar</a>.</p></section>
<section class="card" id="diet"><h2>What do snow leopards eat?</h2>
<p>Snow leopards mainly hunt wild mountain sheep and goats, such as bharal (blue sheep), ibex and argali, and their distribution closely follows these prey. Genetic diet studies suggest small prey such as marmots matter less than once thought. Domestic livestock is taken too, commonly 15 to 30 percent of the diet and sometimes far more where wild prey is scarce, which leads to conflict with herders.</p></section>
<section class="card" id="range"><h2>Where do snow leopards live?</h2>
<p>Snow leopards live across the mountains of 12 countries: Afghanistan, Bhutan, China, India, Kazakhstan, Kyrgyzstan, Mongolia, Nepal, Pakistan, Russia, Tajikistan and Uzbekistan, including the Himalayas, the Tibetan Plateau, the Pamirs, Tian Shan and Altai. They are typically found at 3,000 to 5,000 m and occasionally above 5,500 m in the Himalayas, but at the northern edge of the range they live much lower, at 600 to 2,500 m. Densities are low, from about 0.3 to 6 per 100 km&sup2;, because these cold, dry landscapes support little prey.</p></section>
<section class="card" id="status"><h2>How many snow leopards are left?</h2>
<p>Snow leopards are very hard to count and older figures are rough. The most recent estimate cited by the IUCN Cat Specialist Group is 7,446 to 7,996 individuals, including 2,710 to 3,386 mature adults. The species was moved from Endangered to Vulnerable on the IUCN Red List in 2017, but a further decline of about 10 percent is projected over three generations.</p>
<p>The main threats are retaliatory killing by herders after livestock losses, decline of wild prey through hunting and competition with livestock, and poaching: an estimated 221 to 450 snow leopards have been poached each year since 2008. Conflict reduction methods include predator proof livestock corrals, livestock insurance and vaccination schemes, and community based conservation.</p></section>''',
    faq=[("Is the snow leopard a type of leopard?", "No. Despite the name it is a separate species, Panthera uncia. Genetic studies suggest its closest living relative is the tiger."),
         ("Can snow leopards roar?", "No. Their vocal folds lack the tissue needed for a deep roar, so they yowl and make other calls instead."),
         ("How many snow leopards are there?", "The most recent estimate cited by the IUCN Cat Specialist Group is 7,446 to 7,996 individuals, of which 2,710 to 3,386 are mature adults.")],
    related=[("Tiger facts", "tiger.html"), ("Leopard facts", "leopard.html"), ("Which big cats can roar?", "blog/which-big-cats-can-roar.html")] + SPECIES_REL,
    sources=[CSG["snow"], WWF["snow"], SLT, SDZ["snow"], PAN["snow"], IUCN], priority="0.9")

import content2  # noqa  other pages and blog
import games  # noqa  games hub and games
from content2 import llms  # noqa
