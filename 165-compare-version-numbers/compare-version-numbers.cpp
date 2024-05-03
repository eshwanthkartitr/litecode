#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int compareVersion(string version1, string version2) {
        vector<int> v1 = parse(version1);
        vector<int> v2 = parse(version2);

        // Handle empty version strings
        if (v1.empty() && v2.empty()) {
            return 0; // Both versions are empty, consider them equal
        } else if (v1.empty()) {
            return -1; // version1 is empty, version2 is non-empty, so version1 is smaller
        } else if (v2.empty()) {
            return 1; // version2 is empty, version1 is non-empty, so version1 is larger
        }

        // Compare version parts
        int minSize = min(v1.size(), v2.size());
        for (int i = 0; i < minSize; ++i) {
            if (v1[i] < v2[i]) {
                return -1;
            } else if (v1[i] > v2[i]) {
                return 1;
            }
        }

        
        if (v1.size() > v2.size()) {
            for (int i = minSize; i < v1.size(); ++i) {
                if (v1[i] > 0) {
                    return 1; // version1 has a non-zero part, so it is larger
                }
            }
        } else if (v2.size() > v1.size()) {
            for (int i = minSize; i < v2.size(); ++i) {
                if (v2[i] > 0) {
                    return -1; 
                }
            }
        }

        return 0; 
    }

private:
    vector<int> parse(const string& version) {
        vector<int> result;
        size_t start = 0;
        for (size_t i = 0; i <= version.size(); ++i) {
            if (i == version.size() || version[i] == '.') {
                if (i != start) {
                    result.push_back(stoi(version.substr(start, i - start)));
                }
                start = i + 1;
            }
        }
        return result;
    }
};