# move all files to specific folders based on matching last four characters in filename
for i in Staff_*.csv; do
	filename=$(basename "$i")
	filename="${filename%.*}"
	id=${filename:(-4)}
	mv $i $id
done
