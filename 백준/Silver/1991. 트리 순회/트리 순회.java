import java.io.*;
import java.util.*;

public class Main {

  static Map<Character, Character[]> map = new HashMap<>();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());

    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      char parent = st.nextToken().charAt(0);
      char left = st.nextToken().charAt(0);
      char right = st.nextToken().charAt(0);
      map.put(parent, new Character[]{left, right});
    }

    StringBuilder preorder = new StringBuilder();
    StringBuilder inorder = new StringBuilder();
    StringBuilder postorder = new StringBuilder();

    dfs('A', preorder, inorder, postorder);
    System.out.println(preorder);
    System.out.println(inorder);
    System.out.println(postorder);
  }

  public static void dfs(char key, StringBuilder preorder, StringBuilder inorder, StringBuilder postorder) {
    char left = map.get(key)[0];
    char right = map.get(key)[1];

    preorder.append(key);   // 전위 탐색

    if (left != '.')
      dfs(left, preorder, inorder, postorder);
    inorder.append(key);    // 중위 탐색

    if (right != '.')
      dfs(right, preorder, inorder, postorder);
    postorder.append(key);  // 후위 탐색
  }
}
