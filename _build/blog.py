from build import add, TODAY
from sources import CSG, SDZ, PAN, WWF, NZP, IUCN, WILSON, DURANT, KLEMUK, WEISS, FENNELL, SLT

HETEM = ("Hetem et al. (2013) Cheetah do not abandon hunts because they overheat, Biology Letters", "https://doi.org/10.1098/rsbl.2013.0472")
BC = [("Blog", "blog/index.html")]
POSTS = []
def post(slug, *a, **k):
    k.setdefault("crumbs", BC)
    p = add("blog/" + slug + ".html", *a, **k)
    POSTS.append(p)
    return p

# ---------------------------------------------------------------- 1 ROAR
post("which-big-cats-can-roar", "Which Big Cats Can Roar? And Why Snow Leopards Can't | BigCatWise",
     "Lions, tigers, leopards and jaguars can roar; snow leopards and cheetahs cannot. Here is what the anatomy research says about why, and what the others say instead.",
     "Which big cats can roar, and why can't snow leopards?", headline="Which big cats can roar?",
     lead="Four big cats can roar: the lion, tiger, leopard and jaguar. The snow leopard cannot, even though it belongs to the same genus, <i>Panthera</i>, and neither can the cheetah, which purrs and chirps instead. Research on the throat anatomy of big cats points to the shape and tissue of the vocal folds, not just the throat bones, as the key to a true roar.",
     body='''<section class="card"><h2>The short answer</h2>
<div class="tablewrap"><table><thead><tr><th>Species</th><th>Roars?</th><th>Typical long distance call</th></tr></thead><tbody>
<tr><td><a href="../lion.html">Lion</a></td><td>Yes</td><td>Full roar, often in bouts that end in a series of grunts</td></tr>
<tr><td><a href="../tiger.html">Tiger</a></td><td>Yes</td><td>Roar; also a soft puffing greeting called a chuff</td></tr>
<tr><td><a href="../leopard.html">Leopard</a></td><td>Yes</td><td>A rasping, repeated call often compared to sawing wood</td></tr>
<tr><td><a href="../jaguar.html">Jaguar</a></td><td>Yes</td><td>A series of deep, hoarse grunts</td></tr>
<tr><td><a href="../snow-leopard.html">Snow leopard</a></td><td>No</td><td>Yowls, mews and a chuff</td></tr>
<tr><td><a href="../cheetah.html">Cheetah</a></td><td>No</td><td>Purrs, plus high pitched chirps and other calls</td></tr>
</tbody></table></div></section>
<section class="card"><h2>The old explanation: a stretchy throat bone</h2>
<p>For well over a century, the standard explanation was the hyoid apparatus, the chain of small bones that supports the tongue and larynx. In the roaring cats, part of this chain is not fully bony but is replaced by a ligament that can stretch. The idea was that this flexible hyoid lets the larynx sit lower and move more freely, lengthening the vocal tract and producing a deeper, louder sound. Cats with a fully bony hyoid, like house cats and cheetahs, were thought to purr instead.</p>
<p>The problem is the snow leopard. It shares the partly ligamentous hyoid of the other <i>Panthera</i> cats, yet it does not roar. So the hyoid alone cannot be the whole story.</p></section>
<section class="card"><h2>What newer anatomy studies found</h2>
<p>A detailed 2002 study by Weissengruber and colleagues compared the hyoid apparatus and throat of lions, jaguars, tigers, cheetahs and domestic cats. They concluded that the elastic hyoid by itself does not explain roaring; features of the larynx and especially the vocal folds matter, along with a long vocal tract.</p>
<p>In 2011, Klemuk and colleagues looked closely at the vocal folds of lions and tigers. They found the folds have a flat, square shaped surface and are built from tissue that can withstand a lot of stretching and shearing. That shape helps the folds vibrate at the low frequencies typical of a roar while needing relatively little lung pressure, which is part of why a roar can be both deep and very loud.</p>
<p>The IUCN Cat Specialist Group's profile of the snow leopard puts the missing piece simply: the snow leopard's vocal folds lack the fibro elastic tissue needed for the deep roars of other big cats. It has the "roaring" type of hyoid, but not the roaring type of vocal fold.</p></section>
<section class="card"><h2>Why do big cats roar at all?</h2>
<p>A roar is a long distance message. A lion's roar can carry over several kilometres, so it is an efficient way to tell rivals that a territory is occupied, and to help scattered pride members find each other, without the risk of a fight. Lions often roar most around dusk, through the night and at dawn, when sound travels well and they are most active. Tigers, leopards and jaguars, which live alone, also use calls to advertise their presence to neighbours and potential mates, alongside scent marks.</p></section>
<section class="card"><h2>What sounds do non roaring big cats make?</h2>
<p><b>Snow leopards</b> yowl, especially in the breeding season, mew and hiss, and make a soft, friendly puffing sound called a chuff, which tigers also use as a close range greeting.</p>
<p><b>Cheetahs</b> purr, much like a large domestic cat, and use a bird like chirp, often between a mother and her cubs. These sounds are very different from a roar and do not carry as far.</p></section>
<section class="card"><h2>Can roaring cats purr?</h2>
<p>This is genuinely debated. Domestic cats and cheetahs purr continuously as they breathe in and out. Lions, tigers, leopards and jaguars make some purr like sounds, but whether these are true purrs in the same sense is disputed, and they generally do not purr continuously the way a house cat does. Be wary of sources that state a simple rule either way.</p></section>
<section class="card"><h2>What about pumas and other cats?</h2>
<p>The puma (also called cougar or mountain lion) is a large cat but not a <i>Panthera</i>, and it does not roar; it is known for screams, whistles and purrs. Clouded leopards are not roaring cats either. That is one reason many scientists reserve the term big cat for the five <i>Panthera</i> species, with the cheetah added in everyday use. See <a href="../compare.html#definition">what counts as a big cat</a>.</p></section>
<section class="card"><h2>Key takeaways</h2><ul>
<li>Roaring cats: lion, tiger, leopard, jaguar.</li>
<li>Non roaring big cats: snow leopard and cheetah.</li>
<li>A flexible hyoid is not enough. Roaring depends on vocal fold shape and tissue as well.</li>
<li>Roars are long distance territorial and contact calls.</li></ul></section>''',
     related=[("Big cat behavior", "behavior.html"), ("Snow leopard facts", "snow-leopard.html"), ("Lion facts", "lion.html"), ("Cheetah facts", "cheetah.html"), ("Blog home", "blog/index.html")],
     sources=[WEISS, KLEMUK, CSG["snow"], CSG["lion"], NZP["cheetah"]])

# ---------------------------------------------------------------- 2 SPOTTED CATS
post("leopard-vs-jaguar-vs-cheetah", "Leopard vs Jaguar vs Cheetah: How to Tell Them Apart | BigCatWise",
     "How to tell a leopard, jaguar and cheetah apart in seconds: location, spot pattern, build, face and behavior, with a side by side comparison table.",
     "Leopard vs jaguar vs cheetah: how to tell them apart", headline="Leopard vs jaguar vs cheetah",
     lead="Start with location: a wild spotted big cat in the Americas is a jaguar, while in Africa or Asia it is a leopard or cheetah. Then check the spots. Cheetahs have solid round spots and black tear marks on the face; leopards have rosettes that are usually empty in the middle; jaguars have bigger rosettes that usually contain one or more dots, on a stockier body with a heavier head.",
     body='''<section class="card"><h2>Side by side comparison</h2>
<div class="tablewrap"><table><thead><tr><th></th><th>Leopard</th><th>Jaguar</th><th>Cheetah</th></tr></thead><tbody>
<tr><th scope="row">Where</th><td>Africa and Asia</td><td>Americas only</td><td>Africa, plus a tiny population in Iran</td></tr>
<tr><th scope="row">Markings</th><td>Small, tight rosettes, usually without a central spot</td><td>Larger rosettes, usually with spots inside</td><td>Solid round black spots, no rosettes</td></tr>
<tr><th scope="row">Face</th><td>Plain face with small spots</td><td>Broad, heavy head and strong jaw</td><td>Small head, black tear marks from eye to mouth</td></tr>
<tr><th scope="row">Build</th><td>Muscular but lithe, long tail</td><td>Stocky and powerful, relatively short tail</td><td>Slim, deep chest, long thin legs</td></tr>
<tr><th scope="row">Weight (IUCN CatSG ranges)</th><td>17 to 90 kg</td><td>36 to 148 kg</td><td>23 to 65 kg</td></tr>
<tr><th scope="row">Hunting</th><td>Stalk and pounce, often caches kills in trees</td><td>Ambush near water, skull piercing bite</td><td>Stalk then high speed chase, mainly by day</td></tr>
<tr><th scope="row">Claws</th><td>Fully retractable</td><td>Fully retractable</td><td>Semi retractable</td></tr>
<tr><th scope="row">Roars?</th><td>Yes</td><td>Yes</td><td>No, purrs and chirps</td></tr>
<tr><th scope="row">IUCN Red List</th><td>Vulnerable</td><td>Near Threatened</td><td>Vulnerable</td></tr>
</tbody></table></div></section>
<section class="card"><h2>Step 1: Where was the cat?</h2>
<p>Geography settles most cases. Wild jaguars live from Mexico to northern Argentina, and there are no wild leopards or cheetahs in the Americas. In Africa, leopards and cheetahs often share the same landscapes, so you need to look closer. In Asia, a spotted big cat is almost always a leopard (or a snow leopard in the high mountains), since the only wild Asian cheetahs left are a very small population in Iran. In zoos, of course, location tells you nothing, so read on.</p></section>
<section class="card"><h2>Step 2: Look at the spots</h2>
<p><b>Solid spots mean cheetah.</b> A cheetah's coat is covered in single, solid black dots. Neither leopards nor jaguars have that pattern on their bodies.</p>
<p><b>Rosettes mean leopard or jaguar.</b> A rosette is a ring or broken ring of dark marks around a slightly darker patch. Leopard rosettes are smaller, tighter and usually empty in the centre. Jaguar rosettes are larger, more angular and usually have one or more small dots inside. Both species have solid spots on the head, legs and belly, so look at the flanks.</p></section>
<section class="card"><h2>Step 3: Check the face and build</h2>
<p>The cheetah's black tear marks, running from the inner corner of each eye down to the mouth, are the single quickest giveaway, along with its small, rounded head and greyhound like body. Leopards look balanced and athletic, with a long tail that helps them climb. Jaguars look like heavyweights: a broad head, thick neck and chest, sturdy legs and a noticeably shorter tail.</p></section>
<section class="card"><h2>Step 4: Watch what it does</h2>
<p>Behavior is a strong clue in the wild. A spotted cat lounging on a branch with a carcass wedged beside it is very likely a leopard. A cat sprinting across open grassland in the middle of the day is very likely a cheetah. A cat swimming a river or hunting caiman on a riverbank in South America is a jaguar.</p></section>
<section class="card"><h2>What about black panthers?</h2>
<p>Black panthers are leopards or jaguars with melanism, a genetic variation that produces very dark fur. You can still separate them by location, and in good light the rosettes show through faintly, so the empty versus dotted rosette rule still works. See <a href="../leopard.html#black">black panthers explained</a>.</p></section>
<section class="card"><h2>Other spotted cats that cause confusion</h2>
<p><b>Snow leopards</b> have pale smoky grey fur with open rosettes and an extremely long, thick tail, and live in the mountains of Central and South Asia. <b>Clouded leopards</b> are smaller forest cats of South and Southeast Asia with large, cloud shaped blotches. <b>Servals</b> in Africa are much smaller, with very large ears and long legs, and <b>ocelots</b> in the Americas are small cats with chain like markings.</p></section>
<section class="card"><h2>Quick checklist</h2><ul>
<li>Americas? Jaguar.</li><li>Solid spots and tear marks? Cheetah.</li><li>Empty rosettes, lithe body, Africa or Asia? Leopard.</li><li>Dotted rosettes, big head, stocky body? Jaguar.</li><li>Grey coat and huge tail in the mountains? Snow leopard.</li></ul></section>''',
     related=[("Leopard facts", "leopard.html"), ("Jaguar facts", "jaguar.html"), ("Cheetah facts", "cheetah.html"), ("Big cat comparison table", "compare.html"), ("Blog home", "blog/index.html")],
     sources=[CSG["leopard"], CSG["jaguar"], CSG["cheetah"], SDZ["leopard"], SDZ["jaguar"], SDZ["cheetah"]])

# ---------------------------------------------------------------- 3 CHEETAH SPEED
post("how-fast-is-a-cheetah", "How Fast Is a Cheetah? Top Speed, Acceleration & Limits | BigCatWise",
     "How fast cheetahs really run: 93 km/h measured in wild cheetahs, why most hunts are slower, how long a sprint lasts and what makes them so quick.",
     "How fast is a cheetah? What the research actually measured", headline="How fast is a cheetah?",
     lead="The fastest speed measured in wild hunting cheetahs is 25.9 metres per second, about 93 km/h or 58 mph, recorded with GPS collars in Botswana. The IUCN Cat Specialist Group gives speeds of up to about 103 km/h. But most real hunts are much slower, chases rarely last more than about 300 m, and acceleration, braking and turning matter as much as top speed.",
     body='''<section class="card"><h2>The numbers at a glance</h2>
<div class="tablewrap"><table><tbody>
<tr><th scope="row">Fastest run measured in wild cheetahs</th><td>25.9 m/s, about 93 km/h (58 mph)</td></tr>
<tr><th scope="row">Average top speed per run in the same study</th><td>14.9 m/s, about 54 km/h</td></tr>
<tr><th scope="row">Speed given by the IUCN Cat Specialist Group</th><td>Up to about 103 km/h during a chase</td></tr>
<tr><th scope="row">Typical chase length</th><td>Seldom more than about 300 m</td></tr>
<tr><th scope="row">Stride length</th><td>Up to about 7 m</td></tr>
</tbody></table></div></section>
<section class="card"><h2>How scientists measured wild cheetahs</h2>
<p>Older top speed figures came mostly from a handful of timed runs, often by captive cheetahs chasing a lure on a track. In 2013 a team led by Alan Wilson at the Royal Veterinary College, working with the Botswana Predator Conservation Trust, published the first detailed measurements of wild cheetahs hunting. They designed collars combining GPS with motion sensors and fitted them to five cheetahs in northern Botswana.</p>
<p>Over 367 runs, mostly hunts, the fastest speed recorded was 25.9 m/s. The five cheetahs' individual best speeds ranged from 20.1 to 25.9 m/s, and the average top speed of a run was 14.9 m/s. In other words, wild cheetahs usually do not run anywhere near flat out.</p></section>
<section class="card"><h2>If not top speed, what wins the hunt?</h2>
<p>The same study recorded some of the highest values ever measured in a land mammal for acceleration, deceleration and turning. Reporting on the study noted acceleration power of up to about 120 watts per kilogram of body mass, roughly double that of the fastest racing greyhounds. Successful hunts typically involved hard braking and sharp turns as the prey dodged. The cheetahs in this study mostly hunted impala, often in fairly thick vegetation, so agility mattered more than straight line speed. The authors suggested cheetahs chasing fast gazelles on open East African plains may use higher speeds.</p></section>
<section class="card"><h2>What makes a cheetah so fast?</h2>
<ul><li><b>Flexible spine:</b> it flexes and extends with each bound, adding to stride length, which can reach about 7 m.</li>
<li><b>Long legs and big thigh muscles</b> on a light, slim frame of 23 to 65 kg.</li>
<li><b>Semi retractable claws</b> that stay partly out, acting like the spikes on running shoes for grip when accelerating and turning.</li>
<li><b>A long tail</b>, about half the head and body length, used for balance and steering in turns.</li>
<li><b>Large lungs, heart and nasal passages</b>, which help it take in air quickly, including while it holds a suffocating bite on its prey after the chase.</li></ul></section>
<section class="card"><h2>How long can a cheetah keep it up?</h2>
<p>Not long. Cheetahs are sprinters, and the IUCN Cat Specialist Group notes that chases seldom cover more than about 300 m. A common explanation was that cheetahs give up because they overheat. A 2013 study by Hetem and colleagues, which measured body temperature in free living cheetahs, found that body temperature did not rise enough during hunts to explain stopping, and that it rose more after a successful hunt than during the chase. Their conclusion was that cheetahs do not abandon hunts because they overheat. The more likely limit is the extreme energy and muscle effort of each sprint.</p>
<p>After a chase a cheetah usually needs to rest and recover its breath before eating, and this is when lions and spotted hyenas may steal its kill.</p></section>
<section class="card"><h2>Is the cheetah really the fastest land animal?</h2>
<p>Yes. No other land animal has been reliably measured running faster over a short sprint. For comparison, the Nature paper's editorial summary notes that racing greyhounds reach about 18 m/s, well below the cheetah's measured best of 25.9 m/s.</p></section>
<section class="card"><h2>Key takeaways</h2><ul>
<li>Best measured wild speed: about 93 km/h (58 mph).</li>
<li>Most hunts are run at moderate speeds; agility decides success.</li>
<li>Sprints are short, rarely over about 300 m.</li>
<li>Overheating is not why cheetahs stop, according to direct temperature measurements.</li></ul>
<p>More on the species in our <a href="../cheetah.html">cheetah facts</a> page.</p></section>''',
     related=[("Cheetah facts", "cheetah.html"), ("Big cat behavior", "behavior.html"), ("Leopard vs jaguar vs cheetah", "blog/leopard-vs-jaguar-vs-cheetah.html"), ("Blog home", "blog/index.html")],
     sources=[WILSON, HETEM, ("Scientific American (2013) Speed test devised for wild cheetahs", "https://www.scientificamerican.com/article/speed-test-devised-for-wild-cheetahs/"), CSG["cheetah"], NZP["cheetah"]])

# ---------------------------------------------------------------- 4 TIGER STRIPES
post("why-do-tigers-have-stripes", "Why Do Tigers Have Stripes? The Science of Camouflage | BigCatWise",
     "Why tigers have stripes: camouflage for an ambush hunter, why an orange coat looks green to deer, and how unique stripe patterns let scientists count tigers.",
     "Why do tigers have stripes?", headline="Why do tigers have stripes?",
     lead="Tigers have stripes mainly for camouflage. The dark vertical stripes break up the outline of a large animal among tall grass, reeds and forest shadows, letting an ambush hunter creep close to its prey. And the orange coat works better than it looks to us: deer and most other mammals see colour differently from humans, and to them orange is hard to tell apart from green.",
     body='''<section class="card"><h2>Stripes as disruptive camouflage</h2>
<p>A tiger hunts by stalking to within a short distance of its prey and then rushing it, so the most important thing is not to be noticed first. Camouflage that breaks up an animal's outline is called disruptive colouration. In vegetation full of vertical stems and long shadows, bold vertical stripes make it harder to pick out the shape of a tiger's body against the background, especially in the low light of dawn and dusk when tigers are often active.</p>
<p>Tigers are the only cats with stripes. Other big cats achieve a similar effect with spots and rosettes, which suit the dappled light of woodland and forest.</p></section>
<section class="card"><h2>Why is a tiger orange, not green?</h2>
<p>To a human eye, a bright orange animal seems like poor camouflage in a green forest. The answer lies in who is looking. Humans are trichromats, with three types of colour sensitive cone cell. Most mammals, including deer, are dichromats, and they cannot reliably tell orange and green apart.</p>
<p>A 2019 study by Fennell and colleagues at the University of Bristol, published in the Journal of the Royal Society Interface, modelled how detectable different colours are to human like and dichromat observers in natural scenes. Their simulations showed that, viewed by a dichromat, a tiger's colour is very effective camouflage. They point out that deer are dichromats, so to them most predators like tigers appear green, and there is little evolutionary pressure for tigers to actually become green. They also note that making a green coat would require a major change to mammal biochemistry, since mammal fur colours come from just two pigment types, eumelanin (black and brown) and phaeomelanin (yellow to red).</p></section>
<section class="card"><h2>Is every tiger's stripe pattern unique?</h2>
<p>Yes. According to the IUCN Cat Specialist Group, stripe patterns vary between individuals in the number, width and shape of stripes, and whether they split or break into spots. The pattern on a tiger's left side is also different from its right side. This is enormously useful for conservation: scientists set camera traps in pairs on opposite sides of a trail so they photograph both flanks, then identify individual tigers from their stripes. Repeated detections of known animals let them estimate population size using capture recapture statistics, which underpins many national tiger surveys.</p></section>
<section class="card"><h2>Are tigers striped under the fur?</h2>
<p>The stripe pattern is set in the skin where the hairs grow, so shaved tiger skin shows the pattern as darker and lighter areas. The stripes are not painted on the fur alone.</p></section>
<section class="card"><h2>What about white tigers?</h2>
<p>White tigers still have stripes, which are ash grey to brown rather than black, on a white coat, usually with blue eyes. They are a rare colour variant, not a separate species or subspecies. The IUCN Cat Specialist Group notes that the last documented white tiger in the wild was shot in Bihar, India, in 1958. A white coat would make camouflage harder in most tiger habitats, which may help explain why the variant is so rare in the wild.</p></section>
<section class="card"><h2>Do stripes do anything else?</h2>
<p>Camouflage is the main accepted function. Other markings may carry signals at close range; for example, tigers have a conspicuous white spot on the back of each ear, which researchers have suggested may help communication, such as cubs following their mother, but this is a hypothesis rather than an established fact. How exactly the stripe pattern forms during development in tigers is still being studied.</p></section>
<section class="card"><h2>Key takeaways</h2><ul>
<li>Stripes break up the tiger's outline in grass and forest, helping it ambush prey.</li>
<li>Orange looks similar to green to deer and other dichromatic mammals.</li>
<li>Each tiger's stripes are unique, and left and right sides differ.</li>
<li>Scientists count wild tigers by photographing stripe patterns with camera traps.</li></ul>
<p>More in our <a href="../tiger.html">tiger facts</a> guide.</p></section>''',
     related=[("Tiger facts", "tiger.html"), ("Big cat behavior", "behavior.html"), ("How many big cats are left?", "blog/how-many-big-cats-are-left.html"), ("Blog home", "blog/index.html")],
     sources=[FENNELL, CSG["tiger"], WWF["tiger"], SDZ["tiger"]])

# ---------------------------------------------------------------- 5 POPULATIONS
post("how-many-big-cats-are-left", "How Many Big Cats Are Left in the Wild? 2026 Estimates | BigCatWise",
     "Latest estimates of how many lions, tigers, leopards, jaguars, cheetahs and snow leopards remain in the wild, what the numbers mean, and which is rarest.",
     "How many big cats are left in the wild?", headline="How many big cats are left in the wild?",
     lead="On the latest IUCN Cat Specialist Group figures there are about 3,700 to 5,600 wild tigers excluding cubs, roughly 7,400 to 8,000 snow leopards, about 6,500 mature cheetahs, about 22,000 to 25,000 lions in Africa plus about 670 in India, and 57,000 to 64,000 jaguars in the Amazon alone. There is no reliable global count for leopards. These are estimates with wide error margins.",
     body='''<section class="card"><h2>Latest estimates by species</h2>
<div class="tablewrap"><table><thead><tr><th>Species</th><th>Estimate</th><th>What is counted</th><th>IUCN status</th></tr></thead><tbody>
<tr><td><a href="../tiger.html">Tiger</a></td><td>3,726 to 5,578</td><td>Individuals excluding cubs (about 3,140 mature)</td><td>Endangered</td></tr>
<tr><td><a href="../cheetah.html">Cheetah</a></td><td>About 6,517 mature (about 7,100 adults and adolescents)</td><td>From Durant et al. 2017</td><td>Vulnerable</td></tr>
<tr><td><a href="../snow-leopard.html">Snow leopard</a></td><td>7,446 to 7,996</td><td>All individuals (2,710 to 3,386 mature)</td><td>Vulnerable</td></tr>
<tr><td><a href="../lion.html">Lion</a></td><td>About 22,000 to 25,000 in Africa; about 670 in India</td><td>Adults and subadults (Africa 2025; India 2020)</td><td>Vulnerable</td></tr>
<tr><td><a href="../jaguar.html">Jaguar</a></td><td>57,000 to 64,000 in Amazonia</td><td>About 89% of the total population</td><td>Near Threatened</td></tr>
<tr><td><a href="../leopard.html">Leopard</a></td><td>No reliable global estimate</td><td>Densities from about 1 to over 30 per 100 km&sup2; depending on area</td><td>Vulnerable</td></tr>
</tbody></table></div>
<p class="note">All figures from IUCN SSC Cat Specialist Group species summaries, which draw on IUCN Red List assessments and the studies they cite.</p></section>
<section class="card"><h2>Why the numbers are uncertain</h2>
<p>Big cats are secretive, widely spread and often live at low densities in difficult terrain, so nobody counts them one by one. Researchers estimate numbers from camera trap surveys that identify individuals by their markings, from tracks and signs, from genetic sampling of droppings, and from occupancy models that estimate how much habitat is used. Results from surveyed areas are then extrapolated to similar habitat elsewhere. Methods differ by species and region, and large areas, such as parts of the Sahara or central Africa, have little survey data.</p>
<p>That is why estimates come as ranges and why figures can shift sharply when better data arrive. The snow leopard is a good example: global estimates before 2003 were around 4,000 to 6,500, while the most recent is 7,446 to 7,996. That rise reflects more and better surveys at least as much as any real change in numbers.</p></section>
<section class="card"><h2>Total, adult or mature: read the label</h2>
<p>IUCN Red List assessments focus on mature individuals, meaning adults capable of breeding, because they determine a population's future. That figure is often much lower than the total. For snow leopards, the mature estimate of 2,710 to 3,386 is well under half of the total estimate. When comparing species, check whether a figure counts all animals, adults only or mature breeders.</p></section>
<section class="card"><h2>Which big cat is the rarest?</h2>
<p>By headline number, tigers and snow leopards are the scarcest of the six species, each with only a few thousand mature adults. By IUCN category the tiger is the only one listed as Endangered at species level.</p>
<p>Some populations are far rarer than the species totals suggest:</p>
<ul><li><b>Asiatic cheetah:</b> fewer than 50 mature individuals, only in Iran. Critically Endangered.</li>
<li><b>Jaguars of Brazil's Atlantic Forest:</b> about 200 adults, plus or minus 80.</li>
<li><b>Asiatic lion:</b> about 670 adults and subadults in 2020, all in one landscape in Gujarat, India.</li>
<li><b>Amur leopard:</b> a single small population in the Russian Far East and neighbouring northeast China.</li>
<li><b>West African lions:</b> mostly in populations of fewer than 50, with the largest, about 187 lions, in the W Arly Pendjari complex.</li></ul></section>
<section class="card"><h2>Are big cat numbers going up or down?</h2>
<p>Mostly down, with some bright spots. African lions fell from about 33,000 in 2006 to about 25,000 in 2018 on IUCN Cat Specialist Group figures, though populations in southern Africa are stable or increasing. Of the cheetah subpopulations whose trends could be assessed, 14 of 18 were declining. Leopard range shrank by 11 percent between 2016 and 2023. Tigers have lost most of their range over the past century, yet the 2025 Green Status assessment found that conservation has prevented even greater losses, and India's Asiatic lions have grown steadily from a tiny remnant over the past century. See <a href="../conservation.html">big cat conservation</a> for what is driving these trends and what helps.</p></section>''',
     related=[("Big cat conservation", "conservation.html"), ("Big cat comparison table", "compare.html"), ("Tiger facts", "tiger.html"), ("Snow leopard facts", "snow-leopard.html"), ("Blog home", "blog/index.html")],
     sources=[CSG["tiger"], CSG["lion"], CSG["leopard"], CSG["jaguar"], CSG["cheetah"], CSG["snow"], DURANT, IUCN])

# ---------------------------------------------------------------- BLOG INDEX
add("blog/index.html", "BigCatWise Blog: Answers to Big Cat Questions | BigCatWise",
    "The BigCatWise blog answers specific big cat questions in depth: roaring, cheetah speed, tiger stripes, telling spotted cats apart and how many big cats are left.",
    "BigCatWise blog", kind="page", headline="Blog",
    lead="In depth, sourced answers to specific questions about big cats. New posts are added when there is something genuinely useful to say.",
    body='<div class="grid">' + "".join('<a class="tile" href="%s"><h3>%s</h3><p>%s</p></a>' % (p.path.split("/")[1], p.headline, p.description) for p in POSTS) + '</div>',
    related=[("Compare big cats", "compare.html"), ("Big cat FAQ", "faq.html")], priority="0.7")
