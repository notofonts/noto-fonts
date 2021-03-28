set xdata time
set timefmt '%Y-%m-%d'
set datafile separator ","
set grid
set term png
set xtics rotate
set ylabel "Issues" 
set xlabel 'Time'
set title "Noto Monthly Issues" font ",20"
set output 'periodic-data.png'
plot 'periodic-data.csv' using 1:2 title column with lines, 'periodic-data.csv' using 1:3 title column with lines
set title "Noto Cumulative Issues" font ",20"
set output 'cumulative-data.png'
plot 'cumulative-data.csv' using 1:2 title column with lines, 'cumulative-data.csv' using 1:3 title column with lines

