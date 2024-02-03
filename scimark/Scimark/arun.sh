echo ------------------------------ >> log.txt
echo -----"Tests started on " >> log.txt
echo -----$(date +"%D--%T") >> log.txt

for f in SOR*.py
do
if [[ "$f" < "$1" ]]; then
    echo "$f", already tested, skipped
    continue
else
    echo "$f"
    tm=`retic --guarded "$f"`
    echo "$tm"
    echo "$f" >> log.txt
    echo "$tm" >> log.txt
fi
done






