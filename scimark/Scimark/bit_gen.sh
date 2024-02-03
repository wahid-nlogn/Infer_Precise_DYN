rm log.txt
rm scimark_bits.txt
for f in SOR*
do
	echo "$f"
    echo "$f" >> scimark_bits.txt
    grep '^def ' "$f" > tmp.log
    python3 feature_gen.py >> scimark_bits.txt    
done

