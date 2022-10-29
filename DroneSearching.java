import java.util.*;
import java.awt.*;
import javax.swing.*;

public class DroneSearching extends JFrame {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        System.out.println("We will testing drones out today!");
        System.out.println("The map will be 95 units in size.");

        Scanner scan = new Scanner(System.in);
        JFrame frame = new JFrame("Map");
        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout());
        // JLabel label = new JLabel("JFrame Example");
        JTextArea text = new JTextArea("Drones and Disasters Simulation Field\n");
        JButton button = new JButton();

        button.setText("Button");
        panel.add(text);
        frame.add(panel);
        frame.setSize(200, 300);
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);

        char mapSize = 95 + 2;
        char[][] map = new char[mapSize][mapSize];

        // Environment creation

        makeMap(map, mapSize);

        populateMap(map, mapSize);

        searchMap(map, 1, mapSize / 2);

        printMap(map, mapSize);
        text.append(returnMap(map, mapSize));
    }

    // Map creation
    public static void makeMap(char[][] map, int mapSize) {
        for (int i = 0; i < mapSize; i++) {
            map[i][0] = '#';
        }

        for (int j = 0; j < mapSize; j++) {
            map[0][j] = '#';
        }

        for (int i = 0; i < mapSize; i++) {
            map[i][mapSize - 1] = '#';
        }

        for (int j = 0; j < mapSize; j++) {
            map[mapSize - 1][j] = '#';
        }

        for (int i = 1; i < mapSize - 1; i++) {
            for (int j = 1; j < mapSize - 1; j++) {
                map[i][j] = '-';
            }
        }
    }

    // Obstacle population
    public static void populateMap(char[][] map, int mapSize) {
        Random random = new Random();

        for (int i = 1; i < mapSize - 1; i++) {
            for (int j = 1; j < mapSize - 1; j++) {
                int chance = random.nextInt(101);

                if (chance < 25) {
                    map[i][j] = '|';
                }
            }
        }

        // Drone insertion

        map[0+1][mapSize / 2] = 'D';

        // Place people in someplace

        map[mapSize / 2][mapSize / 2] = 'P';
    }

    // Searching algorithm
    public static void searchMap(char[][] map, int i, int j) {
        char current = map[i][j];

        while (current != 'P') {
            char left = map[i][j - 1];
            char up = map[i - 1][j];
            char right = map[i][j + 1];
            char down = map[i + 1][j];

            if (left != '#' || left != '|')
            {
                searchMap(map, i, j - 1);
            }
            if (up != '#' || up != '|')
            {
                searchMap(map, i - 1, j);
            }
            if (right != '#' || right != '|')
            {
                searchMap(map, i, j + 1);
            }
            if (down != '#' || down != '|')
            {
                searchMap(map, i + 1, j);
            }
            /*char upleft = map[i - 1][j - 1];
            char upright = map[i - 1][j + 1];
            char downleft = map[i + 1][j - 1];
            char downright = map[i + 1][j + 1];*/

            break;
        }

        if (current == 'P')
        {
            System.out.println("Found person!");
        }
    }

    // Map printing
    public static void printMap(char[][] map, int mapSize) {
        for (int i = 0; i < mapSize; i++) {
            for (int j = 0; j < mapSize; j++) {
                System.out.print(map[i][j]);
            }
            System.out.println();
        }
    }

    // Returns map in string
    public static String returnMap(char[][] map, int mapSize) {
        String mapText = "";

        for (int i = 0; i < mapSize; i++) {
            for (int j = 0; j < mapSize; j++) {
                mapText += map[i][j];
            }
            mapText += "\n";
        }

        return mapText;
    }
}