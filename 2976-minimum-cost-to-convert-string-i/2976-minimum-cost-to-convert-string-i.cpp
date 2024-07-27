#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <climits>

using namespace std;

class Solution {
public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        // Graph representation using unordered_map
        unordered_map<char, unordered_map<char, int>> graph;
        
        // Build the graph
        for (int i = 0; i < original.size(); ++i) {
            graph[original[i]][changed[i]] = cost[i];
        }
        
        long long totalCost = 0;
        
        // Process each character
        for (int i = 0; i < source.size(); ++i) {
            if (source[i] == target[i]) {
                continue;
            }
            
            char src = source[i];
            char tgt = target[i];
            
            // Dijkstra's algorithm
            long long possible = LLONG_MAX;
            priority_queue<pair<long long, char>, vector<pair<long long, char>>, greater<pair<long long, char>>> pq;
            unordered_set<char> visited;
            pq.push({0, src});
            
            while (!pq.empty()) {
                auto [currCost, u] = pq.top();
                pq.pop();
                
                if (currCost > possible) {
                    continue;
                }
                
                if (u == tgt) {
                    possible = min(possible, currCost);
                    break;
                }
                
                if (visited.count(u)) {
                    continue;
                }
                
                visited.insert(u);
                
                for (const auto& [v, w] : graph[u]) {
                    if (currCost + w <= possible && !visited.count(v)) {
                        pq.push({currCost + w, v});
                    }
                }
            }
            
            if (possible == LLONG_MAX) {
                return -1;
            }
            
            totalCost += possible;
        }
        
        return totalCost > 0 ? totalCost : -1;
    }
};
