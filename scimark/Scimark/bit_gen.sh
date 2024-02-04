rm scimark_types.txt
for f in SOR*
do
  echo "$f"
  echo "$f" >> scimark_types.txt
  grep '^def ' "$f" > tmp.log
  python3 Extract_Type_info.py >> scimark_types.txt
done
