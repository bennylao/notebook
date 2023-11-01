package LeetCode;

/*
LeetCode Problem 101
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

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
class SymmetricTree {
    public static boolean isSymmetric(TreeNode root) {
        List<TreeNode> NodesInCurrentLayer = new ArrayList<>();
        List<TreeNode> NodesInPreviousLayer = new ArrayList<>();
        NodesInPreviousLayer.add(root);
        NodesInCurrentLayer.add(root);
        while(!NodesInCurrentLayer.stream().allMatch(Objects::isNull)) {
            NodesInPreviousLayer = new ArrayList<>(NodesInCurrentLayer);
            NodesInCurrentLayer = new ArrayList<>();
            for (TreeNode node : NodesInPreviousLayer) {
                if (node == null) {
                    continue;
                }
                NodesInCurrentLayer.add(node.left);
                NodesInCurrentLayer.add(node.right);
            }
            int numberOfNodes = NodesInCurrentLayer.size();

            for (int i = 0; i < numberOfNodes / 2; i++) {
                if (NodesInCurrentLayer.get(i) == null || NodesInCurrentLayer.get(numberOfNodes - i - 1) == null) {
                    if (!(NodesInCurrentLayer.get(i) == null && NodesInCurrentLayer.get(numberOfNodes - i - 1) == null)) {
                        return false;
                    }

                } else if (NodesInCurrentLayer.get(i).val != NodesInCurrentLayer.get(numberOfNodes - i - 1).val) {
                    return false;
                }
            }

        }

        return true;
    }

    public static void main(String[] args) {
        TreeNode n3 = new TreeNode(3);
        TreeNode n21 = new TreeNode(2, null, n3);
        TreeNode n22 = new TreeNode(2, null, n3);
        TreeNode root = new TreeNode(1, n21, n22);


        System.out.println(SymmetricTree.isSymmetric(root));
    }
}