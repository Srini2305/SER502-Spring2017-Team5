/**
 * 
 */
package compiler;

/**
 * @author pankajsingh
 *
 */
public class DeclarativeOperations {

	public void executeStart(Statement smt) throws Exception {
		if(smt.getLineNo()!=0)
			throw new Exception("Start of the program not found");
		// TODO Auto-generated method stub
		
	}

	public void executeStop(Statement smt,int len) throws Exception {
		// TODO Auto-generated method stub
		if(smt.getLineNo()!=(len-1))
			throw new Exception("End of the program not found");
		
	}

	public void executeBegin(Statement smt) {
		// TODO Auto-generated method stub
		//yet to decide how to execute them
		
	}

	public void executeEnd(Statement smt) {
		// TODO Auto-generated method stub
		//yet to decide how to execute them
	}

	public String executePrint(Statement smt) throws Exception {
		// TODO Auto-generated method stub
		
		String val= smt.getOp1();
		if(val.contains("\"") )
		{
			val=val.replaceAll("\"", "");
						
		}
		else{
			//return value from symbol table
			if(ReservedKeywords.isINT(val))
				val=ReservedKeywords.getINT(val)+"";
			else if(ReservedKeywords.isBool(val))
				val=ReservedKeywords.getBool(val)+"";
			else 
				throw new Exception("Variable"+val+" is not found");
		}
		return val;

	}

	public void executeDec(Statement smt) throws Exception {
		// TODO Auto-generated method stub
		String var=smt.getOp1();
		String type=smt.getOp2();
		ReservedKeywords.addVariable(var, type);
		
	}

	public void assignValue(Statement smt) {
		// TODO Auto-generated method stub
		String var=smt.getOp1();
		if(ReservedKeywords.isINT(var))
		{
			String val=smt.getOp2();
			int value=getINTValue(val);
			ReservedKeywords.setINT(var, value);
		}
		else
			if(ReservedKeywords.isBool(var))
			{
				String val=smt.getOp2();
				boolean value=getBoolValue(val);
				ReservedKeywords.setBool(var, value);
			}
	}
	private boolean getBoolValue(String val) {
		// TODO Auto-generated method stub
		if(ReservedKeywords.isBool(val))
		{
			return ReservedKeywords.getBool(val);
		}
			return Boolean.parseBoolean(val);
			
		
	}

	public int getINTValue(String var)
	{
		if(ReservedKeywords.isINT(var))
		{
			return ReservedKeywords.getINT(var);
		}
			return Integer.parseInt(var);
			
		
	}

}
