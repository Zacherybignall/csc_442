import java.lang.reflect.Field;

public class Reflect_modify {
    public static void main(String[] args) throws Exception {

        //Field minTemp = Ship.class.getDeclaredField("MINTEMP");
        int temp;
        try {
            Main main = new Main();
            Field gameField = Main.class.getDeclaredField("game");
            gameField.setAccessible(true);
            Game game = (Game)gameField.get(main);
            game.winner = true;
            game.end = true;
            main.main(null);
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
