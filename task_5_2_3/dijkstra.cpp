#include <cassert>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <set>

using vertex_t = size_t;
using weight_t = int;
using incidence_list_t = std::unordered_map<vertex_t, weight_t>;
using graph_t = std::unordered_map<vertex_t, incidence_list_t>;
using distance_storage_t = std::unordered_map<vertex_t, weight_t>;
using vertex_queue_t = std::set<std::pair<weight_t, vertex_t>>;

template <typename T>
T read_value(std::istream& in) {
    auto value = T{};
    in >> value;
    return  value;
}

graph_t read_graph(std::istream& in) {
    auto graph = graph_t{};
    auto vertex_count = read_value<size_t>(in);
    for (auto vertex = vertex_t{1}; vertex <= vertex_count; ++vertex) {
        graph[vertex] = incidence_list_t{};
    }
    auto edge_count = read_value<size_t>(in);
    for (auto idx = size_t{0}; idx < edge_count; ++idx) {
        vertex_t u = read_value<vertex_t>(in);
        vertex_t v = read_value<vertex_t>(in);
        weight_t w = read_value<weight_t>(in);
        graph[u][v] = w;
    }
    return graph;
}

void read_input(std::istream& in, graph_t& graph, vertex_t& source, vertex_t& target) {
    graph = read_graph(in);
    source = read_value<vertex_t>(in);
    target = read_value<vertex_t>(in);
}

int find_shortest_distance(const graph_t& graph, const vertex_t source, const vertex_t target) {
    auto distances = distance_storage_t{};
    const auto inf = std::numeric_limits<weight_t>::max();
    for (const auto& item : graph) {
        const auto& vertex = item.first;
        distances[vertex] = inf;
    }
    auto isource = distances.find(source);
    assert(isource != distances.end());
    isource->second = 0;
    auto vertex_queue = vertex_queue_t{};
    vertex_queue.insert({0, source});
    while (!vertex_queue.empty()) {
        const auto u_vq_it = vertex_queue.begin();
        const auto u_dist = u_vq_it->first;
        const auto u = u_vq_it->second;
        vertex_queue.erase(u_vq_it);
        auto u_g_it = graph.find(u);
        assert(u_g_it != graph.end());
        for (const auto& neighbour : u_g_it->second) {
            const auto v = neighbour.first;
            const auto uv_weight = neighbour.second;
            const auto v_d_it = distances.find(v);
            assert(v_d_it != distances.end());
            const auto v_dist = v_d_it->second;
            const auto alt_dist = u_dist + uv_weight;
            if (alt_dist < v_dist) {
                if (v_dist != inf) {
                    const auto v_vq_it = vertex_queue.find({v_dist, v});
                    assert(v_vq_it != vertex_queue.end());
                    vertex_queue.erase(v_vq_it);
                }
                v_d_it->second = alt_dist;
                vertex_queue.insert({alt_dist, v});
            }
        }
    }
    const auto t_d_it = distances.find(target);
    assert(t_d_it != distances.end());
    return t_d_it->second == inf ? -1 : static_cast<int>(t_d_it->second);
}

int main() {
    auto graph = graph_t{};
    auto source = vertex_t{};
    auto target = vertex_t{};
    read_input(std::cin, graph, source, target);
    auto shortest_distance = find_shortest_distance(graph, source, target);
    std::cout << shortest_distance << '\n';
    return 0;
}
