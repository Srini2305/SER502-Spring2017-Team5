/**
 * 
 */
package compiler;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.Stack;

/**
 * @author pankajsingh
 *
 */
public class ReservedKeywords {
	private static Set<String> operations=new HashSet<String>();
	private static Set<String> reservWords=new HashSet<String>();
	private static Stack<Integer> intStack=new Stack<Integer>();
	private static Stack<Boolean> booleanStack=new Stack<Boolean>(); 
	private static Map<String,Integer> intSymbols=new HashMap<String,Integer>();
	private static Map<String,Boolean> boolSymbols=new HashMap<String,Boolean>();
	private static String keyINT="INT";
	private static String keyBOOL="BOOL";
	private static String top="TOP";
	private static String topb="TOPB";
	public static void init()
	{
		operations.add("START");
		operations.add("STOP");
		operations.add("PRINT");
		operations.add("BEGIN");
		operations.add("END");
		operations.add("ASSN");
		operations.add("DEC");
		
		//Arithmetic Operations
		
		operations.add("ADD");
		operations.add("SUB");
		operations.add("MUL");
		operations.add("DIV");
		operations.add("MOD");
		
		//Adding boolean operators
		operations.add("AND");
		operations.add("OR");
		
		//Adding comparison operators
		operations.add("EQL");
		operations.add("SML");
		operations.add("GTR");
		operations.add("SMLEQL");
		operations.add("GRTEQL");
		operations.add("NOTEQL");
		
		//Adding branching statements
		operations.add("IF");
		operations.add("ELSE");
		operations.add("LOOP");
		operations.add("GOTO");
		
		//Adding reserved Words
		reservWords.add("INT");
		reservWords.add("BOOL");
	}
	public static int getTop() {
		return intStack.pop();
	}
	public static void setTop(int top) {
		intStack.push(top);
	}
	public static boolean getTopb() {
		return booleanStack.pop();
	}
	public static void setTopb(boolean topb) {
		booleanStack.push(topb);
	}
	public static boolean isOperation(String opr)
	{
		return operations.contains(opr);
	}
	public static void addVariable(String var, String type) throws Exception
	{
		if(isKeyWord(var))
		{
			throw new Exception("Variable name is a reserved keyword");
		}
		if(isAlreadyDeclared(var))
		{
			throw new Exception("Variable "+var+" is already declared");
		}
		if(keyINT.equals(type))
		{
			intSymbols.put(var, 0);
		}
		else if(keyBOOL.equals(type))
		{
			boolSymbols.put(var,false);
		}
	}
	private static boolean isAlreadyDeclared(String var) {
		// TODO Auto-generated method stub
		return intSymbols.containsKey(var)||boolSymbols.containsKey(var);
	}
	private static boolean isKeyWord(String var) {
		// TODO Auto-generated method stub
		return (isOperation(var)||isReserved(var));
	}
	private static boolean isReserved(String var) {
		// TODO Auto-generated method stub
		return false;
	}
	public static boolean isINT(String var)
	{
		return intSymbols.containsKey(var);
	}
	public static boolean isBool(String var)
	{
		return boolSymbols.containsKey(var);
	}
	public static int getINT(String var)
	{
		return intSymbols.get(var);
	}
	public static boolean getBool(String var)
	{
		return boolSymbols.get(var);
	}
	public static void setINT(String var,int value)
	{
		 intSymbols.put(var,value);
	}
	public static void setBool(String var, boolean value)
	{
		 boolSymbols.put(var,value);
	}
	public static boolean getBoolValue(String val) {
		// TODO Auto-generated method stub
		if(topb.equals(val))
		{
			return getTopb();
		}
		else if(ReservedKeywords.isBool(val))
		{
			return ReservedKeywords.getBool(val);
		}
			return Boolean.parseBoolean(val);
			
		
	}

	public static int getINTValue(String var)
	{
		if(top.equals(var))
		{
			return getTop();
		}
		else if(ReservedKeywords.isINT(var))
		{
			return ReservedKeywords.getINT(var);
		}
			return Integer.parseInt(var);
			
		
	}
	

}
