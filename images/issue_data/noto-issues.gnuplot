set xdata time
set key left box
set timefmt '%Y-%m-%d'
set datafile separator ","
set grid
set term png
set xtics rotate
set ylabel "Issues" 
set xlabel 'Time'
set title "Noto Monthly Issues" font ",20"
set output 'periodic-data.png'
plot 'googlefonts.noto-fonts.periodic-data.csv' using 1:2 title column with lines lw 3 lc rgb '#9d9e9f', 'googlefonts.noto-fonts.periodic-data.csv' using 1:3 title column with lines lw 3 lc rgb '#2a3990'
set title "Noto Cumulative Issues" font ",20"
set output 'cumulative-data.png'
plot 'googlefonts.noto-fonts.cumulative-data.csv' using 1:2 title column with lines lw 3 lc rgb '#9d9e9f', 'googlefonts.noto-fonts.cumulative-data.csv' using 1:3 title column with lines lw 3 lc rgb '#2a3990', 'googlefonts.noto-fonts.cumulative-data.csv' using 1:4 title column with lines lw 3 lc rgb 'green'
