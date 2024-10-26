class RedBlackTree {
    private static final boolean RED = true;
    private static final boolean BLACK = false;

    # Внутренний класс для узла дерева
    private class Node {
        int data;
        Node left, right;
        boolean color; // Цвет узла: RED или BLACK

        Node(int data) {
            this.data = data;
            this.color = RED; // Новая нода всегда красная
        }
    }

    private Node root;

    # Метод для добавления нового элемента
    public void insert(int data) {
        root = insert(root, data);
        root.color = BLACK; // Корень всегда черный
    }

    # Рекурсивный метод вставки
    private Node insert(Node node, int data) {
        if (node == null) {
            return new Node(data);
        }

        if (data < node.data) {
            node.left = insert(node.left, data);
        } else if (data > node.data) {
            node.right = insert(node.right, data);
        }

        # Балансировка дерева после вставки
        if (isRed(node.right) && !isRed(node.left)) {
            node = rotateLeft(node); // Малый левый поворот
        }
        if (isRed(node.left) && isRed(node.left.left)) {
            node = rotateRight(node); // Малый правый поворот
        }
        if (isRed(node.left) && isRed(node.right)) {
            flipColors(node); // Смена цвета
        }

        return node;
    }

    # Малый левый поворот
    private Node rotateLeft(Node h) {
        Node x = h.right;
        h.right = x.left;
        x.left = h;
        x.color = h.color;
        h.color = RED;
        return x;
    }

    # Малый правый поворот
    private Node rotateRight(Node h) {
        Node x = h.left;
        h.left = x.right;
        x.right = h;
        x.color = h.color;
        h.color = RED;
        return x;
    }

    # Смена цветов (flip colors)
    private void flipColors(Node h) {
        h.color = RED;
        h.left.color = BLACK;
        h.right.color = BLACK;
    }

    # Проверка, является ли узел красным
    private boolean isRed(Node node) {
        if (node == null) return false;
        return node.color == RED;
    }

    # Метод для печати дерева (in-order обход)
    public void printTree() {
        printTree(root);
    }

    private void printTree(Node node) {
        if (node != null) {
            printTree(node.left);
            System.out.println(node.data + " (" + (node.color ? "RED" : "BLACK") + ")");
            printTree(node.right);
        }
    }

    public static void main(String[] args) {
        RedBlackTree tree = new RedBlackTree();
        
        // Вставка элементов
        tree.insert(10);
        tree.insert(20);
        tree.insert(30);
        tree.insert(15);
        tree.insert(25);
        
        // Печать дерева
        tree.printTree();
    }
}
