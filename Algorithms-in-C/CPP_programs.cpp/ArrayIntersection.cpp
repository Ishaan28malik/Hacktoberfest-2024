#include <iostream>
#include <vector>
#include <unordered_set>

std::vector<int> arrayIntersection(const std::vector<int>& nums1, const std::vector<int>& nums2) {
    std::unordered_set<int> set(nums1.begin(), nums1.end());
    std::vector<int> result;

    for (const int num : nums2) {
        if (set.count(num)) {
            result.push_back(num);
            set.erase(num);
        }
    }

    return result;
}

int main() {
    std::vector<int> nums1 = {1, 2, 2, 1};
    std::vector<int> nums2 = {2, 2};
    
    std::vector<int> result = arrayIntersection(nums1, nums2);
    
    std::cout << "Intersection: ";
    for (int num : result) {
        std::cout << num << " ";
    }
    
    return 0;
}
