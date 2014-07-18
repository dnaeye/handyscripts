# remove all characters including and after "_" in .csv filenames in current directory
for i in *.csv; do
	filename=$(basename "$i")
	filename="${filename%.*}"
	newFileName=$(echo $filename | sed 's/_.*//')
	mv $i $newFileName.csv
	#mv $i 
done
