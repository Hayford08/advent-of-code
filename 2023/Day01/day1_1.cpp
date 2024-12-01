#include <iostream>
#include <fstream>

using namespace std;

int main(){
    freopen("input.txt", "r", stdin);
    string tmp;
    int ans = 0;
    while (getline(cin, tmp)){
        int first = -1;
        int last = -1;
        for (char c : tmp){
            if ('0' <= c && c <= '9'){
                int val = c - '0';
                if (first == -1){
                    first = val;
                }
                last = val;
            }
        }
        ans += first * 10 + last;
    }
    cout << ans << "\n";
}