echo > examplesSP.txt

declare -a arr=("estoy estudiando" 
                "debería estudiar" 
                "quiero que vengas" 
                "habéis viajado a Barcelona ?"   
                "había caminado"
                "he visitado a Iñaki"
                "vení")             

for i in "${arr[@]}"
do
    echo "$i" >> examplesSP.txt
    echo >> examplesSP.txt
    python ParsingSP.py $i >> examplesSP.txt
    echo >> examplesSP.txt
    echo >> examplesSP.txt
    echo >> examplesSP.txt
done
