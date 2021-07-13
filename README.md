# Monopoly_Chance_Calculator
Generates a heat map of a Monopoly board depending on the probability of a piece to land there and also a priority system on which properties to focus on.

The Priority number is the <b>EXPECTED</b> number of turns required for the player to gain back all the money he spent on buying that 
particular property incliding whatever is built on it --- <i>hence it is an indication of how quickly the player will make profit 
out of a property.</i>

Additionally the double Priority numbers are for when a player owns all properties of a street which doubles the rent for them.

The probabilities are found with the assumption that there are 10 players that were allowed to mix well enough.
Thus these probabilities show the chances of finding one of the 10 players on each tile when you look at any random 
(well mixed) round.

These data are in theory able to be used to create a win all strategy but up until now they have been used to precissely
predict the winner of a game well before any intuitive signs showed up indicating towards that players victory.

<h2>Results</h2>

PRIORITY NUMBERS
<#     PROPERTY            1 HOUSE             2 HOUSES            3 HOUSES            4 HOUSES            HOTEL>
1     [1535.1934046973486, 562.9042483890279, 272.9232719461953, 119.40393147646046, 83.15630942110639, 63.45466072749041]
3     [757.4152428272369, 277.71892236998684, 134.6515987248421, 58.91007444211843, 41.02665898647533, 34.784996337250874]
6     [872.4075674896897, 261.72227024690693, 116.32100899862529, 48.46708708276054, 39.258340537036034, 33.310107122333605]
8     [878.4947114055012, 263.54841342165037, 117.13262818740016, 48.80526174475007, 39.53226201324755, 33.54252534457368]
9     [793.2309756652262, 224.74877643848077, 116.34054309756651, 47.593858539913576, 37.60502403153665, 32.610606777348195]
11    [738.7628471055999, 253.29011900763427, 119.60922286471619, 51.59613535340698, 45.59222142137417, 45.02935449024609]
13    [662.772700064744, 227.23635430791222, 107.30605620095854, 46.28888698864878, 40.9025437754242, 40.39757409918439]
14    [596.0990428726894, 193.73218893362403, 89.41485643090341, 41.13083395821556, 42.21501983460571, 32.78544735799792]
16    [518.1058245071971, 161.18847873557243, 76.56452739939691, 35.16839536048853, 31.163105888877332, 28.844254089523485]
18    [503.14285714285717, 156.53333333333336, 74.35333333333334, 34.152727272727276, 30.263111111111115, 28.011228070175438]
19    [498.15249322149515, 149.44574796644852, 72.45854446858111, 33.21016621476634, 29.889149593289705, 27.896539620403725]
21    [504.72966268960323, 169.77270472286654, 85.89581168681248, 39.52623202621178, 38.700310759992426, 38.14969658251287]
23    [522.415612745098, 175.72161519607843, 88.9056388235294, 40.91124863445378, 40.05638672268907, 39.4864787815126]
24    [500.83271647706266, 162.77063285504536, 75.1249074715594, 38.39717492990813, 37.90085421988582, 37.5624537357797]
26    [487.9369289590424, 153.88780067169802, 70.06273851719584, 36.64218668432809, 36.417225624872124, 36.2607309748158]
27    [490.0828350562265, 154.56458644080988, 70.37086862345815, 36.80333597874162, 36.57738555922605, 36.42020265869348]
29    [492.5613259106738, 151.28669295827842, 68.02037357814068, 36.25913626031515, 36.24702161405377, 36.23844040628529]
31    [490.9585908828322, 163.65286362761074, 76.37133635955168, 42.54974454317879, 42.54974454317878, 43.384053259711706]
32    [507.986540056353, 169.328846685451, 79.02012845321048, 44.02550013821726, 44.02550013821726, 44.88874523896662]
34    [534.0625895401591, 161.99898549384827, 74.76876253562227, 42.99203845798281, 43.61511147911299, 44.06016363706312]
37    [527.9729159003283, 165.93434499724606, 79.19593738504926, 45.59766091866472, 46.705296406567506, 47.51756243102955]
39    [413.6802693554772, 155.13010100830394, 68.9467115592462, 30.392674673699137, 36.501200237247986, 36.19702356860425]

PRIORITY NUMBERS WITH DOUBLE GAINS
<#     PROPERTY            1 HOUSE             2 HOUSES            3 HOUSES            4 HOUSES            HOTEL>
1     [767.5967023486743, 281.45212419451394, 136.46163597309766, 59.70196573823023, 41.57815471055319, 31.727330363745207]
3     [378.7076214136184, 138.85946118499342, 67.32579936242105, 29.455037221059214, 20.513329493237666, 17.392498168625437]
6     [436.2037837448448, 130.86113512345347, 58.160504499312644, 24.23354354138027, 19.629170268518017, 16.655053561166802]
8     [439.2473557027506, 131.77420671082518, 58.56631409370008, 24.402630872375035, 19.766131006623777, 16.77126267228684]
9     [396.6154878326131, 112.37438821924039, 58.170271548783255, 23.796929269956788, 18.802512015768325, 16.305303388674098]
11    [369.38142355279996, 126.64505950381714, 59.804611432358094, 25.79806767670349, 22.796110710687085, 22.514677245123046]
13    [331.386350032372, 113.61817715395611, 53.65302810047927, 23.14444349432439, 20.4512718877121, 20.198787049592195]
14    [298.0495214363447, 96.86609446681202, 44.707428215451706, 20.56541697910778, 21.107509917302856, 16.39272367899896]
16    [259.05291225359855, 80.59423936778622, 38.282263699698454, 17.584197680244266, 15.581552944438666, 14.422127044761742]
18    [251.57142857142858, 78.26666666666668, 37.17666666666667, 17.076363636363638, 15.131555555555558, 14.005614035087719]
19    [249.07624661074757, 74.72287398322426, 36.229272234290555, 16.60508310738317, 14.944574796644853, 13.948269810201863]
21    [252.36483134480162, 84.88635236143327, 42.94790584340624, 19.76311601310589, 19.350155379996213, 19.074848291256433]
23    [261.207806372549, 87.86080759803922, 44.4528194117647, 20.45562431722689, 20.028193361344535, 19.7432393907563]
24    [250.41635823853133, 81.38531642752268, 37.5624537357797, 19.198587464954066, 18.95042710994291, 18.78122686788985]
26    [243.9684644795212, 76.94390033584901, 35.03136925859792, 18.321093342164044, 18.208612812436062, 18.1303654874079]
27    [245.04141752811324, 77.28229322040494, 35.185434311729075, 18.40166798937081, 18.288692779613026, 18.21010132934674]
29    [246.2806629553369, 75.64334647913921, 34.01018678907034, 18.129568130157576, 18.123510807026886, 18.119220203142646]
31    [245.4792954414161, 81.82643181380537, 38.18566817977584, 21.274872271589395, 21.27487227158939, 21.692026629855853]
32    [253.9932700281765, 84.6644233427255, 39.51006422660524, 22.01275006910863, 22.01275006910863, 22.44437261948331]
34    [267.03129477007957, 80.99949274692413, 37.384381267811136, 21.496019228991404, 21.807555739556495, 22.03008181853156]
37    [263.98645795016415, 82.96717249862303, 39.59796869252463, 22.79883045933236, 23.352648203283753, 23.758781215514777]
39    [206.8401346777386, 77.56505050415197, 34.4733557796231, 15.196337336849568, 18.250600118623993, 18.098511784302126]

