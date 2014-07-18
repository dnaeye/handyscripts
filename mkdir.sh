# list of file names
lc=(8824 7759 8215 8626 8213 8646 8647 8214 8825 8826 8823 7760 7685 7684 7694 8626 8115 8825 5160 5161 7758 5202)

# loop to create folders
for i in "${lc[@]}"; do
	mkdir $i
done
