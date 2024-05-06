class Solution {
public:
    ListNode* removeNodes(ListNode* headNode) {
        ListNode* currentNode = headNode;
        stack<ListNode*> nodeStack;

        while (currentNode != nullptr) {
            while (!nodeStack.empty() && nodeStack.top()->val < currentNode->val) {
                nodeStack.pop();
            }
            nodeStack.push(currentNode);
            currentNode = currentNode->next;
        }

        ListNode* nextNodeInNewList = nullptr;
        while (!nodeStack.empty()) {
            currentNode = nodeStack.top();
            nodeStack.pop();
            currentNode->next = nextNodeInNewList;
            nextNodeInNewList = currentNode;
        }

        return currentNode;
    }
};