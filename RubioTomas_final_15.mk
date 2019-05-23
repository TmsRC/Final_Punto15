RubioTomas_final_15.pdf: datos.dat
	python graficar.py

datos.dat: solucion.x
	./solucion.x
    
solucion.x: solucion.cpp
	c++ solucion.cpp -o solucion.x

clean:
	rm -rf *.x *.dat *.png