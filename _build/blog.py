from build import add, TODAY
from sources import LAURENSON1994, MILLS2014, DURANT2000, DURANT2004, ATHREYA2013, ODDEN2014, ATHREYA2016, ATHREYA2011, BRACZKOWSKI2018, JACOBSON2016, CARTER2012, LINKIE2011, KARANTH2000, CSG, SDZ, PAN, WWF, NZP, IUCN, WILSON, DURANT, KLEMUK, WEISS, FENNELL, SLT, PACKER1990, PACKER1991, HEINSOHN1995, GOODRICH2010, SIMCHAROEN2014, BARLOW2011, BALME2017, HAYWARD2006, LYNGDOH2014, SHEHZAD2012, ERIKSSON2022, HAYWARD2016JAG, WEST2002, KAYS2002, YAMAGUCHI2004, TAYLOR1973, HETEM2013, SOLARI2025, YANG2025, CANCELLARE2024, WANG2024

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
<li>Americas? Jaguar.</li><li>Solid spots and tear marks? Cheetah.</li><li>Empty rosettes, lithe body, Africa or Asia? Leopard.</li><li>Dotted rosettes, big head, stocky body? Jaguar.</li><li>Grey coat and huge tail in the mountains? Snow leopard.</li></ul><p>For all six species and a region by region list, see <a href="../which-big-cat-is-it.html">which big cat is it?</a></p></section>''',
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
<p>Not long. Cheetahs are sprinters, and the IUCN Cat Specialist Group notes that chases seldom cover more than about 300 m. A common explanation was that cheetahs give up because they overheat. A 2013 study by Hetem and colleagues, which measured body temperature in free living cheetahs, found that body temperature did not rise enough during hunts to explain stopping, and that it rose more after a successful hunt than during the chase. Their conclusion was that cheetahs do not abandon hunts because they overheat. The more likely limit is the extreme energy and muscle effort of each sprint. Our deeper dive is <a href="do-cheetahs-abandon-hunts-because-they-overheat.html">do cheetahs abandon hunts because they overheat?</a></p>
<p>After a chase a cheetah usually needs to rest and recover its breath before eating, and this is when lions and spotted hyenas may steal its kill.</p></section>
<section class="card"><h2>Is the cheetah really the fastest land animal?</h2>
<p>Yes. No other land animal has been reliably measured running faster over a short sprint. For comparison, the Nature paper's editorial summary notes that racing greyhounds reach about 18 m/s, well below the cheetah's measured best of 25.9 m/s.</p></section>
<section class="card"><h2>Key takeaways</h2><ul>
<li>Best measured wild speed: about 93 km/h (58 mph).</li>
<li>Most hunts are run at moderate speeds; agility decides success.</li>
<li>Sprints are short, rarely over about 300 m.</li>
<li>Overheating is not why cheetahs stop, according to direct temperature measurements.</li></ul>
<p>More on the species in our <a href="../cheetah.html">cheetah facts</a> page.</p></section>''',
     related=[("Cheetah facts", "cheetah.html"), ("Big cat behavior", "behavior.html"), ("Leopard vs jaguar vs cheetah", "blog/leopard-vs-jaguar-vs-cheetah.html"), ("Cheetah worksheet for 3rd grade", "teachers/cheetah-worksheet-3rd-grade.html"), ("Blog home", "blog/index.html")],
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

# ---------------------------------------------------------------- 6 LION PRIDES (8 Oct 2026)
post("why-do-lions-live-in-prides", "Why Do Lions Live in Prides? What the Research Shows | BigCatWise",
     "Why lions live in groups when other big cats live alone: the field research on hunting, cub defence and territory, and what DNA revealed about pride kinship.",
     "Why do lions live in prides? It is not mainly about hunting", headline="Why do lions live in prides?",
     published="2026-10-08", modified="2026-10-08",
     lead="Lions live in prides mainly to protect their cubs and to hold on to good territory, not because group hunting gets each lion more food. Long term research in Tanzania's Serengeti found that females in groups did not reliably eat better than lone females, but groups of mothers were effective at defending cubs from infanticidal males, and larger groups won territorial contests against smaller ones.",
     body='''<section class="card"><h2>The short answer</h2>
<ul><li><b>Cub defence:</b> mothers pool their cubs in a nursery group, called a cr&egrave;che, and defend them together against males that would kill them.</li>
<li><b>Territory:</b> prides compete with neighbouring prides, and bigger groups tend to win.</li>
<li><b>Family:</b> the females in a pride are close relatives, so helping each other also helps shared genes.</li>
<li><b>Food is not the main reason:</b> group hunting does not consistently raise each lion's share of the meal.</li></ul></section>
<section class="card"><h2>Lions are the odd cat out</h2>
<p>Most wild cats spend their adult lives alone. Tigers, leopards, jaguars and snow leopards mostly live and hunt solo, meeting mainly to mate, and a mother raises her cubs by herself. The IUCN Cat Specialist Group describes the lion as the most social of all cat species, living in complex social systems called prides and showing group territorial behaviour. It adds that females engage in several cooperative behaviours unique among cats: pride members often give birth around the same time, and the young are reared communally.</p>
<p>A typical African pride is built around four to six adult lionesses, though prides can range from 1 to 21 females, according to the Cat Specialist Group. The lionesses are the core and the most stable part of the pride. One or more adult males, usually a coalition of two, hold tenure over the pride, typically for one breeding cycle of about two to three years. In India's Gir forest, most prides contain only two females. The closest thing to this among the other big cats is the cheetah, where some males form coalitions, often brothers, but female cheetahs live alone (see our <a href="../cheetah.html">cheetah facts</a>).</p></section>
<section class="card"><h2>The obvious idea: hunting together</h2>
<p>For a long time the natural assumption was that lions live in groups because cooperative hunting lets them catch more and bigger prey. Craig Packer, David Scheel and Anne Pusey tested this with years of observations of foraging female lions in the Serengeti, published in <i>The American Naturalist</i> in 1990 under a telling title: "Why lions form groups: food is not enough."</p>
<p>They found that when prey was scarce, two group sizes gave the best foraging success per lion: a single female hunting alone, or a group of five or six. When prey was plentiful, group size made no significant difference. If food alone explained grouping, females in small prides should have hunted alone in the lean season. Instead, radio collar data showed that females in small prides usually foraged in as large a group as they could, even when that lowered their feeding efficiency. Something other than food was holding them together.</p></section>
<section class="card"><h2>Reason 1: defending cubs from infanticide</h2>
<p>When new males take over a pride, they often kill young cubs fathered by the previous males. The Cat Specialist Group notes that infanticide is common after a takeover if cubs are under about 12 months old, and that most females lose their cubs within about a month; the lionesses then come back into breeding condition sooner, so the new males can father cubs earlier.</p>
<p>The 1990 Serengeti study found that mothers keep their cubs in a cr&egrave;che and form highly stable maternity groups that are effective in defending the cubs against infanticidal males. Most large prides contained a cr&egrave;che of four or five mothers, which lines up neatly with the group sizes those prides used.</p></section>
<section class="card"><h2>Reason 2: holding the best territory</h2>
<p>Prides defend territories, and neighbouring prides clash. The same study reported that females compete aggressively against neighbouring prides and that larger groups successfully repel smaller ones in territorial disputes. So lionesses in small prides stick together even at a cost in food.</p>
<p>Territorial defence is not perfectly fair, though. In experiments reported in <i>Science</i> in 1995, Robert Heinsohn and Craig Packer played recordings of roars from unfamiliar lions to simulate an intruding group. Some females consistently led the approach toward the "intruder," while others lagged behind and avoided the risks of fighting. The leaders seemed to recognise the laggards but did not punish them, which the authors argued is hard to explain with simple theories of cooperation.</p></section>
<section class="card"><h2>Reason 3: it is a family business</h2>
<p>Female lions usually stay in the pride where they were born, while young males leave. In 1991, Packer and colleagues used DNA fingerprinting to map relatedness in lion prides and reported their results in <i>Nature</i>. Female pride companions were always closely related. Male companions in a coalition were either closely related or unrelated, and mating partners were usually unrelated.</p>
<p>The DNA work also showed that breeding success among coalition males becomes more uneven as coalitions get larger, and that males rarely form large coalitions with non relatives. In other words, a male only accepts the role of a non breeding "helper" in a big coalition when his partners are close kin, so helping them still passes on some of his genes.</p></section>
<section class="card"><h2>So does hunting together matter at all?</h2>
<p>Yes, but it is not the whole story. Lionesses often hunt together and a group can tackle large prey that a single lion would struggle with. The point of the 1990 research is that hunting success per lion does not, by itself, explain why prides exist or why lionesses gather in the group sizes they do. Protecting cubs and holding territory explain the pattern much better.</p>
<p>Pride sizes also shrink where human hunting pressure is high and prey is scarce, according to the Cat Specialist Group. For more on pride roles, see our <a href="../lion.html#pride">lion pride guide</a> and <a href="../behavior.html">big cat behavior</a>.</p></section>
<section class="card"><h2>Key takeaways</h2><ul>
<li>The lion is the most social cat species; a pride centres on related females.</li>
<li>Serengeti research showed food alone does not explain why lions group.</li>
<li>Groups of mothers defend cubs against infanticidal males, and bigger prides win territorial contests.</li>
<li>Female pridemates are close kin; males in large coalitions are usually relatives.</li></ul></section>''',
     faq=[("Why do lions live in groups when other big cats live alone?", "Research in the Serengeti found that lionesses group mainly to defend their cubs against infanticidal males and to hold territory against neighbouring prides. Food gains from group hunting are not enough on their own to explain it."),
          ("How many lions are in a pride?", "According to the IUCN Cat Specialist Group, African prides average four to six adult lionesses, ranging from 1 to 21, usually with a coalition of about two adult males plus cubs and subadults. In India's Gir forest most prides have only two females."),
          ("Are the lionesses in a pride related?", "Yes. A 1991 DNA fingerprinting study published in Nature found that female pride companions are always closely related, while male coalition partners may be related or unrelated.")],
     related=[("Lion facts", "lion.html"), ("Big cat behavior", "behavior.html"), ("Which big cats can roar?", "blog/which-big-cats-can-roar.html"), ("How many big cats are left?", "blog/how-many-big-cats-are-left.html"), ("Lion pride lesson plan", "teachers/lion-pride-lesson-plan.html"), ("Blog home", "blog/index.html")],
     sources=[PACKER1990, HEINSOHN1995, PACKER1991, CSG["lion"], CSG["cheetah"]])

# ---------------------------------------------------------------- 7 TIGER TERRITORY (11 Oct 2026)
post("how-big-is-a-tigers-territory", "How Big Is a Tiger's Territory? Home Range Research | BigCatWise",
     "A tiger's territory can be 12 km\u00b2 or more than 1,000 km\u00b2. Radio collar studies from Russia, Thailand and Bangladesh show why prey decides the size.",
     "How big is a tiger's territory? From 12 to over 1,000 km\u00b2", headline="How big is a tiger's territory?",
     published="2026-10-11", modified="2026-10-11",
     lead="A tiger's territory can be as small as about 12 to 14 km&sup2; or bigger than 1,000 km&sup2;, depending mainly on how much prey is around. Radio collar studies found female tigers using about 12 to 14 km&sup2; in the Bangladesh Sundarbans, about 70 to 84 km&sup2; in western Thailand and about 390 km&sup2; in the Russian Far East, where males averaged about 1,385 km&sup2;. Males' ranges are several times larger than females', and both sexes keep largely separate territories.",
     body='''<section class="card"><h2>The short answer</h2>
<div class="tablewrap"><table><thead><tr><th>Study area</th><th>Female home range</th><th>Male home range</th><th>Study</th></tr></thead><tbody>
<tr><td>Sundarbans mangroves, Bangladesh</td><td>About 12 to 14 km&sup2; (2 females)</td><td>Not measured</td><td>Barlow et al. 2011</td></tr>
<tr><td>Huai Kha Khaeng, Thailand</td><td>About 70 to 84 km&sup2; (7 females)</td><td>About 267 to 294 km&sup2; (4 males)</td><td>Simcharoen et al. 2014</td></tr>
<tr><td>Sikhote-Alin, Russian Far East</td><td>About 390 km&sup2; (14 females)</td><td>About 1,385 km&sup2; (5 males)</td><td>Goodrich et al. 2010</td></tr>
</tbody></table></div>
<p class="note">Figures are study means. Researchers used different methods (minimum convex polygons or kernel estimates), so the ranges in each row reflect the method used, and small samples mean individual tigers can differ a lot.</p></section>
<section class="card"><h2>Territory or home range?</h2>
<p>A home range is the whole area an animal uses for its everyday life: hunting, resting and raising young. A territory is an area an animal defends or keeps for itself. For tigers the two are close to the same thing, because adult tigers are solitary and neighbours of the same sex barely overlap. In the Russian study, the average overlap between neighbouring females was only about 0.11, and between neighbouring males about 0.14, on a scale where 1 would mean sharing the same ground completely. In Thailand, the researchers found that territories of both males and females had little overlap, which indicated that both sexes were territorial. For the basics of tiger life, see our <a href="../tiger.html#life">tiger facts</a>.</p></section>
<section class="card"><h2>The biggest territories: Amur tigers in Russia</h2>
<p>The largest home ranges come from the cold forests of the Russian Far East. J. Marc Goodrich, Dale Miquelle and colleagues followed radio collared Amur tigers on the Sikhote-Alin Biosphere Zapovednik from 1992 to 2006 and published the results in the <i>Journal of Mammalogy</i> in 2010.</p>
<p>Resident females used home ranges averaging about 390 km&sup2; (20 home ranges of 14 females), while males averaged about 1,385 km&sup2; (6 home ranges of 5 males). The difference between the sexes was statistically significant.</p>
<p>The study also tracked what young tigers did when they grew up. All seven radio collared male cubs left their mother's home range, but only two of six female cubs did. Daughters tended to settle next to, or inside part of, their mother's range.</p></section>
<section class="card"><h2>Mid sized territories: tigers in Thailand</h2>
<p>In Huai Kha Khaeng Wildlife Sanctuary in western Thailand, Achara Simcharoen and colleagues fitted GPS collars to 11 tigers, four males and seven females, and reported the results in <i>Oryx</i> in 2014. Male home ranges averaged 267 to 294 km&sup2; and female ranges averaged 70 to 84 km&sup2;, depending on the method. That is roughly a fifth of the Russian female figure.</p></section>
<section class="card"><h2>The smallest: tigers in mangrove forest</h2>
<p>In the Bangladesh Sundarbans, the world's largest mangrove forest, Adam Barlow and colleagues collared two adult females and published preliminary results in <i>Oryx</i> in 2011. Their home ranges averaged only 12.3 to 14.2 km&sup2;. The authors calculated that a range of about 14.2 km&sup2; would mean roughly seven adult females per 100 km&sup2; in that part of the forest. Even in this small range, one tiger moved up to 11.3 km in a single day. The authors cautioned that the estimates are preliminary, based on just two tigers, but said they point to good quality tiger habitat in the Sundarbans.</p></section>
<section class="card"><h2>Why the size varies so much: prey</h2>
<p>The main driver is food. When the Thailand team compared female home range size and prey abundance at six locations in Thailand and at sites in India, Nepal, Bangladesh and Russia, they found a significant negative correlation: the more prey an area had, the smaller the female tigers' home ranges. A female needs a range big enough to feed herself and her cubs, so where prey is thin, she has to cover far more ground. The IUCN Cat Specialist Group estimates that a tiger needs around 50 to 60 large prey animals a year, which helps explain why prey poor forests demand such huge ranges.</p>
<p>Males range more widely than females. A male's range often overlaps those of one to three females.</p></section>
<section class="card"><h2>Why territory size matters for conservation</h2>
<p>Territory size sets how many tigers a reserve can hold. A reserve that could support many females in rich mangrove or lowland forest might hold only a handful in the Russian Far East. That is why the Thailand authors suggested that monitoring prey abundance and home range size can give managers practical targets for tiger conservation.</p>
<p>The Russian study found a second link. When human caused deaths were low, females survived long enough to split their home range with their daughters, which produced smaller home ranges and a higher density of breeding females. When human caused deaths were high, females often died before they could hand over part of their range, and tiger density stayed well below what the habitat could support. The authors concluded that the effects of poaching reach beyond the animals killed, and that reserves must be well protected if they are to act as source populations for nearby unprotected forest. For more on threats and recovery, see <a href="../conservation.html">big cat conservation</a> and <a href="how-many-big-cats-are-left.html">how many big cats are left</a>.</p></section>
<section class="card"><h2>Key takeaways</h2><ul>
<li>Tiger territories range from about 12 km&sup2; in the Sundarbans to more than 1,000 km&sup2; for males in Russia.</li>
<li>Male ranges are several times larger than female ranges.</li>
<li>Neighbouring tigers of the same sex barely overlap, so tigers are territorial.</li>
<li>More prey means smaller female home ranges, and poaching keeps tiger density below what the habitat could support.</li></ul></section>''',
     faq=[("How big is a tiger's territory?", "It depends on prey. Radio collar studies found female home ranges averaging about 12 to 14 km&sup2; in the Bangladesh Sundarbans, about 70 to 84 km&sup2; in western Thailand and about 390 km&sup2; in the Russian Far East, where males averaged about 1,385 km&sup2;."),
          ("Do male tigers have bigger territories than females?", "Yes. In Thailand male ranges averaged 267 to 294 km&sup2; against 70 to 84 km&sup2; for females, and in Russia males averaged about 1,385 km&sup2; against about 390 km&sup2; for females."),
          ("Why do tiger territories vary so much in size?", "Mainly because of prey. A 2014 study comparing sites in Thailand, India, Nepal, Bangladesh and Russia found that female home ranges were smaller where prey was more abundant."),
          ("Do tigers share territory?", "Very little. Neighbouring tigers of the same sex had only slight overlap in Russia and Thailand. Young females often settle next to or within part of their mother's range, while young males leave.")],
     related=[("Tiger facts", "tiger.html"), ("Big cat behavior", "behavior.html"), ("Big cat habitats", "habitats.html"), ("Why do tigers have stripes?", "blog/why-do-tigers-have-stripes.html"), ("Why do lions live in prides?", "blog/why-do-lions-live-in-prides.html"), ("Blog home", "blog/index.html")],
     sources=[GOODRICH2010, SIMCHAROEN2014, BARLOW2011, CSG["tiger"]])

# ---------------------------------------------------------------- 8 LEOPARDS IN TREES (12 Oct 2026)
post("why-do-leopards-drag-their-kills-into-trees", "Why Do Leopards Drag Their Kills Into Trees? The Research | BigCatWise",
     "Leopards hoist about half their kills into trees, mainly to stop hyenas stealing them. What a study of 2,032 kills in South Africa found.",
     "Why do leopards drag their kills into trees? To beat the hyenas", headline="Why do leopards drag their kills into trees?",
     published="2026-10-12", modified="2026-10-12",
     lead="Leopards drag their kills into trees mainly to stop other predators stealing them, especially spotted hyenas. A study of 2,032 kills made by 104 leopards in South Africa's Sabi Sand Game Reserve found that leopards hoisted 51% of their kills, that at least 21% of kills were stolen, mostly by hyenas, and that kills left on the ground were more likely to be lost. Females that lost more kills raised fewer cubs.",
     body='''<section class="card"><h2>The short answer</h2>
<p>Hoisting a carcass into a tree is a form of food caching: the leopard stores its meal somewhere other animals cannot easily reach and comes back to feed over time. Researchers have proposed four possible reasons for it, which can overlap. The evidence from the largest study so far points clearly to one of them.</p>
<div class="tablewrap"><table><thead><tr><th>Possible reason</th><th>The idea</th><th>What the 2017 study found</th></tr></thead><tbody>
<tr><td>Avoiding theft (kleptoparasitism)</td><td>Keep the kill away from hyenas and lions</td><td>Strongly supported</td></tr>
<tr><td>Feeding time</td><td>Store a large meal to eat over a longer period</td><td>Hoisted kills were fed on for longer, but this looked like a side benefit</td></tr>
<tr><td>Food spoiling</td><td>Keep meat away from heat and scavenging insects</td><td>Possible added benefit, not the main driver</td></tr>
<tr><td>Food glut</td><td>Store surplus when prey is easy to catch</td><td>Leopards hoisted less often during resource pulses, not more</td></tr>
</tbody></table></div></section>
<section class="card"><h2>The study: 2,032 kills by 104 leopards</h2>
<p>Guy Balme, Jennifer Miller, Ross Pitman and Luke Hunter studied leopards in the Sabi Sand Game Reserve, next to Kruger National Park in South Africa, and published the results in the <i>Journal of Animal Ecology</i> in 2017. They used records of 2,032 prey items killed by 104 known leopards between 2013 and 2015. For each kill they looked at whether it was hoisted, how long the leopard fed on it and whether another animal took it, then tested how this varied with the leopard's sex and age, the size of the prey, vegetation, elevation, weather, and the risk posed by dominant competitors such as hyenas and lions.</p>
<p>Leopards hoisted 51% of their kills. At least 21% of all kills were kleptoparasitized, the scientific term for having food stolen by another animal, and most of the thieves were spotted hyenas (<i>Crocuta crocuta</i>).</p></section>
<section class="card"><h2>Which kills get hoisted?</h2>
<p>Leopards did not hoist everything. They were most likely to haul up kills of an intermediate size. A very small prey animal can be eaten quickly on the spot, so there is little to protect, while a very large one may be too heavy to drag up a trunk. Leopards were also more likely to hoist when certain competitors were around, and less likely to hoist during a resource pulse, a period when prey was abundant and easy to catch. That last result counts against the idea that tree caching is mainly about storing surplus food.</p>
<p>Once a kill was in a tree, the leopard fed on it for longer than on kills left on the ground. In other words, the tree acts as a safe larder that lets the cat return to the same carcass.</p></section>
<section class="card"><h2>Which kills get stolen?</h2>
<p>Kills were more likely to be stolen when the prey was larger, when it was not hoisted, and in parts of the reserve where the chance of meeting hyenas was highest. Thefts were also more likely at lower temperatures. Spotted hyenas are poor climbers, so a carcass wedged in the fork of a tree is much harder for them to reach than one lying in the grass. For more on how leopards hunt and where they live, see our <a href="../leopard.html#hunting">leopard facts</a>.</p></section>
<section class="card"><h2>Why it matters: lost kills mean fewer cubs</h2>
<p>The most striking result is about breeding. Female leopards that lost a higher share of their kills to thieves had lower annual reproductive success than females that lost fewer kills. Stolen meat is not just a missed meal; for a mother raising cubs alone it can mean fewer surviving young. The authors concluded that their results strongly support the kleptoparasitism avoidance explanation, and that hoisting is a key adaptation that lets leopards live alongside high densities of larger competitors.</p></section>
<section class="card"><h2>Does this shape what leopards hunt?</h2>
<p>Possibly. A separate review by Matt Hayward and colleagues, published in the <i>Journal of Zoology</i> in 2006, analysed 33 studies of leopard diet from 13 countries. It found that leopards preferentially prey on species weighing roughly 10 to 40 kg, with a most preferred prey mass of about 25 kg. Impala, bushbuck and common duiker were significantly preferred. The authors noted that leopards favour prey that lives in small herds and dense habitat and poses little risk of injury during capture.</p>
<p>The 2017 study adds a twist. Its authors argued that leopards may pick smaller prey than simple optimal foraging theory would predict, trading the extra meat from a big kill against the higher chance of losing it to hyenas. A 25 kg impala that fits in a tree may be worth more to a leopard than a bigger animal it cannot protect.</p></section>
<section class="card"><h2>Do other big cats do this?</h2>
<p>Tree caching is a leopard speciality. Lions and tigers are much heavier, live in different settings and handle competitors differently: lions defend kills as a group, which is one of the themes in <a href="why-do-lions-live-in-prides.html">why do lions live in prides?</a> Cheetahs, by contrast, often lose kills to lions and hyenas and eat quickly instead. You can compare how the spotted cats differ in <a href="leopard-vs-jaguar-vs-cheetah.html">leopard vs jaguar vs cheetah</a>.</p></section>
<section class="card"><h2>Key takeaways</h2><ul>
<li>In Sabi Sand, leopards hoisted 51% of 2,032 recorded kills.</li>
<li>At least 21% of kills were stolen, mostly by spotted hyenas, and kills left on the ground were more likely to be taken.</li>
<li>Leopards hoisted mid sized kills most often and fed longer on hoisted kills.</li>
<li>Females that lost more kills had lower annual reproductive success.</li>
<li>Leopards prefer prey of about 10 to 40 kg, a size they can kill safely and often carry.</li></ul></section>''',
     faq=[("Why do leopards drag their kills into trees?", "Mainly to stop other predators stealing them. A study of 2,032 kills in South Africa found that kills left on the ground were more likely to be stolen, mostly by spotted hyenas, and the authors concluded that hoisting is chiefly a way to avoid theft."),
          ("How often do leopards put kills in trees?", "In the Sabi Sand Game Reserve, leopards hoisted 51% of their kills between 2013 and 2015. They were most likely to hoist kills of an intermediate size."),
          ("What steals food from leopards?", "Mostly spotted hyenas. At least 21% of leopard kills in the Sabi Sand study were stolen, and hyenas took most of them."),
          ("What size prey do leopards prefer?", "A review of 33 diet studies found leopards prefer prey of about 10 to 40 kg, with a most preferred mass of about 25 kg. Impala, bushbuck and common duiker were significantly preferred.")],
     related=[("Leopard facts", "leopard.html"), ("Big cat behavior", "behavior.html"), ("Leopard vs jaguar vs cheetah", "blog/leopard-vs-jaguar-vs-cheetah.html"), ("Why do lions live in prides?", "blog/why-do-lions-live-in-prides.html"), ("Research papers", "research/index.html"), ("Blog home", "blog/index.html")],
     sources=[BALME2017, HAYWARD2006, CSG["leopard"]])

# ---------------------------------------------------------------- 9 SNOW LEOPARD DIET (13 Oct 2026)
post("what-do-snow-leopards-eat", "What Do Snow Leopards Eat? Diet and Favourite Prey | BigCatWise",
     "Snow leopards mainly eat wild mountain goats and sheep, especially ibex and blue sheep of about 55 kg. What a review of 1,696 scats and a DNA study found.",
     "What do snow leopards eat? Mostly wild goats and sheep heavier than themselves", headline="What do snow leopards eat?",
     published="2026-10-13", modified="2026-10-13",
     lead="Snow leopards mainly eat wild mountain goats and sheep. A review of 25 diet studies covering 1,696 scats from across the species' range found that their main prey are Siberian ibex, blue sheep (bharal), Himalayan tahr, argali and marmots, and that they significantly prefer Siberian ibex and blue sheep weighing about 55 kg, which is heavier than the cat itself. Domestic livestock is also eaten: in one DNA study in Mongolia it turned up in about one in five droppings.",
     body='''<section class="card"><h2>The short answer</h2>
<p>A snow leopard weighs roughly 30 to 50 kg, according to the IUCN SSC Cat Specialist Group, yet its preferred prey weighs more than that. It is a specialist hunter of the large hoofed animals that live on steep mountain slopes, and it tops up its diet with smaller animals and, where herders graze their animals, with livestock.</p>
<div class="tablewrap"><table><thead><tr><th>Prey</th><th>What it is</th><th>How important</th></tr></thead><tbody>
<tr><td>Siberian ibex</td><td>A wild mountain goat of Central Asia</td><td>Main prey and significantly preferred</td></tr>
<tr><td>Blue sheep (bharal)</td><td>A wild sheep of the Himalayas and Tibetan Plateau</td><td>Main prey and significantly preferred</td></tr>
<tr><td>Himalayan tahr</td><td>A wild goat of the southern Himalayas</td><td>Main prey where it occurs</td></tr>
<tr><td>Argali</td><td>The largest wild sheep</td><td>Main prey in parts of the range</td></tr>
<tr><td>Marmots</td><td>Large ground squirrels</td><td>Main small prey</td></tr>
<tr><td>Domestic goats, sheep and other livestock</td><td>Herders' animals grazing in snow leopard habitat</td><td>Regular, and a source of conflict</td></tr>
</tbody></table></div>
<p class="note">Main prey and preferences are from Lyngdoh et al. (2014). See the sources list below.</p></section>
<section class="card"><h2>The range wide review: 1,696 scats</h2>
<p>Salvador Lyngdoh and colleagues, including the prey preference specialist Matt Hayward, pulled together 14 published and 11 unpublished snow leopard diet studies and published the analysis in <i>PLoS ONE</i> in 2014. Between them the studies had analysed 1,696 snow leopard scats (droppings) from across the cat's range. For each prey species the team worked out both how often it appeared and how much meat it supplied, using a standard correction factor that converts the remains found in scats into the weight of prey actually eaten.</p>
<p>Three findings stand out. First, the snow leopard has a narrow, specialised diet: a measure of dietary breadth called Levin's index showed it relies on a small number of prey species. Second, the significantly preferred prey weighed 55 &plusmn; 5 kg, and the preferred weight range was 36 to 76 kg. Third, the diet differs from region to region. The team identified four distinct zones across the range, each with its own mix of mountain landscape and prey, which is why the authors stress that conservation plans need to protect the right prey in the right place.</p></section>
<section class="card"><h2>A DNA study in Mongolia</h2>
<p>Identifying prey from hair and bone in droppings is tricky, and so is being sure a dropping came from a snow leopard and not a fox or a wolf. To get around this, Wasim Shehzad and colleagues used DNA. Working in the Tost Mountains in the South Gobi of Mongolia, they extracted DNA from 81 snow leopard droppings, sequenced a short stretch of a mitochondrial gene, and matched it to prey species. Their results were published in <i>PLoS ONE</i> in 2012.</p>
<p>They found five different prey items in total:</p>
<ul>
<li>Siberian ibex in 70.4% of droppings</li>
<li>Domestic goat in 17.3%</li>
<li>Argali in 8.6%</li>
<li>Large hoofed animals in 98.8% of droppings overall: wild ones in 79% and domestic livestock in 19.7%</li>
</ul>
<p>These figures are frequency of occurrence, the share of droppings that contained each prey, not the share of meat eaten. Even so, they show how heavily this population depends on ibex, and that livestock is a real but smaller part of the diet.</p></section>
<section class="card"><h2>Why such big prey?</h2>
<p>Large wild goats and sheep are the most abundant big animals in the cold, rocky places where snow leopards live, so it makes sense for the cat to specialise on them. Snow leopards usually stalk from above and use the steep terrain to close the distance before a short charge, a style suited to animals that live on cliffs. You can read more about the cat's build in our <a href="../snow-leopard.html#adapt">snow leopard facts</a>.</p>
<p>It is interesting to compare this with the leopard, a different species despite the shared name. A separate review by Hayward and colleagues of 33 leopard diet studies found that leopards prefer prey of about 10 to 40 kg, with a most preferred mass of about 25 kg. The snow leopard, although it is often lighter than a big male leopard, targets prey roughly twice that size. We cover leopard feeding in <a href="why-do-leopards-drag-their-kills-into-trees.html">why do leopards drag their kills into trees?</a></p></section>
<section class="card"><h2>Do snow leopards eat livestock?</h2>
<p>Yes, and it matters for their survival. The IUCN SSC Cat Specialist Group notes that livestock commonly makes up about 15 to 30 percent of the snow leopard's diet, and sometimes far more where wild prey is scarce. The Mongolian DNA study fits that picture, with livestock in 19.7% of droppings. Losses to snow leopards can lead herders to kill the cats in retaliation, which is one of the main threats to the species. That is why many conservation projects focus on predator proof corrals and on keeping wild ibex and blue sheep populations healthy, so the cats have less reason to turn to goats and sheep. Our <a href="../conservation.html">big cat conservation</a> page explains the wider picture.</p></section>
<section class="card"><h2>Key takeaways</h2><ul>
<li>Snow leopards are diet specialists that mainly hunt wild mountain goats and sheep.</li>
<li>Their main prey are Siberian ibex, blue sheep, Himalayan tahr, argali and marmots.</li>
<li>Preferred prey weighs about 55 kg, within a preferred range of 36 to 76 kg, which is heavier than the cat.</li>
<li>In a DNA study in Mongolia, ibex appeared in 70.4% of droppings and livestock in 19.7%.</li>
<li>Protecting wild prey helps reduce livestock losses and retaliatory killing.</li></ul></section>''',
     faq=[("What do snow leopards eat?", "Mainly wild mountain goats and sheep. A review of 25 diet studies found their main prey are Siberian ibex, blue sheep, Himalayan tahr, argali and marmots, with a significant preference for Siberian ibex and blue sheep."),
          ("What is a snow leopard's favourite prey?", "Siberian ibex and blue sheep (bharal). The 2014 range wide review found snow leopards significantly prefer these two species, and prefer prey weighing about 55 kg."),
          ("Can a snow leopard kill prey bigger than itself?", "Yes. Snow leopards weigh roughly 30 to 50 kg, but their preferred prey weighs 36 to 76 kg, so they regularly take animals heavier than themselves."),
          ("Do snow leopards eat livestock?", "Yes. In a DNA study of 81 snow leopard droppings in Mongolia, domestic livestock appeared in 19.7% of them, and the IUCN Cat Specialist Group says livestock commonly makes up 15 to 30 percent of the diet.")],
     related=[("Snow leopard facts", "snow-leopard.html"), ("Big cat behavior", "behavior.html"), ("Why do leopards drag their kills into trees?", "blog/why-do-leopards-drag-their-kills-into-trees.html"), ("Which big cats can roar?", "blog/which-big-cats-can-roar.html"), ("Research papers", "research/index.html"), ("Blog home", "blog/index.html")],
     sources=[LYNGDOH2014, SHEHZAD2012, HAYWARD2006, CSG["snow"]])

# ---------------------------------------------------------------- 10 JAGUAR WATER HUNTING (14 Oct 2026)
post("do-jaguars-hunt-in-water", "Do Jaguars Hunt in Water? Aquatic Prey Research | BigCatWise",
     "Yes. Jaguars swim and hunt fish, caiman and other aquatic prey. A Pantanal study found fish in 46% of scats and aquatic reptiles in 55%, with mammals only 11%.",
     "Do jaguars hunt in water? Yes, and in some wetlands it reshapes their whole ecology", headline="Do jaguars hunt in water?",
     published="2026-10-14", modified="2026-10-14",
     lead="Yes. Jaguars are strong swimmers and regularly take prey in and beside water, including fish, caiman, turtles and capybaras. In one seasonally flooded reserve in Brazil's Pantanal, a 2022 study found fish in 46% of jaguar scats and aquatic reptiles in 55%, while mammals appeared in only 11%. That aquatic food supply supported the highest jaguar density yet estimated and unusual social behaviour such as cooperative fishing.",
     body='''<section class="card"><h2>The short answer</h2>
<p>Among the six big cats on this site, the jaguar is the one most at home in water. It swims well, crosses rivers and lakes, and often hunts along riverbanks and in flooded wetlands. That is not a side habit. In some places aquatic animals dominate its diet, and that changes how densely jaguars can live and even how social they are. For the species basics, see our <a href="../jaguar.html#water">jaguar facts</a>.</p>
<div class="tablewrap"><table><thead><tr><th>Finding</th><th>Detail</th></tr></thead><tbody>
<tr><td>Fish in jaguar scats (Pantanal study)</td><td>46% of 138 scats</td></tr>
<tr><td>Aquatic reptiles in those scats</td><td>55%</td></tr>
<tr><td>Mammals in those scats</td><td>11%</td></tr>
<tr><td>Jaguar density in that reserve</td><td>12.4 jaguars per 100 km&sup2;</td></tr>
<tr><td>Preferred prey across the jaguar's range</td><td>Capybara and giant anteater</td></tr>
</tbody></table></div>
<p class="note">Scat percentages are frequency of occurrence: the share of droppings that contained each prey type. One dropping can contain more than one type, so the figures can add up to more than 100%. Pantanal figures are from Eriksson et al. (2022); preferred prey from Hayward et al. (2016).</p></section>
<section class="card"><h2>A Pantanal population that lives on aquatic food</h2>
<p>Charlotte Eriksson and colleagues studied jaguars in a seasonally flooded protected area in the Brazilian Pantanal and published the results in <i>Ecology</i> in 2022. They analysed 138 jaguar scats, ran camera traps for 8,065 trap nights, and fitted GPS collars to 13 jaguars.</p>
<p>The diet was unlike the usual picture of a jaguar living mainly on peccaries, deer and other mammals. Fish turned up in 46% of scats and aquatic reptiles in 55%. Mammals appeared in only 11%. The authors describe this as the first jaguar population known to feed extensively on fish and to consume mammals so little. Those aquatic subsidies, energy moving from water into the jaguar's food web, supported an estimated density of 12.4 jaguars per 100 km&sup2;, which they report as the highest jaguar density estimate to date.</p>
<p>They also saw behaviour that is rare for this mostly solitary cat: cooperative fishing, adults of the same sex travelling together, and play between same sex adults. The paper's wider point is that aquatic subsidies, often discussed for omnivores, can reshape the ecology of an obligate carnivore too.</p></section>
<section class="card"><h2>What jaguars prefer across their whole range</h2>
<p>Not every jaguar lives in a flooded wetland. Matt Hayward and colleagues reviewed 25 studies covering 3,214 jaguar kills across the species' range and published the analysis in <i>Frontiers in Ecology and Evolution</i> in 2016.</p>
<p>They found that jaguars significantly preferred capybara and giant anteater, and avoided agoutis, carnivorans, primates, the black eared opossum and tapirs. Prey selection tracked abundance and herd size more than body size alone. Accessible prey weighed about 6 to 60 kg; preferred prey weighed about 45 to 85 kg; and the mean mass of significantly preferred prey was 32 &plusmn; 13 kg, giving a predator to prey body mass ratio of about 1 to 0.53, which is smaller than for many other solitary big cats.</p>
<p>Capybaras are semi aquatic rodents that live near rivers and lakes, so even this range wide preference list has a strong water link. The review also notes that jaguar diets are unusually diverse and include turtles, fish, crocodilians and other aquatic prey, which fits the jaguar's habit of using wet habitats.</p></section>
<section class="card"><h2>How a jaguar kills aquatic and armoured prey</h2>
<p>The IUCN SSC Cat Specialist Group describes the jaguar as the only big cat that regularly kills prey by piercing the skull with its canines. That skull bite, plus a powerful head and robust teeth, suits tough or dangerous prey such as turtles and caiman as well as mammals. Jaguars also break the necks of large prey and kill small prey with a blow to the head. You can read more under <a href="../jaguar.html#bite">jaguar bite and hunting</a>.</p>
<p>This is different from the leopard's tree caching strategy in Africa and Asia. Leopards often hoist kills into trees to stop hyenas stealing them; see <a href="why-do-leopards-drag-their-kills-into-trees.html">why do leopards drag their kills into trees?</a> Jaguars, living where the competitor mix and habitats differ, lean more on water edge ambush and a killing bite built for hard prey.</p></section>
<section class="card"><h2>Where this happens</h2>
<p>Jaguars range from Mexico to northern Argentina and are most often found in wet lowland habitats: rainforest, swamps and seasonally flooded wetlands such as the Pantanal, usually below 1,000 m. The Amazon holds most of the world's jaguars. Wetlands with abundant fish, caiman and capybaras are exactly the places where aquatic hunting pays off. Our <a href="../habitats.html">habitats guide</a> puts the jaguar's wetlands in context with the other big cats.</p></section>
<section class="card"><h2>Key takeaways</h2><ul>
<li>Jaguars swim well and regularly hunt fish, caiman, turtles, capybaras and other water linked prey.</li>
<li>In one Pantanal study, fish appeared in 46% of scats and aquatic reptiles in 55%, with mammals in only 11%.</li>
<li>That aquatic food supply supported 12.4 jaguars per 100 km&sup2; and unusual social behaviour including cooperative fishing.</li>
<li>Across the range, preferred prey include capybara and giant anteater; preferred prey mass is about 45 to 85 kg.</li>
<li>The jaguar's skull piercing bite suits tough aquatic and armoured prey.</li></ul></section>''',
     faq=[("Do jaguars hunt in water?", "Yes. Jaguars are strong swimmers and regularly take fish, caiman, turtles and other aquatic or semi aquatic prey. In a Pantanal study, fish appeared in 46% of jaguar scats and aquatic reptiles in 55%."),
          ("Do jaguars eat fish?", "Yes. In a seasonally flooded Pantanal reserve, fish turned up in 46% of 138 jaguar scats, the first population described as feeding extensively on fish."),
          ("What is a jaguar's favourite prey?", "Across the range, a review of 3,214 kills found jaguars significantly prefer capybara and giant anteater. Preferred prey weigh about 45 to 85 kg."),
          ("Are jaguars social when they fish?", "Usually jaguars are solitary, but the Pantanal study documented cooperative fishing and other same sex adult interactions where aquatic food was abundant.")],
     related=[("Jaguar facts", "jaguar.html"), ("Big cat behavior", "behavior.html"), ("Leopard vs jaguar vs cheetah", "blog/leopard-vs-jaguar-vs-cheetah.html"), ("Why do leopards drag their kills into trees?", "blog/why-do-leopards-drag-their-kills-into-trees.html"), ("Research papers", "research/index.html"), ("Blog home", "blog/index.html")],
     sources=[ERIKSSON2022, HAYWARD2016JAG, CSG["jaguar"], SDZ["jaguar"]])


# ---------------------------------------------------------------- 12 LION MANE (15 Oct 2026)
post("why-do-male-lions-have-manes", "Why Do Male Lions Have Manes? What the Research Shows | BigCatWise",
     "A lion's mane is a signal: darker manes mark healthier, higher testosterone males that females prefer. Research on mane colour, heat costs and maneless lions.",
     "Why do male lions have manes? The mane is a signal, and it has a cost", headline="Why do male lions have manes?",
     published="2026-10-15", modified="2026-10-15",
     lead="Male lions have manes mainly as a signal. Long term research in Tanzania's Serengeti found that a darker mane reflects better nutrition and higher testosterone, that lionesses prefer darker maned males, and that rival males pay attention to mane length, which tracks fighting success. The signal is honest because it is costly: big dark manes make males hotter, and in hot places manes are lighter, shorter or almost absent.",
     body='''<section class="card"><h2>The short answer</h2>
<ul><li><b>Attracting females:</b> lionesses preferred males with darker manes in Serengeti research.</li>
<li><b>Warning rivals:</b> mane length signals fighting success, and other males take notice.</li>
<li><b>Advertising condition:</b> mane darkness reflects nutrition and testosterone, so it is hard to fake.</li>
<li><b>Paying a price:</b> dark, heavy manes raise body surface temperature, which is why manes shrink in hot habitats.</li></ul>
<p>The lion is the only big cat in which adult males and females look so different, and the mane is the reason. For the basics, see our <a href="../lion.html#appearance">lion appearance guide</a>.</p></section>
<section class="card"><h2>What the Serengeti study found</h2>
<p>Peyton West and Craig Packer used data from the long running Serengeti Lion Project in Tanzania and published their results in <i>Science</i> in 2002. They looked at what mane length and mane colour tell other lions, and what a mane costs its owner.</p>
<p>The two features turned out to carry different messages. Mane darkness reflected a male's nutrition and testosterone, and it influenced both female choice and competition between males. Mane length signalled fighting success, but it appeared to matter mainly to other males sizing up a rival, not to females.</p>
<p>Darker maned males did better over a lifetime. The study reported that they had longer reproductive lifespans and higher survival of their offspring. That is a strong reason for a female to choose one, and a strong reason for a rival to think twice before picking a fight.</p></section>
<section class="card"><h2>The cost: a mane is a hot coat</h2>
<p>A thick, dark mane around the head and neck traps heat. West and Packer found that maned males were hotter than females, and that dark maned males had higher surface temperatures, more abnormal sperm and lower food intake during the hottest months of the year.</p>
<p>That cost is what keeps the signal honest. Only a male in good condition can carry a big dark mane without suffering too much from it, so the mane works as a reliable advertisement. The study also found that males had lighter or shorter manes in hotter seasons, hotter years and hotter habitats. Because manes respond to temperature in this way, the authors suggested manes may change as the climate warms.</p></section>
<section class="card"><h2>Maneless lions: the Tsavo puzzle</h2>
<p>Not every adult male lion has a big mane. Roland Kays and Bruce Patterson described a population in Tsavo National Park, Kenya, that is largely maneless, in the <i>Canadian Journal of Zoology</i> in 2002. Adult males there typically had only sparse blond hair forming a crest along the back, a beard, chest tufts or sideburns. The researchers saw no fully maned lions.</p>
<p>These males were normal members of pride life: they were seen mating, hunting, playing with cubs, scent marking and roaring to advertise territory. The researchers had expected Tsavo's dry, prey poor landscape to produce small groups and weaker sexual selection for manes. Female groups were in fact large, averaging 7.4, so that "small groups, small manes" idea did not hold. One difference stood out: each of the five prides they studied had only one adult male, rather than the coalitions of two to four seen elsewhere. Tsavo is also hot and arid, which fits the Serengeti finding that heat pushes manes to be smaller.</p></section>
<section class="card"><h2>When did lions get manes?</h2>
<p>Manes are not as old as lions themselves. In a 2004 review in the <i>Journal of Zoology</i>, Nobuyuki Yamaguchi, Alan Cooper, Lars Werdelin and David Macdonald traced the lion's history from Pliocene east Africa to its spread across Eurasia and the Americas. The first lions were presumed to have been maneless, and maneless forms seem to have persisted in Europe until around 10,000 years ago.</p>
<p>The review suggests the maned form may have appeared about 320,000 to 190,000 years ago and then spread, replacing earlier maneless forms across Africa and western Eurasia. The authors also argue that lions probably became group living before they spread out of Africa. That fits the idea that the mane is tied to social life, where males compete for prides and females choose among them. Read more in <a href="why-do-lions-live-in-prides.html">why do lions live in prides?</a></p></section>
<section class="card"><h2>Do female lions ever have manes?</h2>
<p>Normally no. A mane develops in males as they mature, and the Serengeti work links mane darkness to testosterone. In the wild, adult lionesses have the plain tawny coat without a mane, and young males start with little or none. Manes are one of several visual signals big cats use; see <a href="../behavior.html#communication">how big cats communicate</a> for roars, scent marks and other signals.</p></section>
<section class="card"><h2>Key takeaways</h2><ul>
<li>The mane is a signal: darker manes reflect nutrition and testosterone; longer manes reflect fighting success.</li>
<li>Lionesses preferred darker maned males, which had longer breeding lives and better cub survival.</li>
<li>Manes are costly: they make males hotter, and manes are lighter or shorter in hot seasons and habitats.</li>
<li>Some lions, such as many males in Tsavo, Kenya, are almost maneless but still hold prides.</li>
<li>The maned form probably appeared only a few hundred thousand years ago.</li></ul></section>''',
     faq=[("Why do male lions have manes?", "Mainly as a signal. Serengeti research found that mane darkness reflects a male's nutrition and testosterone and attracts females, while mane length signals fighting success to rival males."),
          ("Does a darker mane mean a stronger lion?", "In the Serengeti, darker maned males had longer reproductive lifespans and higher offspring survival, and lionesses preferred them. Darker manes also carried a heat cost."),
          ("Why do some male lions have no mane?", "Many males in Tsavo National Park, Kenya, are largely maneless, with only sparse hair on the back, chin or chest. Hot conditions are linked to smaller manes, and these males still mate, hunt and hold territory."),
          ("Do manes keep lions hot?", "Yes. Maned males were hotter than females, and dark maned males had higher surface temperatures and lower food intake in the hottest months.")],
     related=[("Lion facts", "lion.html"), ("Why do lions live in prides?", "blog/why-do-lions-live-in-prides.html"), ("Big cat behavior", "behavior.html"), ("Which big cats can roar?", "blog/which-big-cats-can-roar.html"), ("Research papers", "research/index.html"), ("Blog home", "blog/index.html")],
     sources=[WEST2002, KAYS2002, YAMAGUCHI2004, CSG["lion"]])


# ---------------------------------------------------------------- 11 TIGER ENCLOSURE WARNING (13 Oct 2026)
BBC1 = ("BBC News (10 October 2026) Man dies after tiger attack at Yorkshire Wildlife Park", "https://www.bbc.co.uk/news/articles/c6n9r3n7858zo")
BBC2 = ("BBC News (October 2026) Yorkshire Wildlife Park remains closed after fatal tiger attack", "https://www.bbc.co.uk/news/articles/cmgr8221v4x1o")
BBC3 = ("BBC News (October 2026) Yorkshire Wildlife Park fatal tiger attack: what we know so far", "https://www.bbc.com/news/articles/c9146j15gnggo")
IND1 = ("The Independent (October 2026) Man killed was visiting park alone, say police, as investigation launched", "https://www.independent.co.uk/news/uk/home-news/tiger-attack-yorkshire-wildfire-park-zoo-latest-updates-b3065608.html")
CNN1 = ("CNN, Sophie Tanno (10 October 2026) 'Serious incident' at tiger enclosure forces closure of UK wildlife park", "https://www.cnn.com/2026/10/10/uk/serious-incident-tiger-enclosure-uk-park")
NZPT = ("Smithsonian's National Zoo and Conservation Biology Institute: Tiger", "https://www.nationalzoo.si.edu/animals/tiger")
SDZDIET = ("San Diego Zoo Wildlife Alliance Library: Tiger fact sheet, diet and feeding", "https://ielc.libguides.com/sdzg/factsheets/tiger/diet")
WTHP = ("Wild Tiger Health Project: Prey of tigers", "https://wildtigerhealthproject.org/resources-category/prey-of-tigers/")
WWFUK = ("WWF UK: Top 10 facts about tigers", "https://www.wwf.org.uk/learn/fascinating-facts/tigers")
post("never-enter-a-tiger-enclosure", "Never Enter a Tiger Enclosure: Lessons From Yorkshire Wildlife Park | BigCatWise",
     "On 10 October 2026 a man died after entering the tiger enclosure at Yorkshire Wildlife Park. What is known, why zoo barriers matter, and how tigers hunt.",
     "Never cross a zoo barrier: the Yorkshire Wildlife Park tiger death and tiger safety", headline="Never enter a tiger enclosure: lessons from Yorkshire Wildlife Park",
     published="2026-10-13", modified="2026-10-13",
     lead="On Saturday 10 October 2026, a man died after entering the Amur tiger enclosure at Yorkshire Wildlife Park near Doncaster, England, according to South Yorkshire Police as reported by the BBC. Our thoughts are with his family and friends, and with the visitors and staff who saw what happened. This post sets out only what reputable news outlets have reported, and explains, with sources, why the barriers at a tiger enclosure exist and why nobody should ever cross one.",
     body='''<section class="card"><h2>What happened</h2>
<p>South Yorkshire Police said it was called at 13:35 BST to reports of a man entering the tiger enclosure at the park. The tiger attacked him and he died at the scene. Police said the tiger was uninjured, stayed in the enclosure, and there was no wider risk to the public (BBC News, 10 October 2026).</p>
<p>The BBC reported that the man climbed down into the enclosure from the raised visitor walkway. An eyewitness told the BBC she saw him climb onto the barriers and that a woman nearby spoke to him before he went in. The Independent reported witnesses saying he overpowered a woman who tried to stop him, and police said they did not believe he was accompanied by anyone. The man has not been named.</p>
<p>The park said its emergency response procedures were "immediately activated", and the park was evacuated and closed (CNN; BBC News). The park confirmed that the tiger, a five year old Amur tiger called Altai, is safe and will not be euthanised. City of Doncaster Council, the park's licensing authority, has launched a health and safety investigation (BBC News; The Independent). We will not speculate about why the man entered the enclosure; that is for the investigation.</p></section>
<section class="card"><h2>The warning: barriers are there for a reason</h2>
<p>According to the BBC, the park's Land of the Tigers area is a purpose built two acre reserve with a raised walkway and fencing above the section where the tigers roam. That design lets people watch tigers closely while keeping a full physical separation between people and animals. Climbing a barrier, leaning over one, or dropping anything into an enclosure removes that separation. Please:</p>
<ul>
<li>Never climb, sit on or lean over a barrier, fence or railing at an animal enclosure.</li>
<li>Never let children sit on railings or be held over them.</li>
<li>Never enter an enclosure for any reason, including to retrieve a dropped phone, hat or toy. Tell a member of staff instead.</li>
<li>If you see someone trying to get past a barrier, do not follow them. Alert staff or call emergency services straight away.</li>
<li>Follow staff instructions during any evacuation.</li></ul>
<p>If you are struggling and have thoughts of harming yourself, please talk to someone now. In the UK you can call Samaritans free on 116 123; in the US you can call or text 988.</p></section>
<section class="card"><h2>Why tigers are so dangerous at close range</h2>
<p>A tiger in a zoo is still a tiger. It keeps the instincts and body of a wild apex predator.</p>
<p><b>Tigers are ambush hunters.</b> The Smithsonian's National Zoo describes tigers as ambush predators that rely on stealth and strength: they lie in wait, pounce, bring prey to the ground and finish the kill by breaking or biting the neck. The San Diego Zoo Wildlife Alliance's tiger fact sheet lists the three typical elements of a tiger's hunt as concealment, a stalk and a sudden rush.</p>
<p><b>The rush is short and fast.</b> The Wild Tiger Health Project notes that tigers usually stalk to within less than 25 metres of prey before the final rush, relying on overtaking it quickly rather than a long chase. A person inside an enclosure is almost always much closer than that.</p>
<p><b>The bite is built to kill large animals.</b> According to the San Diego fact sheet, tigers kill smaller prey with a bite to the back of the neck and larger prey with a throat bite that cuts off the air supply. The Smithsonian notes that tigers mainly hunt large hoofed animals such as wild boar and deer, and also take buffalo, sloth bears, leopards and even crocodiles.</p>
<p><b>Lying still or crawling does not make you safe.</b> Low, slow or unusual movement in front of a predator is not a reliable signal of "no threat", and once a person is inside the enclosure, nobody outside can safely reach them quickly. Keepers rely on trained procedures, locked doors and separation, never on going in with the animal. You can read more about tiger behaviour on our <a href="../tiger.html">tiger facts</a> page and our <a href="../behavior.html">big cat behaviour</a> guide.</p></section>
<section class="card"><h2>What about wild tigers?</h2>
<p>Wild tigers usually avoid people, and most visitors to tiger reserves will be on guided tours with rules set by the park authority. Follow those rules exactly, stay in vehicles or on marked routes, and never approach, feed or follow a tiger. WWF notes that tigers walk silently on soft toe pads and that their stripes act as camouflage, so a tiger can be close without being seen. Our <a href="how-big-is-a-tigers-territory.html">how big is a tiger's territory?</a> post explains how widely tigers range, and our <a href="../disclaimer.html">disclaimer</a> applies: this is general education, not professional safety advice.</p></section>
<section class="card"><h2>Key takeaways</h2><ul>
<li>On 10 October 2026, a man died after entering the tiger enclosure at Yorkshire Wildlife Park; a council health and safety investigation is under way.</li>
<li>The tiger, Altai, was unhurt and will not be euthanised, the park said.</li>
<li>Tigers are stalk and ambush predators that kill large prey with a neck or throat bite.</li>
<li>Never climb, lean over or cross a zoo barrier, for any reason. Call staff instead.</li></ul></section>''',
     faq=[("What happened at Yorkshire Wildlife Park on 10 October 2026?", "A man entered the Amur tiger enclosure from the visitor walkway at about 13:30 BST, was attacked by the tiger and died at the scene, according to South Yorkshire Police as reported by the BBC."),
          ("Will the tiger be put down?", "No. The park said the tiger, Altai, is safe and well and will not be euthanised as a result of the incident (BBC News)."),
          ("What should I do if I drop something into an animal enclosure?", "Leave it and tell a member of staff. Never climb a barrier or enter an enclosure to retrieve anything."),
          ("How do tigers kill their prey?", "Tigers stalk and ambush prey, then kill with a bite to the back of the neck for smaller prey or a suffocating throat bite for larger prey (San Diego Zoo Wildlife Alliance tiger fact sheet).")],
     related=[("Tiger facts", "tiger.html"), ("Big cat behavior", "behavior.html"), ("How big is a tiger's territory?", "blog/how-big-is-a-tigers-territory.html"), ("Why do tigers have stripes?", "blog/why-do-tigers-have-stripes.html"), ("Disclaimer", "disclaimer.html"), ("Blog home", "blog/index.html")],
     sources=[BBC1, BBC2, BBC3, IND1, CNN1, NZPT, SDZDIET, WTHP, WWFUK])


# ---------------------------------------------------------------- 13 CHEETAH OVERHEAT MYTH (16 Oct 2026)
post("do-cheetahs-abandon-hunts-because-they-overheat", "Do Cheetahs Abandon Hunts Because They Overheat? | BigCatWise",
     "No: free-living cheetahs stop chases without overheating. Body temperature averaged 38.4 C at chase end; heat rises more after a kill than during the sprint.",
     "Do cheetahs abandon hunts because they overheat? Direct measurements say no", headline="Do cheetahs abandon hunts because they overheat?",
     published="2026-10-16", modified="2026-10-16",
     lead="No. When researchers measured body temperature in free living cheetahs hunting spontaneously in Namibia, body temperature averaged about 38.4&deg;C at the moment a chase ended, typical of the cats' daily rhythm, and did not reach the 40.5&deg;C ceiling from an old treadmill study. Cheetahs do abandon most hunts, but overheating is not the reason. After a successful kill, temperature rose about twice as much as after a failed chase, which the authors interpret as stress hyperthermia, not exercise heat.",
     body='''<section class="card"><h2>The short answer</h2>
<ul>
<li><b>The myth:</b> cheetahs store so much heat when they sprint that they must quit or risk overheating.</li>
<li><b>Where it came from:</b> a 1973 treadmill study on two hand reared cheetahs that stopped at about 40.5&deg;C rectal temperature.</li>
<li><b>What free living cheetahs showed:</b> body temperature did not rise enough during real hunts to explain quitting; it averaged about 38.4&deg;C when chases ended.</li>
<li><b>After a kill:</b> temperature rose about 1.3&deg;C, roughly twice the rise after an unsuccessful hunt, even when activity was similar.</li>
</ul>
<p>For measured top speeds and how short most sprints are, see <a href="how-fast-is-a-cheetah.html">how fast is a cheetah?</a> and our <a href="../cheetah.html">cheetah facts</a> page.</p></section>
<section class="card"><h2>Where the overheating story started</h2>
<p>In 1973, C. Richard Taylor and V. J. Rowntree published a study in the <i>American Journal of Physiology</i> on heat balance in running cheetahs. They exercised two hand reared cheetahs on a treadmill, measured how heat was produced and lost, and concluded that running cheetahs store metabolic heat. Further exercise soon became thermally impossible, they argued, at a ceiling rectal temperature of about 40.5&deg;C.</p>
<p>That paper was groundbreaking for its time, and textbooks and popular accounts often used it to explain why cheetahs abandon chases and rest so long after a sprint. The problem is that a treadmill does not look like a real hunt. In that study the cats ran at up to about 30 km/h and stopped within about 2 km. Wild cheetahs can sprint much faster over much shorter distances: typically under about 300 m, and rarely more than about 500 m.</p></section>
<section class="card"><h2>What free living cheetahs actually do</h2>
<p>In 2013, Robyn Hetem and colleagues at the University of the Witwatersrand tested the idea directly. They implanted temperature loggers (recording every minute) and activity loggers in free living cheetahs at the AfriCat Foundation rehabilitation camp in central Namibia, then let the cats hunt naturally for months. Four cheetahs yielded usable hunt data (two of six study animals were later killed by a resident leopard).</p>
<p>Key results from Biology Letters:</p>
<ul>
<li>Mean body temperature across the day was about 38.3&deg;C, with a daily range of about 2.3&deg;C.</li>
<li>At the moment intense chase activity ended, body temperature averaged about 38.4&deg;C for successful hunts and about 38.3&deg;C for unsuccessful ones, no different from the cats usual 24 hour mean.</li>
<li>Body temperature seldom reached the 40.5&deg;C treadmill ceiling, and far less often than the cheetahs abandoned hunts.</li>
<li>Even on a chase that came close to the commonly reported maximum distance of about 300 m, temperature did not rise measurably during the sprint itself.</li>
</ul>
<p>After unsuccessful hunts, body temperature rose only about 0.5&deg;C. That is a small fraction of the heat rise you would expect if cheetahs stored most of the metabolic heat from a full speed sprint the way the treadmill model assumed.</p></section>
<section class="card"><h2>Why temperature rises more after a kill</h2>
<p>Hunting still had thermal consequences, but not during the chase. After successful hunts, body temperature rose for about 40 minutes on average and by about 1.3&deg;C, to a peak near 39.2&deg;C. After unsuccessful hunts the rise was only about 0.5&deg;C, to about 38.7&deg;C. Activity during the hunts was similar, so the extra heat was not simply harder running.</p>
<p>The authors ruled out several simple explanations. The rise was not from eating (cheetahs often rest before they start to feed). It was not explained by air temperature or prey mass. And if the 1.3&deg;C rise came only from chase metabolism, the implied oxygen use would be unrealistically high. Their proposal: the post kill rise is <b>stress hyperthermia</b>, linked to high sympathetic nervous system activity. Cheetahs are often described as nervous or highly alert at kills, watching for lions, leopards and hyenas that steal food and kill cubs. Supporting that idea, a lame cheetah that could not run still showed a similar temperature rise after joining a sibling at a kill it had not chased.</p></section>
<section class="card"><h2>So why do cheetahs stop?</h2>
<p>They still abandon most hunts. Reviews and field studies often put overall hunting success under about 40%. Hetem and colleagues conclude the reason is not overheating; the true limits are still being pinned down. A separate 2013 study by Alan Wilson and colleagues, using GPS and motion sensor collars on wild cheetahs in Botswana, showed that hunts demand extreme acceleration, braking and turning, not only top speed, and that most runs never reach flat out speed. The extreme muscle power of a short sprint is a more plausible limit than a thermal ceiling that free living cats rarely approach.</p>
<p>After a chase, cheetahs often pant hard and rest. That recovery window is when lions and spotted hyenas are most dangerous to them. Daytime hunting and short recovery at the carcass are part of how cheetahs try to stay clear of those competitors; see <a href="../behavior.html">big cat behavior</a> and <a href="../cheetah.html#hunting">how cheetahs hunt</a>.</p></section>
<section class="card"><h2>What this does not prove</h2>
<p>The Namibia study measured cheetahs hunting by ambush in fairly dense vegetation. The authors note that open pursuit on hot grassland, or hotter climates, might still produce higher chase temperatures. The result overturns the simple textbook claim that overheating explains abandoned hunts; it does not say cheetahs never get hot.</p></section>
<section class="card"><h2>Key takeaways</h2><ul>
<li>The overheating explanation traces mainly to a 1973 treadmill study with a 40.5&deg;C ceiling.</li>
<li>Free living cheetahs ended chases at about 38.4&deg;C, within their normal daily range.</li>
<li>Temperature rose more after a successful kill than after a failed chase, consistent with stress hyperthermia at the carcass.</li>
<li>Cheetahs still fail most hunts; the limit is more likely sprint effort and hunt dynamics than stored heat.</li></ul></section>''',
     faq=[("Do cheetahs abandon hunts because they overheat?", "No. In free living cheetahs in Namibia, body temperature averaged about 38.4&deg;C when chases ended and did not reach the 40.5&deg;C ceiling from a 1973 treadmill study. They abandon hunts for other reasons."),
          ("Where did the cheetah overheating idea come from?", "Mainly from Taylor and Rowntree (1973), who ran two hand reared cheetahs on a treadmill and concluded they stored metabolic heat and hit a thermal limit near 40.5&deg;C."),
          ("Why does cheetah body temperature rise after a kill?", "Hetem et al. (2013) found a rise of about 1.3&deg;C after successful hunts versus about 0.5&deg;C after unsuccessful ones. They propose stress hyperthermia linked to alertness at the kill, not leftover sprint heat."),
          ("How successful are cheetah hunts?", "Field studies cited by Hetem and colleagues put overall success under about 40%. Most chases are abandoned even when prey seems within reach.")],
     related=[("How fast is a cheetah?", "blog/how-fast-is-a-cheetah.html"), ("Cheetah facts", "cheetah.html"), ("Big cat behavior", "behavior.html"), ("Leopard vs jaguar vs cheetah", "blog/leopard-vs-jaguar-vs-cheetah.html"), ("Research papers", "research/index.html"), ("Blog home", "blog/index.html")],
     sources=[HETEM2013, TAYLOR1973, WILSON, CSG["cheetah"], NZP["cheetah"]])

# ---------------------------------------------------------------- 14 ARE TIGERS NOCTURNAL (18 Oct 2026)
post("are-tigers-nocturnal", "Are Tigers Nocturnal? When Tigers Are Most Active | BigCatWise",
     "Mostly, but not strictly. Wild tigers are most active at night, dawn and dusk, track their prey's schedule, and turn more nocturnal where people are busy by day.",
     "Are tigers nocturnal? When tigers are most active, according to camera trap studies", headline="Are tigers nocturnal?",
     published="2026-10-18", modified="2026-10-18",
     lead="Mostly, but not strictly. Wild tigers do most of their moving and hunting at night and around dawn and dusk, and they are best described as nocturnal to crepuscular rather than strictly nocturnal. Camera trap and radio tracking studies show that a tiger's schedule bends to two things: when its prey is active, and when people are around. In Nepal, tigers shared the very same trails as people and vehicles but became much less active during the day, when human traffic peaked.",
     body='''<section class="card"><h2>The short answer</h2>
<ul>
<li><b>Usual pattern:</b> most activity at night and in the twilight hours of dawn and dusk; much of the hot daytime is spent resting in cover.</li>
<li><b>Not a fixed rule:</b> tigers can and do move and hunt by day, especially where they are undisturbed.</li>
<li><b>Prey sets the clock:</b> in Sumatra, tiger activity overlapped strongly with muntjac and sambar deer, two of its prey species.</li>
<li><b>People push tigers into the night:</b> around Chitwan National Park, Nepal, tigers cut back daytime activity where human activity peaked by day.</li>
</ul>
<p>For the basics on size, range and diet, see our <a href="../tiger.html">tiger facts</a> page and <a href="../tiger.html#hunting">what tigers eat</a>.</p></section>
<section class="card"><h2>How scientists know when tigers are active</h2>
<p>Tigers are rare, wary and live in dense forest, so researchers rarely watch them directly. Two tools do most of the work. <b>Camera traps</b>, automatic cameras triggered by movement, stamp every photo with a time, so thousands of photos add up to a 24 hour activity profile. <b>Radio collars</b> let researchers track how far and when an individual moves. Comparing the activity curves of tigers, their prey and people shows who is active at the same time, a measure called <b>temporal overlap</b>.</p>
<p>The Smithsonian's National Zoo describes Sumatran tigers as hunting primarily at night, using sight and sound to find prey. The field studies below show why that is a tendency rather than a law.</p></section>
<section class="card"><h2>Tigers follow their prey's schedule</h2>
<p>In 2011, Matthew Linkie and Martin Ridout published a study in the <i>Journal of Zoology</i> on the critically endangered Sumatran tiger. They used 126 camera traps, running for a combined 8,984 camera days across four study areas from disturbed lowland forest to primary submontane forest, to compare the daily activity of tigers with five presumed prey species.</p>
<ul>
<li>They described the tiger as <b>crepuscular</b>, most active around dawn and dusk.</li>
<li>Tiger activity overlapped strongly with red muntjac (overlap coefficient about 0.80 on a scale from 0, no overlap, to 1, complete overlap) and with sambar deer (about 0.81).</li>
<li>Overlap with the largest prey available, the mostly nocturnal Malayan tapir, was much lower (about 0.52). The authors suggest tapir is not a principal prey species there, even though foraging theory might predict a big cat would favour the biggest prey.</li>
</ul>
<p>An earlier radio tracking and scat study in Nagarahole, southern India, by K. Ullas Karanth and Melvin Sunquist (2000) reached a similar conclusion from a different angle. Tracking tigers, leopards and dholes between 1986 and 1992, they found that the activity patterns of the predators appeared to be related mainly to the activity of their principal prey, rather than to avoiding one another. They found no temporal separation of predatory activity between tigers and leopards in that forest. For how tigers space themselves across the land, see <a href="how-big-is-a-tigers-territory.html">how big is a tiger's territory?</a></p></section>
<section class="card"><h2>Tigers shift to the night around people</h2>
<p>The clearest evidence of flexibility comes from Nepal. In a 2012 study in the <i>Proceedings of the National Academy of Sciences</i>, Neil Carter and colleagues ran field cameras inside and outside Chitwan National Park in 2010 and 2011. People on foot and vehicles were everywhere in the study area, yet tiger density was also high.</p>
<ul>
<li>Even at the level of individual camera locations, tigers used the same places as people on foot and vehicles in both years.</li>
<li>Tigers offset their activity, becoming much less active during the day, when human activity peaked.</li>
<li>The authors suggest that abundant prey and low levels of poaching also helped tigers and people coexist.</li>
</ul>
<p>This matters for conservation. A common belief is that large carnivores cannot share space with people at fine scales. The Chitwan results suggest tigers can share space if they can share it in time, using the night for the trails people use by day. That flexibility has limits: it depends on enough prey and little poaching.</p></section>
<section class="card"><h2>What this means for tiger watching and safety</h2>
<p>Because activity peaks around dawn and dusk, wildlife safaris in tiger reserves often schedule drives for early morning and late afternoon. The same pattern is a reason people living near tiger forests are advised to be most careful at those hours. Tigers in zoos keep a different routine shaped by feeding times and keepers, so a sleepy zoo tiger at midday says little about wild behaviour. Our <a href="never-enter-a-tiger-enclosure.html">tiger enclosure safety guide</a> covers zoo safety.</p></section>
<section class="card"><h2>What these studies do not prove</h2>
<p>Each study covered particular places and years. Activity can differ with season, habitat, prey community and human pressure, so no single curve describes every tiger. Camera traps also record when tigers pass cameras on trails, which is a good but imperfect stand in for overall activity. For how tigers compare with other big cats in behaviour, see <a href="../behavior.html">big cat behavior</a>.</p></section>
<section class="card"><h2>Key takeaways</h2><ul>
<li>Wild tigers are mainly nocturnal and crepuscular, not strictly nocturnal.</li>
<li>In Sumatra, tiger activity closely matched muntjac and sambar deer.</li>
<li>In southern India, predator activity tracked principal prey more than avoidance of other predators.</li>
<li>Near Chitwan, Nepal, tigers used the same trails as people but avoided the daytime human peak.</li></ul></section>''',
     faq=[("Are tigers nocturnal?", "Mostly. Wild tigers are most active at night and around dawn and dusk, but they are not strictly nocturnal and can be active by day, especially where people are scarce."),
          ("What time of day are tigers most active?", "Usually around dawn, dusk and at night. A camera trap study of Sumatran tigers described them as crepuscular, with activity closely matching muntjac and sambar deer."),
          ("Do tigers hunt during the day?", "Sometimes. Activity tends to follow the prey's schedule, so tigers may hunt in daylight where prey is active and disturbance is low."),
          ("Why are tigers more nocturnal near people?", "In Nepal's Chitwan region, tigers used the same trails as people and vehicles but were much less active during the day, when human activity peaked (Carter et al. 2012).")],
     related=[("Tiger facts", "tiger.html"), ("How big is a tiger's territory?", "blog/how-big-is-a-tigers-territory.html"), ("Why do tigers have stripes?", "blog/why-do-tigers-have-stripes.html"), ("Big cat behavior", "behavior.html"), ("Research papers", "research/index.html"), ("Blog home", "blog/index.html")],
     sources=[LINKIE2011, CARTER2012, KARANTH2000, NZP["tiger"], CSG["tiger"]])

# ---------------------------------------------------------------- 15 CAN LEOPARDS LIVE NEAR PEOPLE (19 Oct 2026)
post("can-leopards-live-near-people", "Can Leopards Live Near People? What Studies in India Show | BigCatWise",
     "Yes, to a striking degree. In India leopards live in dense farmland with no wild prey, eat mostly domestic animals, visit homes at night and rarely attack people.",
     "Can leopards live near people? What field studies of leopards in India's farmland and cities show", headline="Can leopards live near people?",
     published="2026-10-19", modified="2026-10-19",
     lead="Yes. In western India, leopards live at high density in farmland with more than 300 people per km&sup2; and almost no wild hoofed prey. They feed mostly on domestic animals, especially dogs, pass within a few metres of houses at night and stay out of sight by day. In that study area, attacks on people were rare. Coexistence is fragile, though: when leopards were trapped and moved away to reduce conflict, attacks on people went up, not down.",
     body='''<section class="card"><h2>The short answer</h2>
<ul>
<li><b>Leopards persist in farmland:</b> a camera trap study in western Maharashtra found about 4.8 adult leopards per 100 km&sup2; in cropland with no wilderness.</li>
<li><b>They live off domestic animals:</b> 87% of prey biomass in leopard scats from the same region came from domestic animals, and 39% from dogs alone.</li>
<li><b>They move by night:</b> GPS collared leopards in villages came close to houses at night but almost never by day.</li>
<li><b>Moving them made things worse:</b> a large translocation programme in Junnar was followed by a rise in attacks on people from about 4 to about 17 a year.</li>
</ul>
<p>For the basics on size, range and status, see our <a href="../leopard.html">leopard facts</a> page.</p></section>
<section class="card"><h2>Leopards in a landscape with no wilderness</h2>
<p>Protected areas cover only about 5% of India's land, so wide ranging carnivores must also use farmland. In a 2013 study in <i>PLoS ONE</i>, Vidya Athreya and colleagues used camera traps and capture recapture analysis to estimate carnivore density in an agricultural landscape of western Maharashtra with more than 300 people per km&sup2;. The area was cropland, devoid of wilderness and of wild herbivore prey.</p>
<p>Leopards occurred at about 4.8 adults per 100 km&sup2; and striped hyaenas at about 5.0 per 100 km&sup2;. The authors write that roughly 10 large carnivores per 100 km&sup2; sharing space with dense human populations in a completely modified landscape had never been reported before. Human attacks by leopards were rare in the study area, even though leopards had been involved in serious conflict, including human deaths, in adjoining areas.</p></section>
<section class="card"><h2>What leopards eat in farmland</h2>
<p>Without deer or antelope, what keeps these leopards alive? A follow up study in <i>Oryx</i> (Athreya et al. 2016) analysed 85 confirmed leopard scats from the croplands of Ahmednagar district. Domestic animals made up 87% of the prey biomass, and domestic dogs alone made up 39%. The only wild prey found were rodents, small Indian civet, bonnet macaque and other primates, mongooses and birds.</p>
<p>Interviews in 77 randomly chosen households showed how much domestic prey was available: about 169 adult cattle, 54 calves, 174 goats, 24 dogs and 61 cats per km&sup2;. Relative to those numbers, dogs and cats were over represented in the diet compared with the more numerous goats and cattle. The researchers calculated that the standing biomass of dogs and cats alone was enough to sustain the high density of carnivores in the area. For leopard diet in wilder places, see <a href="why-do-leopards-drag-their-kills-into-trees.html">why leopards drag kills into trees</a>.</p></section>
<section class="card"><h2>How leopards move among villages</h2>
<p>In 2014, Morten Odden and colleagues fitted GPS collars to five leopards in Maharashtra (four) and Himachal Pradesh (one). Three were released close to where they were caught. These used small home ranges of about 8 km&sup2; (a young male), 11 km&sup2; and 15 km&sup2; (two females). The authors suggest such small ranges mean food from human sources was plentiful, even with wild prey absent.</p>
<ul>
<li>Movement was markedly nocturnal: hourly steps averaged about 339 m at night against about 60 m by day.</li>
<li>Night locations were significantly closer to settlements than day locations.</li>
<li>Leopards in areas with many people visited houses regularly at night, with 20% of locations within 25 m of a house, but this happened in under 1% of daytime locations.</li>
<li>One leopard in a sparsely populated area avoided settlements both day and night.</li>
</ul>
<p>The other two leopards had been moved 52 km before release. They travelled far and in a set direction (the male covered 89 km in a straight line in 37 days) before settling in much larger ranges of about 42 and 65 km&sup2;. Tigers in Nepal show a similar shift towards the night where people are busy by day; see <a href="are-tigers-nocturnal.html">are tigers nocturnal?</a></p></section>
<section class="card"><h2>Why moving "problem" leopards backfired</h2>
<p>A common response to leopards near villages is to trap them and release them in a forest. Athreya and colleagues tested that idea in <i>Conservation Biology</i> (2011). In the year from February 2001, 29 leopards were captured in the rural Junnar region of Maharashtra (4,275 km&sup2;, about 185 people per km&sup2;), where attacks on livestock were common and attacks on people rare. They were released an average of 39.5 km away in nearby forests, and 11 more leopards were brought into the same forests from other districts.</p>
<p>From 1993 to 2001, Junnar averaged about four leopard attacks on people a year. After the translocations began, the average rose to 17. Attacks increased after nearby releases, became more lethal as more leopards came in from other districts, and were most likely where the most outside leopards had been released. The authors conclude the leopards did not stay put and that translocation induced attacks. Suggested reasons include capture stress, travel through unfamiliar land and loss of fear of people in captivity.</p></section>
<section class="card"><h2>Leopards in a megacity</h2>
<p>Leopards also live on the edges of Mumbai, one of the world's largest cities. In a 2018 paper in <i>Frontiers in Ecology and the Environment</i>, Alexander Braczkowski and colleagues argued that by preying on stray dogs, these leopards may reduce dog bites, the risk of rabies and the cost of dog sterilisation. Under one set of assumptions they estimated that leopard presence could save up to 90 human lives a year. That is a modelled estimate, not a count, and the authors stress that living with carnivores involves real trade offs between safety and conservation.</p></section>
<section class="card"><h2>Adaptable does not mean safe from extinction</h2>
<p>It is tempting to conclude that a cat this adaptable is not at risk. A 2016 range wide review in <i>PeerJ</i> by Andrew Jacobson and colleagues, calls that a misconception. Leopards now occupy only 25 to 37% of their historic range since 1750, and only about 17% of the remaining range is protected. Three subspecies, the Amur, Arabian and North Chinese leopards, have each lost as much as 98% of their historic range. For the full threat picture, see <a href="how-many-big-cats-are-left.html">how many big cats are left?</a> and <a href="../conservation.html">big cat conservation</a>.</p></section>
<section class="card"><h2>What these studies do not show</h2>
<p>Most of this evidence comes from a few landscapes in India, where cultural tolerance of wildlife is often high. It does not mean leopards are harmless: they kill livestock and pets, and attacks on people do happen. The GPS study tracked only five animals. The lesson is narrower and more useful: leopards can share land with people, and how people respond to them strongly shapes how safe that sharing is.</p></section>
<section class="card"><h2>Key takeaways</h2><ul>
<li>Leopards can live at high density in Indian farmland with no wild hoofed prey.</li>
<li>There they eat mainly domestic animals, especially dogs.</li>
<li>They approach homes at night and avoid people by day.</li>
<li>Trapping and moving leopards was followed by more attacks on people, not fewer.</li>
</ul></section>''',
     faq=[("Can leopards live near people?", "Yes. In western Maharashtra, India, leopards lived at about 4.8 adults per 100 km&sup2; in farmland with more than 300 people per km&sup2;, and attacks on people there were rare (Athreya et al. 2013)."),
          ("What do leopards eat near villages?", "Mostly domestic animals. In Ahmednagar district, 87% of prey biomass in leopard scats was domestic animals and 39% was dogs alone (Athreya et al. 2016)."),
          ("Does moving leopards away stop attacks?", "In Junnar, Maharashtra, it did the opposite. After 29 leopards were captured and released elsewhere, attacks on people rose from about four to 17 a year (Athreya et al. 2011)."),
          ("Are there leopards in Mumbai?", "Yes. Leopards live on the edges of Mumbai, and one study estimated that by eating stray dogs they may reduce dog bites and rabies risk (Braczkowski et al. 2018)."),
          ("If leopards are so adaptable, why are they Vulnerable?", "Because they have still lost most of their range. Leopards occupy only 25 to 37% of their historic range, and some subspecies have lost as much as 98% (Jacobson et al. 2016).")],
     related=[("Leopard facts", "leopard.html"), ("Why do leopards drag their kills into trees?", "blog/why-do-leopards-drag-their-kills-into-trees.html"), ("Leopard vs jaguar vs cheetah", "blog/leopard-vs-jaguar-vs-cheetah.html"), ("Are tigers nocturnal?", "blog/are-tigers-nocturnal.html"), ("Big cat conservation", "conservation.html"), ("Research papers", "research/index.html"), ("Blog home", "blog/index.html")],
     sources=[ATHREYA2013, ATHREYA2016, ODDEN2014, ATHREYA2011, BRACZKOWSKI2018, JACOBSON2016, CSG["leopard"]])

# ---------------------------------------------------------------- 16 CHEETAH CUB SURVIVAL (20 Oct 2026)
post("why-do-so-few-cheetah-cubs-survive", "Why Do So Few Cheetah Cubs Survive? What the Research Shows | BigCatWise",
     "On the Serengeti Plains only about 1 in 20 cheetah cubs reached independence, mostly because lions and hyenas killed them. Elsewhere, survival can be far higher.",
     "Why do so few cheetah cubs survive? Cub mortality, predators and what field studies show", headline="Why do so few cheetah cubs survive?",
     published="2026-10-20", modified="2026-10-20",
     lead="In the best known study, on the Serengeti Plains of Tanzania, a newborn cheetah cub had only about a 4.8% chance of reaching independence. Predators caused nearly three quarters of cub deaths, and lions made most of those kills, with spotted hyenas also taking many cubs once they left the den. But the Serengeti is not the whole story: in the Kgalagadi Transfrontier Park in southern Africa, cub survival was about seven times higher, and lions were not found to be involved in cub deaths.",
     body='''<section class="card"><h2>The short answer in numbers</h2>
<p>Karen Laurenson followed cheetah mothers and their litters on the Serengeti Plains and published the results in the <i>Journal of Zoology</i> in 1994. Her figures are still the ones most often quoted:</p>
<div class="tablewrap"><table><thead><tr><th>Stage</th><th>What happened on the Serengeti Plains</th></tr></thead><tbody>
<tr><td>Birth to about 8 weeks (in the lair)</td><td>About 72% of litters died before the cubs first left the lair</td></tr>
<tr><td>8 weeks to 14 months</td><td>About 83% of the cubs that did emerge died before adolescence</td></tr>
<tr><td>Overall</td><td>A cub's estimated chance of reaching independence at birth: 4.8%</td></tr>
<tr><td>Main cause</td><td>Predation, 73% of all cub deaths; about 78% of those kills were by lions</td></tr>
</tbody></table></div>
<p>Laurenson described this as extremely high compared with other large mammals. For context on how many cubs a mother has to begin with, see the <a href="../cheetah.html#facts">cheetah quick facts</a>.</p></section>
<section class="card"><h2>Inside the lair: the first eight weeks</h2>
<p>Cheetah mothers raise their cubs alone, keeping very young cubs hidden in a lair while they go off to hunt. In Laurenson's study, lions were the main cause of death at this stage. Not every loss was a kill, though. Some cubs starved after their mothers abandoned them, and others died in grass fires or bad weather.</p>
<p>The risk did not end when the cubs came out. The study found that the instantaneous death rate was highest straight after the cubs emerged from the lair, when they began following their mother across open plains.</p></section>
<section class="card"><h2>After the lair: lions and hyenas</h2>
<p>Once cubs were moving with their mother, predation accounted for virtually all of the deaths that followed. At this stage lions and spotted hyenas took roughly the same share of cubs.</p>
<p>Mothers are not passive. Laurenson found that how vigilant a mother was, and how much antipredator behavior she showed, mirrored how vulnerable her cubs were at each age. Whether a mother responded aggressively to a predator also depended on which predator it was. A cheetah weighs far less than a lion, so a mother's options are limited, which helps explain why vigilance matters so much.</p></section>
<section class="card"><h2>Cheetahs work hard to avoid lions and hyenas</h2>
<p>Sarah Durant tested how cheetahs react to the threat of larger carnivores using audio playbacks, published in <i>Behavioral Ecology</i> in 2000. When she played lion or hyena calls near Serengeti cheetahs, they actively moved away, compared with control trials where no sound was played.</p>
<ul>
<li>After hearing competitors, cheetahs were much less likely to hunt, so they made fewer kills.</li>
<li>They moved just as far after lion calls as after hyena calls, but spent more time looking at the loudspeaker and were less likely to make a kill after lion calls. Durant read this as cheetahs seeing lions as the bigger threat.</li>
<li>Males, females and mothers responded alike, which suggested they were reacting mainly to competition rather than to a direct threat to cubs.</li>
</ul>
<p>Avoiding lions therefore has a cost: time spent moving away or watching for danger is time not spent hunting, and a mother with cubs has to feed herself and them. Lions and hyenas also steal cheetah kills, as the <a href="../cheetah.html#hunting">cheetah hunting section</a> explains.</p></section>
<section class="card"><h2>Twenty years of Serengeti cheetahs</h2>
<p>A longer view came from Durant, Marcella Kelly and Tim Caro in 2004, using a 20 year record of individually known cheetahs on the Serengeti Plains. They found that:</p>
<ul>
<li>Recruitment of young was negatively associated with the number of lions, linking the high predation seen in earlier studies to population dynamics.</li>
<li>Recruitment rose with the number of Thomson's gazelles, the cheetah's main prey there, and fell with rainfall.</li>
<li>Recruitment peaked when mothers were around 6 to 7 years old.</li>
<li>Adolescents that stayed in temporary sibling groups survived better than those on their own, particularly males with sisters.</li>
<li>Males had markedly lower survival than females.</li>
</ul></section>
<section class="card"><h2>Is the Serengeti typical?</h2>
<p>Not necessarily. In 2014 Gus and Margie Mills reported on cheetahs in the Kgalagadi Transfrontier Park, which spans South Africa and Botswana. Cub survival there was about seven times higher than on the Serengeti Plains. Predation was still the most common cause of cub death, but lions were not found to be involved.</p>
<p>They also argued that a close look at the Serengeti data does not unequivocally prove that lions dominate as predators of cheetah cubs there, and that very high cub mortality may not be as widespread as is commonly believed. That matters because the Serengeti figures had fed a belief that areas with many large carnivores are poor places to conserve cheetahs.</p>
<p>The fair summary is that cheetah cubs can face extreme losses, especially on open plains with many lions and hyenas, but survival varies a lot between ecosystems.</p></section>
<section class="card"><h2>Why this matters for conservation</h2>
<p>Cheetahs are listed as Vulnerable, and most remaining populations are small. When few cubs survive, a population depends heavily on adult females living long enough to raise several litters. Knowing where and why cubs die helps decide which areas can sustain cheetahs, and the Kgalagadi results suggest that places with lions should not be written off. See <a href="../cheetah.html#status">how many cheetahs are left</a> and <a href="../conservation.html">big cat conservation</a>.</p></section>
<section class="card"><h2>Key takeaways</h2><ul>
<li>On the Serengeti Plains, only about 4.8% of cheetah cubs were estimated to reach independence.</li>
<li>Predation caused about 73% of cub deaths there, mostly by lions; hyenas took many cubs after they left the lair.</li>
<li>Cheetahs move away from lion and hyena calls and hunt less afterwards.</li>
<li>In the Kgalagadi, cub survival was about seven times higher and lions were not found to kill cubs.</li>
</ul></section>''',
     faq=[("What percentage of cheetah cubs survive?", "It depends on the place. On the Serengeti Plains, Laurenson (1994) estimated a newborn cub had a 4.8% chance of reaching independence. In the Kgalagadi Transfrontier Park, Mills and Mills (2014) found survival about seven times higher."),
          ("What kills cheetah cubs?", "Mostly predators. On the Serengeti Plains predation caused 73.2% of cub deaths, and 78.2% of those kills were by lions. Spotted hyenas also took many cubs after they left the lair. Some cubs died of starvation after being abandoned, or in grass fires and bad weather (Laurenson 1994)."),
          ("When are cheetah cubs most at risk?", "Very early. About 72% of litters died before leaving the lair at around eight weeks, and the death rate was highest right after cubs emerged (Laurenson 1994)."),
          ("Do lions kill cheetah cubs everywhere?", "No. In the Kgalagadi Transfrontier Park, lions were not found to be involved in cub deaths, and the authors questioned whether lions clearly dominate cub predation even on the Serengeti (Mills and Mills 2014)."),
          ("How do cheetah mothers protect their cubs?", "By hiding young cubs in a lair, staying vigilant, and sometimes confronting predators. Mothers' vigilance matched how vulnerable their cubs were, and whether they responded aggressively depended on the predator species (Laurenson 1994).")],
     related=[("Cheetah facts", "cheetah.html"), ("How fast is a cheetah?", "blog/how-fast-is-a-cheetah.html"), ("Do cheetahs abandon hunts because they overheat?", "blog/do-cheetahs-abandon-hunts-because-they-overheat.html"), ("Why do lions live in prides?", "blog/why-do-lions-live-in-prides.html"), ("How many big cats are left?", "blog/how-many-big-cats-are-left.html"), ("Research papers", "research/index.html"), ("Blog home", "blog/index.html")],
     sources=[LAURENSON1994, DURANT2000, DURANT2004, MILLS2014, CSG["cheetah"]])

# ---------------------------------------------------------------- 17 SNOW LEOPARD GENETIC DIVERSITY (21 Oct 2026)
post("why-do-snow-leopards-have-low-genetic-diversity", "Why Do Snow Leopards Have Such Low Genetic Diversity? | BigCatWise",
     "Genome studies find snow leopards have the lowest genetic diversity of any big cat, mostly because their population has always been small. Here is what that means.",
     "Why do snow leopards have such low genetic diversity? What genome studies show", headline="Why do snow leopards have such low genetic diversity?",
     published="2026-10-21", modified="2026-10-21",
     lead="Snow leopards have the lowest genetic diversity of any big cat species, according to a 2025 study that sequenced the whole genomes of 41 snow leopards. The main reason appears to be that their population has stayed small for most of their evolutionary history, not simply recent inbreeding. A second 2025 genome study, of 52 wild snow leopards, reached a similar conclusion and also found a silver lining: many of the most harmful mutations seem to have been purged over time.",
     body='''<section class="card"><h2>What "genetic diversity" means</h2>
<p>Genetic diversity is the amount of variation in DNA between individuals of a species. A species with plenty of variation has more raw material to adapt when conditions change, for example a new disease or a warming climate. Species whose populations stay small for a long time tend to lose variation, because chance plays a larger role in which gene versions are passed on.</p>
<p>Until recently snow leopards were the least studied big cat genetically. Katherine Solari and colleagues, writing in <i>PNAS</i> in 2025, noted that a dearth of genetic data was unique to snow leopards among all big cat species. Two large genome studies published in 2025 have now started to fill that gap.</p></section>
<section class="card"><h2>The lowest diversity of any big cat</h2>
<p>Solari's team used whole genome sequencing data for 41 snow leopards, 37 of them newly sequenced. Their headline finding was that snow leopards have the lowest genetic diversity of any big cat species.</p>
<p>The authors also looked at why. Their results pointed to a persistently small population size throughout the snow leopard's evolutionary history, rather than recent inbreeding, as the likely cause. In other words, the low diversity is mostly an old pattern, not just a symptom of recent poaching or habitat loss.</p>
<p>Lin Yang and colleagues, writing in <i>Genome Biology</i> in 2025, sequenced a high quality chromosome level reference genome plus the genomes of 52 wild snow leopards. They likewise found that snow leopards have extremely low genomic diversity, and also higher inbreeding than other species in the order Carnivora.</p></section>
<section class="card"><h2>The silver lining: purged harmful mutations</h2>
<p>Low diversity is not the whole story. Both genome studies found evidence that snow leopards carry relatively few of the most damaging mutations:</p>
<ul>
<li>Solari and colleagues found that snow leopards have significantly less highly deleterious homozygous load (two copies of a seriously harmful variant) than numerous other <i>Panthera</i> species, which suggests effective purging while their population was small.</li>
<li>Yang and colleagues concluded that strong deleterious mutations were effectively purged by historical population bottlenecks and inbreeding, and suggested this may be a vital genetic mechanism behind the species' survival and viability.</li>
</ul>
<p>Purging happens because, in a small population, harmful recessive variants are more often inherited in two copies, exposed and removed by natural selection. That may help explain how snow leopards have persisted for so long with so little variation.</p></section>
<section class="card"><h2>Two populations, north and south</h2>
<p>The genome studies also mapped how snow leopards are split across their huge mountain range:</p>
<ul>
<li>Solari and colleagues found a primary genetic divide between the northern and southern parts of the range around the Dzungarian Basin, and a secondary divide south of Kyrgyzstan around the Taklamakan Desert.</li>
<li>Yang and colleagues found two large lineages, northern and southern, and linked their divergence to the Last Glacial Maximum. They suggested that microclimate differences and large rivers between the western and central Himalayas help keep the two lineages distinct.</li>
<li>In Yang's data the northern lineage had lower diversity and higher inbreeding and genetic load than the southern lineage, consistent with a recent population decline in the north.</li>
</ul>
<p>Earlier work with other markers agrees on the broad picture. Imogene Cancellare and colleagues genotyped 182 snow leopards from across the range (<i>Biodiversity and Conservation</i>, 2024). Their microsatellite data indicated two global genetic populations, while mitochondrial DNA showed little phylogeographic structure and suggested a single refugial origin for all sampled populations, with tentative evidence of a glacial refugium in the Tian Shan, Pamir, Hindu Kush and Karakoram mountains.</p></section>
<section class="card"><h2>A clue to life at high altitude</h2>
<p>Yang's study also found that a gene called <i>EPAS1</i> shows signs of positive selection in the southern lineage, with almost fixed amino acid changes, and that the frequency of this variant increases with elevation. <i>EPAS1</i> is involved in how the body responds to low oxygen, so this is a promising lead on how some snow leopards cope with very high mountains. For the physical adaptations, see <a href="../snow-leopard.html#adapt">how snow leopards are adapted to the cold</a>.</p></section>
<section class="card"><h2>Evidence from the Tibetan Plateau</h2>
<p>Snow leopards on the Tibetan Plateau tell a similar story. Shiqing Wang and colleagues assembled mitochondrial genomes for 136 snow leopards from the plateau (<i>Conservation Genetics</i>, 2025). They found 84 variable sites and 32 distinct haplotypes, 24 of them reported for the first time, and concluded that genetic diversity in this population is low. They also found signs of two distinct subpopulations within the plateau group.</p></section>
<section class="card"><h2>Why this matters for conservation</h2>
<p>Snow leopards are listed as Vulnerable, and threats such as retaliatory killing and poaching continue (see <a href="../snow-leopard.html#status">how many snow leopards are left</a>). Solari and colleagues warned that, without a large population or much standing genetic variation to buffer them, snow leopard persistence may be more tenuous than currently appreciated. Cancellare's team recommended using genetic data to define and protect meaningful conservation units. Keeping populations connected across the northern and southern ranges is part of that, alongside protecting their wild prey (see <a href="what-do-snow-leopards-eat.html">what snow leopards eat</a>) and the wider work described in <a href="../conservation.html">big cat conservation</a>.</p></section>
<section class="card"><h2>Key takeaways</h2><ul>
<li>Snow leopards have the lowest genetic diversity of any big cat species (Solari et al. 2025).</li>
<li>The likely cause is a persistently small population over their evolutionary history, rather than only recent inbreeding.</li>
<li>Highly harmful mutations appear to have been purged, which may have helped the species persist.</li>
<li>Snow leopards form two main genetic groups, northern and southern, and the northern lineage shows signs of recent decline.</li>
</ul></section>''',
     faq=[("Do snow leopards have low genetic diversity?", "Yes. A 2025 whole genome study of 41 snow leopards found they have the lowest genetic diversity of any big cat species (Solari et al. 2025), and a second study of 52 wild snow leopards also found extremely low genomic diversity (Yang et al. 2025)."),
          ("Why is snow leopard genetic diversity so low?", "Mainly because their population appears to have been small throughout their evolutionary history, rather than only because of recent inbreeding (Solari et al. 2025)."),
          ("Are snow leopards inbred?", "Yang et al. (2025) found higher inbreeding in snow leopards than in other Carnivora species, and higher in the northern lineage than the southern one. Solari et al. (2025) concluded that the low diversity is driven mainly by long-term small population size rather than recent inbreeding."),
          ("How many genetic populations of snow leopards are there?", "Studies point to two main groups, northern and southern. Whole genome data place the main divide around the Dzungarian Basin, with a secondary divide around the Taklamakan Desert (Solari et al. 2025); microsatellite data also indicate two global populations (Cancellare et al. 2024)."),
          ("Is low genetic diversity dangerous for snow leopards?", "It can make them less able to adapt to new threats. Researchers warn their persistence may be more tenuous than appreciated, although highly harmful mutations appear to have been purged over time (Solari et al. 2025; Yang et al. 2025).")],
     related=[("Snow leopard facts", "snow-leopard.html"), ("What do snow leopards eat?", "blog/what-do-snow-leopards-eat.html"), ("Which big cats can roar?", "blog/which-big-cats-can-roar.html"), ("How many big cats are left?", "blog/how-many-big-cats-are-left.html"), ("Big cat conservation", "conservation.html"), ("Research papers", "research/index.html"), ("Blog home", "blog/index.html")],
     sources=[SOLARI2025, YANG2025, CANCELLARE2024, WANG2024, CSG["snow"]])

# ---------------------------------------------------------------- BLOG INDEX
add("blog/index.html", "BigCatWise Blog: Answers to Big Cat Questions | BigCatWise",
    "Sourced answers to big cat questions: which cats roar, why lions live in prides, cheetah speed, tiger territory, leopards in trees and more.",
    "BigCatWise blog", kind="page", headline="Blog",
    lead="In depth, sourced answers to specific questions about big cats. New posts are added when there is something genuinely useful to say.",
    body='<div class="grid">' + "".join('<a class="tile" href="%s"><h3>%s</h3><p>%s</p></a>' % (p.path.split("/")[1], p.headline, p.description) for p in POSTS) + '</div>',
    related=[("Compare big cats", "compare.html"), ("Big cat FAQ", "faq.html")], priority="0.7")
