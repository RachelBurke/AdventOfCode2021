import java.io.*; 
import java.util.*;

public class Day2Code1
{
    public static void main(String[] args) {
    
        ArrayList<String> list = new ArrayList<String>();
            
        try {
            FileInputStream fStream = new FileInputStream("Day2Input.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fStream));
            
            String strLine;
            
            while ((strLine = br.readLine()) != null)   {
            list.add(strLine);
            }
            
            fStream.close();
        } catch (Exception e) {
            System.err.println("Error while reading file: " + e.getMessage());
        }
            
        int depth = 0;
        int horizontal = 0;
        
        if (list.size() > 0) {
            for(String str : list) {
                String[] direction = str.split(" ");
                if(direction[0].equals("forward")) {
                    horizontal += Integer.parseInt(direction[1]);
                } else if(direction[0].equals("down")) {
                    depth += Integer.parseInt(direction[1]);
                } else if(direction[0].equals("up")) {
                    depth -= Integer.parseInt(direction[1]);
                }
            }
        }
        System.out.println("Depth: " + depth); // 777
        System.out.println("Horizontal: " + horizontal); // 1878
        System.out.println("Product: " + depth * horizontal); // 1459206
    }
}
