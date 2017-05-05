echo > examplesYID.txt

declare -a arr=("oyb ikh zol zayn a malke ikh volt veln az du zolst farbeygn" 
                "mir flegn zingn lider" 
                "tants" 
                "er fleg gevolt du zolst shraybn a bukh"
                "ikh volt tantsn oyb du voltst zingn"   
                "du flegst gehat gegangen"
                "ikh vel hobn gehat an epl")             

for i in "${arr[@]}"
do
    echo "$i" >> examplesYID.txt
    echo >> examplesYID.txt
    python ParsingYID.py $i >> examplesYID.txt
    echo >> examplesYID.txt
    echo >> examplesYID.txt
    echo >> examplesYID.txt
done
