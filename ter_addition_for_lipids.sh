#!/bin/bash

input_file="$1"
output_file="$2"

awk '
{
    if (prev_line != "" && $0 ~ /^HETATM/ && prev_line ~ /^HETATM/ && substr(prev_line, 18, 2) == "OL" && substr($0, 18, 2) == "PA") {
        print prev_line
        print "TER"
    } else if (prev_line != "") {
        print prev_line
    }
    prev_line = $0
}
END {
    if (prev_line != "") {
        print prev_line
    }
}' "$input_file" > "$output_file"

