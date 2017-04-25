/**
 * 
 */
package compiler;

import java.util.ArrayList;
import java.util.List;

/**
 * @author pankajsingh
 *
 */
public class StatementsExecutor {
	List<String> statements;
	DeclarativeOperations dec;
	ArithemeticOperations ariOps;
	public StatementsExecutor(List<String> statements)
	{
		this.statements=statements;
		dec=new DeclarativeOperations();
		ariOps=new ArithemeticOperations();
		
	}
	public List<String> generateOutput()
	{
		List<String> output=new ArrayList<String>();
		int len=statements.size();
		Statement smt=new Statement();
		for(int i=0;i<len;i++)
		{
			try {
				smt.createStatement(statements.get(i));
			
			switch(smt.getOperation())
			{
			//declarative statements
				case "START": dec.executeStart(smt);
								break;
				case "STOP": dec.executeStop(smt,len);
								break;	
				case "BEGIN": dec.executeBegin(smt);
								break;
				case "END": dec.executeEnd(smt);
								break;	
				case "PRINT": String value=dec.executePrint(smt);
								output.add(value);
								break;	
				case "DEC": dec.executeDec(smt);
								break;
				case "ASSN": dec.assignValue(smt);
								break;	
								
								
			//Arithmetic Statements	
								
				case "ADD": ariOps.executeADD(smt);
							break;	
				case "SUB": ariOps.executeSUB(smt);
							break;	
				case "MUL": ariOps.executeMUL(smt);
							break;	
				case "DIV": ariOps.executeDIV(smt);
							break;
				case "MOD": ariOps.executeMOD(smt);
							break;	
													
			}

			} catch (Exception e) {
				// TODO Auto-generated catch block
				output.add("Error: "+e.getMessage()+" :: line: "+smt.getLineNo());
				return output;
			}
		}
		return output;
	}
	private String[] getTokens(String string) {
		//if line number is included

		return null;
	}

}
