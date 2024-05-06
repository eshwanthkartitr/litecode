class Solution {
public:
    ListNode* removeNodes(ListNode* head) {
        if(head->next == NULL) return head;
        head->next = removeNodes(head->next);
        if(head->next->val > head->val) return head->next;
        else return head;
    }
};