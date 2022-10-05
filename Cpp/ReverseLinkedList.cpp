// Problem No. 206
// Question : https://leetcode.com/problems/reverse-linked-list/description/

// Solution :

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
     ListNode* reverseList(ListNode* head) {
        struct ListNode *p=head,*q=head,*temp;
    if((head==NULL) || (head->next==NULL)){
        return head;
    }int f=0;
    p=p->next;
    temp=p;
    while(temp!=NULL){
        temp=p->next;
        p->next=q;
        if(f==1){
            head=p;
        }
        if(f==0){
            q->next=NULL;
            f=1;
            head=p;
        }
        q=p;
        p=temp;
    }
    return head;
        
    }
};

