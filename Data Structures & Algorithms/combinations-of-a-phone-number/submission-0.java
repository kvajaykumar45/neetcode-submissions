class Solution {
   static HashMap<Character, String> keypad = new HashMap<>();
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if(digits.length() == 0)
            return result;
        keypad.put('1',new String());
        keypad.put('0',new String());
        keypad.put('2',"abc");
        keypad.put('3',"def");
        keypad.put('4',"ghi");
        keypad.put('5',"jkl");
        keypad.put('6',"mno");
        keypad.put('7',"pqrs");
        keypad.put('8',"tuv");
        keypad.put('9',"wxyz");
        generate(digits, 0, new StringBuilder(), result);
        return result;        
    }
    public static void generate(String digits, int index, StringBuilder s, List<String> result )
    {
        if(index == digits.length())
        {
            result.add(s.toString());
            return;
        }
       
        char ch = digits.charAt(index);
        String letters = keypad.get(ch); 
        if(letters.isEmpty())
            generate(digits, index+1, s, result);
        else
        {
        for(int i=0; i<letters.length(); i++)
        {
            s.append(letters.charAt(i));
            generate(digits, index+1, s, result);
            s.deleteCharAt(s.length()-1);
        }  
        }   
    }
}
