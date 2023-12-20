#include <iostream>
#include <cmath>

// function f
int f(int N) {
    return (int)(std::ceil(std::sqrt(N))) * (int)(std::ceil(std::sqrt(N))) 
           - (int)(std::floor(std::sqrt(N))) * (int)(std::floor(std::sqrt(N)));
}

int main() {
    // Answer
    int ans = 1;
    // Calculate result
    int num = 0;
    // Limit
    int N = 100000;

    // Calculation
    while (true) {
        num += f(ans);
        if (num >= N) {
            break;
        }
        ans++;
    }

    // Output
    std::cout << "ans is: " << ans << std::endl;

    return 0;
}