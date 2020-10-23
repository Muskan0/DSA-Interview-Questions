# https://leetcode.com/problems/symmetric-tree/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSymmetric(TreeNode root) {
        // iterative version
        Queue<TreeNode> q= new LinkedList();
        q.add(root);
        q.add(root);
        while(!q.isEmpty()){
            TreeNode v1=q.poll();
            TreeNode v2=q.poll();
            if(v1==null && v2==null)
                continue;
            if(v1==null || v2==null)
                return false;
            if (v1.val!=v2.val)
                return false;
            q.add(v1.right);
            q.add(v2.left);
            q.add(v1.left);
            q.add(v2.right);
        }
        return true;
    }
}
