#! /bin/bash -
script_base="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
real_dirname="image_files"
link_dirname="images"

pushd () {
    command pushd "$@" > /dev/null
}

popd () {
    command popd "$@" > /dev/null
}

mkdir -p "$script_base"/"$link_dirname"
pushd "$script_base"/"$link_dirname"
mkdir -p "ALL" "DEFAULT" "FIFO" "FIFO READ" "FIFO WRITE" "SINGLE" "SINGLE READ" "SINGLE WRITE" "TYPE1" "TYPE2" "SPEED_10" "SPEED_11" "SPEED_12" "SPEED_13" "SPEED_14" "SPEED_20" "FIFO READ TYPE1" "FIFO WRITE TYPE1"
rm -f {DEFAULT,SINGLE*,FIFO*,ALL,TYPE*,SPEED_*}/*
popd

for wave in "${script_base}"/"${real_dirname}"/* ; do
    if [ -d "$wave" ]; then
	echo "Processing" "$(basename "$wave")"
	convert "$wave/$(basename "$wave").png" -background Khaki -pointsize 25 label:"$(echo "$(cat "$wave/trans.txt")")" -gravity West -append "$wave/$(basename "$wave")_trans.png"

	pushd "${script_base}/${link_dirname}/ALL"
	ln -s "../../${real_dirname}/$(basename "$wave")/$(basename "$wave")_trans.png" "$(basename "$wave").png"
	popd

	for category in "${script_base}"/"${link_dirname}"/* ; do
	    if [ -d "$category" ]; then
		if grep -q "$(basename "$category")" "$wave/trans.txt"; then
		    pushd "$category"
		    ln -s "../../${real_dirname}/$(basename "$wave")/$(basename "$wave")_trans.png" "$(basename "$wave").png"
		    popd
		fi
	    fi
	done
    fi
done
