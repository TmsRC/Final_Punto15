#include <iostream>
#include <fstream>
using namespace std;

double Ey(double t);
double Ex(double t);

int main() {
    
    ofstream outfile;
    outfile.open("datos.dat");
    
    double q = 2.0;
    double m = 7294.29;
    
    double t = 0;
    double Tmax = 10;
    double dt= 0.1;
    double x = 1;
    double y = 0;
    double vx = 0;
    double vy = 1;
    
    while(t<=Tmax) {
        
        outfile << t << " " << x << " " << y << endl;
        
        t += dt/2;
        x += vx*dt;
        vx += Ex(t)*q/m*dt;
        y += vy*dt;
        vy += Ey(t)*dt;
        t+=dt/2;
    }
    
    outfile.close();
    
    return 0;
}

double Ey(double t) {
    if(t>3 || t<7) {
        return 3.0;
    }
    else {
        return 0;
    }
}

double Ex(double t) {
    return 0;
}