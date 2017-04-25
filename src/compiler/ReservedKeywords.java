/**
 * 
 */
package compiler;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * @author pankajsingh
 *
 */
public class ReservedKeywords {
	private static Set<String> operations=new HashSet<String>();
	private static Set<String> reservWords=new HashSet<String>();
	private static Map<String,Integer> intSymbols=new HashMap<String,Integer>();
	private static Map<String,Boolean> boolSymbols=new HashMap<String,Boolean>();
	public static void init()
	{
		operations.add("START");
		operations.add("STOP");
		operations.add("PRINT");
		operations.add("BEGIN");
		operations.add("END");
		operations.add("ASSN");
		operations.add("DEC");
//		operations.add("");
//		operations.add();
//		operations.add();
		
		//Adding reserved Words
		reservWords.add("INT");
		reservWords.add("BOOL");
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
		if("INT".equals(type))
		{
			intSymbols.put(var, 0);
		}
		else if("BOOL".equals(type))
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
	

}
