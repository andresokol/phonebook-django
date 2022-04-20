# Telnet

```
telnet andresokol.github.io 80

GET /art/ HTTP/1.1
Host: andresokol.github.io
Accept: text/html

GET /art/1-whale.png
Host: andresokol.github.io
```


```
nc -l 8000

```

# Apache Benchmark

```
ab -n 500 -g load_500.dat http://127.0.0.1:8000/
ab -n 500 -c 10 -g load_500_10.dat http://127.0.0.1:8000/
```

```
set size 1,0.7
set grid y
set xlabel "request"
set ylabel "response time (ms)"

cd 'D:\practicum'
plot "load_500.dat" using 9 smooth sbezier with lines title "load 500" lw 4

plot "load_500.dat" using 9 smooth sbezier with lines title "load 500" lw 4, "load_500_10.dat" using 9 smooth sbezier with lines title "load 500-10" lw 4
```