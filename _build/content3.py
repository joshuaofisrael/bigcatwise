from build import add
from sources import CSG, SDZ, IUCN, DURANT
from content import jump

ALLCSG = [CSG[k] for k in ("lion", "tiger", "leopard", "jaguar", "cheetah", "snow")]

ID_TABLE = '''<div class="tablewrap"><table><thead><tr><th>Feature</th><th><a href="leopard.html">Leopard</a></th><th><a href="jaguar.html">Jaguar</a></th><th><a href="cheetah.html">Cheetah</a></th><th><a href="snow-leopard.html">Snow leopard</a></th><th><a href="tiger.html">Tiger</a></th><th><a href="lion.html">Lion</a></th></tr></thead><tbody>
<tr><th scope="row">Body markings</th><td>Small rosettes, usually empty in the middle</td><td>Large rosettes, usually with dots inside</td><td>Solid round black spots</td><td>Open dark rosettes on grey</td><td>Black stripes</td><td>Plain; cubs faintly spotted</td></tr>
<tr><th scope="row">Base colour</th><td>Pale yellow to golden</td><td>Golden to tawny</td><td>Tawny to pale gold</td><td>Smoky grey to cream</td><td>Reddish orange, white underside</td><td>Tawny</td></tr>
<tr><th scope="row">Face</th><td>Plain with small spots</td><td>Broad, heavy head</td><td>Small head, black tear marks eye to mouth</td><td>Small head, pale eyes, thick fur</td><td>Striped face, white patches</td><td>Males have a mane</td></tr>
<tr><th scope="row">Build</th><td>Muscular, lithe</td><td>Stocky, powerful</td><td>Slim, long legs, deep chest</td><td>Compact, short forelimbs, big paws</td><td>Very large, powerful</td><td>Large, males heavier</td></tr>
<tr><th scope="row">Tail</th><td>Long</td><td>Relatively short, ringed near tip</td><td>Long, ringed near tip</td><td>Very long and thick, up to about 1 m</td><td>Long, ringed</td><td>Dark tuft at tip</td></tr>
<tr><th scope="row">Weight (IUCN CatSG)</th><td>17 to 90 kg</td><td>36 to 148 kg</td><td>23 to 65 kg</td><td>30 to 50 kg</td><td>75 to 325 kg</td><td>110 to 272 kg</td></tr>
<tr><th scope="row">Wild range</th><td>Africa and Asia</td><td>Americas only</td><td>Africa; Iran</td><td>Mountains of Central and South Asia</td><td>Asia only</td><td>Africa; Gir, India</td></tr>
<tr><th scope="row">Behavior clue</th><td>Rests and stores kills in trees</td><td>Near water, swims readily</td><td>Sprints after prey in daylight</td><td>On steep rocky slopes</td><td>Solitary, forest and grassland</td><td>In groups (prides)</td></tr>
<tr><th scope="row">Roars?</th><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr>
</tbody></table></div>'''

REGIONS = [
 ("africa", "Africa", "Lion, leopard, cheetah",
  "<p><b>Lions</b> live across much of sub-Saharan Africa, with strongholds in eastern and southern Africa and only small, isolated populations in West Africa; they are extinct in North Africa. <b>Leopards</b> occur across most of sub-Saharan Africa, with South Africa a stronghold; the former populations in Morocco and Algeria are thought to have vanished. <b>Cheetahs</b> have two main strongholds, Namibia and Botswana, and Kenya and Tanzania, with very sparse populations in the Sahara. All three can share the same savanna, and about two thirds of cheetahs live outside protected areas.</p>"),
 ("south-asia", "South Asia", "Tiger, leopard, snow leopard, Asiatic lion (plus reintroduced cheetahs in India)",
  "<p><b>Tigers</b> breed in India, Nepal, Bhutan and Bangladesh, including the Sundarbans mangroves. <b>Leopards</b> are widespread, from lowland forests to the Himalayas, and also live in Sri Lanka. The only wild <b>Asiatic lions</b> live in and around Gir forest in Gujarat, India. <b>Snow leopards</b> live high in the Himalayas and neighbouring ranges of India, Nepal, Bhutan, Pakistan and Afghanistan. In 2022 India began bringing <b>cheetahs</b> from southern Africa to Kuno National Park.</p>"),
 ("southeast-asia", "Southeast Asia", "Tiger, leopard",
  "<p><b>Tigers</b> survive in Malaysia, Thailand, Myanmar and on Sumatra in Indonesia, but have disappeared from Vietnam, Lao PDR and Cambodia. <b>Leopards</b> are now gone or functionally gone from most of Southeast Asia, surviving mainly in Thailand, Myanmar, Malaysia and on Java. The clouded leopards of this region are a separate, smaller genus and are not covered on this site.</p>"),
 ("east-asia", "East Asia and the Russian Far East", "Tiger, leopard, snow leopard",
  "<p><b>Amur tigers</b> and <b>Amur leopards</b> live in the forests of the Russian Far East and neighbouring northeast China, the leopards as a single population. Leopards formerly called North China leopards survive in small protected areas in central China. <b>Snow leopards</b> live in the mountains of western China, Mongolia and southern Siberia (Russia). The South China tiger is likely extinct in the wild.</p>"),
 ("central-asia", "Central Asia", "Snow leopard (rare leopards in the Caucasus and Iran)",
  "<p><b>Snow leopards</b> live in the Tian Shan, Pamir and Altai mountains of Kazakhstan, Kyrgyzstan, Tajikistan, Uzbekistan and Mongolia, often at lower elevations at the northern edge of the range. <b>Leopards</b> persist in small numbers in Iran, Turkmenistan and the Caucasus, including a small population in the Zangezur ridge of Armenia and Azerbaijan. The Caspian tiger is extinct, though there are plans to reintroduce tigers to Kazakhstan.</p>"),
 ("middle-east", "Middle East", "Leopard (very rare), Asiatic cheetah (Iran only)",
  "<p>The last <b>Asiatic cheetahs</b> live in Iran, with fewer than 50 mature individuals thought to remain. <b>Leopards</b> survive in very small numbers in Iran, the Arabian Peninsula and eastern Turkey, and the Arabian population is decreasing drastically. Lions once lived here too but disappeared by the twentieth century; they were last recorded in Iraq in 1918 and Iran in 1942.</p>"),
 ("americas", "The Americas", "Jaguar",
  "<p>The <b>jaguar</b> is the only big cat in the Americas, ranging from Mexico through Central America to northern Argentina, with occasional individuals recorded in the southwestern United States. The Amazon holds about 89 percent of all jaguars. The puma (cougar or mountain lion) is also widespread in the Americas but is not usually counted as a big cat and cannot roar.</p>"),
 ("elsewhere", "Europe, Australia and Antarctica", "None today",
  "<p>There are no wild big cats in Australia or Antarctica, and none across most of Europe. Lions lived in southeastern Europe until about the first century CE. The only big cats near Europe today are the rare leopards of the Caucasus region. Reports of large wild cats in places like Britain or Australia have not been confirmed as established wild populations.</p>"),
]
region_table = ('<div class="tablewrap"><table><thead><tr><th>Region</th><th>Wild big cats</th></tr></thead><tbody>' +
                "".join('<tr><td><a href="#%s">%s</a></td><td>%s</td></tr>' % (i, n, c) for i, n, c, _ in REGIONS) + '</tbody></table></div>')
ALIASES = {"south-asia": ["asia", "india"], "americas": ["north-america", "central-america", "south-america"], "elsewhere": ["europe", "australia"], "middle-east": ["iran"]}
region_sections = "".join('%s<section class="card" id="%s"><h3>%s</h3><p class="sci">%s</p>%s</section>' % ("".join('<span id="%s"></span>' % a for a in ALIASES.get(i, [])), i, n, c, t) for i, n, c, t in REGIONS)
region_jump = '<p class="jump">Jump to a region: ' + " | ".join('<a href="#%s">%s</a>' % (i, n) for i, n, c, t in REGIONS) + '</p>' 

add("which-big-cat-is-it.html", "Which Big Cat Is It? Identification Guide & Big Cats by Region | BigCatWise",
    "Identify any big cat: leopard vs jaguar vs cheetah, snow leopard, tiger and lion compared side by side, plus a region by region guide to which big cats live where.",
    "Which big cat is it? Identification guide and big cats by region", headline="Which big cat is it? ID guide",
    lead="To identify a big cat, check three things: where it is, what its markings look like and how it is built. Stripes mean tiger; a plain coat (and a mane on males) means lion; solid spots and black tear marks mean cheetah; small empty rosettes mean leopard; large rosettes with dots inside on a stocky body mean jaguar; and a smoky grey coat with a huge tail in high mountains means snow leopard. In the wild, location alone often settles it: the only big cat in the Americas is the jaguar.",
    body=jump([("key", "Quick key"), ("side-by-side", "Side by side"), ("spotted", "Leopard vs jaguar vs cheetah"), ("others", "Snow leopard, tiger, lion"),
               ("variants", "Black panthers and white tigers"), ("lookalikes", "Lookalikes"), ("by-region", "Big cats by region")]) +
    '''<section class="card" id="key"><h2>Quick identification key</h2><ol>
<li><b>Stripes?</b> It is a <a href="tiger.html">tiger</a>, the only striped cat.</li>
<li><b>Plain tawny coat, no spots on adults?</b> It is a <a href="lion.html">lion</a>. Adult males have a mane; both sexes have a dark tail tuft.</li>
<li><b>Solid round spots, black lines from eyes to mouth, slim greyhound build?</b> It is a <a href="cheetah.html">cheetah</a>.</li>
<li><b>Grey or cream coat, open rosettes, very long thick tail, mountain terrain?</b> It is a <a href="snow-leopard.html">snow leopard</a>.</li>
<li><b>Rosettes on a golden coat?</b> In the Americas it is a <a href="jaguar.html">jaguar</a>; in Africa or Asia it is a <a href="leopard.html">leopard</a>. In a zoo, look inside the rosettes: dots inside and a stocky body mean jaguar, empty rosettes and a lithe body mean leopard.</li>
<li><b>Completely black?</b> A melanistic leopard (Africa, Asia) or jaguar (Americas). See <a href="#variants">black panthers</a>.</li></ol></section>
<section class="card" id="side-by-side"><h2>All six big cats side by side</h2>''' + ID_TABLE +
    '''<p class="note">Weights are the full ranges listed by the IUCN SSC Cat Specialist Group, covering both sexes and all populations. For population and status figures see the <a href="compare.html">big cat comparison table</a>.</p></section>
<section class="card" id="spotted"><h2>Leopard vs jaguar vs cheetah</h2>
<p>These three cause most identification mistakes. Use this order:</p>
<h3>1. Location</h3><p>Wild jaguars live only from Mexico to northern Argentina (with occasional visitors to the southwestern United States). Wild leopards and cheetahs live only in Africa and Asia, and in Asia wild cheetahs survive only in Iran. So a spotted big cat in the Americas is a jaguar, and in South or Southeast Asia it is almost certainly a leopard.</p>
<h3>2. Spot pattern on the flanks</h3><ul><li><b>Cheetah:</b> single solid black dots, evenly scattered. No rosettes.</li>
<li><b>Leopard:</b> rosettes are small and tightly packed, usually with no spot in the centre.</li>
<li><b>Jaguar:</b> rosettes are larger and more angular, usually with one or more dots inside.</li></ul>
<p>All three have solid spots on the head and legs, so judge by the sides of the body.</p>
<h3>3. Face</h3><p>The cheetah's black tear marks, running from the inner eye to the corner of the mouth, are unique among big cats. The jaguar's head is noticeably broad and heavy for its body; the leopard's is in proportion.</p>
<h3>4. Build and tail</h3><p>Cheetahs are slim and long legged, built for sprinting, with semi retractable claws. Leopards are muscular but lithe with a long tail. Jaguars are the heavyweights: deep chested, thick limbed and with a relatively short tail.</p>
<h3>5. Behavior</h3><p>A spotted cat with a carcass up a tree is probably a leopard. One sprinting across open plains in daylight is probably a cheetah. One swimming or hunting caiman along a South American river is a jaguar.</p>
<p>More detail in our post <a href="blog/leopard-vs-jaguar-vs-cheetah.html">leopard vs jaguar vs cheetah</a>.</p></section>
<section class="card" id="others"><h2>Snow leopard, tiger and lion</h2>
<p><b>Snow leopard:</b> the only big cat with a pale smoky grey to cream coat. Its rosettes are open and dark, its paws are broad and furry, and its tail is exceptionally long and thick, up to about 1 m, or 75 to 90 percent of its head and body length. It lives in high mountains, typically at 3,000 to 5,000 m, so terrain is a strong clue.</p>
<p><b>Tiger:</b> unmistakable thanks to its stripes, which are unique to each individual. Tigers also have a white spot on the back of each ear.</p>
<p><b>Lion:</b> the only big cat with a plain adult coat and the only one where males and females look obviously different, thanks to the male's mane. Some males have short or sparse manes, so look also for the black tail tuft and for a group of cats together, since lions are the only social big cat.</p></section>
<section class="card" id="variants"><h2>Black panthers, white tigers and other colour variants</h2>
<p><b>Black panther</b> is not a species. It is the common name for a melanistic leopard or jaguar, whose very dark fur still shows faint rosettes in good light. Location tells you which: Africa or Asia means leopard, the Americas mean jaguar.</p>
<p><b>White tigers</b> are a rare colour variant of the ordinary tiger, with grey to brown stripes on a white coat, not a separate species. According to the IUCN Cat Specialist Group, the last documented white tiger in the wild was shot in India in 1958.</p></section>
<section class="card" id="lookalikes"><h2>Lookalikes that are not big cats</h2><ul>
<li><b>Puma</b> (cougar, mountain lion): a large, plain tan cat of the Americas. Adults have no spots, but puma kittens are spotted. Pumas cannot roar.</li>
<li><b>Clouded leopards:</b> smaller forest cats of South and Southeast Asia with large cloud shaped blotches and very long canine teeth.</li>
<li><b>Serval:</b> a much smaller, long legged African cat with huge ears and solid spots; sometimes mistaken for a young cheetah.</li>
<li><b>Ocelot:</b> a small spotted cat of the Americas with chain like markings; sometimes mistaken for a young jaguar.</li>
<li><b>Lynx and caracal:</b> medium sized cats with tufted ears and short (lynx) or medium length (caracal) tails.</li></ul></section>
<section class="card" id="by-region"><h2>Big cats by region: which big cats live where?</h2>
<p>Use this section to narrow down what you could be looking at in the wild. Each region links to a detailed section below.</p>''' + region_jump + region_table + '</section>' + region_sections,
    faq=[("How can you tell a leopard from a jaguar?", "Check location first: wild jaguars live only in the Americas and wild leopards only in Africa and Asia. Otherwise, jaguar rosettes are larger and usually have dots inside, and jaguars are stockier with a broader head and shorter tail."),
         ("How do you tell a cheetah from a leopard?", "Cheetahs have solid round spots, black tear marks from the eyes to the mouth and a slim, long legged build. Leopards have rosettes and a more muscular body."),
         ("Which big cats live in Africa?", "Lions, leopards and cheetahs. There are no wild tigers, jaguars or snow leopards in Africa."),
         ("Which big cat lives in the Americas?", "Only the jaguar, from Mexico to northern Argentina. The puma also lives there but is not usually counted as a big cat."),
         ("What is a black panther?", "A melanistic leopard in Africa or Asia, or a melanistic jaguar in the Americas. It is not a separate species.")],
    related=[("Big cat comparison table", "compare.html"), ("Where big cats live", "habitats.html"), ("Leopard vs jaguar vs cheetah", "blog/leopard-vs-jaguar-vs-cheetah.html"),
             ("Leopard facts", "leopard.html"), ("Jaguar facts", "jaguar.html"), ("Cheetah facts", "cheetah.html")],
    sources=ALLCSG + [SDZ["leopard"], SDZ["jaguar"], SDZ["cheetah"], SDZ["snow"], IUCN], priority="1.0")
