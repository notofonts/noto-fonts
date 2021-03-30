# set terminal pngcairo nocrop enhanced size 600,400 font ",8"
set datafile separator ","
set output '12-month-data.png'
set title "Noto Issues Last 12 Month" font ",20"
set key left box
set term png
set timefmt '%Y-%m-%d'
set boxwidth 0.8 absolute
set xtics rotate
set border 1
set style fill solid 1.00 border lt -1
set style histogram clustered gap 1 title textcolor lt -1
set style data histograms
set xtics border scale 1,0 nomirror autojustify norangelimit
set ylabel "Issues" 
set xlabel 'Time'
unset ytics

set key off auto columnheader
set key left box
set yrange [0:*]
set offset 0,0,graph 0.05,0

set linetype 1 lc rgb '#9d9e9f'
set linetype 2 lc rgb '#2a3990'

absoluteBoxwidth = 0.8
dx = 1/6.0 * (1 - absoluteBoxwidth)/2.0

plot 'googlefonts.noto-fonts.12month-data.csv' using 2:xtic(1),\
         '' u 3,\
         '' u ($0 - dx):2:2 with labels right offset 0,1 ,\
         '' u ($0 + dx):3:3 with labels left offset 0,1