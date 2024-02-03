
#rm log.txt
rm sor_bits.txt
for f in SOR*
do
	echo "$f"
    echo "$f" >> sor_bits.txt
    grep '^def ' "$f" > tmp.log
    python3 retic.py >> sor_bits.txt    
done
