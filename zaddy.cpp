
#include <iostream>
#include <vector>

int main(int argc, const char* args[]) {

    
    const std::vector<std::string> list = { "hello", "world", "my", "name", "is", "habib" };

    for (auto i = list.begin(); i < list.end(); i++) {
        std::cout << *i;
        std::cout << "\n";
    }

    return 0;
}