<map version="freeplane 1.2.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="GAME" ID="ID_1723255651" CREATED="1283093380553" MODIFIED="1396322382015"><hook NAME="MapStyle" zoom="1.003">

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node">
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right">
<stylenode LOCALIZED_TEXT="default" MAX_WIDTH="600" COLOR="#000000" STYLE="as_parent">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.note"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="5"/>
<node TEXT="Data Classes" POSITION="right" ID="ID_1550716541" CREATED="1396322383250" MODIFIED="1396322393109">
<edge COLOR="#ff0000"/>
<node TEXT="Item" ID="ID_1332590124" CREATED="1396326656937" MODIFIED="1396326658875">
<node TEXT="data" ID="ID_1785160355" CREATED="1396326674656" MODIFIED="1396326685093">
<node TEXT="itemNumber" ID="ID_1949279756" CREATED="1396327085140" MODIFIED="1396327094093"/>
<node TEXT="name" ID="ID_339748428" CREATED="1396327094343" MODIFIED="1396327101328"/>
<node TEXT="itemType" ID="ID_852233083" CREATED="1396327101671" MODIFIED="1396327107265"/>
<node TEXT="effect" ID="ID_1403405894" CREATED="1396327107671" MODIFIED="1396327110375">
<node TEXT="Type: Stats" ID="ID_692225447" CREATED="1398194430969" MODIFIED="1398194440203"/>
</node>
<node TEXT="equipRequirements" ID="ID_1836353065" CREATED="1396327110812" MODIFIED="1396327117640">
<node TEXT="Type: Stats" ID="ID_40908678" CREATED="1398193402578" MODIFIED="1398194445250"/>
</node>
<node TEXT="description" ID="ID_1062779580" CREATED="1396327117984" MODIFIED="1396327123656"/>
</node>
<node TEXT="methods" ID="ID_1034758435" CREATED="1396326685421" MODIFIED="1396326686906">
<node TEXT="getters and setters for data" ID="ID_1676355384" CREATED="1396327145421" MODIFIED="1396327150609"/>
<node TEXT="__init__" ID="ID_1249214449" CREATED="1398196159563" MODIFIED="1398196163860">
<node TEXT="itemNumber" ID="ID_1317384388" CREATED="1398196167438" MODIFIED="1398196172703"/>
<node TEXT="itemType" ID="ID_55320942" CREATED="1398196174594" MODIFIED="1398196178688"/>
<node TEXT="name" ID="ID_288543461" CREATED="1398196173063" MODIFIED="1398196174141"/>
<node TEXT="description" ID="ID_724156663" CREATED="1398196194531" MODIFIED="1398196197828"/>
<node TEXT="effect" ID="ID_1349462764" CREATED="1398196180250" MODIFIED="1398196182235">
<node TEXT="Type: Attack" ID="ID_1035973565" CREATED="1398196226281" MODIFIED="1398196241094"/>
</node>
<node TEXT="equipRequirements" ID="ID_1492164867" CREATED="1398196182453" MODIFIED="1398196191625">
<node TEXT="Type: Stats" ID="ID_176755683" CREATED="1398196356203" MODIFIED="1398196359406"/>
</node>
</node>
<node TEXT="isUsable()" ID="ID_798032913" CREATED="1396327151500" MODIFIED="1396327159343">
<node TEXT="returns whether or not the item is usable (e.g. Potion)" ID="ID_1721479061" CREATED="1396327159734" MODIFIED="1396327233906"/>
</node>
<node TEXT="isEquipable()" ID="ID_1922585433" CREATED="1396327235031" MODIFIED="1396327243421">
<node TEXT="returns whether or not the item is an equip type. (e.g. Helmet)" ID="ID_301275587" CREATED="1396327247796" MODIFIED="1396327270031"/>
</node>
</node>
</node>
<node TEXT="Inventory" ID="ID_1159675393" CREATED="1396326659703" MODIFIED="1396326662093">
<node TEXT="data" ID="ID_981197232" CREATED="1396326688453" MODIFIED="1396326691250">
<node TEXT="size" ID="ID_1262435724" CREATED="1396327272890" MODIFIED="1396327287906"/>
<node TEXT="numItems" ID="ID_972957894" CREATED="1396327288109" MODIFIED="1396327293671"/>
<node TEXT="inventory" ID="ID_910238283" CREATED="1396327294421" MODIFIED="1396327299140"/>
</node>
<node TEXT="methods" ID="ID_1936571522" CREATED="1396326691828" MODIFIED="1396326692890">
<node TEXT="getters and setters for data" ID="ID_1606547500" CREATED="1396327362140" MODIFIED="1396327747484"/>
<node TEXT="__init__" ID="ID_833531469" CREATED="1398196627281" MODIFIED="1398196633406">
<node TEXT="size" ID="ID_964345067" CREATED="1398196634266" MODIFIED="1398196636328"/>
</node>
<node TEXT="addItem(item)" ID="ID_1713115995" CREATED="1396327747953" MODIFIED="1396327903140">
<node TEXT="Add an item to the first spot available on the list." ID="ID_1776922002" CREATED="1396327996171" MODIFIED="1396328011500"/>
</node>
<node TEXT="removeItem(num)" ID="ID_1611535433" CREATED="1396327916359" MODIFIED="1396327940828">
<node TEXT="Remove item on the slot &apos;num&apos;" ID="ID_1028313041" CREATED="1396328014515" MODIFIED="1396328030781"/>
</node>
<node TEXT="takeItem(num)" ID="ID_1998876634" CREATED="1396327922250" MODIFIED="1396327937562">
<node TEXT="Remove item in slot &apos;num&apos; and return as output" ID="ID_90922079" CREATED="1396328035390" MODIFIED="1396328054031"/>
</node>
<node TEXT="switchItem(num, item)" ID="ID_460684081" CREATED="1396327976281" MODIFIED="1396327990828">
<node TEXT="Switch item with the item in the inventory&apos;s slot &apos;num&apos;" ID="ID_1197586258" CREATED="1396328055515" MODIFIED="1396328074203"/>
</node>
</node>
</node>
<node TEXT="Environment" ID="ID_658040641" CREATED="1396326633718" MODIFIED="1396326643671">
<node TEXT="data" ID="ID_505769731" CREATED="1396326664140" MODIFIED="1396326665796">
<node TEXT="x" ID="ID_852132889" CREATED="1396326954203" MODIFIED="1396326955687"/>
<node TEXT="y" ID="ID_1733640554" CREATED="1396326955890" MODIFIED="1396326956250"/>
<node TEXT="grid" ID="ID_558473291" CREATED="1396326940812" MODIFIED="1396326953937"/>
</node>
<node TEXT="methods" ID="ID_864564195" CREATED="1396326666156" MODIFIED="1396326668921">
<node TEXT="getters and setters for data" ID="ID_656771085" CREATED="1396326972421" MODIFIED="1396327128906"/>
<node TEXT="set/getComponents" ID="ID_1620061778" CREATED="1396327011109" MODIFIED="1396327053984">
<node TEXT="change/get the whole environment" ID="ID_1223290886" CREATED="1396327055093" MODIFIED="1396327081843"/>
<node TEXT="*- OPTIONAL -*" ID="ID_432723381" CREATED="1396327961500" MODIFIED="1396327970343"/>
</node>
</node>
</node>
<node TEXT="EnvironmentComponent" ID="ID_1889473366" CREATED="1396326644593" MODIFIED="1396326650250">
<node TEXT="data" ID="ID_1058424" CREATED="1396326669984" MODIFIED="1396326671312">
<node TEXT="x" ID="ID_404028910" CREATED="1396326703609" MODIFIED="1396326892625"/>
<node TEXT="y" ID="ID_1463256766" CREATED="1396326893015" MODIFIED="1396326893843"/>
<node TEXT="environmentType" ID="ID_1407132916" CREATED="1396326894078" MODIFIED="1396326897750"/>
<node TEXT="solid" ID="ID_1979314174" CREATED="1396326897953" MODIFIED="1396326902968"/>
<node TEXT="effect" ID="ID_1547196242" CREATED="1396326903203" MODIFIED="1396326906531"/>
<node TEXT="orientation" ID="ID_1647016390" CREATED="1396326906734" MODIFIED="1396326911000"/>
</node>
<node TEXT="methods" ID="ID_4705073" CREATED="1396326671656" MODIFIED="1396326673140">
<node TEXT="getters and setters for data" ID="ID_1588092892" CREATED="1396326918109" MODIFIED="1396327133312"/>
</node>
</node>
<node TEXT="Stats" ID="ID_482529774" CREATED="1398190642578" MODIFIED="1398200452500">
<node TEXT="data" ID="ID_359674906" CREATED="1398190654828" MODIFIED="1398190656797">
<node TEXT="HP" ID="ID_187075465" CREATED="1398190657813" MODIFIED="1398190660844"/>
<node TEXT="MP" ID="ID_1195832988" CREATED="1398190661156" MODIFIED="1398190662250"/>
<node TEXT="Defence" ID="ID_145896124" CREATED="1398190662453" MODIFIED="1398190680078"/>
<node TEXT="Accuracy" ID="ID_41967993" CREATED="1398190665063" MODIFIED="1398190675875"/>
<node TEXT="Damage Range" ID="ID_1589022442" CREATED="1398190488891" MODIFIED="1398190548578">
<node TEXT="HighEnd" ID="ID_1540778730" CREATED="1398190554438" MODIFIED="1398190565531"/>
<node TEXT="LowEnd" ID="ID_254597693" CREATED="1398190558360" MODIFIED="1398190563000"/>
<node TEXT="[low, high] (?)" ID="ID_960234442" CREATED="1398192344875" MODIFIED="1398192356313"/>
</node>
<node TEXT="Speed" ID="ID_1706816308" CREATED="1398191692406" MODIFIED="1398191693969"/>
<node TEXT="Strength (STR)" ID="ID_797716686" CREATED="1398190548938" MODIFIED="1398190576516"/>
<node TEXT="Intelligence (INT)" ID="ID_1579220085" CREATED="1398190576828" MODIFIED="1398190584906"/>
<node TEXT="Wisdom (WIS)" ID="ID_1380806278" CREATED="1398190585219" MODIFIED="1398190590719"/>
<node TEXT="Luck (LUCK)" ID="ID_1714838312" CREATED="1398190590938" MODIFIED="1398190597203"/>
</node>
<node TEXT="methods" ID="ID_816583781" CREATED="1398190804797" MODIFIED="1398190807953">
<node TEXT="getters and setters for data" ID="ID_1547388753" CREATED="1398192452953" MODIFIED="1398192458906"/>
<node TEXT="__init__" ID="ID_1132904586" CREATED="1398197375641" MODIFIED="1398197379547">
<node TEXT="HP" ID="ID_750204962" CREATED="1398190657813" MODIFIED="1398190660844"/>
<node TEXT="MP" ID="ID_1638245190" CREATED="1398190661156" MODIFIED="1398190662250"/>
<node TEXT="Defence" ID="ID_221431175" CREATED="1398190662453" MODIFIED="1398190680078"/>
<node TEXT="Accuracy" ID="ID_707567447" CREATED="1398190665063" MODIFIED="1398190675875"/>
<node TEXT="Damage Range" ID="ID_1122290863" CREATED="1398190488891" MODIFIED="1398190548578">
<node TEXT="HighEnd" ID="ID_707987418" CREATED="1398190554438" MODIFIED="1398190565531"/>
<node TEXT="LowEnd" ID="ID_1395053074" CREATED="1398190558360" MODIFIED="1398190563000"/>
<node TEXT="[low, high] (?)" ID="ID_601922950" CREATED="1398192344875" MODIFIED="1398192356313"/>
</node>
<node TEXT="Speed" ID="ID_1330639762" CREATED="1398191692406" MODIFIED="1398191693969"/>
<node TEXT="Strength (STR)" ID="ID_1604048945" CREATED="1398190548938" MODIFIED="1398190576516"/>
<node TEXT="Intelligence (INT)" ID="ID_1231754799" CREATED="1398190576828" MODIFIED="1398190584906"/>
<node TEXT="Wisdom (WIS)" ID="ID_1339695847" CREATED="1398190585219" MODIFIED="1398190590719"/>
<node TEXT="Luck (LUCK)" ID="ID_1382991754" CREATED="1398190590938" MODIFIED="1398190597203"/>
</node>
<node TEXT="isGreaterThan(Stat)" ID="ID_353663639" CREATED="1398190810235" MODIFIED="1398190824313">
<node TEXT="Compares current stat to other stat to see if certain components are greater than other&apos;s" ID="ID_1891479393" CREATED="1398190825860" MODIFIED="1398190919250"/>
<node TEXT="Only compares STR, INT, WIS, LUCK" ID="ID_691814588" CREATED="1398190874750" MODIFIED="1398190929750"/>
</node>
</node>
</node>
<node TEXT="Character ---" ID="ID_1164193223" CREATED="1396328177406" MODIFIED="1398200466656">
<node TEXT="data" ID="ID_727663927" CREATED="1396328188109" MODIFIED="1396328189578">
<node TEXT="name" ID="ID_508212579" CREATED="1398191878781" MODIFIED="1398191883516"/>
<node TEXT="level" ID="ID_818393406" CREATED="1398191908406" MODIFIED="1398191910297"/>
<node TEXT="inventory" ID="ID_842932592" CREATED="1396328285437" MODIFIED="1398194458203">
<node TEXT="Type: Inventory" ID="ID_1061597151" CREATED="1398194460453" MODIFIED="1398194464594"/>
</node>
<node TEXT="equipment" ID="ID_1968774206" CREATED="1398191747203" MODIFIED="1398194476063">
<node TEXT="Type: Inventory" ID="ID_1199675202" CREATED="1398194460453" MODIFIED="1398194464594"/>
</node>
<node TEXT="skillsInventory (?)" ID="ID_1310006422" CREATED="1398192076422" MODIFIED="1398194472656">
<node TEXT="Type: Inventory" ID="ID_527161917" CREATED="1398194460453" MODIFIED="1398194464594"/>
</node>
<node TEXT="baseStats" ID="ID_214102369" CREATED="1398190705125" MODIFIED="1398194488000">
<node TEXT="Type: Stats" ID="ID_1690820264" CREATED="1398194479735" MODIFIED="1398194484500"/>
</node>
<node TEXT="afterStats" ID="ID_276866063" CREATED="1398190446328" MODIFIED="1398194511688">
<node TEXT="Type: Stats" ID="ID_208059434" CREATED="1398194479735" MODIFIED="1398194484500"/>
<node TEXT="represents stats with equipment." ID="ID_1050885198" CREATED="1398192281360" MODIFIED="1398192301453"/>
</node>
<node TEXT="currentStats" ID="ID_473638663" CREATED="1398190610485" MODIFIED="1398194514391">
<node TEXT="Type: Stats" ID="ID_856102817" CREATED="1398194479735" MODIFIED="1398194484500"/>
<node TEXT="HP" ID="ID_1086018680" CREATED="1398190615063" MODIFIED="1398190617188"/>
<node TEXT="MP" ID="ID_1356849058" CREATED="1398190617406" MODIFIED="1398190618391"/>
</node>
<node TEXT="Position" ID="ID_1430077499" CREATED="1398192724313" MODIFIED="1398194534828">
<node TEXT="Type: Vector" ID="ID_849726749" CREATED="1398194517250" MODIFIED="1398194522047"/>
<node TEXT="Vector(x,y)" ID="ID_1114753426" CREATED="1398398757281" MODIFIED="1398398789406"/>
</node>
<node TEXT="Velocity" ID="ID_1931813885" CREATED="1398192727438" MODIFIED="1398194532219">
<font BOLD="false"/>
<node TEXT="Type: Vector" ID="ID_196903212" CREATED="1398194517250" MODIFIED="1398194522047"/>
<node TEXT="Vector(x,y)" ID="ID_120097419" CREATED="1398398757281" MODIFIED="1398398789406"/>
</node>
<node TEXT="-skills unlocked- (?)" ID="ID_1562196404" CREATED="1396328288078" MODIFIED="1398194544063"/>
<node TEXT="attackDelay (?)" ID="ID_1854575892" CREATED="1398191643578" MODIFIED="1398191660656"/>
</node>
<node TEXT="methods" ID="ID_871166239" CREATED="1396328324781" MODIFIED="1396328327687">
<node TEXT="getters and setters for data" ID="ID_944595559" CREATED="1396328328093" MODIFIED="1396328334656"/>
<node TEXT="__init__" ID="ID_643860830" CREATED="1398191854688" MODIFIED="1398191862078">
<node TEXT="name" ID="ID_1341633370" CREATED="1398191862656" MODIFIED="1398191891688"/>
<node TEXT="level" ID="ID_1341626068" CREATED="1398191891969" MODIFIED="1398191901094"/>
<node TEXT="baseStat" ID="ID_1798883830" CREATED="1398191916610" MODIFIED="1398191922485"/>
<node TEXT="actualStat" ID="ID_1440581148" CREATED="1398191922797" MODIFIED="1398191925641"/>
<node TEXT="skillsUnlocked (?)" ID="ID_44370117" CREATED="1398191927047" MODIFIED="1398192036375"/>
<node TEXT="inventory" ID="ID_813136825" CREATED="1398197256485" MODIFIED="1398197260656"/>
<node TEXT="equipment" ID="ID_1396247696" CREATED="1398197260906" MODIFIED="1398197265172"/>
</node>
<node TEXT="updateStats()" ID="ID_468649279" CREATED="1398190972953" MODIFIED="1398190992360">
<node TEXT="Should be called whenever any item is equipped or used (could be potionlike item)" ID="ID_1328473331" CREATED="1398190993500" MODIFIED="1398191022094"/>
</node>
<node TEXT="attack()" ID="ID_1562155868" CREATED="1398191591375" MODIFIED="1398191596156">
<node TEXT="returns type Attack" ID="ID_133233577" CREATED="1398191596735" MODIFIED="1398191601860"/>
</node>
<node TEXT="mAttack(num)" ID="ID_1578221735" CREATED="1398191608125" MODIFIED="1398191616922">
<node TEXT="returns type Attack" ID="ID_1208301354" CREATED="1398191618016" MODIFIED="1398191624188"/>
</node>
<node TEXT="damage(Attack) (?)" ID="ID_1349426412" CREATED="1398191798297" MODIFIED="1398191828469">
<node TEXT="returns dead or not" ID="ID_1018382261" CREATED="1398191806219" MODIFIED="1398191831516"/>
</node>
</node>
</node>
<node TEXT="Skill ---" ID="ID_260530553" CREATED="1398192707953" MODIFIED="1398200459610">
<node TEXT="data" ID="ID_826378954" CREATED="1398193153578" MODIFIED="1398193155000">
<node TEXT="name" ID="ID_1969125145" CREATED="1398193463828" MODIFIED="1398193465719"/>
<node TEXT="level" ID="ID_524096682" CREATED="1398192761906" MODIFIED="1398192763047"/>
<node TEXT="description" ID="ID_1203038973" CREATED="1398193707953" MODIFIED="1398193712422"/>
<node TEXT="baseStat" ID="ID_535959094" CREATED="1398192763250" MODIFIED="1398192874703"/>
<node TEXT="incrementStat" ID="ID_1016600688" CREATED="1398192737047" MODIFIED="1398192877828"/>
<node TEXT="actualStat" ID="ID_1786057376" CREATED="1398192864844" MODIFIED="1398192880516"/>
<node TEXT="isAttack" ID="ID_1915361029" CREATED="1398192776860" MODIFIED="1398192779531"/>
<node TEXT="isBuff (?)" ID="ID_845883866" CREATED="1398193341078" MODIFIED="1398193356625"/>
<node TEXT="isPassive" ID="ID_1344766698" CREATED="1398192779735" MODIFIED="1398192818469"/>
<node TEXT="timeDelay" ID="ID_1880276237" CREATED="1398192901875" MODIFIED="1398192909860">
<node TEXT="represent time between uses of skill" ID="ID_546449942" CREATED="1398192930406" MODIFIED="1398192940516"/>
<node TEXT="if passive, time is 0" ID="ID_725586015" CREATED="1398193325297" MODIFIED="1398193363266"/>
</node>
<node TEXT="timeLeft" ID="ID_885123518" CREATED="1398193636985" MODIFIED="1398193649110">
<node TEXT="time.time() + timeDelay" ID="ID_1084231489" CREATED="1398193649844" MODIFIED="1398193672813"/>
<node TEXT="only updates when attack used." ID="ID_1315592490" CREATED="1398193663766" MODIFIED="1398193684250"/>
</node>
</node>
<node TEXT="methods" ID="ID_1291717365" CREATED="1398193163250" MODIFIED="1398193165750">
<node TEXT="getters and setters for data" ID="ID_1005520700" CREATED="1398193168360" MODIFIED="1398193240703"/>
<node TEXT="use()" ID="ID_633167048" CREATED="1398193241797" MODIFIED="1398193245110">
<node TEXT="returns Attack" ID="ID_1670858824" CREATED="1398193245844" MODIFIED="1398193251703"/>
</node>
<node TEXT="__init__" ID="ID_104299509" CREATED="1398193266891" MODIFIED="1398193271438">
<node TEXT="name" ID="ID_951960393" CREATED="1398193470453" MODIFIED="1398193472766"/>
<node TEXT="level" ID="ID_1337752366" CREATED="1398193295547" MODIFIED="1398193298078"/>
<node TEXT="description" ID="ID_1417434526" CREATED="1398193718360" MODIFIED="1398193722406"/>
<node TEXT="baseStat" ID="ID_1847603451" CREATED="1398193271891" MODIFIED="1398193278281"/>
<node TEXT="incrementStat" ID="ID_807001619" CREATED="1398193278594" MODIFIED="1398193281406"/>
<node TEXT="isAttack" ID="ID_959263682" CREATED="1398193308172" MODIFIED="1398193311610"/>
<node TEXT="isBuff (?)" ID="ID_844936736" CREATED="1398193347719" MODIFIED="1398193351938"/>
<node TEXT="isPassive" ID="ID_129821124" CREATED="1398193311860" MODIFIED="1398193315969"/>
<node TEXT="timeDelay" ID="ID_915886610" CREATED="1398193317578" MODIFIED="1398193320063"/>
</node>
</node>
</node>
<node TEXT="Attack ---" ID="ID_1216604635" CREATED="1398193536703" MODIFIED="1398200462547">
<node TEXT="data" ID="ID_1188538884" CREATED="1398194284516" MODIFIED="1398194296188">
<node TEXT="name" ID="ID_677272111" CREATED="1398194867641" MODIFIED="1398194868813"/>
<node TEXT="description" ID="ID_1048008961" CREATED="1398194869016" MODIFIED="1398194871453"/>
<node TEXT="timeLength" ID="ID_223899854" CREATED="1398194299688" MODIFIED="1398194643000">
<node TEXT="represents the time (or ticks) that the attack lasts after hitting." ID="ID_947612656" CREATED="1398194767766" MODIFIED="1398194813016"/>
</node>
<node TEXT="base" ID="ID_1753898581" CREATED="1398194682125" MODIFIED="1398194855922">
<node TEXT="[Stats, Attack]" ID="ID_76777751" CREATED="1398194705391" MODIFIED="1398194713438"/>
</node>
<node TEXT="timed" ID="ID_1375090785" CREATED="1398194646750" MODIFIED="1398194853016">
<node TEXT="[Stats, Attack]" ID="ID_713540340" CREATED="1398194667016" MODIFIED="1398194680438"/>
</node>
<node TEXT="isPermanent" ID="ID_905063748" CREATED="1398194758860" MODIFIED="1398194764328"/>
</node>
<node TEXT="methods" ID="ID_1229892296" CREATED="1398194296438" MODIFIED="1398194298125">
<node TEXT="getters and setters" ID="ID_105468738" CREATED="1398194916938" MODIFIED="1398194920985"/>
<node TEXT="__init__" ID="ID_1466958129" CREATED="1398195129672" MODIFIED="1398195133656">
<node TEXT="name" ID="ID_1986701481" CREATED="1398195134485" MODIFIED="1398195142313"/>
<node TEXT="description" ID="ID_167846428" CREATED="1398195142516" MODIFIED="1398195147063"/>
<node TEXT="timeLength" ID="ID_1816398016" CREATED="1398195147297" MODIFIED="1398195153360"/>
<node TEXT="base" ID="ID_239983441" CREATED="1398195153641" MODIFIED="1398195159860"/>
<node TEXT="timed" ID="ID_1841464552" CREATED="1398195160031" MODIFIED="1398195161531"/>
<node TEXT="isPermanent" ID="ID_701636548" CREATED="1398195161719" MODIFIED="1398195166094"/>
</node>
</node>
</node>
</node>
<node TEXT="Data" POSITION="right" ID="ID_141681782" CREATED="1398195242438" MODIFIED="1398195244813">
<edge COLOR="#ff00ff"/>
<node TEXT="Skills" ID="ID_643519406" CREATED="1398195521594" MODIFIED="1398195524156"/>
<node TEXT="Environments" ID="ID_106552043" CREATED="1398195536610" MODIFIED="1398195541625"/>
<node TEXT="Items" ID="ID_1261869933" CREATED="1398398721015" MODIFIED="1398398722765"/>
<node TEXT="Enemies (?)" ID="ID_1782853065" CREATED="1398195543594" MODIFIED="1398195548328"/>
</node>
<node TEXT="Function Classes" POSITION="right" ID="ID_1413081306" CREATED="1396328339015" MODIFIED="1396328344984">
<edge COLOR="#00ff00"/>
<node TEXT="GameIO" ID="ID_362474481" CREATED="1396328345765" MODIFIED="1396328365812">
<node TEXT="methods" ID="ID_6269105" CREATED="1396328369437" MODIFIED="1396328376796">
<node TEXT="loadGame(location)" ID="ID_628635759" CREATED="1396328377593" MODIFIED="1396328387468"/>
<node TEXT="saveGame(location)" ID="ID_1991264855" CREATED="1396328387796" MODIFIED="1396328393859"/>
</node>
</node>
<node TEXT="ImageHandler" ID="ID_143937646" CREATED="1398398708734" MODIFIED="1398398714625"/>
</node>
<node TEXT="Gameplay States" POSITION="right" ID="ID_1980663329" CREATED="1396328121687" MODIFIED="1396328143296">
<edge COLOR="#0000ff"/>
<node TEXT="Main Menu" ID="ID_1065206864" CREATED="1396328133656" MODIFIED="1396328148781"/>
<node TEXT="inGame" ID="ID_484574417" CREATED="1396328144281" MODIFIED="1396328161718"/>
<node TEXT="LoadingWindow." ID="ID_682724536" CREATED="1396330048937" MODIFIED="1396330054421"/>
</node>
<node TEXT="Order" POSITION="right" ID="ID_397522161" CREATED="1399092481481" MODIFIED="1399092484325">
<edge COLOR="#00ffff"/>
<node TEXT="Initiate" ID="ID_1109628383" CREATED="1399092485747" MODIFIED="1399092494950"/>
<node TEXT="Main Menu" ID="ID_1160127023" CREATED="1399092495544" MODIFIED="1399092497481"/>
<node TEXT="Game" ID="ID_262828891" CREATED="1399092497731" MODIFIED="1399092506466"/>
</node>
</node>
</map>
